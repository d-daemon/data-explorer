import streamlit as st
from src.pages.data_explorer import show as show_data_explorer
from src.utils.helpers import apply_custom_css

# Page configuration
st.set_page_config(
    page_title="Data Explorer",
    page_icon="👻",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Apply custom CSS
    apply_custom_css()

    # Main page content (Data Explorer functionality)
    show_data_explorer()

if __name__ == "__main__":
    main()
