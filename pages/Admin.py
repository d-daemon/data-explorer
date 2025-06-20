import streamlit as st
from src.utils.helpers import apply_custom_css
from src.components.metadata_display import MetadataManager
import os

st.set_page_config(
    page_title="Admin - Data Explorer",
    page_icon="⚙️",
    layout="wide"
)

def main():
    apply_custom_css()

    st.markdown("# ⚙️ System Administration")
    st.markdown("---")

    # Admin content
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 System Statistics")

        # File statistics
        docs_dir = "docs"
        if os.path.exists(docs_dir):
            excel_files = [f for f in os.listdir(docs_dir) if f.endswith(('.xlsx', '.xls'))]
            st.metric("Available Files", len(excel_files))

            total_size = sum(os.path.getsize(os.path.join(docs_dir, f)) for f in excel_files)
            st.metric("Total Size", f"{total_size / 1024 / 1024:.1f} MB")

        # Metadata info
        metadata = MetadataManager.load_metadata()
        st.metric("Configured Systems", len(metadata))

    with col2:
        st.markdown("### 🔧 Management Actions")

        if st.button("🔄 Refresh Data Cache"):
            st.cache_data.clear()
            st.success("Data cache cleared!")

        if st.button("📝 View Metadata"):
            metadata = MetadataManager.load_metadata()
            st.json(metadata)

    # File management
    st.markdown("### 📁 File Management")

    docs_dir = "docs"
    if os.path.exists(docs_dir):
        excel_files = [f for f in os.listdir(docs_dir) if f.endswith(('.xlsx', '.xls'))]

        if excel_files:
            for file in excel_files:
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.text(file)
                with col2:
                    file_size = os.path.getsize(os.path.join(docs_dir, file))
                    st.text(f"{file_size / 1024:.1f} KB")
                with col3:
                    if st.button("📊", key=f"info_{file}", help="View file info"):
                        st.info(f"File: {file}")

if __name__ == "__main__":
    main()
