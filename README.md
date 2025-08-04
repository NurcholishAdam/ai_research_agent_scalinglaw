# 🤖 AI Research Agent

A powerful, modular AI research agent built with LangGraph, LangMem, and Groq. This agent can conduct structured research, maintain semantic memory, and provide comprehensive answers to complex questions.

## 🌟 Features

### Core Research Capabilities
- **Structured Research Planning**: Automatically creates multi-step research plans
- **ReAct Pattern**: Reasoning and Acting in a structured loop
- **Multiple LLM Support**: Groq (primary) and Mistral integration
- **Interactive Mode**: Command-line interface for ongoing research sessions
- **Extensible Architecture**: Easy to add new tools and capabilities

### 🧠 Advanced Memory System (Phase 2)
- **Hierarchical Memory**: Short-term, long-term, and episodic memory layers
- **Knowledge Graph Construction**: Automatic concept relationship mapping
- **Citation Tracking**: Network analysis of research sources and references
- **Memory Consolidation**: Intelligent promotion of important findings
- **Research Session Management**: Complete episode tracking and analysis
- **Concept Extraction**: Automatic identification of key concepts and relationships

### 🔬 Research Tools Arsenal (Phase 3)
- **Web Research Suite**: DuckDuckGo search, Wikipedia integration, arXiv papers, news search
- **Document Processing**: PDF analysis, text extraction, structure analysis, content summarization
- **Data Visualization**: Timeline charts, concept networks, metrics dashboards, word frequency analysis
- **Intelligent Tool Selection**: Automatic tool recommendation based on research context
- **Multi-Source Integration**: Seamless combination of memory and external research sources

### 🧠 Intelligence Layer (Phase 4)
- **Multi-Agent Collaboration**: Researcher, Critic, and Synthesizer agents working together
- **Hypothesis Generation**: Automatic generation of testable research hypotheses
- **Hypothesis Testing**: Evidence-based validation and ranking of hypotheses
- **Quality Assessment**: Comprehensive research quality scoring and validation
- **Fact-Checking**: Multi-perspective credibility analysis and source verification
- **Research Methodology**: Intelligent selection and critique of research approaches

### 🎨 User Experience (Phase 5)
- **Streamlit Web Interface**: Professional web UI with real-time progress tracking
- **Gradio Alternative Interface**: Simple, shareable web interface for quick research
- **Interactive Visualizations**: Real-time charts, graphs, and progress indicators
- **Professional Report Generation**: HTML, Markdown, PDF, and DOCX export formats
- **Advanced Configuration**: Customizable research depth and feature toggles
- **Mobile-Friendly Design**: Responsive interfaces that work on all devices

## 🏗️ Architecture

```
User ↔ Agent Interface (CLI/Web)
         ↓
      LangGraph Agent (ReAct Pattern)
  ┌────────────┐      ┌───────────┐
  │ Memory     │◄────►│ Vector DB │
  │ (LangMem)  │      │ (Chroma)  │
  └────┬───────┘      └───────────┘
       │     ┌────────────────┐
       └────►│ Inference LLM  │
             │ (Groq/Mistral) │
             └────────────────┘
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Clone and navigate to the project
cd ai_research_agent

# Run setup script
python setup.py

# Set your API keys
export GROQ_API_KEY='your_groq_api_key_here'
```

### 2. Test the Agent

```bash
# Run component tests
python test_agent.py
```

### 3. Start Researching

```bash
# Interactive mode
python main.py

# Direct question mode
python main.py "How does quantum computing work?"
```

## 📋 Requirements

- Python 3.8+
- Groq API key (required)
- Mistral API key (optional)
- OpenAI API key (optional, for embeddings)

## 🔧 Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```bash
GROQ_API_KEY=your_groq_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here  # optional
OPENAI_API_KEY=your_openai_api_key_here    # optional
```

### API Keys

- **Groq**: Get from [console.groq.com](https://console.groq.com/keys)
- **Mistral**: Get from [console.mistral.ai](https://console.mistral.ai/)
- **OpenAI**: Get from [platform.openai.com](https://platform.openai.com/api-keys)

## 🎯 Usage Examples

### Interactive Research Session

```bash
$ python main.py

🤖 AI Research Agent - Interactive Mode
==================================================

🔬 Enter your research question: What are the latest developments in AI safety?

🔬 Starting research on: What are the latest developments in AI safety?
============================================================

📋 Research Plan:
  1. Search for recent AI safety research and publications
  2. Identify key organizations and researchers in AI safety
  3. Analyze current AI safety challenges and proposed solutions
  4. Examine recent policy developments and industry initiatives

🔍 Research Steps Completed: 4

🎯 Final Answer:
----------------------------------------
[Comprehensive research results...]
----------------------------------------
```

### Direct Question Mode

```bash
python main.py "Explain machine learning algorithms"
```

## 🧩 Project Structure

```
ai_research_agent/
├── agent/
│   └── research_agent.py     # Main agent logic with ReAct pattern
├── llm/
│   └── groq_wrapper.py       # LLM integrations
├── memory/
│   ├── langmem_tools.py      # Semantic memory tools
│   └── vector_store.py       # Vector database setup
├── tools/
│   ├── web_search.py         # Web search capabilities
│   └── __init__.py
├── main.py                   # Entry point and CLI interface
├── config.py                 # Configuration management
├── test_agent.py            # Test suite
├── setup.py                 # Setup and installation script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔬 How It Works

### Research Process

1. **Planning Phase**: Agent analyzes the question and creates a structured research plan
2. **Execution Phase**: Each research step is executed systematically:
   - Search semantic memory for relevant information
   - Analyze findings and identify gaps
   - Store important discoveries for future reference
3. **Synthesis Phase**: All findings are combined into a comprehensive answer

### Memory System

- **Semantic Memory**: Uses LangMem for intelligent information storage and retrieval
- **Context Preservation**: Research context is maintained across sessions
- **Automatic Indexing**: Important findings are automatically stored with metadata

### Agent Architecture

- **State Management**: Proper state tracking throughout the research process
- **Tool Integration**: Seamless integration of memory and search tools
- **Error Handling**: Robust error handling and fallback mechanisms

## 🛠️ Development

### Adding New Tools

1. Create tool in `tools/` directory
2. Import and integrate in `research_agent.py`
3. Update tool executor with new capabilities

### Extending Memory

1. Enhance `memory/langmem_tools.py` with new memory operations
2. Add specialized memory tools for different research domains
3. Implement hierarchical memory structures

### Custom LLM Integration

1. Create wrapper in `llm/` directory following `groq_wrapper.py` pattern
2. Update `config.py` with new API configuration
3. Integrate in agent initialization

## 🧪 Testing

```bash
# Run full test suite
python test_agent.py

# Test specific components
python -c "from memory.langmem_tools import get_memory_tools; print('Memory tools:', len(get_memory_tools()))"
```

## 🚧 Roadmap

### ✅ Phase 1: Core Agent Implementation (COMPLETE)
- ✅ ReAct pattern with proper state management
- ✅ Research planning capabilities
- ✅ Multi-step reasoning workflows
- ✅ Memory tools integration

### ✅ Phase 2: Advanced Memory System (COMPLETE)
- ✅ Hierarchical memory (short-term, long-term, episodic)
- ✅ Knowledge graph construction with NetworkX
- ✅ Citation tracking and network analysis
- ✅ Memory consolidation algorithms
- ✅ Research session management
- ✅ Concept extraction and relationship mapping
- ✅ Knowledge graph visualization tools

### ✅ Phase 3: Research Tools Arsenal (COMPLETE)
- ✅ Web scraping and search integration (DuckDuckGo, Wikipedia, arXiv, News)
- ✅ PDF/document ingestion pipeline with text extraction
- ✅ Academic paper analysis tools (arXiv integration)
- ✅ Data visualization generators (timelines, networks, dashboards)
- ✅ Intelligent tool selection and recommendation system
- ✅ Multi-source research integration

### ✅ Phase 4: Intelligence Layer (COMPLETE)
- ✅ Multi-agent collaboration (researcher + critic + synthesizer)
- ✅ Hypothesis generation and testing
- ✅ Quality assessment and fact-checking
- ✅ Research methodology selection and critique
- ✅ Evidence-based validation and ranking
- ✅ Multi-perspective analysis and synthesis

### ✅ Phase 5: User Experience (COMPLETE)
- ✅ Web interface (Streamlit/Gradio)
- ✅ Real-time progress tracking
- ✅ Interactive research reports
- ✅ Export capabilities (PDF, DOCX, HTML, Markdown)
- ✅ Professional report generation with templates
- ✅ Mobile-friendly responsive design
- ✅ Advanced configuration options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🆘 Troubleshooting

### Common Issues

**"No module named 'langgraph'"**
```bash
pip install langgraph
```

**"GROQ_API_KEY not found"**
```bash
export GROQ_API_KEY='your_actual_api_key'
```

**Memory tool errors**
```bash
pip install langmem chromadb
```

### Getting Help

1. Check the test output: `python test_agent.py`
2. Verify your API keys are set correctly
3. Ensure all requirements are installed: `pip install -r requirements.txt`

---

**Happy Researching! 🔬✨**