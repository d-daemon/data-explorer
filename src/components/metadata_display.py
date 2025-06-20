import streamlit as st
import json
import yaml
from typing import Dict, Any

from ..constants import DOCS_DIR, METADATA_FILE

class MetadataManager:
    """Handle metadata operations"""

    @staticmethod
    def load_metadata() -> Dict[str, Any]:
        """Load metadata for available files"""
        metadata_path = DOCS_DIR / METADATA_FILE

        if metadata_path.exists():
            try:
                if METADATA_FILE.endswith('.json'):
                    with open(metadata_path, 'r') as f:
                        return json.load(f)
                elif METADATA_FILE.endswith('.yaml') or METADATA_FILE.endswith('.yml'):
                    with open(metadata_path, 'r') as f:
                        return yaml.safe_load(f)
            except Exception as e:
                st.warning(f"Could not load metadata: {str(e)}")

        return {}

    @staticmethod
    def get_available_systems() -> Dict[str, str]:
        """Get mapping of source systems to filenames"""
        if not DOCS_DIR.exists():
            DOCS_DIR.mkdir(parents=True, exist_ok=True)
            return {}

        metadata = MetadataManager.load_metadata()
        systems = {}

        # Get all Excel files
        excel_files = []
        for file_path in DOCS_DIR.glob("*.xlsx"):
            excel_files.append(file_path.name)
        for file_path in DOCS_DIR.glob("*.xls"):
            excel_files.append(file_path.name)

        # Map source systems to filenames
        for filename in excel_files:
            file_key = filename.replace('.xlsx', '').replace('.xls', '')
            file_info = metadata.get(file_key, {})
            source_system = file_info.get('source_system', filename)
            systems[source_system] = filename

        return systems

    @staticmethod
    def display_info_banner(filename: str, metadata: Dict[str, Any]):
        """Display information banner for selected file with horizontal dividers"""
        file_key = filename.replace('.xlsx', '').replace('.xls', '')
        file_info = metadata.get(file_key, {})

        if file_info:
            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("**🏢 Source System**")
                st.markdown(f"**{file_info.get('source_system', 'Unknown System')}**")
                if 'description' in file_info:
                    st.caption(file_info['description'])
                if 'last_updated' in file_info:
                    st.caption(f"Updated: {file_info['last_updated']}")

            with col2:
                st.markdown("**👥 ITSO Information**")
                itso_info = file_info.get('itso', {})
                if 'owner' in itso_info:
                    st.markdown(f"Owner: {itso_info['owner']}")
                if 'contact' in itso_info:
                    st.caption(f"Contact: {itso_info['contact']}")
                if 'team' in itso_info:
                    st.caption(f"Team: {itso_info['team']}")

            with col3:
                st.markdown("**📋 Additional Info**")
                misc_info = file_info.get('misc', {})
                for key, value in misc_info.items():
                    st.caption(f"{key.replace('_', ' ').title()}: {value}")

            st.markdown("---")
