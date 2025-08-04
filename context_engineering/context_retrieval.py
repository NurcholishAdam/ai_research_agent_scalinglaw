#!/usr/bin/env python3
"""
Layer 1: Context Retrieval System for AI Research Agent
Advanced context retrieval with multi-source integration and semantic understanding
"""

import json
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, asdict

class ContextType(Enum):
    RESEARCH_HISTORY = "research_history"
    DOMAIN_KNOWLEDGE = "domain_knowledge"
    METHODOLOGY = "methodology"
    RELATED_CONCEPTS = "related_concepts"
    EXTERNAL_SOURCES = "external_sources"
    USER_PREFERENCES = "user_preferences"
    TOOL_CONTEXT = "tool_context"
    TEMPORAL_CONTEXT = "temporal_context"

class RetrievalStrategy(Enum):
    SEMANTIC_SIMILARITY = "semantic_similarity"
    TEMPORAL_RELEVANCE = "temporal_relevance"
    IMPORTANCE_WEIGHTED = "importance_weighted"
    HYBRID_APPROACH = "hybrid_approach"
    CONTEXTUAL_EMBEDDING = "contextual_embedding"

@dataclass
class ContextItem:
    id: str
    content: str
    context_type: ContextType
    relevance_score: float
    timestamp: str
    metadata: Dict[str, Any]
    source: str
    embedding: Optional[List[float]] = None

class ContextRetriever:
    """Layer 1: Advanced context retrieval system with multi-layered approach"""
    
    def __init__(self, memory_manager=None, research_tools=None):
        self.context_cache: Dict[str, List[ContextItem]] = {}
        self.retrieval_history: List[Dict[str, Any]] = []
        self.memory_manager = memory_manager
        self.research_tools = research_tools
        self.context_embeddings: Dict[str, List[float]] = {}
        print("🔍 Layer 1: Advanced Context Retriever initialized")
    
    def retrieve_context(
        self,
        query: str,
        context_types: List[ContextType],
        strategy: RetrievalStrategy = RetrievalStrategy.HYBRID_APPROACH,
        max_items: int = 15,
        relevance_threshold: float = 0.5
    ) -> List[ContextItem]:
        """Multi-layered context retrieval with advanced filtering"""
        
        print(f"🔍 Retrieving context for: '{query[:50]}...'")
        
        # Layer 1.1: Primary context retrieval
        primary_items = self._primary_retrieval(query, context_types, strategy)
        
        # Layer 1.2: Semantic enhancement
        enhanced_items = self._semantic_enhancement(query, primary_items)
        
        # Layer 1.3: Relevance filtering
        filtered_items = [item for item in enhanced_items if item.relevance_score >= relevance_threshold]
        
        # Layer 1.4: Contextual ranking
        ranked_items = self._contextual_ranking(query, filtered_items)
        
        # Final selection
        final_items = ranked_items[:max_items]
        
        # Log retrieval with enhanced metadata
        self._log_retrieval(query, context_types, strategy, final_items)
        
        print(f"✅ Retrieved {len(final_items)} context items (avg relevance: {sum(item.relevance_score for item in final_items) / len(final_items) if final_items else 0:.3f})")
        
        return final_items
    
    def _primary_retrieval(
        self,
        query: str,
        context_types: List[ContextType],
        strategy: RetrievalStrategy
    ) -> List[ContextItem]:
        """Layer 1.1: Primary context retrieval from multiple sources"""
        
        retrieved_items = []
        
        for context_type in context_types:
            items = self._retrieve_by_type(query, context_type, strategy)
            retrieved_items.extend(items)
        
        return retrieved_items
    
    def _semantic_enhancement(self, query: str, items: List[ContextItem]) -> List[ContextItem]:
        """Layer 1.2: Enhance items with semantic analysis"""
        
        enhanced_items = []
        
        for item in items:
            # Calculate semantic similarity
            semantic_boost = self._calculate_semantic_similarity(query, item.content)
            
            # Adjust relevance score based on semantic similarity
            enhanced_score = min(1.0, item.relevance_score + (semantic_boost * 0.2))
            
            enhanced_item = ContextItem(
                id=item.id,
                content=item.content,
                context_type=item.context_type,
                relevance_score=enhanced_score,
                timestamp=item.timestamp,
                metadata={**item.metadata, "semantic_boost": semantic_boost},
                source=item.source,
                embedding=self._generate_mock_embedding(item.content)
            )
            
            enhanced_items.append(enhanced_item)
        
        return enhanced_items
    
    def _contextual_ranking(self, query: str, items: List[ContextItem]) -> List[ContextItem]:
        """Layer 1.4: Advanced contextual ranking"""
        
        context_type_weights = {
            ContextType.RESEARCH_HISTORY: 0.9,
            ContextType.DOMAIN_KNOWLEDGE: 0.85,
            ContextType.METHODOLOGY: 0.8,
            ContextType.EXTERNAL_SOURCES: 0.75,
            ContextType.RELATED_CONCEPTS: 0.7,
            ContextType.TOOL_CONTEXT: 0.65,
            ContextType.USER_PREFERENCES: 0.6,
            ContextType.TEMPORAL_CONTEXT: 0.55
        }
        
        def ranking_score(item: ContextItem) -> float:
            base_score = item.relevance_score
            type_weight = context_type_weights.get(item.context_type, 0.5)
            temporal_factor = self._calculate_temporal_relevance(item.timestamp)
            source_reliability = self._get_source_reliability(item.source)
            
            return (base_score * 0.4 + 
                   type_weight * 0.3 + 
                   temporal_factor * 0.2 + 
                   source_reliability * 0.1)
        
        return sorted(items, key=ranking_score, reverse=True)
    
    def _retrieve_by_type(
        self,
        query: str,
        context_type: ContextType,
        strategy: RetrievalStrategy
    ) -> List[ContextItem]:
        """Enhanced type-specific retrieval"""
        
        if context_type == ContextType.RESEARCH_HISTORY:
            return self._get_research_history_context(query, strategy)
        elif context_type == ContextType.DOMAIN_KNOWLEDGE:
            return self._get_domain_knowledge_context(query, strategy)
        elif context_type == ContextType.METHODOLOGY:
            return self._get_methodology_context(query, strategy)
        elif context_type == ContextType.RELATED_CONCEPTS:
            return self._get_related_concepts_context(query, strategy)
        elif context_type == ContextType.EXTERNAL_SOURCES:
            return self._get_external_sources_context(query, strategy)
        elif context_type == ContextType.USER_PREFERENCES:
            return self._get_user_preferences_context(query, strategy)
        elif context_type == ContextType.TOOL_CONTEXT:
            return self._get_tool_context(query, strategy)
        elif context_type == ContextType.TEMPORAL_CONTEXT:
            return self._get_temporal_context(query, strategy)
        
        return []
    
    def _get_research_history_context(self, query: str, strategy: RetrievalStrategy) -> List[ContextItem]:
        """Enhanced research history retrieval"""
        items = []
        
        # Simulate memory manager integration
        if self.memory_manager:
            items.append(ContextItem(
                id=str(uuid.uuid4()),
                content=f"Previous research sessions on '{query}' revealed key patterns and methodological insights",
                context_type=ContextType.RESEARCH_HISTORY,
                relevance_score=0.88,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "research_sessions": 3,
                    "findings_count": 12,
                    "success_rate": 0.85,
                    "methodology_used": "systematic_analysis"
                },
                source="advanced_memory_manager"
            ))
        else:
            items.append(ContextItem(
                id=str(uuid.uuid4()),
                content=f"Research history indicates '{query}' has been explored with positive outcomes",
                context_type=ContextType.RESEARCH_HISTORY,
                relevance_score=0.82,
                timestamp=datetime.now().isoformat(),
                metadata={"simulated": True, "confidence": 0.8},
                source="research_memory"
            ))
        
        return items
    
    def _get_domain_knowledge_context(self, query: str, strategy: RetrievalStrategy) -> List[ContextItem]:
        """Enhanced domain knowledge retrieval"""
        return [
            ContextItem(
                id=str(uuid.uuid4()),
                content=f"Domain expertise analysis for '{query}' indicates strong connections to established theoretical frameworks",
                context_type=ContextType.DOMAIN_KNOWLEDGE,
                relevance_score=0.82,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "domain_confidence": 0.9,
                    "theoretical_frameworks": ["framework_a", "framework_b"],
                    "expert_consensus": 0.85,
                    "knowledge_depth": "comprehensive"
                },
                source="knowledge_graph"
            )
        ]
    
    def _get_methodology_context(self, query: str, strategy: RetrievalStrategy) -> List[ContextItem]:
        """Enhanced methodology context"""
        return [
            ContextItem(
                id=str(uuid.uuid4()),
                content=f"Optimal research methodology for '{query}' combines systematic review with empirical analysis",
                context_type=ContextType.METHODOLOGY,
                relevance_score=0.79,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "methodology_type": "hybrid_approach",
                    "effectiveness_score": 0.92,
                    "time_efficiency": 0.78,
                    "resource_requirements": "moderate"
                },
                source="methodology_optimizer"
            )
        ]
    
    def _get_tool_context(self, query: str, strategy: RetrievalStrategy) -> List[ContextItem]:
        """Get tool-specific context"""
        return [
            ContextItem(
                id=str(uuid.uuid4()),
                content=f"Tool analysis suggests web search and academic databases are optimal for '{query}' research",
                context_type=ContextType.TOOL_CONTEXT,
                relevance_score=0.76,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "recommended_tools": ["web_search", "arxiv_search", "wikipedia"],
                    "tool_effectiveness": {"web_search": 0.85, "arxiv": 0.92},
                    "execution_order": ["background", "academic", "current"]
                },
                source="tool_reasoner"
            )
        ]
    
    def _get_temporal_context(self, query: str, strategy: RetrievalStrategy) -> List[ContextItem]:
        """Get temporal context"""
        return [
            ContextItem(
                id=str(uuid.uuid4()),
                content=f"Temporal analysis shows '{query}' has evolving significance with recent developments",
                context_type=ContextType.TEMPORAL_CONTEXT,
                relevance_score=0.73,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "temporal_trend": "increasing",
                    "recent_activity": "high",
                    "historical_importance": 0.8,
                    "future_relevance": 0.9
                },
                source="temporal_analyzer"
            )
        ]
    
    def _get_related_concepts_context(self, query: str, strategy: RetrievalStrategy) -> List[ContextItem]:
        """Enhanced related concepts"""
        return [
            ContextItem(
                id=str(uuid.uuid4()),
                content=f"Concept network analysis reveals '{query}' connects to multiple research domains",
                context_type=ContextType.RELATED_CONCEPTS,
                relevance_score=0.71,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "concept_clusters": 4,
                    "connection_strength": 0.78,
                    "interdisciplinary_links": 6,
                    "expansion_potential": "high"
                },
                source="concept_network"
            )
        ]
    
    def _get_external_sources_context(self, query: str, strategy: RetrievalStrategy) -> List[ContextItem]:
        """Enhanced external sources"""
        return [
            ContextItem(
                id=str(uuid.uuid4()),
                content=f"External source analysis for '{query}' identifies high-quality recent publications and datasets",
                context_type=ContextType.EXTERNAL_SOURCES,
                relevance_score=0.77,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "source_quality": 0.89,
                    "publication_recency": "last_6_months",
                    "dataset_availability": True,
                    "citation_impact": "high"
                },
                source="external_analyzer"
            )
        ]
    
    def _get_user_preferences_context(self, query: str, strategy: RetrievalStrategy) -> List[ContextItem]:
        """Enhanced user preferences"""
        return [
            ContextItem(
                id=str(uuid.uuid4()),
                content=f"User preference analysis indicates preference for detailed, well-sourced research on '{query}'",
                context_type=ContextType.USER_PREFERENCES,
                relevance_score=0.68,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "detail_preference": "comprehensive",
                    "source_preference": "academic_primary",
                    "format_preference": "structured",
                    "interaction_style": "analytical"
                },
                source="user_profiler"
            )
        ]
    
    def _calculate_semantic_similarity(self, query: str, content: str) -> float:
        """Calculate semantic similarity (simplified)"""
        query_words = set(query.lower().split())
        content_words = set(content.lower().split())
        
        if not query_words:
            return 0.0
        
        overlap = len(query_words.intersection(content_words))
        return min(1.0, overlap / len(query_words))
    
    def _generate_mock_embedding(self, text: str) -> List[float]:
        """Generate mock embedding for demonstration"""
        import random
        random.seed(hash(text) % 2**32)
        return [random.random() for _ in range(384)]
    
    def _calculate_temporal_relevance(self, timestamp: str) -> float:
        """Calculate temporal relevance factor"""
        try:
            item_time = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            current_time = datetime.now()
            time_diff = (current_time - item_time).total_seconds()
            
            decay_factor = max(0.1, 1.0 - (time_diff / (30 * 24 * 3600)))
            return decay_factor
        except:
            return 0.5
    
    def _get_source_reliability(self, source: str) -> float:
        """Get source reliability score"""
        reliability_scores = {
            "advanced_memory_manager": 0.95,
            "knowledge_graph": 0.90,
            "methodology_optimizer": 0.88,
            "tool_reasoner": 0.85,
            "external_analyzer": 0.82,
            "concept_network": 0.80,
            "temporal_analyzer": 0.78,
            "user_profiler": 0.75
        }
        return reliability_scores.get(source, 0.6)
    
    def _log_retrieval(
        self,
        query: str,
        context_types: List[ContextType],
        strategy: RetrievalStrategy,
        final_items: List[ContextItem]
    ):
        """Enhanced retrieval logging"""
        self.retrieval_history.append({
            "query": query,
            "context_types": [ct.value for ct in context_types],
            "strategy": strategy.value,
            "items_retrieved": len(final_items),
            "average_relevance": sum(item.relevance_score for item in final_items) / len(final_items) if final_items else 0,
            "context_distribution": self._get_context_distribution(final_items),
            "timestamp": datetime.now().isoformat()
        })
    
    def _get_context_distribution(self, items: List[ContextItem]) -> Dict[str, int]:
        """Get distribution of context types in retrieved items"""
        distribution = {}
        for item in items:
            context_type = item.context_type.value
            distribution[context_type] = distribution.get(context_type, 0) + 1
        return distribution
    
    def get_retrieval_statistics(self) -> Dict[str, Any]:
        """Enhanced retrieval statistics"""
        if not self.retrieval_history:
            return {"total_retrievals": 0, "average_items": 0}
        
        total_items = sum(r["items_retrieved"] for r in self.retrieval_history)
        avg_items = total_items / len(self.retrieval_history)
        avg_relevance = sum(r["average_relevance"] for r in self.retrieval_history) / len(self.retrieval_history)
        
        return {
            "total_retrievals": len(self.retrieval_history),
            "average_items_per_retrieval": round(avg_items, 2),
            "total_items_retrieved": total_items,
            "average_relevance_score": round(avg_relevance, 3),
            "most_used_strategy": self._get_most_used_strategy(),
            "context_type_usage": self._get_context_type_usage(),
            "retrieval_efficiency": self._calculate_retrieval_efficiency()
        }
    
    def _get_most_used_strategy(self) -> str:
        """Get the most frequently used retrieval strategy"""
        if not self.retrieval_history:
            return "none"
        
        strategy_counts = {}
        for retrieval in self.retrieval_history:
            strategy = retrieval["strategy"]
            strategy_counts[strategy] = strategy_counts.get(strategy, 0) + 1
        
        return max(strategy_counts, key=strategy_counts.get)
    
    def _get_context_type_usage(self) -> Dict[str, int]:
        """Get usage statistics for context types"""
        type_usage = {}
        for retrieval in self.retrieval_history:
            for context_type in retrieval["context_types"]:
                type_usage[context_type] = type_usage.get(context_type, 0) + 1
        return type_usage
    
    def _calculate_retrieval_efficiency(self) -> float:
        """Calculate overall retrieval efficiency"""
        if not self.retrieval_history:
            return 0.0
        
        efficiency_scores = []
        for retrieval in self.retrieval_history:
            relevance = retrieval["average_relevance"]
            item_count = retrieval["items_retrieved"]
            optimal_count = 10
            count_efficiency = 1.0 - abs(item_count - optimal_count) / optimal_count
            efficiency = (relevance * 0.7) + (count_efficiency * 0.3)
            efficiency_scores.append(efficiency)
        
        return round(sum(efficiency_scores) / len(efficiency_scores), 3)