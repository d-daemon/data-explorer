import streamlit as st
import pandas as pd
import io
from typing import Dict

class ExportManager:
    """Handle data export operations"""

    @staticmethod
    def create_download_link(df: pd.DataFrame, filename: str = "filtered_data_dictionary.xlsx") -> bytes:
        """Create Excel download data"""
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Filtered_Data', index=False)

        return output.getvalue()

    @staticmethod
    def create_workbook_download(sheets_dict: Dict[str, pd.DataFrame]) -> bytes:
        """Create multi-sheet Excel download"""
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            for sheet_name, sheet_df in sheets_dict.items():
                sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

        return output.getvalue()

    @staticmethod
    def render_export_section(sheets_dict: Dict[str, pd.DataFrame]):
        """Render the export section"""
        st.subheader("📥 Export Data")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Export current view:**")
            if st.button("📊 Prepare Excel Download", key="prep_excel"):
                st.info("Apply filters first, then use download buttons that appear below results.")

        with col2:
            st.markdown("**Export format:**")
            if st.button("📄 Prepare CSV Download", key="prep_csv"):
                st.info("Apply filters first, then use download buttons that appear below results.")

        with col3:
            st.markdown("**Export all sheets:**")
            if st.button("📋 Download All Sheets", key="download_all"):
                processed_data = ExportManager.create_workbook_download(sheets_dict)
                st.download_button(
                    label="📊 Download All Sheets",
                    data=processed_data,
                    file_name="complete_data_dictionary.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key="download_all_excel"
                )

    @staticmethod
    def render_result_export_buttons(filtered_df: pd.DataFrame, sheet_name: str):
        """Render export buttons for filtered results"""
        if len(filtered_df) > 0:
            st.subheader("📥 Export Filtered Data")
            col1, col2, col3 = st.columns(3)

            with col1:
                excel_data = ExportManager.create_download_link(filtered_df)
                st.download_button(
                    label="📊 Download as Excel",
                    data=excel_data,
                    file_name=f"filtered_{sheet_name}_data_dictionary.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key=f"excel_final_{sheet_name}"
                )

            with col2:
                csv_data = filtered_df.to_csv(index=False)
                st.download_button(
                    label="📄 Download as CSV",
                    data=csv_data,
                    file_name=f"filtered_{sheet_name}_data_dictionary.csv",
                    mime="text/csv",
                    key=f"csv_final_{sheet_name}"
                )

            with col3:
                st.metric("Filtered Records", len(filtered_df))
