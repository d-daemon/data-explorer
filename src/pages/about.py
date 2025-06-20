import streamlit as st

def show():
    """About and contact page"""

    # Header
    st.markdown("# ℹ️ About Data Explorer")
    st.markdown("---")

    # Overview section
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## 🎯 Purpose

        The Data Explorer is an internal tool designed to help teams easily search, 
        filter, and explore data dictionaries from various source systems. It provides a 
        user-friendly interface for data analysts, developers, and business users to quickly 
        find the data they need.

        ## ✨ Key Features

        - **🔍 Powerful Search**: Global search across all columns with instant results
        - **🎛️ Dynamic Filtering**: Add custom filters with advanced operators
        - **📊 Flexible Views**: Choose which columns to display
        - **📑 Multi-Sheet Support**: Handle complex Excel workbooks with multiple sheets
        - **📥 Export Options**: Download filtered results or complete datasets
        - **🏢 System Integration**: Pre-configured access to multiple data sources
        """)

    with col2:
        st.markdown("""
        ## 📈 Version Info

        **Current Version:** 1.0
        **Last Updated:** June 2025
        **Built With:** Streamlit, Pandas, Python  
        **Status:** ✅ Active Development
        """)

        # Usage statistics (you could make these dynamic)
        st.markdown("## 📊 Usage Stats")
        st.metric("Systems Integrated", "1+")
        st.metric("Monthly Active Users", "1+")
        st.metric("Data Sources", "1")

    st.markdown("---")

    # Team and contact section
    st.markdown("## 👥 Team & Contact")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🛠️ Development Team

        **Lead Developer**  
        Your Name  
        📧 your.email@company.com  

        **Data Architecture**  
        Team Lead Name  
        📧 team.lead@company.com  
        """)

    with col2:
        st.markdown("""
        ### 🎯 Product Owner

        **Business Owner**  
        Product Manager Name  
        📧 pm@company.com  

        **ITSO Contact**  
        Data Governance Lead  
        📧 governance@company.com  
        """)

    with col3:
        st.markdown("""
        ### 🆘 Support

        **Technical Issues**  
        Create a ticket in ServiceNow  

        **Feature Requests**  
        Email the development team  

        **Data Questions**  
        Contact the data owners  
        """)

    st.markdown("---")

    # Contributing section
    st.markdown("## 🤝 How to Contribute")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 📝 Reporting Issues

        If you encounter bugs or have suggestions:

        1. **Check existing issues** first
        2. **Provide detailed description** of the problem
        3. **Include steps to reproduce** the issue
        4. **Add screenshots** if helpful
        5. **Mention your browser/OS** for compatibility issues
        """)

    with col2:
        st.markdown("""
        ### 💡 Requesting Features

        For new feature requests:

        1. **Describe the business need** clearly
        2. **Explain the expected behavior**
        3. **Provide use case examples**
        4. **Consider impact on other users**
        5. **Suggest implementation approach** if technical
        """)

    # Technical details
    with st.expander("🔧 Technical Details"):
        st.markdown("""
        ### Architecture

        - **Frontend**: Streamlit (Python)
        - **Data Processing**: Pandas, OpenPyXL
        - **Deployment**: Internal server/cloud
        - **File Storage**: Local docs directory
        - **Metadata**: JSON configuration files

        ### File Structure
        ```
        data_explorer/
        ├── Data_Explorer.py           # Main page (Streamlit auto-names from filename)
        ├── pages/
        │   ├── About.py
        │   ├── Admin.py
        │   └── User_Guide.py
        ├── src/
        │   ├── constants.py
        │   ├── core/
        │   ├── components/
        │   ├── pages/
        │   └── utils/
        ├── docs/                     # Your data files
        └── requirements.txt
        ```

        ### Adding New Data Sources

        1. Add Excel files to `docs/` directory
        2. Update `metadata.json` with system information
        3. Test the integration
        4. Document the new source
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Data Dictionary Explorer v2.0 | Built with ❤️ for the Data Team</p>
    </div>
    """, unsafe_allow_html=True)
