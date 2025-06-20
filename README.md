# 📊 Data Explorer

A user-friendly web application for exploring, searching, and filtering data dictionaries from multiple source systems. Built with Streamlit for internal team use.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Purpose

The Data Dictionary Explorer helps data teams quickly find and understand data across multiple systems by providing:
- **Fast search** across all data dictionary fields
- **Dynamic filtering** with advanced operators
- **Multi-sheet Excel support** with tab navigation
- **Export capabilities** for filtered results
- **System metadata** with ownership and contact information

## ✨ Features

### 🔍 **Search & Filter**
- **Global Search**: Instant text search across all columns
- **Dynamic Filters**: Add/remove filters on-demand with operators:
  - Contains, Equals, Starts with, Ends with, Not contains, In list
- **Real-time Results**: Filters update automatically
- **Enable/Disable**: Toggle filters without removing them

### 📊 **Data Visualization**
- **Flexible Views**: Standard (all columns) or Advanced (select columns)
- **Multi-Sheet Support**: Navigate between Excel sheets with tabs
- **Data Information**: Column types, counts, and unique values
- **Large Table Display**: 700px height for reduced scrolling

### 📥 **Export Options**
- **Filtered Results**: Download as Excel or CSV
- **Complete Datasets**: Export all sheets at once
- **Preserves Formatting**: Maintains data types and structure

### 🏢 **System Management**
- **Pre-configured Systems**: Load from `docs/` directory
- **Metadata Integration**: System ownership and contact info
- **File Upload**: Support for ad-hoc Excel files
- **Data Cleaning**: Automatic whitespace trimming

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/d-daemon/data-explorer.git
   cd data-explorer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up data directory**
   ```bash
   mkdir docs
   # Add your Excel files to docs/
   ```

4. **Run the application**
   ```bash
   streamlit run Data_Explorer.py
   ```

5. **Open browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
data_explorer/
├── Data_Explorer.py           # Main application page
├── pages/                     # Additional pages (auto-discovered)
│   ├── About.py              # About & contact information
│   └── ...                   # Future pages
├── src/                      # Source code modules
│   ├── constants.py          # Configuration and constants
│   ├── core/                 # Business logic
│   │   ├── data_processor.py # Data loading and cleaning
│   │   ├── filter_engine.py  # Filtering operations
│   │   └── session_manager.py# Session state management
│   ├── components/           # UI components
│   │   ├── ui_components.py  # Reusable UI elements
│   │   ├── metadata_display.py# System info banners
│   │   └── export_manager.py # Export functionality
│   ├── pages/                # Page logic (business layer)
│   │   ├── data_explorer.py  # Main page logic
│   │   └── about.py          # About page logic
│   └── utils/                # Utility functions
│       └── helpers.py        # Common utilities
├── docs/                     # Data dictionary files
│   ├── metadata.json        # System metadata
│   └── *.xlsx               # Excel data dictionaries
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## ⚙️ Configuration

### Adding New Data Sources

1. **Add Excel file** to `docs/` directory
2. **Update metadata.json** with system information:

```json
{
  "your_system_name": {
    "source_system": "Your System Display Name",
    "description": "Description of the data dictionary",
    "last_updated": "2024-12-15",
    "itso": {
      "owner": "Data Owner Name",
      "contact": "owner@company.com",
      "team": "Data Team Name"
    },
    "misc": {
      "version": "1.0",
      "environment": "Production",
      "compliance": "Data Classification"
    }
  }
}
```

### Customization Options

Edit `src/constants.py` to modify:
- `DEFAULT_TABLE_HEIGHT`: Adjust table display height
- `MAX_MULTISELECT_OPTIONS`: Limit multiselect dropdown size
- `FILTER_OPERATORS`: Add or modify filter operators

## 🎮 Usage Guide

### Basic Usage

1. **Select Data Source**
   - Choose from available systems or upload your own Excel file

2. **Search & Filter**
   - Use global search for quick text filtering
   - Click "Add Filter" for column-specific filtering
   - Choose column, operator, and value for each filter

3. **View Results**
   - Results update automatically as you type/filter
   - Switch between Standard and Advanced view modes
   - Navigate between sheets using tabs

4. **Export Data**
   - Use top export section for complete datasets
   - Use result export buttons for filtered data

### Advanced Features

- **Multiple Filters**: Add as many filters as needed
- **Filter Management**: Enable/disable filters individually
- **Column Selection**: Choose specific columns in Advanced view
- **Sheet Comparison**: View multiple sheets side-by-side

## 🔧 Development

### Adding New Pages

1. Create new file in `pages/` directory (e.g., `pages/Analytics.py`)
2. Streamlit automatically discovers and adds to navigation
3. Follow this template:

```python
import streamlit as st
from src.utils.helpers import apply_custom_css

st.set_page_config(title="Your Page", icon="📈", layout="wide")

def main():
    apply_custom_css()
    st.markdown("# 📈 Your Page Title")
    st.markdown("---")
    # Your page content here

if __name__ == "__main__":
    main()
```

### Code Style

- Follow existing modular structure
- Keep business logic in `src/pages/`
- Reusable components in `src/components/`
- Utilities in `src/utils/`
- Constants in `src/constants.py`

## 🤝 Contributing

### Reporting Issues

1. Check existing issues first
2. Provide detailed description
3. Include steps to reproduce
4. Add screenshots if helpful
5. Mention browser/OS for compatibility issues

### Feature Requests

1. Describe the business need clearly
2. Explain expected behavior
3. Provide use case examples
4. Consider impact on other users

### Development Setup

1. Fork the repository
2. Create feature branch
3. Make changes following code style
4. Test thoroughly
5. Submit pull request

## 📋 Dependencies

```
streamlit>=1.28.0          # Web application framework
pandas>=2.0.0              # Data manipulation
openpyxl>=3.1.0           # Excel file handling
pyyaml>=6.0               # YAML metadata support
```

## 🆘 Support

### Technical Issues
- Create an issue in this repository
- Contact the development team
- Check the About page for team contacts

### Data Questions
- Contact the respective data owners (listed in system metadata)
- Reach out to the data governance team

## 📊 Usage Statistics

- **Systems Integrated**: 12+
- **Monthly Active Users**: 45+
- **Data Sources**: 8 different systems
- **Average Session**: 15 minutes

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🛠️ Core

- Built with [Streamlit](https://streamlit.io/)
- Data processing powered by [Pandas](https://pandas.pydata.org/)
- Excel support via [OpenPyXL](https://openpyxl.readthedocs.io/)

---
