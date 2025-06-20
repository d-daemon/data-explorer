import streamlit as st
import pandas as pd
from typing import Dict
from ..constants import DOCS_DIR

class DataProcessor:
    """Handle data loading and processing"""

    @staticmethod
    @st.cache_data
    def load_all_sheets(file_source: str, uploaded_file=None) -> Dict[str, pd.DataFrame]:
        """Load all sheets from Excel file"""
        try:
            if file_source == "upload" and uploaded_file:
                excel_file = pd.ExcelFile(uploaded_file)
            else:
                file_path = DOCS_DIR / file_source
                excel_file = pd.ExcelFile(file_path)

            sheets_dict = {}

            for sheet_name in excel_file.sheet_names:
                if file_source == "upload" and uploaded_file:
                    df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
                else:
                    df = pd.read_excel(file_path, sheet_name=sheet_name)

                # Clean data
                df = DataProcessor._clean_dataframe(df)
                sheets_dict[sheet_name] = df

            return sheets_dict
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")
            return {}

    @staticmethod
    def _clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        """Clean dataframe columns and values"""
        # Clean column names
        df.columns = df.columns.astype(str).str.strip()

        # Trim whitespace from string columns while preserving nulls
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].apply(
                    lambda x: x.strip() if pd.notna(x) and isinstance(x, str) else x
                )

        return df
