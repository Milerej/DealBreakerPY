import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Gartner Contract Evaluation Platform",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #1e40af, #3b82f6);
        color: white;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
    }
    .alert-danger {
        background-color: #fef2f2;
        border: 1px solid #fecaca;
        color: #dc2626;
        padding: 15px;
        border-radius: 6px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("📊 Gartner Contract Evaluation Platform")
st.markdown("*Intelligent analytics for procurement decision-making*")

# Sidebar navigation
tab_selection = st.sidebar.selectbox(
    "Navigate to:",
    ["Overview Dashboard", "Insights Engine", "AI Discovery Bot", "Decision Optimizer", "Report Generator"]
)

# Sample data (you'd replace this with your actual data)
@st.cache_data
def load_data():
    # Mock data based on your HTML
    usage_data = {
        'User': ['Ace Tan (CISO)', 'Dom Chan', 'YZ Feng (CDAO)', 'Chan Vivi', 'Wang JH'],
        'Documents': [1749, 559, 300, 261, 209],
        'Calls': [47, 31, 22, 0, 13],
        'Conferences': [14, 1, 7, 1, 0],
        'Total_Activity': [1810, 591, 329, 262, 222]
    }
    return pd.DataFrame(usage_data)

def overview_dashboard():
    st.header("Overview Dashboard")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>38</h2>
            <p>Licensed Users</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>68%</h2>
            <p>Active Users (26 of 38)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #dc2626, #ef4444);">
            <h2>$632</h2>
            <p>Cost per Download</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2>4.1</h2>
            <p>User Satisfaction (5.0 scale)</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Usage Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Usage Analysis (Aug 2023 - Mar 2025)")
        st.write("**Total Activity:** 6,524 interactions")
        st.write("**Document Downloads:** 6,170 reports")
        st.write("**Analyst Calls:** 306 consultations")
        st.write("**Conference Sessions:** 48 attendances")
        
        # Create a simple chart
        activity_data = {
            'Type': ['Documents', 'Calls', 'Conferences'],
            'Count': [6170, 306, 48],
            'Percentage': [94.6, 4.7, 0.7]
        }
        fig = px.pie(pd.DataFrame(activity_data), values='Count', names='Type', 
                     title="Activity Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("👥 Top User Analysis")
        df = load_data()
        st.dataframe(df, use_container_width=True)
    
    # Budget Crisis Alert
    st.markdown("""
    <div class="alert-danger">
        <strong>🚨 BUDGET EMERGENCY: $3.9M in 20 months</strong><br>
        Contract pace: 100% over budget ($1.95M expected)<br>
        Projected final cost: $7.02M vs $3.5M contracted
    </div>
    """, unsafe_allow_html=True)

def insights_engine():
    st.header("💡 Insights Engine")
    
    st.info("**Management Summary:** Key insights to guide procurement decisions and budget optimization")
    
    # Value vs Cost Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Are Users Getting Value?")
        st.success("✅ YES - Strong Value Perception\n• 76% of users rate Gartner as useful\n• High engagement: 326 interactions/month average")
        
        st.subheader("Does Value Justify $3.9M Cost?")
        st.warning("⚠️ QUESTIONABLE - High Cost Per Unit\n• Cost per download: $632 vs benchmark $50-100\n• Total cost 100% over expected budget pace")
    
    with col2:
        st.subheader("Budget Crisis Reality")
        st.error("🚨 BUDGET EMERGENCY: $3.9M in 20 months\n• Contract pace: 100% over budget\n• Need $7M+ total funding or service cuts")

def ai_discovery_bot():
    st.header("🤖 AI Discovery Bot")
    
    # Quick Questions
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Quick Questions")
        if st.button("Show me departments with highest ROI"):
            st.session_state.chat_response = "The departments with highest ROI are: 1) Strategy Team (4.2:1 ratio), 2) IT Department (3.8:1 ratio), 3) Business Development (3.4:1 ratio)."
        
        if st.button("What alternatives do users prefer?"):
            st.session_state.chat_response = "Survey data shows 34% prefer alternatives: Forrester (18%), IDC (12%), McKinsey (4%). Main reasons: cost concerns (45%)."
        
        if st.button("Analyze cost trends over time"):
            st.session_state.chat_response = "Cost trends show 12% increase over 3 years, but value per dollar has improved 23%. Usage peaks during Q1 budget cycles."
    
    with col2:
        st.subheader("AI Chat Interface")
        
        # Chat input
        user_input = st.text_input("Ask me about your Gartner data...")
        
        if user_input:
            st.session_state.chat_response = f"Based on your question about '{user_input}', I can analyze the data patterns and provide insights."
        
        # Display response
        if hasattr(st.session_state, 'chat_response'):
            st.write("**AI Assistant:**", st.session_state.chat_response)

def decision_optimizer():
    st.header("⚙️ Decision Optimizer")
    
    # Scenario Planning
    st.subheader("Scenario Planning Tool")
    
    col1, col2 = st.columns(2)
    
    with col1:
        budget_constraint = st.selectbox(
            "Budget Constraint",
            ["Current Trajectory ($3.9M → $7.02M)", "Budget Cap at $3.5M (67% usage cut)", "Moderate Control ($5M budget)"]
        )
        
        seat_strategy = st.selectbox(
            "User Allocation Strategy",
            ["Maintain Current (38 users)", "Remove Low Users (15 users)", "Premium Only (8 high-value users)"]
        )
        
        contract_term = st.selectbox("Contract Term", ["1 Year", "2 Years", "3 Years"])
    
    with col2:
        st.subheader("Scenario Analysis Results")
        
        if "Premium Only" in seat_strategy:
            st.success("**Recommended:** Premium users only\n**Savings:** $2.2M annually\n**Risk Level:** Low")
        elif "Budget Cap" in budget_constraint:
            st.warning("**Strategy:** Implement strict usage controls\n**Cost:** $3.5M (within budget)\n**Risk Level:** Moderate")
        else:
            st.error("**Strategy:** Current trajectory unsustainable\n**Cost:** $7.02M projected\n**Risk Level:** Critical")

def report_generator():
    st.header("📄 Report Generator")
    
    # Report Configuration
    report_type = st.selectbox(
        "Report Type",
        ["TAC 'B' Approval Report", "Contract Renewal Analysis", "Provider Comparison Study"]
    )
    
    # Report sections
    st.subheader("Include Sections")
    sections = st.multiselect(
        "Select sections to include:",
        ["Executive Summary", "Usage Analysis", "Cost-Benefit Analysis", "Risk Assessment", 
         "Recommendations", "Detailed Metrics", "Survey Results", "Benchmarking"],
        default=["Executive Summary", "Usage Analysis", "Cost-Benefit Analysis", "Recommendations"]
    )
    
    # Generate Report Button
    if st.button("Generate Report"):
        st.subheader("Report Preview")
        
        st.markdown(f"""
        ## {report_type}
        
        ### Executive Summary
        Based on comprehensive analysis of usage data, user feedback, and market comparisons, 
        this report recommends continuation of Gartner research services with optimized seat allocation.
        
        ### Key Findings
        - **Utilization:** 68% active usage rate across 38 allocated seats
        - **Budget Crisis:** $3.9M spent vs $1.95M expected (100% overrun)
        - **User Satisfaction:** 4.1/5 average rating
        - **Cost per Download:** $632 (significantly above benchmark)
        
        ### Recommendation
        """)
        
        st.success("**Implement emergency budget controls with premium user model**\nProjected savings: $2.2M annually\nMaintained service quality for key users")
        
        # Export buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("📄 Export to PDF")
        with col2:
            st.button("📊 Export to Excel")
        with col3:
            st.button("✅ Submit for Approval")

# Main app logic
if tab_selection == "Overview Dashboard":
    overview_dashboard()
elif tab_selection == "Insights Engine":
    insights_engine()
elif tab_selection == "AI Discovery Bot":
    ai_discovery_bot()
elif tab_selection == "Decision Optimizer":
    decision_optimizer()
elif tab_selection == "Report Generator":
    report_generator()
