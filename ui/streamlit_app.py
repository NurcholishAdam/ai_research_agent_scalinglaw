# -*- coding: utf-8 -*-
"""
Streamlit Web Interface for AI Research Agent - Phase 5 User Experience
Provides interactive web interface with real-time progress tracking
"""

import streamlit as st
import asyncio
import json
import time
from datetime import datetime
from typing import Dict, Any, List
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

# Import our research agent
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.research_agent import create_agent
from memory.advanced_memory_manager import AdvancedMemoryManager
from tools.research_tools_manager import get_research_tools_manager

class StreamlitResearchInterface:
    """Streamlit interface for the research agent"""
    
    def __init__(self):
        self.setup_page_config()
        self.initialize_session_state()
        
    def setup_page_config(self):
        """Configure Streamlit page"""
        st.set_page_config(
            page_title="AI Research Agent",
            page_icon="🔬",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS
        st.markdown("""
        <style>
        .main-header {
            font-size: 3rem;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 2rem;
        }
        .research-card {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
        .progress-container {
            background-color: #ffffff;
            padding: 1rem;
            border-radius: 0.5rem;
            border: 1px solid #e0e0e0;
        }
        .metric-card {
            background-color: #ffffff;
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
    
    def initialize_session_state(self):
        """Initialize Streamlit session state"""
        if 'research_history' not in st.session_state:
            st.session_state.research_history = []
        if 'current_research' not in st.session_state:
            st.session_state.current_research = None
        if 'research_progress' not in st.session_state:
            st.session_state.research_progress = {}
        if 'memory_manager' not in st.session_state:
            st.session_state.memory_manager = AdvancedMemoryManager()
    
    def render_header(self):
        """Render the main header"""
        st.markdown('<h1 class="main-header">🔬 AI Research Agent</h1>', unsafe_allow_html=True)
        st.markdown("### The Most Advanced AI Research Intelligence System")
        
        # Feature highlights
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("🧠 **Multi-Agent Intelligence**")
        with col2:
            st.markdown("🔬 **Hypothesis Testing**")
        with col3:
            st.markdown("📊 **Quality Assessment**")
        with col4:
            st.markdown("🌐 **Multi-Source Research**")
    
    def render_sidebar(self):
        """Render the sidebar with controls and information"""
        with st.sidebar:
            st.header("🎛️ Research Controls")
            
            # Research configuration
            st.subheader("Configuration")
            research_depth = st.selectbox(
                "Research Depth",
                ["Quick", "Standard", "Comprehensive"],
                index=1
            )
            
            enable_hypothesis = st.checkbox("Enable Hypothesis Generation", value=True)
            enable_multi_agent = st.checkbox("Enable Multi-Agent Analysis", value=True)
            enable_visualization = st.checkbox("Generate Visualizations", value=True)
            
            st.divider()
            
            # Memory statistics
            st.subheader("📊 Memory Statistics")
            try:
                stats = st.session_state.memory_manager.hierarchical_memory.get_memory_statistics()
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Short-term", stats.get('short_term_count', 0))
                    st.metric("Episodes", stats.get('episodic_count', 0))
                with col2:
                    st.metric("Long-term", stats.get('long_term_count', 0))
                    st.metric("Concepts", stats.get('concepts_tracked', 0))
                    
            except Exception as e:
                st.error(f"Memory stats error: {e}")
            
            st.divider()
            
            # Research history
            st.subheader("📚 Recent Research")
            if st.session_state.research_history:
                for i, research in enumerate(st.session_state.research_history[-5:]):
                    with st.expander(f"Research {len(st.session_state.research_history) - i}"):
                        st.write(f"**Question:** {research['question'][:100]}...")
                        st.write(f"**Quality Score:** {research.get('quality_score', 'N/A')}")
                        st.write(f"**Date:** {research.get('timestamp', 'Unknown')}")
            else:
                st.info("No research history yet")
            
            return {
                'depth': research_depth,
                'hypothesis': enable_hypothesis,
                'multi_agent': enable_multi_agent,
                'visualization': enable_visualization
            }
    
    def render_research_input(self):
        """Render the research input section"""
        st.header("🔍 Start New Research")
        
        # Research question input
        research_question = st.text_area(
            "Enter your research question:",
            placeholder="e.g., What are the latest developments in quantum computing and their potential applications?",
            height=100
        )
        
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            start_research = st.button("🚀 Start Research", type="primary", use_container_width=True)
        
        with col2:
            if st.button("💡 Get Suggestions", use_container_width=True):
                self.show_research_suggestions()
        
        with col3:
            if st.button("🛠️ Tool Guide", use_container_width=True):
                self.show_tool_guide()
        
        return research_question, start_research
    
    def show_research_suggestions(self):
        """Show research question suggestions"""
        suggestions = [
            "What are the ethical implications of AI in healthcare?",
            "How do different renewable energy technologies compare in efficiency?",
            "What are the latest breakthroughs in quantum computing?",
            "How does climate change affect global food security?",
            "What are the emerging trends in cybersecurity?",
            "How do different economic models predict inflation?",
            "What are the competing theories about consciousness?",
            "How does social media impact mental health?"
        ]
        
        st.info("💡 **Research Question Suggestions:**\n\n" + "\n".join([f"• {s}" for s in suggestions]))
    
    def show_tool_guide(self):
        """Show tool usage guide"""
        st.info("""
        🛠️ **Research Tools Available:**
        
        **Web Research:**
        • DuckDuckGo Search - Current information
        • Wikipedia - Background knowledge
        • arXiv - Academic papers
        • News Search - Latest developments
        
        **Document Processing:**
        • PDF Analysis - Extract and analyze documents
        • Structure Analysis - Organize content
        
        **Intelligence Layer:**
        • Multi-Agent Analysis - Multiple perspectives
        • Hypothesis Testing - Scientific validation
        • Quality Assessment - Credibility scoring
        """)
    
    def run_research_with_progress(self, question: str, config: Dict[str, Any]):
        """Run research with real-time progress tracking"""
        
        # Initialize progress tracking
        progress_container = st.container()
        status_container = st.container()
        
        with progress_container:
            st.header("🔄 Research Progress")
            
            # Progress bars
            overall_progress = st.progress(0)
            current_step_progress = st.progress(0)
            
            # Status indicators
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                planning_status = st.empty()
            with col2:
                research_status = st.empty()
            with col3:
                intelligence_status = st.empty()
            with col4:
                synthesis_status = st.empty()
        
        with status_container:
            status_text = st.empty()
            current_step_text = st.empty()
        
        try:
            # Create agent
            agent = create_agent()
            
            # Initialize state
            initial_state = {
                "messages": [],
                "research_question": question,
                "research_plan": [],
                "current_step": 0,
                "findings": [],
                "final_answer": "",
                "iteration_count": 0,
                "hypotheses": [],
                "multi_agent_analysis": {},
                "quality_assessment": {},
                "intelligence_insights": {}
            }
            
            # Update progress - Planning
            planning_status.success("📋 Planning")
            status_text.info("🧠 Creating research plan...")
            overall_progress.progress(0.1)
            
            # Run research with progress updates
            result = self.execute_research_with_updates(
                agent, initial_state, 
                overall_progress, current_step_progress,
                status_text, current_step_text,
                research_status, intelligence_status, synthesis_status
            )
            
            # Final progress update
            overall_progress.progress(1.0)
            current_step_progress.progress(1.0)
            status_text.success("✅ Research completed successfully!")
            
            # Update status indicators
            planning_status.success("✅ Planning")
            research_status.success("✅ Research")
            intelligence_status.success("✅ Intelligence")
            synthesis_status.success("✅ Synthesis")
            
            return result
            
        except Exception as e:
            st.error(f"Research failed: {str(e)}")
            return None
    
    def execute_research_with_updates(self, agent, initial_state, 
                                    overall_progress, step_progress,
                                    status_text, step_text,
                                    research_status, intelligence_status, synthesis_status):
        """Execute research with real-time updates"""
        
        # This is a simplified version - in a real implementation,
        # you'd need to modify the agent to provide progress callbacks
        
        status_text.info("🔍 Executing research steps...")
        overall_progress.progress(0.3)
        research_status.warning("🔄 Research")
        
        # Simulate research execution with progress
        for i in range(3):
            step_text.info(f"Step {i+1}: Analyzing research question...")
            step_progress.progress((i+1)/3)
            time.sleep(1)  # Simulate processing time
        
        # Intelligence analysis
        status_text.info("🧠 Running intelligence analysis...")
        overall_progress.progress(0.7)
        intelligence_status.warning("🔄 Intelligence")
        time.sleep(2)
        
        # Synthesis
        status_text.info("🎯 Synthesizing final answer...")
        overall_progress.progress(0.9)
        synthesis_status.warning("🔄 Synthesis")
        time.sleep(1)
        
        # Execute the actual research
        result = agent.invoke(initial_state)
        
        return result
    
    def render_research_results(self, result: Dict[str, Any], question: str):
        """Render comprehensive research results"""
        
        st.header("📊 Research Results")
        
        # Research overview
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Research Steps", len(result.get("findings", [])))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            quality_score = result.get("quality_assessment", {}).get("overall_quality_score", "N/A")
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Quality Score", f"{quality_score}/10" if quality_score != "N/A" else "N/A")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            hypotheses_count = len(result.get("hypotheses", []))
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Hypotheses", hypotheses_count)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            confidence = result.get("quality_assessment", {}).get("confidence_assessment", "N/A")
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Confidence", f"{confidence:.2f}" if confidence != "N/A" else "N/A")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Tabs for different result sections
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📝 Final Answer", 
            "🔬 Research Process", 
            "🧠 Intelligence Analysis", 
            "📊 Visualizations",
            "📋 Export"
        ])
        
        with tab1:
            self.render_final_answer(result)
        
        with tab2:
            self.render_research_process(result)
        
        with tab3:
            self.render_intelligence_analysis(result)
        
        with tab4:
            self.render_visualizations(result, question)
        
        with tab5:
            self.render_export_options(result, question)
    
    def render_final_answer(self, result: Dict[str, Any]):
        """Render the final answer section"""
        st.subheader("🎯 Final Answer")
        
        final_answer = result.get("final_answer", "No final answer generated")
        
        # Display final answer in a nice format
        st.markdown('<div class="research-card">', unsafe_allow_html=True)
        st.markdown(final_answer)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Answer quality indicators
        quality_assessment = result.get("quality_assessment", {})
        if quality_assessment:
            st.subheader("📊 Answer Quality Assessment")
            
            col1, col2 = st.columns(2)
            
            with col1:
                quality_indicators = quality_assessment.get("quality_indicators", {})
                st.write("**Quality Indicators:**")
                for indicator, status in quality_indicators.items():
                    icon = "✅" if status else "❌"
                    st.write(f"{icon} {indicator.replace('_', ' ').title()}")
            
            with col2:
                st.write("**Research Metrics:**")
                st.write(f"• Total Findings: {quality_assessment.get('total_findings', 0)}")
                st.write(f"• External Sources: {quality_assessment.get('external_sources_used', 0)}")
                st.write(f"• Source Diversity: {quality_assessment.get('source_diversity', 0)}")
    
    def render_research_process(self, result: Dict[str, Any]):
        """Render the research process section"""
        st.subheader("🔍 Research Process")
        
        # Research plan
        research_plan = result.get("research_plan", [])
        if research_plan:
            st.write("**Research Plan:**")
            for i, step in enumerate(research_plan, 1):
                st.write(f"{i}. {step}")
        
        st.divider()
        
        # Research findings
        findings = result.get("findings", [])
        if findings:
            st.write("**Research Findings:**")
            
            for finding in findings:
                with st.expander(f"Step {finding['step'] + 1}: {finding['step_description']}"):
                    
                    # Analysis
                    analysis = finding.get("analysis", "")
                    if "KEY_FINDINGS:" in analysis:
                        key_findings = analysis.split("KEY_FINDINGS:")[1].split("NEW_CONCEPTS:")[0].strip()
                        st.write("**Key Findings:**")
                        st.write(key_findings)
                    
                    # Sources used
                    sources_used = finding.get("sources_used", {})
                    if sources_used:
                        st.write("**Sources Used:**")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Memory", sources_used.get("memory_basic", 0))
                        with col2:
                            st.metric("Advanced Memory", sources_used.get("memory_advanced", 0))
                        with col3:
                            st.metric("External", sources_used.get("external_sources", 0))
                    
                    # External research preview
                    external_research = finding.get("external_research", [])
                    if external_research:
                        st.write("**External Research:**")
                        for research in external_research[:2]:
                            st.write(f"• {research[:100]}...")
    
    def render_intelligence_analysis(self, result: Dict[str, Any]):
        """Render the intelligence analysis section"""
        st.subheader("🧠 Intelligence Layer Analysis")
        
        # Multi-agent analysis
        multi_agent_analysis = result.get("multi_agent_analysis", {})
        if multi_agent_analysis:
            st.write("**Multi-Agent Collaboration:**")
            
            # Confidence scores
            confidence_scores = multi_agent_analysis.get("confidence_scores", {})
            if confidence_scores:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Researcher", f"{confidence_scores.get('researcher_avg', 0):.2f}")
                with col2:
                    st.metric("Critic", f"{confidence_scores.get('critic_avg', 0):.2f}")
                with col3:
                    st.metric("Synthesizer", f"{confidence_scores.get('synthesis_confidence', 0):.2f}")
            
            # Collaboration summary
            collab_summary = multi_agent_analysis.get("collaboration_summary", {})
            if collab_summary:
                st.write("**Collaboration Summary:**")
                st.write(f"• Total Agent Responses: {collab_summary.get('total_agent_responses', 0)}")
                st.write(f"• Average Confidence: {collab_summary.get('average_confidence', 0):.2f}")
                
                quality_indicators = collab_summary.get("quality_indicators", {})
                for indicator, status in quality_indicators.items():
                    icon = "✅" if status else "❌"
                    st.write(f"{icon} {indicator.replace('_', ' ').title()}")
        
        st.divider()
        
        # Hypotheses
        hypotheses = result.get("hypotheses", [])
        if hypotheses:
            st.write("**Generated Hypotheses:**")
            
            for i, hypothesis in enumerate(hypotheses, 1):
                with st.expander(f"Hypothesis {i}: {hypothesis['statement'][:80]}..."):
                    st.write(f"**Type:** {hypothesis['type']}")
                    st.write(f"**Confidence:** {hypothesis['confidence']:.2f}")
                    
                    if hypothesis.get('supporting_evidence'):
                        st.write("**Supporting Evidence:**")
                        for evidence in hypothesis['supporting_evidence'][:3]:
                            st.write(f"• {evidence}")
                    
                    if hypothesis.get('predictions'):
                        st.write("**Predictions:**")
                        for prediction in hypothesis['predictions'][:3]:
                            st.write(f"• {prediction}")
    
    def render_visualizations(self, result: Dict[str, Any], question: str):
        """Render visualizations section"""
        st.subheader("📊 Research Visualizations")
        
        # Research process timeline
        self.create_research_timeline(result)
        
        st.divider()
        
        # Quality assessment radar chart
        self.create_quality_radar_chart(result)
        
        st.divider()
        
        # Source distribution
        self.create_source_distribution_chart(result)
    
    def create_research_timeline(self, result: Dict[str, Any]):
        """Create research process timeline"""
        st.write("**Research Process Timeline**")
        
        findings = result.get("findings", [])
        if not findings:
            st.info("No research steps to visualize")
            return
        
        # Create timeline data
        timeline_data = []
        for finding in findings:
            timeline_data.append({
                'step': finding['step'] + 1,
                'description': finding['step_description'],
                'sources': finding.get('sources_used', {}).get('external_sources', 0)
            })
        
        # Create timeline chart
        fig = go.Figure()
        
        steps = [item['step'] for item in timeline_data]
        descriptions = [item['description'][:50] + "..." for item in timeline_data]
        sources = [item['sources'] for item in timeline_data]
        
        fig.add_trace(go.Scatter(
            x=steps,
            y=[1] * len(steps),
            mode='markers+text',
            marker=dict(
                size=[20 + s*10 for s in sources],
                color=sources,
                colorscale='Blues',
                showscale=True,
                colorbar=dict(title="External Sources")
            ),
            text=descriptions,
            textposition="top center",
            name="Research Steps"
        ))
        
        fig.update_layout(
            title="Research Process Timeline",
            xaxis_title="Research Step",
            yaxis=dict(showticklabels=False, showgrid=False),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def create_quality_radar_chart(self, result: Dict[str, Any]):
        """Create quality assessment radar chart"""
        st.write("**Research Quality Assessment**")
        
        quality_assessment = result.get("quality_assessment", {})
        if not quality_assessment:
            st.info("No quality assessment data available")
            return
        
        # Quality metrics
        metrics = {
            'Completeness': min(quality_assessment.get('total_findings', 0) / 5 * 10, 10),
            'Source Diversity': min(quality_assessment.get('source_diversity', 0) / 4 * 10, 10),
            'External Validation': quality_assessment.get('external_sources_used', 0) / max(quality_assessment.get('total_findings', 1), 1) * 10,
            'Confidence': quality_assessment.get('confidence_assessment', 0) * 10,
            'Overall Quality': quality_assessment.get('overall_quality_score', 0)
        }
        
        # Create radar chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=list(metrics.values()),
            theta=list(metrics.keys()),
            fill='toself',
            name='Quality Metrics'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=True,
            title="Research Quality Radar Chart"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def create_source_distribution_chart(self, result: Dict[str, Any]):
        """Create source distribution chart"""
        st.write("**Source Distribution**")
        
        findings = result.get("findings", [])
        if not findings:
            st.info("No source data available")
            return
        
        # Aggregate source usage
        source_totals = {
            'Memory (Basic)': 0,
            'Memory (Advanced)': 0,
            'External Sources': 0
        }
        
        for finding in findings:
            sources_used = finding.get("sources_used", {})
            source_totals['Memory (Basic)'] += sources_used.get('memory_basic', 0)
            source_totals['Memory (Advanced)'] += sources_used.get('memory_advanced', 0)
            source_totals['External Sources'] += sources_used.get('external_sources', 0)
        
        # Create pie chart
        fig = go.Figure(data=[go.Pie(
            labels=list(source_totals.keys()),
            values=list(source_totals.values()),
            hole=.3
        )])
        
        fig.update_layout(
            title="Source Usage Distribution",
            annotations=[dict(text='Sources', x=0.5, y=0.5, font_size=20, showarrow=False)]
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_export_options(self, result: Dict[str, Any], question: str):
        """Render export options"""
        st.subheader("📋 Export Research Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📄 Export as PDF", use_container_width=True):
                self.export_as_pdf(result, question)
        
        with col2:
            if st.button("📊 Export as JSON", use_container_width=True):
                self.export_as_json(result, question)
        
        with col3:
            if st.button("📝 Export as Markdown", use_container_width=True):
                self.export_as_markdown(result, question)
        
        # Export preview
        st.subheader("📋 Export Preview")
        
        export_format = st.selectbox("Preview Format", ["Markdown", "JSON", "Summary"])
        
        if export_format == "Markdown":
            markdown_content = self.generate_markdown_report(result, question)
            st.code(markdown_content, language="markdown")
        
        elif export_format == "JSON":
            json_content = json.dumps(result, indent=2, default=str)
            st.code(json_content, language="json")
        
        elif export_format == "Summary":
            summary = self.generate_summary_report(result, question)
            st.markdown(summary)
    
    def export_as_pdf(self, result: Dict[str, Any], question: str):
        """Export research results as PDF"""
        st.info("PDF export functionality would be implemented here using reportlab")
    
    def export_as_json(self, result: Dict[str, Any], question: str):
        """Export research results as JSON"""
        json_str = json.dumps(result, indent=2, default=str)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name=f"research_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    
    def export_as_markdown(self, result: Dict[str, Any], question: str):
        """Export research results as Markdown"""
        markdown_content = self.generate_markdown_report(result, question)
        st.download_button(
            label="Download Markdown",
            data=markdown_content,
            file_name=f"research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown"
        )
    
    def generate_markdown_report(self, result: Dict[str, Any], question: str) -> str:
        """Generate markdown report"""
        report = f"""# Research Report

## Research Question
{question}

## Final Answer
{result.get('final_answer', 'No final answer generated')}

## Research Process
"""
        
        research_plan = result.get('research_plan', [])
        if research_plan:
            report += "\n### Research Plan\n"
            for i, step in enumerate(research_plan, 1):
                report += f"{i}. {step}\n"
        
        findings = result.get('findings', [])
        if findings:
            report += "\n### Key Findings\n"
            for finding in findings:
                report += f"\n#### Step {finding['step'] + 1}: {finding['step_description']}\n"
                analysis = finding.get('analysis', '')
                if 'KEY_FINDINGS:' in analysis:
                    key_findings = analysis.split('KEY_FINDINGS:')[1].split('NEW_CONCEPTS:')[0].strip()
                    report += f"{key_findings}\n"
        
        # Quality assessment
        quality_assessment = result.get('quality_assessment', {})
        if quality_assessment:
            report += f"\n## Quality Assessment\n"
            report += f"- Overall Quality Score: {quality_assessment.get('overall_quality_score', 'N/A')}/10\n"
            report += f"- Confidence Level: {quality_assessment.get('confidence_assessment', 'N/A')}\n"
            report += f"- Total Findings: {quality_assessment.get('total_findings', 0)}\n"
            report += f"- External Sources Used: {quality_assessment.get('external_sources_used', 0)}\n"
        
        report += f"\n---\n*Generated by AI Research Agent on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
        
        return report
    
    def generate_summary_report(self, result: Dict[str, Any], question: str) -> str:
        """Generate summary report"""
        quality_score = result.get('quality_assessment', {}).get('overall_quality_score', 'N/A')
        findings_count = len(result.get('findings', []))
        hypotheses_count = len(result.get('hypotheses', []))
        
        summary = f"""
        **Research Summary**
        
        **Question:** {question}
        
        **Key Metrics:**
        - Research Steps Completed: {findings_count}
        - Quality Score: {quality_score}/10
        - Hypotheses Generated: {hypotheses_count}
        
        **Final Answer Preview:**
        {result.get('final_answer', 'No final answer')[:300]}...
        """
        
        return summary
    
    def run(self):
        """Main application runner"""
        # Render header
        self.render_header()
        
        # Render sidebar and get configuration
        config = self.render_sidebar()
        
        # Main content area
        research_question, start_research = self.render_research_input()
        
        # Handle research execution
        if start_research and research_question.strip():
            with st.spinner("Initializing research agent..."):
                result = self.run_research_with_progress(research_question, config)
            
            if result:
                # Store in session state
                research_record = {
                    'question': research_question,
                    'result': result,
                    'timestamp': datetime.now().isoformat(),
                    'quality_score': result.get('quality_assessment', {}).get('overall_quality_score', 'N/A')
                }
                st.session_state.research_history.append(research_record)
                st.session_state.current_research = research_record
                
                # Render results
                self.render_research_results(result, research_question)
        
        # Show current research if available
        elif st.session_state.current_research:
            st.header("📊 Current Research Results")
            current = st.session_state.current_research
            self.render_research_results(current['result'], current['question'])

def main():
    """Main function to run the Streamlit app"""
    app = StreamlitResearchInterface()
    app.run()

if __name__ == "__main__":
    main()