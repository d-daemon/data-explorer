import streamlit as st
import pandas as pd
from typing import Tuple, Dict, Any, List

from ..core.session_manager import SessionStateManager
from ..constants import FILTER_OPERATORS, MAX_MULTISELECT_OPTIONS

class UIComponents:
    """Reusable UI components"""

    @staticmethod
    def render_global_search(sheet_name: str) -> str:
        """Render global search input"""
        clear_counter = SessionStateManager.get_clear_counter(sheet_name)

        search_term = st.text_input(
            "Search across all fields:",
            placeholder="Type and press Enter or click outside box...",
            help="Results update when you press Enter or click outside the search box",
            key=f"search_{sheet_name}_{clear_counter}",
            label_visibility="visible"
        )

        return search_term if search_term else ""

    @staticmethod
    def render_dynamic_filters(sheet_name: str, df: pd.DataFrame) -> Tuple[Dict[str, Any], Dict[str, Dict[str, str]]]:
        """Render dynamic filter interface"""
        st.markdown("**🎛️ Dynamic Column Filters**")

        # Filter controls
        col1, col2, col3 = st.columns([1, 1, 2])

        with col1:
            if st.button("⚙️ Add Filter", key=f"add_filter_{sheet_name}"):
                current_count = SessionStateManager.get_filter_count(sheet_name)
                SessionStateManager.set_filter_count(sheet_name, current_count + 1)

        with col2:
            if st.button("🗑️ Clear All Filters", key=f"clear_all_{sheet_name}"):
                SessionStateManager.set_filter_count(sheet_name, 0)
                SessionStateManager.increment_clear_counter(sheet_name)
                st.rerun()

        with col3:
            active_count = SessionStateManager.get_filter_count(sheet_name)
            st.markdown(f"**Active Filters: {active_count}**")

        # Render individual filters
        return UIComponents._render_filter_rows(sheet_name, df)

    @staticmethod
    def _render_filter_rows(sheet_name: str, df: pd.DataFrame) -> Tuple[Dict[str, Any], Dict[str, Dict[str, str]]]:
        """Render individual filter rows"""
        clear_counter = SessionStateManager.get_clear_counter(sheet_name)
        filter_count = SessionStateManager.get_filter_count(sheet_name)

        basic_filters = {}
        advanced_filters = {}

        for i in range(filter_count):
            col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 1, 1])

            with col1:
                selected_column = st.selectbox(
                    "Column:",
                    df.columns,
                    key=f"dyn_col_{sheet_name}_{clear_counter}_{i}",
                    help="Choose column to filter"
                )

            with col2:
                filter_type = st.selectbox(
                    "Operator:",
                    FILTER_OPERATORS,
                    key=f"dyn_op_{sheet_name}_{clear_counter}_{i}",
                    help="Filter operation"
                )

            with col3:
                filter_value = UIComponents._render_filter_value_input(
                    selected_column, filter_type, df, sheet_name, clear_counter, i
                )

                # Categorize filters
                if filter_value:
                    if filter_type == "in_list":
                        basic_filters[selected_column] = filter_value
                    else:
                        advanced_filters[selected_column] = {
                            'value': filter_value,
                            'operator': filter_type
                        }

            with col4:
                enabled = st.checkbox(
                    "On",
                    value=True,
                    key=f"dyn_en_{sheet_name}_{clear_counter}_{i}",
                    help="Enable/disable this filter"
                )
                if not enabled:
                    # Remove disabled filters
                    basic_filters.pop(selected_column, None)
                    advanced_filters.pop(selected_column, None)

            with col5:
                if st.button("❌", key=f"dyn_del_{sheet_name}_{clear_counter}_{i}", help="Remove this filter"):
                    SessionStateManager.set_filter_count(sheet_name, filter_count - 1)
                    st.rerun()

        # Show helpful message when no filters
        if filter_count == 0:
            st.info("💡 Click 'Add Filter' to create column-specific filters. Use the global search above for quick text searching.")

        return basic_filters, advanced_filters

    @staticmethod
    def _render_filter_value_input(column: str, filter_type: str, df: pd.DataFrame,
                                   sheet_name: str, clear_counter: int, index: int):
        """Render appropriate input for filter value"""
        if filter_type == "in_list":
            unique_values = df[column].dropna().unique()
            if len(unique_values) <= MAX_MULTISELECT_OPTIONS:
                return st.multiselect(
                    "Values:",
                    options=sorted(unique_values.astype(str)),
                    key=f"dyn_val_{sheet_name}_{clear_counter}_{index}",
                    help="Select multiple values"
                )
            else:
                st.info("Too many unique values. Use 'contains' instead.")
                return None
        else:
            return st.text_input(
                "Value:",
                key=f"dyn_val_{sheet_name}_{clear_counter}_{index}",
                help="Enter filter value"
            )

    @staticmethod
    def render_view_mode_controls(sheet_name: str, df: pd.DataFrame) -> Tuple[List[str], str]:
        """Render view mode controls and return display columns"""
        col1, col2 = st.columns([1, 2])

        with col1:
            view_mode = st.radio(
                "View Mode:",
                ["Standard", "Advanced"],
                key=f"view_mode_{sheet_name}",
                horizontal=True,
                help="Standard: Show all columns | Advanced: Select specific columns"
            )

        display_columns = list(df.columns)

        if view_mode == "Advanced":
            with col2:
                clear_counter = SessionStateManager.get_clear_counter(sheet_name)
                display_columns = st.multiselect(
                    "Select columns to display:",
                    options=list(df.columns),
                    default=list(df.columns),
                    help="Choose which columns to show in the table",
                    key=f"columns_{sheet_name}_{clear_counter}"
                )
                if not display_columns:
                    display_columns = list(df.columns)

        return display_columns, view_mode
