import streamlit as st
from ..constants import CUSTOM_CSS

def apply_custom_css():
    """Apply custom CSS for dark theme"""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def show_instructions():
    """Show instructions when no file is selected"""
    st.info("👆 Please select an available system or upload your Excel data dictionary file to get started.")

    st.markdown("""
    ### How to use this tool:

    1. **Select Data Source** - Choose from available systems or upload your own
    2. **Navigate Sheets** - Use tabs to switch between different sheets
    3. **Global Search** - Type in the search box for instant text filtering
    4. **Dynamic Filters** - Click 'Add Filter' to create custom column filters
    5. **Configure Filters** - Choose column, operator, and value for each filter
    6. **Select View Mode** - Standard (all columns) or Advanced (select columns)
    7. **Export** your filtered data using the top export section

    ### Features:
    - 🔍 **Global Search**: Search across all columns instantly
    - 🎛️ **Dynamic Filters**: 
      - **Add/Remove**: Create only the filters you need
      - **Full Operators**: Contains, equals, starts with, ends with, not contains, in list
      - **Enable/Disable**: Toggle filters on/off without removing them
      - **Visual Count**: See how many active filters you have
    - 📊 **Flexible Views**:
      - **Standard View**: Display all columns
      - **Advanced View**: Select specific columns to display
    - 📑 **Tab Navigation**: Easy switching between multiple sheets
    - 📥 **Smart Export**: Download all sheets or filtered results
    - 📁 **System Management**: Pre-load files for team access
    - 🧹 **Data Cleaning**: Automatic whitespace trimming while preserving nulls

    ### Dynamic Filter Benefits:
    - **On-Demand**: Add only the filters you actually need
    - **Customizable**: Each filter has its own column, operator, and value
    - **Manageable**: Enable/disable or remove filters individually
    - **Efficient**: No cluttered interface with unused filter options
    - **Flexible**: Works with both simple and complex filtering needs

    ### Setting Up Available Systems:
    1. Create a `docs/` directory
    2. Add your Excel files to this directory
    3. Create a `metadata.json` file with system information
    4. Install dependencies: `pip install streamlit pandas openpyxl pyyaml`
    """)
