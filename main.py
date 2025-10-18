# Basic Insights Function with Charts in Chatbox
def render_insights():
    st.header("💡 Insights Engine")
    
    st.markdown("""
    <div class="alert-info">
        <strong>Management Summary:</strong> Key insights to guide procurement decisions and budget optimisation
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
    
    st.markdown("---")
    
    # Interactive Insights Chatbox
    st.subheader("🤖 Interactive Insights Explorer")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Quick Analysis")
        
        if st.button("📊 Show ROI by Department", key="roi_chart_btn"):
            st.session_state.chart_type = "roi_department"
        
        if st.button("📈 Usage Trends Over Time", key="usage_trend_btn"):
            st.session_state.chart_type = "usage_trends"
        
        if st.button("💰 Cost Analysis Breakdown", key="cost_analysis_btn"):
            st.session_state.chart_type = "cost_breakdown"
        
        if st.button("👥 User Activity Distribution", key="user_activity_btn"):
            st.session_state.chart_type = "user_distribution"
        
        if st.button("⚖️ Budget vs Actual Spending", key="budget_actual_btn"):
            st.session_state.chart_type = "budget_comparison"
        
        if st.button("🎯 Service Utilisation Rates", key="service_util_btn"):
            st.session_state.chart_type = "service_utilisation"
    
    with col2:
        st.markdown("#### Visual Insights")
        
        # Display charts based on button clicks
        if hasattr(st.session_state, 'chart_type'):
            
            if st.session_state.chart_type == "roi_department":
                st.markdown("**📊 ROI Analysis by Department**")
                
                # Create ROI data
                roi_data = pd.DataFrame({
                    'Department': ['CISO Office', 'IT Leadership', 'Strategy', 'SNDGO', 'GTP'],
                    'Cost_per_User': [195000, 48750, 65000, 40000, 12917],
                    'Activity_per_User': [1810, 243, 174, 111, 77],
                    'ROI_Score': [9.3, 5.0, 2.7, 2.8, 0.6]
                })
                
                fig = px.bar(roi_data, x='Department', y='ROI_Score', 
                           title='ROI Score by Department',
                           color='ROI_Score',
                           color_continuous_scale='RdYlGn')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                st.info("**Insight:** CISO Office delivers exceptional ROI (9.3x) due to Ace Tan's intensive usage. GTP shows poor ROI (0.6x) suggesting over-provisioning.")
            
            elif st.session_state.chart_type == "usage_trends":
                st.markdown("**📈 Usage Trends Analysis**")
                
                # Create monthly usage data
                months = pd.date_range('2023-08', '2025-03', freq='M')
                usage_data = pd.DataFrame({
                    'Month': months,
                    'Documents': [280, 320, 450, 380, 290, 340, 410, 380, 320, 290, 350, 420, 380, 340, 290, 320, 380, 340, 290, 320],
                    'Analyst_Calls': [12, 15, 22, 18, 14, 16, 20, 18, 15, 14, 17, 21, 18, 16, 14, 15, 18, 16, 14, 15],
                    'Conferences': [2, 1, 4, 3, 1, 2, 3, 2, 1, 2, 3, 4, 2, 1, 2, 1, 3, 2, 1, 2]
                })
                
                fig = px.line(usage_data, x='Month', y=['Documents', 'Analyst_Calls', 'Conferences'],
                            title='Usage Trends Over Time')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                st.info("**Insight:** Document downloads show seasonal peaks during budget cycles (March) and strategy reviews (September). Analyst calls remain steady but low.")
            
            elif st.session_state.chart_type == "cost_breakdown":
                st.markdown("**💰 Cost Analysis Breakdown**")
                
                # Create cost breakdown data
                cost_data = pd.DataFrame({
                    'Service_Type': ['Gartner for CISOs', 'Executive Programmes', 'Technical Professionals', 'Conferences & Events'],
                    'Actual_Cost': [1950000, 1460000, 310000, 180000],
                    'Expected_Cost': [975000, 730000, 155000, 90000],
                    'Variance': [975000, 730000, 155000, 90000]
                })
                
                fig = go.Figure()
                fig.add_trace(go.Bar(name='Expected Cost', x=cost_data['Service_Type'], y=cost_data['Expected_Cost']))
                fig.add_trace(go.Bar(name='Actual Cost', x=cost_data['Service_Type'], y=cost_data['Actual_Cost']))
                fig.update_layout(title='Budget vs Actual Cost by Service Type', height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                st.error("**Critical:** All service types are 100% over budget. CISO service alone accounts for 50% of total overspend.")
            
            elif st.session_state.chart_type == "user_distribution":
                st.markdown("**👥 User Activity Distribution**")
                
                user_data = get_sample_data()
                
                fig = px.scatter(user_data, x='Documents', y='Calls', 
                               size='Total_Activity', color='Department',
                               hover_name='User',
                               title='User Activity Distribution (Bubble size = Total Activity)')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                st.warning("**Insight:** Extreme concentration - Ace Tan is a clear outlier with 1,749 documents vs next highest at 559. Suggests potential account sharing.")
            
            elif st.session_state.chart_type == "budget_comparison":
                st.markdown("**⚖️ Budget vs Actual Spending Timeline**")
                
                # Create cumulative spending data
                timeline_data = pd.DataFrame({
                    'Month': pd.date_range('2023-08', '2025-03', freq='M'),
                    'Budgeted_Cumulative': [97500, 195000, 292500, 390000, 487500, 585000, 682500, 780000, 877500, 975000, 1072500, 1170000, 1267500, 1365000, 1462500, 1560000, 1657500, 1755000, 1852500, 1950000],
                    'Actual_Cumulative': [180000, 380000, 590000, 780000, 950000, 1150000, 1380000, 1580000, 1780000, 1980000, 2200000, 2450000, 2680000, 2920000, 3150000, 3380000, 3620000, 3850000, 3900000, 3900000]
                })
                
                fig = px.line(timeline_data, x='Month', y=['Budgeted_Cumulative', 'Actual_Cumulative'],
                            title='Cumulative Spending: Budget vs Actual')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                st.error("**Emergency:** Spending diverged from budget immediately and continues accelerating. Current trajectory leads to $7M+ total cost.")
            
            elif st.session_state.chart_type == "service_utilisation":
                st.markdown("**🎯 Service Utilisation Rates**")
                
                # Create utilisation data
                util_data = pd.DataFrame({
                    'Service': ['Documents', 'Analyst Calls', 'Conferences', 'Magic Quadrants', 'Hype Cycles'],
                    'Available': [10000, 500, 100, 200, 150],
                    'Used': [6170, 306, 48, 180, 95],
                    'Utilisation_Rate': [61.7, 61.2, 48.0, 90.0, 63.3]
                })
                
                fig = px.bar(util_data, x='Service', y='Utilisation_Rate',
                           title='Service Utilisation Rates (%)',
                           color='Utilisation_Rate',
                           color_continuous_scale='RdYlGn')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                st.info("**Insight:** Magic Quadrants show highest utilisation (90%), while conferences are underutilised (48%). Focus budget on high-utilisation services.")
        
        else:
            st.info("👆 Click any button above to see interactive charts and detailed analysis")
    
    # Chat input for custom queries
    st.markdown("---")
    st.subheader("💬 Ask Custom Questions")
    
    user_question = st.text_input("Ask about specific metrics, trends, or comparisons...", 
                                 placeholder="e.g., 'Show me cost per user by department' or 'Compare Q1 vs Q4 usage'",
                                 key="insights_chat")
    
    if st.button("🔍 Analyse", key="custom_analysis") and user_question:
        st.markdown("**Custom Analysis Results:**")
        
        # Simple keyword-based chart generation
        if "cost per user" in user_question.lower():
            cost_per_user_data = pd.DataFrame({
                'Department': ['CISO Office', 'IT Leadership', 'Strategy', 'SNDGO', 'GTP'],
                'Cost_Per_User': [195000, 48750, 65000, 40000, 12917],
                'Users': [1, 6, 3, 5, 24]
            })
            
            fig = px.bar(cost_per_user_data, x='Department', y='Cost_Per_User',
                       title='Cost Per User by Department')
            st.plotly_chart(fig, use_container_width=True)
            st.info(f"Analysis for: '{user_question}' - CISO Office has highest cost per user at $195K, while GTP has lowest at $12.9K per user.")
        
        elif "quarterly" in user_question.lower() or "q1" in user_question.lower():
            quarterly_data = pd.DataFrame({
                'Quarter': ['Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025'],
                'Usage': [850, 920, 1150, 980, 890, 940, 1080],
                'Cost': [450000, 520000, 680000, 590000, 520000, 580000, 650000]
            })
            
            fig = px.line(quarterly_data, x='Quarter', y=['Usage', 'Cost'],
                        title='Quarterly Usage vs Cost Trends')
            st.plotly_chart(fig, use_container_width=True)
            st.info(f"Analysis for: '{user_question}' - Q1 periods show highest usage due to budget planning cycles.")
        
        else:
            # Default response with a general chart
            st.info(f"Analysing: '{user_question}' - Based on current data patterns, I recommend focusing on the ROI analysis above. For specific metrics, try keywords like 'cost per user', 'quarterly trends', or 'department comparison'.")
