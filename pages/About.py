import streamlit as st
from src.pages.about import show as show_about
from src.utils.helpers import apply_custom_css

# Page configuration
st.set_page_config(
    page_title="About - Data Explorer",
    page_icon="ℹ️",
    layout="wide"
)

def main():
    # Apply custom CSS
    apply_custom_css()

    # About page content
    show_about()

if __name__ == "__main__":
    main()
