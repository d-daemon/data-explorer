import streamlit as st

class SessionStateManager:
    """Centralized session state management"""

    @staticmethod
    def init_sheet_state(sheet_name: str):
        """Initialize session state for a sheet"""
        defaults = {
            f'view_mode_{sheet_name}': 'Standard',
            f'clear_counter_{sheet_name}': 0,
            f'filter_count_{sheet_name}': 0
        }

        for key, default_value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = default_value

    @staticmethod
    def get_clear_counter(sheet_name: str) -> int:
        return st.session_state.get(f'clear_counter_{sheet_name}', 0)

    @staticmethod
    def increment_clear_counter(sheet_name: str):
        st.session_state[f'clear_counter_{sheet_name}'] += 1

    @staticmethod
    def get_filter_count(sheet_name: str) -> int:
        return st.session_state.get(f'filter_count_{sheet_name}', 0)

    @staticmethod
    def set_filter_count(sheet_name: str, count: int):
        st.session_state[f'filter_count_{sheet_name}'] = count
