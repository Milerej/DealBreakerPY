import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Gartner Contract Evaluation Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
    layout="wide"
)

# Custom CSS styling
@@ -283,7 +282,7 @@
        if st.button("What alternatives do users prefer?", key="alt_btn"):
            st.session_state.last_response = "Survey data shows 34% prefer alternatives: Forrester (18%), IDC (12%), McKinsey (4%). Main reasons: cost concerns (67%), content overlap (23%), user interface preferences (32%)."

        if st.button("Analyze cost trends over time", key="cost_btn"):
        if st.button("Analyse cost trends over time", key="cost_btn"):
            st.session_state.last_response = "Cost trends show 100% increase over expected pace. Usage peaks during Q1 budget cycles and Q3 strategic planning periods. Current trajectory unsustainable without intervention."

        if st.button("Which content types drive most value?", key="content_btn"):
@@ -296,7 +295,7 @@
        user_input = st.text_input("Ask me about your Gartner data...", key="chat_input")

        if st.button("Send", key="send_btn") and user_input:
            st.session_state.last_response = f"Based on your question about '{user_input}', I can analyze the data patterns. The key insight is that your usage shows extreme concentration with Ace Tan driving 28% of total activity, suggesting either exceptional value extraction or potential account sharing that needs investigation."
            st.session_state.last_response = f"Based on your question about '{user_input}', I can analyse the data patterns. The key insight is that your usage shows extreme concentration with Ace Tan driving 28% of total activity, suggesting either exceptional value extraction or potential account sharing that needs investigation."

        # Display response
        if hasattr(st.session_state, 'last_response'):
@@ -395,7 +394,7 @@
        ### Critical Issues
        - **Unsustainable Spending:** Current trajectory leads to $7.02M total cost
        - **Extreme Outlier:** One user driving nearly 30% of total usage
        - **Service Imbalance:** GTP users showing low utilization (77 interactions/user)
        - **Service Imbalance:** GTP users showing low utilisation (77 interactions/user)
        
        ### Recommendation
        """)
@@ -424,7 +423,7 @@
    "📊 Overview Dashboard", 
    "💡 Insights Engine", 
    "🤖 AI Discovery Bot", 
    "⚙️ Decision Optimizer", 
    "⚙️ Decision Optimiser", 
    "📄 Report Generator"
])

@@ -442,21 +441,3 @@

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
