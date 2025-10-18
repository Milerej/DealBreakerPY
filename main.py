import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Gartner Contract Evaluation Platform",
    page_icon="📊",
    layout="wide"
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
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Header
st.markdown("""
<div class="main-header">
    <h1>📊 Gartner Contract Evaluation Platform</h1>
    <p>Intelligent analytics for procurement decision-making</p>
</div>
""", unsafe_allow_html=True)

# Sample data function (embedded for now)
@st.cache_data
def get_sample_data():
    """Get sample user data"""
    return pd.DataFrame({
        'User': ['Ace Tan (CISO)', 'Dom Chan', 'YZ Feng (CDAO)', 'Chan Vivi', 'Wang JH', 
                'Sally', 'GPD Ng', 'P En', 'Andrew Ng', 'Frank Liew'],
        'Documents': [1749, 559, 300, 261, 209, 174, 72, 156, 43, 36],
        'Calls': [47, 31, 22, 0, 13, 7, 36, 8, 0, 0],
        'Conferences': [14, 1, 7, 1, 0, 1, 2, 3, 0, 0],
        'Total_Activity': [1810, 591, 329, 262, 222, 182, 110, 167, 43, 36],
        'Department': ['CISO Office', 'IT Leadership', 'IT Leadership', 'Strategy', 'SNDGO', 
                      'Strategy', 'IT', 'SNDGO', 'GTP', 'GTP']
    })

# Basic Overview Dashboard Function
def render_overview():
    st.header("📊 Overview Dashboard")
    
    # Key Metrics Row
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
        <div class="metric-card-danger">
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
    
    st.markdown("---")
    
    # Usage Analysis Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Usage Analysis (Aug 2023 - Mar 2025)")
        
        st.markdown("""
        **Total Activity:** 6,524 interactions  
        **Document Downloads:** 6,170 reports  
        **Analyst Calls:** 306 consultations  
        **Conference Sessions:** 48 attendances  
        
        **Peak Months:** March (Budget Planning), September (Strategy Reviews)  
        **Activity Distribution:** 94.6% docs, 4.7% calls, 0.7% conferences
        """)
    
    with col2:
        st.subheader("👥 Top User Analysis")
        
        # Load and display user data
        user_data = get_sample_data()
        st.dataframe(
            user_data[['User', 'Documents', 'Calls', 'Conferences', 'Total_Activity']],
            use_container_width=True,
            hide_index=True
        )
        
        st.caption("Top 5 users account for 54% of total activity")
    
    # Budget Crisis Alert
    st.markdown("""
    <div class="alert-danger">
        <strong>⚠️ Budget Variance Alert:</strong> Actual spending $3.9M vs $3.5M contracted (11% over budget)<br>
        <strong>🚨 BUDGET EMERGENCY:</strong> $3.9M spent in 20 months vs $1.95M expected (100% over pace)<br>
        <strong>Projected Final Cost:</strong> $7.02M vs $3.5M contracted without intervention
    </div>
    """, unsafe_allow_html=True)
    
    # Service Plan Analysis
    st.subheader("📊 Service Plan Utilization Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Gartner for CISOs")
        st.write("**Users:** 1 (Ace Tan)")
        st.write("**Total Activity:** 1,810 interactions")
        st.write("**Per-User Avg:** 1,810/user")
        st.progress(1.0)
        st.success("✅ Exceptional Value")
        st.caption("Single power user with extreme high usage (91 interactions/month)")
    
    with col2:
        st.markdown("#### Executive Programs")
        st.write("**Users:** 6 (Leadership Team)")
        st.write("**Total Activity:** 1,459 interactions")
        st.write("**Per-User Avg:** 243/user")
        st.progress(0.65)
        st.warning("⚠️ Mixed Performance")
        st.caption("High variance - Dom Chan (591) vs others (~50-300)")
    
    with col3:
        st.markdown("#### Technical Professionals (GTP)")
        st.write("**Users:** 24 (SMB EA team)")
        st.write("**Total Activity:** 1,847 interactions")
        st.write("**Per-User Avg:** 77/user")
        st.progress(0.2)
        st.error("🚨 Needs Restructuring")
        st.caption("Low per-user utilization suggests over-provisioning")

# Basic Insights Function
def render_insights():
    st.header("💡 Insights Engine")
    
    st.markdown("""
    <div class="alert-info">
        <strong>Management Summary:</strong> Key insights to guide procurement decisions and budget optimization
    </div>
    """, unsafe_allow_html=True)
    
    # Value vs Cost Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Are Users Getting Value?")
        st.markdown("""
        <div class="alert-success">
            <strong>✅ YES - Strong Value Perception</strong><br>
            • 76% of users rate Gartner as "useful" or "very useful"<br>
            • High engagement: 326 interactions/month average<br>
            • Power users like Ace Tan show exceptional usage (91/month)
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Does Value Justify $3.9M Cost?")
        st.markdown("""
        <div class="alert-warning">
            <strong>⚠️ QUESTIONABLE - High Cost Per Unit</strong><br>
            • Cost per download: $632 vs industry benchmark ~$50-100<br>
            • Cost per interaction: $598 (very premium pricing)<br>
            • Total cost 100% over expected budget pace
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Budget Crisis Reality")
        st.markdown("""
        <div class="alert-danger">
            <strong>🚨 BUDGET EMERGENCY: $3.9M in 20 months</strong><br>
            • Contract pace: 100% over budget ($1.95M expected)<br>
            • GT Segment: $3.1M vs $1.56M expected<br>
            • SNDGO Segment: $0.8M vs $0.39M expected
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Immediate Actions Required:")
        st.markdown("""
        - **Emergency:** Implement spend controls immediately
        - **User limits:** Cap high-usage outliers (Ace Tan: 28% of usage)
        - **Budget review:** Need $7M+ total funding or service cuts
        """)

# Basic AI Bot Function
def render_ai_bot():
    st.header("🤖 AI Discovery Bot")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Quick Questions")
        
        if st.button("Show me departments with highest ROI", key="roi_btn"):
            st.session_state.last_response = "The departments with highest ROI are: 1) CISO Office (exceptional usage), 2) IT Leadership (high engagement), 3) Strategy Team (consistent usage). CISO Office shows exceptional value due to Ace Tan's intensive usage pattern."
        
        if st.button("What alternatives do users prefer?", key="alt_btn"):
            st.session_state.last_response = "Survey data shows 34% prefer alternatives: Forrester (18%), IDC (12%), McKinsey (4%). Main reasons: cost concerns (67%), content overlap (23%), user interface preferences (32%)."
        
        if st.button("Analyse cost trends over time", key="cost_btn"):
            st.session_state.last_response = "Cost trends show 100% increase over expected pace. Usage peaks during Q1 budget cycles and Q3 strategic planning periods. Current trajectory unsustainable without intervention."
        
        if st.button("Which content types drive most value?", key="content_btn"):
            st.session_state.last_response = "Document downloads drive 94.6% of activity, analyst calls 4.7%, conferences 0.7%. High-value users prefer direct research access over events. Cost per interaction varies dramatically by service type."
    
    with col2:
        st.subheader("AI Chat Interface")
        
        # Chat input
        user_input = st.text_input("Ask me about your Gartner data...", key="chat_input")
        
        if st.button("Send", key="send_btn") and user_input:
            st.session_state.last_response = f"Based on your question about '{user_input}', I can analyse the data patterns. The key insight is that your usage shows extreme concentration with Ace Tan driving 28% of total activity, suggesting either exceptional value extraction or potential account sharing that needs investigation."
        
        # Display response
        if hasattr(st.session_state, 'last_response'):
            st.markdown("**AI Assistant:**")
            st.info(st.session_state.last_response)

# Basic Optimizer Function
def render_optimizer():
    st.header("⚙️ Decision Optimizer")
    
    st.subheader("Scenario Planning Tool")
    
    col1, col2 = st.columns(2)
    
    with col1:
        budget_constraint = st.selectbox(
            "Budget Constraint",
            ["Current Trajectory ($3.9M → $7.02M)", "Budget Cap at $3.5M (67% usage cut)", "Moderate Control ($5M budget)"],
            key="budget_select"
        )
        
        seat_strategy = st.selectbox(
            "User Allocation Strategy",
            ["Maintain Current (38 users)", "Remove Low Users (15 users)", "Premium Only (8 high-value users)"],
            key="seat_select"
        )
        
        contract_term = st.selectbox("Contract Term", ["1 Year", "2 Years", "3 Years"], key="term_select")
    
    with col2:
        st.subheader("Scenario Analysis Results")
        
        if "Premium Only" in seat_strategy:
            st.markdown("""
            <div class="alert-success">
                <strong>Recommended:</strong> Premium users only<br>
                <strong>Savings:</strong> $2.2M annually<br>
                <strong>Risk Level:</strong> Low
            </div>
            """, unsafe_allow_html=True)
        elif "Budget Cap" in budget_constraint:
            st.markdown("""
            <div class="alert-warning">
                <strong>Strategy:</strong> Implement strict usage controls<br>
                <strong>Cost:</strong> $3.5M (within budget)<br>
                <strong>Risk Level:</strong> Moderate
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="alert-danger">
                <strong>Strategy:</strong> Current trajectory unsustainable<br>
                <strong>Cost:</strong> $7.02M projected<br>
                <strong>Risk Level:</strong> Critical
            </div>
            """, unsafe_allow_html=True)

# Basic Reports Function
def render_reports():
    st.header("📄 Report Generator")
    
    # Report Configuration
    report_type = st.selectbox(
        "Report Type",
        ["TAC 'B' Approval Report", "Contract Renewal Analysis", "Provider Comparison Study"],
        key="report_type_select"
    )
    
    # Report sections
    st.subheader("Include Sections")
    sections = st.multiselect(
        "Select sections to include:",
        ["Executive Summary", "Usage Analysis", "Cost-Benefit Analysis", "Risk Assessment", 
         "Recommendations", "Detailed Metrics", "Survey Results", "Benchmarking"],
        default=["Executive Summary", "Usage Analysis", "Cost-Benefit Analysis", "Recommendations"],
        key="sections_select"
    )
    
    # Generate Report Button
    if st.button("Generate Report", key="generate_btn"):
        st.subheader("Report Preview")
        
        st.markdown(f"""
        ## {report_type}
        
        ### Executive Summary
        Based on comprehensive analysis of usage data, user feedback, and market comparisons, 
        this report recommends **emergency budget controls** for the Gartner research services contract.
        
        ### Key Findings
        - **Budget Crisis:** $3.9M spent vs $1.95M expected (100% overrun)
        - **Usage Concentration:** Single user (Ace Tan) consuming 28% of contract value
        - **User Satisfaction:** 4.1/5 average rating with 76% finding service useful
        - **Cost Efficiency:** $632 per download (significantly above benchmark)
        
        ### Critical Issues
        - **Unsustainable Spending:** Current trajectory leads to $7.02M total cost
        - **Extreme Outlier:** One user driving nearly 30% of total usage
        - **Service Imbalance:** GTP users showing low utilisation (77 interactions/user)
        
        ### Recommendation
        """)
        
        st.markdown("""
        <div class="alert-danger">
            <strong>IMMEDIATE ACTION REQUIRED:</strong><br>
            • Implement emergency spending caps within 30 days<br>
            • Investigate Ace Tan's usage pattern for business justification<br>
            • Restructure to premium user model (8 high-value users)<br>
            • Projected savings: $2.2M annually vs current trajectory
        </div>
        """, unsafe_allow_html=True)
        
        # Export buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("📄 Export to PDF", key="pdf_btn")
        with col2:
            st.button("📊 Export to Excel", key="excel_btn")
        with col3:
            st.button("✅ Submit for Approval", key="submit_btn")

# Navigation using tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview Dashboard", 
    "💡 Insights Engine", 
    "🤖 AI Discovery Bot", 
    "⚙️ Decision Optimiser", 
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
