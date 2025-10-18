import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Gartner Contract Evaluation Platform",
    page_icon="📊",
    layout="wide"
)

# Custom CSS styling (shared across all pages)
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1e40af, #3b82f6);
        color: white;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        margin: 10px 0;
    }
    
    .metric-card-danger {
        background: linear-gradient(135deg, #dc2626, #ef4444);
        color: white;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        margin: 10px 0;
    }
    
    .alert-success {
        background-color: #f0f9ff;
        border-left: 4px solid #059669;
        color: #059669;
        padding: 15px;
        border-radius: 6px;
        margin: 10px 0;
    }
    
    .alert-warning {
        background-color: #fffbeb;
        border-left: 4px solid #d97706;
        color: #d97706;
        padding: 15px;
        border-radius: 6px;
        margin: 10px 0;
    }
    
    .alert-danger {
        background-color: #fef2f2;
        border-left: 4px solid #dc2626;
        color: #dc2626;
        padding: 15px;
        border-radius: 6px;
        margin: 10px 0;
    }
    
    .alert-info {
        background-color: #eff6ff;
        border-left: 4px solid #3b82f6;
        color: #1e40af;
        padding: 15px;
        border-radius: 6px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>📊 Gartner Contract Evaluation Platform</h1>
    <p>Intelligent analytics for procurement decision-making</p>
</div>
""", unsafe_allow_html=True)

# Welcome message for main page
st.markdown("""
## Welcome to the Gartner Contract Evaluation Platform

This platform provides comprehensive analytics and insights for your Gartner research services contract. 

### Quick Navigation:
- **📊 Overview Dashboard** - Key metrics and usage statistics
- **💡 Insights Engine** - Strategic analysis and recommendations  
- **🤖 AI Discovery Bot** - Interactive data exploration
- **⚙️ Decision Optimiser** - Scenario planning and optimization
- **📄 Report Generator** - Automated report creation

Use the sidebar to navigate between different sections of the platform.
""")

# Quick stats on main page
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Users", "38", "Licensed")
    
with col2:
    st.metric("Active Users", "26", "68% utilisation")
    
with col3:
    st.metric("Budget Status", "$3.9M", "100% over pace")
