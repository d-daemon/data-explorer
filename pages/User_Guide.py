import streamlit as st
from src.utils.helpers import apply_custom_css

st.set_page_config(
    page_title="User Guide - Data Explorer",
    page_icon="📖",
    layout="wide"
)

def main():
    apply_custom_css()

    st.markdown("# 📖 User Guide")
    st.markdown("---")

    st.markdown("""
    ## 🎯 Getting Started

    ### Step 1: Select Your Data Source
    Choose from pre-configured systems or upload your own Excel file.

    ### Step 2: Search and Filter
    Use the global search or add specific column filters.

    ### Step 3: Export Results
    Download your filtered data as Excel or CSV.

    ## 🔍 Advanced Features

    ### Dynamic Filters
    - **Contains**: Find text anywhere in the field
    - **Equals**: Exact match
    - **Starts with**: Text begins with your search
    - **Ends with**: Text ends with your search
    - **Not contains**: Exclude records with specific text
    - **In list**: Select multiple specific values

    ### View Modes
    - **Standard**: See all columns
    - **Advanced**: Choose specific columns to display

    ## 💡 Tips and Tricks

    1. **Use global search first** for broad filtering
    2. **Add specific filters** to narrow down results
    3. **Enable/disable filters** to test different combinations
    4. **Use "In list" operator** for categorical data
    5. **Export early and often** to save your work
    """)

if __name__ == "__main__":
    main()
