#!/usr/bin/env python3
"""
Context Engineering Framework for AI Research Agent
Provides sophisticated context management, retrieval, processing, and tool reasoning
"""

from .context_retrieval import ContextRetriever, ContextType, RetrievalStrategy
from .context_processing import ContextProcessor, ProcessingMode, ContextFilter
from .context_management import ContextManager, ContextScope, ContextPriority
from .tool_reasoning import ToolReasoner, ReasoningMode, ToolSelection
from .context_orchestrator import ContextOrchestrator

__all__ = [
    'ContextRetriever',
    'ContextProcessor', 
    'ContextManager',
    'ToolReasoner',
    'ContextOrchestrator',
    'ContextType',
    'RetrievalStrategy',
    'ProcessingMode',
    'ContextFilter',
    'ContextScope',
    'ContextPriority',
    'ReasoningMode',
    'ToolSelection'
]

__version__ = "1.0.0"
__author__ = "AI Research Agent Team"
__description__ = "Advanced Context Engineering for Intelligent Research Systems"
