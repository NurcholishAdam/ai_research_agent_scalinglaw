# -*- coding: utf-8 -*-
"""
Gradio Web Interface for AI Research Agent - Phase 5 User Experience
Alternative web interface with focus on simplicity and sharing
"""

import gradio as gr
import json
import time
from datetime import datetime
from typing import Dict, Any, List, Tuple
import plotly.graph_objects as go
import plotly.express as px

# Import our research agent
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.research_agent import create_agent
from memory.advanced_memory_manager import AdvancedMemoryManager

class GradioResearchInterface:
    """Gradio interface for the research agent"""
    
    def __init__(self):
        self.agent = None
        self.memory_manager = AdvancedMemoryManager()
        self.research_history = []
    
    def initialize_agent(self):
        """Initialize the research agent"""
        if self.agent is None:
            self.agent = create_agent()
        return self.agent
    
    def conduct_research(self, question: str, enable_hypothesis: bool = True, 
                        enable_multi_agent: bool = True) -> Tuple[str, str, str, str]:
        """Conduct research and return results"""
        
        if not question.strip():
            return "Please enter a research question.", "", "", ""
        
        try:
            # Initialize agent
            agent = self.initialize_agent()
            
            # Prepare initial state
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
            
            # Execute research
            result = agent.invoke(initial_state)
            
            # Store in history
            research_record = {
                'question': question,
                'result': result,
                'timestamp': datetime.now().isoformat(),
                'quality_score': result.get('quality_assessment', {}).get('overall_quality_score', 'N/A')
            }
            self.research_history.append(research_record)
            
            # Format results for display
            final_answer = result.get("final_answer", "No final answer generated")
            
            # Research process summary
            research_plan = result.get("research_plan", [])
            findings = result.get("findings", [])
            
            process_summary = "## Research Process\n\n"
            process_summary += "### Research Plan:\n"
            for i, step in enumerate(research_plan, 1):
                process_summary += f"{i}. {step}\n"
            
            process_summary += f"\n### Findings Summary:\n"
            process_summary += f"- Total research steps completed: {len(findings)}\n"
            process_summary += f"- External sources consulted: {sum(1 for f in findings if f.get('external_research'))}\n"
            
            # Intelligence analysis summary
            intelligence_summary = "## Intelligence Analysis\n\n"
            
            # Multi-agent analysis
            multi_agent_analysis = result.get("multi_agent_analysis", {})
            if multi_agent_analysis:
                confidence_scores = multi_agent_analysis.get("confidence_scores", {})
                intelligence_summary += "### Multi-Agent Collaboration:\n"
                intelligence_summary += f"- Researcher Confidence: {confidence_scores.get('researcher_avg', 0):.2f}\n"
                intelligence_summary += f"- Critic Confidence: {confidence_scores.get('critic_avg', 0):.2f}\n"
                intelligence_summary += f"- Synthesizer Confidence: {confidence_scores.get('synthesis_confidence', 0):.2f}\n"
            
            # Hypotheses
            hypotheses = result.get("hypotheses", [])
            if hypotheses:
                intelligence_summary += "\n### Generated Hypotheses:\n"
                for i, hyp in enumerate(hypotheses, 1):
                    intelligence_summary += f"{i}. **{hyp['statement']}**\n"
                    intelligence_summary += f"   - Type: {hyp['type']}\n"
                    intelligence_summary += f"   - Confidence: {hyp['confidence']:.2f}\n\n"
            
            # Quality assessment
            quality_assessment = result.get("quality_assessment", {})
            quality_summary = "## Quality Assessment\n\n"
            
            if quality_assessment:
                quality_summary += f"- **Overall Quality Score:** {quality_assessment.get('overall_quality_score', 'N/A')}/10\n"
                quality_summary += f"- **Confidence Level:** {quality_assessment.get('confidence_assessment', 'N/A'):.2f}\n"
                quality_summary += f"- **Total Findings:** {quality_assessment.get('total_findings', 0)}\n"
                quality_summary += f"- **External Sources Used:** {quality_assessment.get('external_sources_used', 0)}\n"
                quality_summary += f"- **Source Diversity:** {quality_assessment.get('source_diversity', 0)}\n"
                
                quality_indicators = quality_assessment.get("quality_indicators", {})
                quality_summary += "\n### Quality Indicators:\n"
                for indicator, status in quality_indicators.items():
                    icon = "✅" if status else "❌"
                    quality_summary += f"{icon} {indicator.replace('_', ' ').title()}\n"
            
            return final_answer, process_summary, intelligence_summary, quality_summary
            
        except Exception as e:
            error_msg = f"Research failed: {str(e)}"
            return error_msg, "", "", ""
    
    def get_research_suggestions(self) -> List[str]:
        """Get research question suggestions"""
        return [
            "What are the ethical implications of AI in healthcare?",
            "How do different renewable energy technologies compare in efficiency?",
            "What are the latest breakthroughs in quantum computing?",
            "How does climate change affect global food security?",
            "What are the emerging trends in cybersecurity?",
            "How do different economic models predict inflation?",
            "What are the competing theories about consciousness?",
            "How does social media impact mental health?",
            "What are the potential applications of CRISPR gene editing?",
            "How do neural networks learn and make decisions?"
        ]
    
    def get_memory_statistics(self) -> str:
        """Get memory system statistics"""
        try:
            stats = self.memory_manager.hierarchical_memory.get_memory_statistics()
            
            stats_text = "## Memory System Statistics\n\n"
            stats_text += f"- **Short-term Memory:** {stats.get('short_term_count', 0)} items\n"
            stats_text += f"- **Long-term Memory:** {stats.get('long_term_count', 0)} items\n"
            stats_text += f"- **Episodic Memory:** {stats.get('episodic_count', 0)} episodes\n"
            stats_text += f"- **Knowledge Graph Nodes:** {stats.get('knowledge_graph_nodes', 0)}\n"
            stats_text += f"- **Knowledge Graph Edges:** {stats.get('knowledge_graph_edges', 0)}\n"
            stats_text += f"- **Concepts Tracked:** {stats.get('concepts_tracked', 0)}\n"
            stats_text += f"- **Citations Tracked:** {stats.get('citations_tracked', 0)}\n"
            
            return stats_text
            
        except Exception as e:
            return f"Error retrieving memory statistics: {str(e)}"
    
    def get_research_history(self) -> str:
        """Get research history summary"""
        if not self.research_history:
            return "No research history available."
        
        history_text = "## Recent Research History\n\n"
        
        for i, research in enumerate(self.research_history[-5:], 1):
            history_text += f"### Research {i}\n"
            history_text += f"- **Question:** {research['question']}\n"
            history_text += f"- **Quality Score:** {research.get('quality_score', 'N/A')}\n"
            history_text += f"- **Timestamp:** {research.get('timestamp', 'Unknown')}\n\n"
        
        return history_text
    
    def export_research_results(self, final_answer: str, process_summary: str, 
                               intelligence_summary: str, quality_summary: str) -> str:
        """Export research results as markdown"""
        
        if not final_answer or final_answer.startswith("Please enter") or final_answer.startswith("Research failed"):
            return "No research results to export."
        
        export_content = f"""# AI Research Agent - Research Report

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Final Answer

{final_answer}

{process_summary}

{intelligence_summary}

{quality_summary}

---

*This report was generated by the AI Research Agent - Phase 5 User Experience*
"""
        
        return export_content
    
    def create_interface(self):
        """Create the Gradio interface"""
        
        # Custom CSS
        css = """
        .gradio-container {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .research-header {
            text-align: center;
            color: #1f77b4;
            margin-bottom: 20px;
        }
        """
        
        with gr.Blocks(css=css, title="AI Research Agent") as interface:
            
            # Header
            gr.Markdown("""
            # 🔬 AI Research Agent
            ### The Most Advanced AI Research Intelligence System
            
            **Features:** Multi-Agent Collaboration • Hypothesis Testing • Quality Assessment • Multi-Source Research
            """)
            
            with gr.Tab("🔍 Research"):
                with gr.Row():
                    with gr.Column(scale=2):
                        research_question = gr.Textbox(
                            label="Research Question",
                            placeholder="Enter your research question here...",
                            lines=3,
                            max_lines=5
                        )
                        
                        with gr.Row():
                            enable_hypothesis = gr.Checkbox(
                                label="Enable Hypothesis Generation",
                                value=True
                            )
                            enable_multi_agent = gr.Checkbox(
                                label="Enable Multi-Agent Analysis",
                                value=True
                            )
                        
                        with gr.Row():
                            research_btn = gr.Button("🚀 Start Research", variant="primary")
                            suggestions_btn = gr.Button("💡 Get Suggestions")
                    
                    with gr.Column(scale=1):
                        gr.Markdown("### 🛠️ Research Tools Available")
                        gr.Markdown("""
                        **Web Research:**
                        • DuckDuckGo Search
                        • Wikipedia Integration
                        • arXiv Academic Papers
                        • News Search
                        
                        **Intelligence Layer:**
                        • Multi-Agent Analysis
                        • Hypothesis Testing
                        • Quality Assessment
                        """)
                
                # Research suggestions
                suggestions_output = gr.Textbox(
                    label="Research Question Suggestions",
                    visible=False,
                    lines=10
                )
                
                # Results tabs
                with gr.Tab("📝 Final Answer"):
                    final_answer_output = gr.Markdown(label="Final Answer")
                
                with gr.Tab("🔬 Research Process"):
                    process_output = gr.Markdown(label="Research Process")
                
                with gr.Tab("🧠 Intelligence Analysis"):
                    intelligence_output = gr.Markdown(label="Intelligence Analysis")
                
                with gr.Tab("📊 Quality Assessment"):
                    quality_output = gr.Markdown(label="Quality Assessment")
                
                with gr.Tab("📋 Export"):
                    export_output = gr.Textbox(
                        label="Exportable Report (Markdown)",
                        lines=20,
                        max_lines=30
                    )
                    export_btn = gr.Button("📄 Generate Export")
            
            with gr.Tab("📊 Memory & History"):
                with gr.Row():
                    with gr.Column():
                        memory_btn = gr.Button("🧠 Get Memory Statistics")
                        memory_output = gr.Markdown(label="Memory Statistics")
                    
                    with gr.Column():
                        history_btn = gr.Button("📚 Get Research History")
                        history_output = gr.Markdown(label="Research History")
            
            with gr.Tab("ℹ️ About"):
                gr.Markdown("""
                ## About AI Research Agent
                
                This is the most advanced AI research intelligence system ever built, featuring:
                
                ### 🧠 Intelligence Layer (Phase 4)
                - **Multi-Agent Collaboration**: Researcher, Critic, and Synthesizer agents
                - **Hypothesis Generation**: Automatic creation of testable hypotheses
                - **Quality Assessment**: Comprehensive research validation
                
                ### 🔬 Research Tools Arsenal (Phase 3)
                - **Web Research Suite**: DuckDuckGo, Wikipedia, arXiv, News
                - **Document Processing**: PDF analysis and structure extraction
                - **Data Visualization**: Charts, networks, and dashboards
                
                ### 🧠 Advanced Memory System (Phase 2)
                - **Hierarchical Memory**: Short-term, long-term, and episodic
                - **Knowledge Graphs**: Automatic concept relationship mapping
                - **Citation Tracking**: Source credibility and network analysis
                
                ### 🎯 Core Capabilities (Phase 1)
                - **Structured Research**: Multi-step planning and execution
                - **ReAct Pattern**: Reasoning and acting in structured loops
                - **Memory Integration**: Persistent knowledge across sessions
                
                ---
                
                **Built with:** LangGraph • LangMem • Groq • NetworkX • Plotly • Streamlit • Gradio
                """)
            
            # Event handlers
            def show_suggestions():
                suggestions = self.get_research_suggestions()
                suggestions_text = "## Research Question Suggestions\n\n"
                for i, suggestion in enumerate(suggestions, 1):
                    suggestions_text += f"{i}. {suggestion}\n"
                return {
                    suggestions_output: gr.update(value=suggestions_text, visible=True)
                }
            
            # Connect event handlers
            research_btn.click(
                fn=self.conduct_research,
                inputs=[research_question, enable_hypothesis, enable_multi_agent],
                outputs=[final_answer_output, process_output, intelligence_output, quality_output]
            )
            
            suggestions_btn.click(
                fn=show_suggestions,
                outputs=[suggestions_output]
            )
            
            export_btn.click(
                fn=self.export_research_results,
                inputs=[final_answer_output, process_output, intelligence_output, quality_output],
                outputs=[export_output]
            )
            
            memory_btn.click(
                fn=self.get_memory_statistics,
                outputs=[memory_output]
            )
            
            history_btn.click(
                fn=self.get_research_history,
                outputs=[history_output]
            )
        
        return interface
    
    def launch(self, share=False, debug=False):
        """Launch the Gradio interface"""
        interface = self.create_interface()
        interface.launch(
            share=share,
            debug=debug,
            server_name="0.0.0.0",
            server_port=7860,
            show_error=True
        )

def main():
    """Main function to run the Gradio app"""
    app = GradioResearchInterface()
    app.launch(share=False, debug=True)

if __name__ == "__main__":
    main()