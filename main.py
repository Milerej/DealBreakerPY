import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

# Add components directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'components'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))

from overview import render_overview
from insights import render_insights
from ai_bot import render_ai_bot
from optimizer import render_optimizer
from reports import render_reports

# Page configuration
st.set_page_config(
    page_title="Gartner Contract Evaluation Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
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
    
    .insight-card {
        background: #f8fafc;
        border-left: 4px solid #1e40af;
        padding: 15px;
        margin: 10px 0;
        border-radius: 6px;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        background-color: #f1f5f9;
        border-radius: 8px;
        color: #64748b;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #1e40af;
        color: white;
    }
    
    .chat-message {
        padding: 10px 15px;
        margin: 10px 0;
        border-radius: 8px;
        max-width: 80%;
    }
    
    .user-message {
        background: #1e40af;
        color: white;
        margin-left: auto;
    }
    
    .bot-message {
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        color: #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'current_scenario' not in st.session_state:
    st.session_state.current_scenario = {}

# Header
st.markdown("""
<div class="main-header">
    <h1>📊 Gartner Contract Evaluation Platform</h1>
    <p>Intelligent analytics for procurement decision-making</p>
</div>
""", unsafe_allow_html=True)

# Navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview Dashboard", 
    "💡 Insights Engine", 
    "🤖 AI Discovery Bot", 
    "⚙️ Decision Optimizer", 
    "📄 Report Generator"
])

with tab1:
    render_overview()

with tab2:
    render_insights()

with tab3:
    render_ai_bot()

with tab4:
    render_optimizer()

with tab5:
    render_reports()

# Sidebar information
with st.sidebar:
    st.markdown("### 📋 Quick Stats")
    st.metric("Total Users", "38")
    st.metric("Active Users", "26 (68%)")
    st.metric("Budget Status", "$3.9M", delta="$400K over")
    st.metric("Cost/Download", "$632")
    
    st.markdown("---")
    st.markdown("### 🚨 Alerts")
    st.error("Budget overrun: 100% over pace")
    st.warning("Ace Tan: 28% of total usage")
    st.info("Contract expires in 16 months")
    
    st.markdown("---")
    st.markdown("### 📞 Support")
    st.markdown("For technical support or questions about this platform, contact the procurement team.")

if __name__ == "__main__":
    st.run()
