import streamlit as st
import pandas as pd
from typing import Optional, Tuple, Any

from src.core.data_processor import DataProcessor
from src.core.session_manager import SessionStateManager
from src.core.filter_engine import FilterEngine
from src.components.ui_components import UIComponents
from src.components.metadata_display import MetadataManager
from src.components.export_manager import ExportManager
from src.constants import DEFAULT_TABLE_HEIGHT
from src.utils.helpers import show_instructions

def show():
    """Main data explorer page"""
    # Updated header to match About page style
    st.markdown("# 🔍 Data Explorer")
    st.markdown("---")

    # File selection
    selected_file, uploaded_file, file_source = render_file_selection()

    if not (selected_file or uploaded_file):
        show_instructions()
        return

    # Load metadata and display banner for available systems
    if selected_file:
        metadata = MetadataManager.load_metadata()
        MetadataManager.display_info_banner(selected_file, metadata)

    # Load all sheets
    sheets_dict = DataProcessor.load_all_sheets(file_source, uploaded_file)

    if not sheets_dict:
        st.error("Could not load data from the selected file.")
        return

    # Export section
    ExportManager.render_export_section(sheets_dict)

    # Sheet processing
    sheet_names = list(sheets_dict.keys())

    if len(sheet_names) == 1:
        # Single sheet
        st.info(f"Working with sheet: **{sheet_names[0]}**")
        process_sheet_data(sheets_dict[sheet_names[0]], sheet_names[0])
    else:
        # Multiple sheets with tabs
        st.subheader("📑 Sheet Selection")
        tabs = st.tabs(sheet_names)

        for i, sheet_name in enumerate(sheet_names):
            with tabs[i]:
                process_sheet_data(sheets_dict[sheet_name], sheet_name)

def render_file_selection() -> Tuple[Optional[str], Optional[Any], Optional[str]]:
    """Render file selection interface"""
    st.subheader("📁 Data Source Selection")

    available_systems = MetadataManager.get_available_systems()

    col1, col2 = st.columns(2)
    with col1:
        data_source = st.radio(
            "Choose data source:",
            ["Available Systems", "Upload New File"],
            help="Select from pre-loaded systems or upload your own"
        )

    selected_file = None
    uploaded_file = None
    file_source = None

    if data_source == "Available Systems":
        if available_systems:
            with col2:
                selected_system = st.selectbox(
                    "Select source system:",
                    list(available_systems.keys()),
                    help="Choose from available data dictionary systems"
                )
            selected_file = available_systems[selected_system]
            file_source = selected_file
        else:
            st.info("No systems available. Please add Excel files to `docs/` or upload a file.")
            return None, None, None
    else:
        uploaded_file = st.file_uploader(
            "Upload your data dictionary (Excel file)",
            type=['xlsx', 'xls'],
            help="Upload your Excel file containing the data dictionary"
        )
        file_source = "upload"

    return selected_file, uploaded_file, file_source

def process_sheet_data(df: pd.DataFrame, sheet_name: str) -> pd.DataFrame:
    """Process and display data for a single sheet"""
    # Initialize session state
    SessionStateManager.init_sheet_state(sheet_name)

    # Search & Filter Section
    st.subheader("🔍 Search & Filter")

    # Global search
    global_search = UIComponents.render_global_search(sheet_name)

    # Dynamic filters
    basic_filters, advanced_filters = UIComponents.render_dynamic_filters(sheet_name, df)

    # View mode controls
    display_columns, view_mode = UIComponents.render_view_mode_controls(sheet_name, df)

    # Apply filters
    filtered_df = FilterEngine.apply_filters(df, global_search, basic_filters, advanced_filters)

    # Results section
    st.header(f"📋 Results ({len(filtered_df)} records)")

    if len(filtered_df) == 0:
        st.warning("No records match your search criteria. Try adjusting your filters.")
    else:
        # Show filtered data
        display_df = filtered_df[display_columns] if display_columns else filtered_df
        st.dataframe(
            display_df,
            use_container_width=True,
            height=DEFAULT_TABLE_HEIGHT
        )

    # Data info section for advanced mode
    if view_mode == "Advanced":
        with st.expander("📊 Data Information"):
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Data Type': df.dtypes,
                'Non-Null Count': df.count(),
                'Unique Values': [df[col].nunique() for col in df.columns]
            })
            st.dataframe(col_info, use_container_width=True)

    return filtered_df
