# -*- coding: utf-8 -*-
"""
AI Research Agent - Main Entry Point
Enhanced with proper state management and interactive capabilities
"""

from agent.research_agent import create_agent
import json

def run_research(question: str):
    """Run a research session with the given question"""
    print(f"🔬 Starting research on: {question}")
    print("=" * 60)
    
    # Create the agent
    agent = create_agent()
    
    # Initialize state - Phase 6 Enhanced with RLHF
    import uuid
    session_id = str(uuid.uuid4())
    
    initial_state = {
        "messages": [],
        "research_question": question,
        "research_plan": [],
        "current_step": 0,
        "findings": [],
        "final_answer": "",
        "iteration_count": 0,
        # Phase 4 Intelligence Layer components
        "hypotheses": [],
        "multi_agent_analysis": {},
        "quality_assessment": {},
        "intelligence_insights": {},
        # Phase 6 RLHF components
        "session_id": session_id,
        "rlhf_feedback": {},
        "reward_scores": {}
    }
    
    try:
        # Run the research
        result = agent.invoke(initial_state)
        
        # Display results
        print("\n📋 Research Plan:")
        for i, step in enumerate(result["research_plan"], 1):
            print(f"  {i}. {step}")
        
        print(f"\n🔍 Research Steps Completed: {len(result['findings'])}")
        
        print("\n📊 Key Findings:")
        for finding in result["findings"]:
            print(f"\n  Step {finding['step'] + 1}: {finding['step_description']}")
            print(f"  Analysis: {finding['analysis'][:200]}...")
        
        print("\n🎯 Final Answer:")
        print("-" * 40)
        print(result["final_answer"])
        print("-" * 40)
        
        return result
        
    except Exception as e:
        print(f"❌ Error during research: {str(e)}")
        return None

def interactive_mode():
    """Run the agent in interactive mode"""
    print("🤖 AI Research Agent - Interactive Mode")
    print("Type 'quit' to exit, 'help' for commands")
    print("=" * 50)
    
    while True:
        try:
            question = input("\n🔬 Enter your research question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            elif question.lower() == 'help':
                print("\nAvailable commands:")
                print("  - Enter any research question to start research")
                print("  - 'quit' or 'exit' to leave")
                print("  - 'help' to see this message")
                continue
            elif not question:
                print("Please enter a valid research question.")
                continue
            
            # Run research
            result = run_research(question)
            
            if result:
                # Ask if user wants to continue
                continue_research = input("\n🔄 Continue with another question? (y/n): ").strip().lower()
                if continue_research not in ['y', 'yes']:
                    print("👋 Research session ended!")
                    break
            
        except KeyboardInterrupt:
            print("\n\n👋 Research interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    # You can run in different modes
    import sys
    
    if len(sys.argv) > 1:
        # Command line mode with question as argument
        question = " ".join(sys.argv[1:])
        run_research(question)
    else:
        # Interactive mode
        interactive_mode()