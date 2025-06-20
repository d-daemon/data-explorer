from pathlib import Path

# File paths
DOCS_DIR = Path("docs")
METADATA_FILE = "metadata.json"

# UI Configuration
DEFAULT_TABLE_HEIGHT = 700
MAX_MULTISELECT_OPTIONS = 100

# Filter operators
FILTER_OPERATORS = [
    "contains", "equals", "starts_with",
    "ends_with", "not_contains", "in_list"
]

# Styling
CUSTOM_CSS = """
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #58a6ff;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stExpander > div:first-child {
        background-color: #374151;
        border-radius: 0.3rem;
    }
    .stMultiSelect > div {
        background-color: #374151;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
"""
