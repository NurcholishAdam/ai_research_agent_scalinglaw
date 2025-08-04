#!/usr/bin/env python3
"""
Layer 2: Context Processing System for AI Research Agent
Advanced context processing with filtering, transformation, and enrichment
"""

import json
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, asdict
from .context_retrieval import ContextItem, ContextType

class ProcessingMode(Enum):
    FILTER_ONLY = "filter_only"
    TRANSFORM_ONLY = "transform_only"
    ENRICH_ONLY = "enrich_only"
    COMPREHENSIVE = "comprehensive"
    ADAPTIVE = "adaptive"

class ContextFilter(Enum):
    RELEVANCE_THRESHOLD = "relevance_threshold"
    TEMPORAL_WINDOW = "temporal_window"
    SOURCE_RELIABILITY = "source_reliability"
    CONTENT_QUALITY = "content_quality"
    DUPLICATE_REMOVAL = "duplicate_removal"
    DOMAIN_SPECIFIC = "domain_specific"

@dataclass
class ProcessedContext:
    original_items: List[ContextItem]
    processed_items: List[ContextItem]
    transformations_applied: List[str]
    filters_applied: List[str]
    enrichments_added: List[str]
    processing_metadata: Dict[str, Any]
    quality_score: float

@dataclass
class ContextCluster:
    id: str
    theme: str
    items: List[ContextItem]
    coherence_score: float
    representative_item: ContextItem

class ContextProcessor:
    """Layer 2: Advanced context processing system"""
    
    def __init__(self):
        self.processing_history: List[Dict[str, Any]] = {}
        self.quality_metrics: Dict[str, float] = {}
        self.transformation_cache: Dict[str, Any] = {}
        print("⚙️ Layer 2: Context Processor initialized")
    
    def process_context(
        self,
        context_items: List[ContextItem],
        mode: ProcessingMode = ProcessingMode.COMPREHENSIVE,
        filters: List[ContextFilter] = None,
        target_quality: float = 0.8,
        max_items: int = 12
    ) -> ProcessedContext:
        """Comprehensive context processing pipeline"""
        
        print(f"⚙️ Processing {len(context_items)} context items (mode: {mode.value})")
        
        original_items = context_items.copy()
        processed_items = context_items.copy()
        transformations = []
        filters_applied = []
        enrichments = []
        
        # Layer 2.1: Context Filtering
        if mode in [ProcessingMode.FILTER_ONLY, ProcessingMode.COMPREHENSIVE, ProcessingMode.ADAPTIVE]:
            processed_items, applied_filters = self._apply_filters(processed_items, filters or [])
            filters_applied.extend(applied_filters)
        
        # Layer 2.2: Context Transformation
        if mode in [ProcessingMode.TRANSFORM_ONLY, ProcessingMode.COMPREHENSIVE, ProcessingMode.ADAPTIVE]:
            processed_items, applied_transforms = self._apply_transformations(processed_items)
            transformations.extend(applied_transforms)
        
        # Layer 2.3: Context Enrichment
        if mode in [ProcessingMode.ENRICH_ONLY, ProcessingMode.COMPREHENSIVE, ProcessingMode.ADAPTIVE]:
            processed_items, applied_enrichments = self._apply_enrichments(processed_items)
            enrichments.extend(applied_enrichments)
        
        # Layer 2.4: Quality Assessment and Optimization
        processed_items = self._optimize_for_quality(processed_items, target_quality, max_items)
        
        # Calculate overall quality score
        quality_score = self._calculate_quality_score(processed_items)
        
        # Create processing metadata
        processing_metadata = {
            "original_count": len(original_items),
            "processed_count": len(processed_items),
            "reduction_ratio": 1 - (len(processed_items) / len(original_items)) if original_items else 0,
            "average_relevance": sum(item.relevance_score for item in processed_items) / len(processed_items) if processed_items else 0,
            "processing_timestamp": datetime.now().isoformat(),
            "mode_used": mode.value
        }
        
        result = ProcessedContext(
            original_items=original_items,
            processed_items=processed_items,
            transformations_applied=transformations,
            filters_applied=filters_applied,
            enrichments_added=enrichments,
            processing_metadata=processing_metadata,
            quality_score=quality_score
        )
        
        # Log processing
        self._log_processing(result)
        
        print(f"✅ Processed to {len(processed_items)} items (quality: {quality_score:.3f})")
        
        return result
    
    def _apply_filters(
        self,
        items: List[ContextItem],
        filters: List[ContextFilter]
    ) -> Tuple[List[ContextItem], List[str]]:
        """Layer 2.1: Apply context filters"""
        
        filtered_items = items.copy()
        applied_filters = []
        
        for filter_type in filters:
            if filter_type == ContextFilter.RELEVANCE_THRESHOLD:
                filtered_items = [item for item in filtered_items if item.relevance_score >= 0.6]
                applied_filters.append("relevance_threshold_0.6")
            
            elif filter_type == ContextFilter.TEMPORAL_WINDOW:
                # Keep items from last 30 days
                cutoff_time = datetime.now().timestamp() - (30 * 24 * 3600)
                filtered_items = [
                    item for item in filtered_items
                    if self._parse_timestamp(item.timestamp) >= cutoff_time
                ]
                applied_filters.append("temporal_window_30_days")
            
            elif filter_type == ContextFilter.SOURCE_RELIABILITY:
                # Filter by source reliability
                reliable_sources = {
                    "advanced_memory_manager", "knowledge_graph", "methodology_optimizer",
                    "tool_reasoner", "external_analyzer"
                }
                filtered_items = [
                    item for item in filtered_items
                    if item.source in reliable_sources
                ]
                applied_filters.append("source_reliability_filter")
            
            elif filter_type == ContextFilter.CONTENT_QUALITY:
                # Filter by content quality metrics
                filtered_items = [
                    item for item in filtered_items
                    if self._assess_content_quality(item) >= 0.7
                ]
                applied_filters.append("content_quality_filter")
            
            elif filter_type == ContextFilter.DUPLICATE_REMOVAL:
                # Remove duplicate or highly similar items
                filtered_items = self._remove_duplicates(filtered_items)
                applied_filters.append("duplicate_removal")
            
            elif filter_type == ContextFilter.DOMAIN_SPECIFIC:
                # Keep domain-relevant items
                filtered_items = self._filter_domain_relevant(filtered_items)
                applied_filters.append("domain_specific_filter")
        
        return filtered_items, applied_filters
    
    def _apply_transformations(
        self,
        items: List[ContextItem]
    ) -> Tuple[List[ContextItem], List[str]]:
        """Layer 2.2: Apply context transformations"""
        
        transformed_items = []
        applied_transforms = []
        
        for item in items:
            transformed_item = item
            
            # Transform 1: Content summarization for long items
            if len(item.content) > 500:
                transformed_item = self._summarize_content(transformed_item)
                if "content_summarization" not in applied_transforms:
                    applied_transforms.append("content_summarization")
            
            # Transform 2: Relevance score normalization
            transformed_item = self._normalize_relevance_score(transformed_item)
            if "relevance_normalization" not in applied_transforms:
                applied_transforms.append("relevance_normalization")
            
            # Transform 3: Metadata standardization
            transformed_item = self._standardize_metadata(transformed_item)
            if "metadata_standardization" not in applied_transforms:
                applied_transforms.append("metadata_standardization")
            
            transformed_items.append(transformed_item)
        
        return transformed_items, applied_transforms
    
    def _apply_enrichments(
        self,
        items: List[ContextItem]
    ) -> Tuple[List[ContextItem], List[str]]:
        """Layer 2.3: Apply context enrichments"""
        
        enriched_items = []
        applied_enrichments = []
        
        for item in items:
            enriched_item = item
            
            # Enrichment 1: Add semantic tags
            enriched_item = self._add_semantic_tags(enriched_item)
            if "semantic_tagging" not in applied_enrichments:
                applied_enrichments.append("semantic_tagging")
            
            # Enrichment 2: Add relationship indicators
            enriched_item = self._add_relationship_indicators(enriched_item, items)
            if "relationship_indicators" not in applied_enrichments:
                applied_enrichments.append("relationship_indicators")
            
            # Enrichment 3: Add confidence metrics
            enriched_item = self._add_confidence_metrics(enriched_item)
            if "confidence_metrics" not in applied_enrichments:
                applied_enrichments.append("confidence_metrics")
            
            enriched_items.append(enriched_item)
        
        return enriched_items, applied_enrichments
    
    def _optimize_for_quality(
        self,
        items: List[ContextItem],
        target_quality: float,
        max_items: int
    ) -> List[ContextItem]:
        """Layer 2.4: Optimize context for quality and size"""
        
        # Sort by composite quality score
        def quality_score(item: ContextItem) -> float:
            base_relevance = item.relevance_score
            content_quality = self._assess_content_quality(item)
            source_reliability = self._get_source_reliability_score(item.source)
            
            return (base_relevance * 0.5 + content_quality * 0.3 + source_reliability * 0.2)
        
        sorted_items = sorted(items, key=quality_score, reverse=True)
        
        # Select items that meet quality threshold
        quality_items = [item for item in sorted_items if quality_score(item) >= target_quality]
        
        # If we have too few quality items, gradually lower threshold
        if len(quality_items) < max_items // 2:
            adjusted_threshold = target_quality * 0.8
            quality_items = [item for item in sorted_items if quality_score(item) >= adjusted_threshold]
        
        # Limit to max_items
        return quality_items[:max_items]
    
    def cluster_contexts(
        self,
        items: List[ContextItem],
        max_clusters: int = 5
    ) -> List[ContextCluster]:
        """Advanced context clustering by theme and similarity"""
        
        print(f"🔗 Clustering {len(items)} context items into max {max_clusters} clusters")
        
        # Simple clustering based on context types and content similarity
        clusters = {}
        
        for item in items:
            # Use context type as primary clustering dimension
            cluster_key = item.context_type.value
            
            if cluster_key not in clusters:
                clusters[cluster_key] = []
            clusters[cluster_key].append(item)
        
        # Convert to ContextCluster objects
        context_clusters = []
        for theme, cluster_items in clusters.items():
            if not cluster_items:
                continue
            
            # Find representative item (highest relevance)
            representative = max(cluster_items, key=lambda x: x.relevance_score)
            
            # Calculate coherence score
            coherence = self._calculate_cluster_coherence(cluster_items)
            
            cluster = ContextCluster(
                id=str(uuid.uuid4()),
                theme=theme,
                items=cluster_items,
                coherence_score=coherence,
                representative_item=representative
            )
            
            context_clusters.append(cluster)
        
        # Sort by coherence and limit
        context_clusters.sort(key=lambda x: x.coherence_score, reverse=True)
        
        print(f"✅ Created {len(context_clusters)} context clusters")
        
        return context_clusters[:max_clusters]
    
    def _summarize_content(self, item: ContextItem) -> ContextItem:
        """Summarize long content"""
        if len(item.content) <= 500:
            return item
        
        # Simple summarization (in real implementation, use advanced NLP)
        sentences = item.content.split('. ')
        summary = '. '.join(sentences[:3]) + '...'
        
        new_metadata = item.metadata.copy()
        new_metadata['original_length'] = len(item.content)
        new_metadata['summarized'] = True
        
        return ContextItem(
            id=item.id,
            content=summary,
            context_type=item.context_type,
            relevance_score=item.relevance_score,
            timestamp=item.timestamp,
            metadata=new_metadata,
            source=item.source,
            embedding=item.embedding
        )
    
    def _normalize_relevance_score(self, item: ContextItem) -> ContextItem:
        """Normalize relevance score"""
        # Apply sigmoid normalization to smooth extreme values
        import math
        normalized_score = 1 / (1 + math.exp(-5 * (item.relevance_score - 0.5)))
        
        return ContextItem(
            id=item.id,
            content=item.content,
            context_type=item.context_type,
            relevance_score=normalized_score,
            timestamp=item.timestamp,
            metadata=item.metadata,
            source=item.source,
            embedding=item.embedding
        )
    
    def _standardize_metadata(self, item: ContextItem) -> ContextItem:
        """Standardize metadata format"""
        standardized_metadata = {
            "processing_timestamp": datetime.now().isoformat(),
            "original_metadata": item.metadata,
            "quality_indicators": {
                "content_length": len(item.content),
                "has_metadata": bool(item.metadata),
                "source_type": self._classify_source_type(item.source)
            }
        }
        
        return ContextItem(
            id=item.id,
            content=item.content,
            context_type=item.context_type,
            relevance_score=item.relevance_score,
            timestamp=item.timestamp,
            metadata=standardized_metadata,
            source=item.source,
            embedding=item.embedding
        )
    
    def _add_semantic_tags(self, item: ContextItem) -> ContextItem:
        """Add semantic tags to context item"""
        # Simple keyword extraction (in real implementation, use NLP)
        content_lower = item.content.lower()
        
        semantic_tags = []
        if any(word in content_lower for word in ['research', 'study', 'analysis']):
            semantic_tags.append('research_oriented')
        if any(word in content_lower for word in ['method', 'approach', 'technique']):
            semantic_tags.append('methodological')
        if any(word in content_lower for word in ['data', 'evidence', 'findings']):
            semantic_tags.append('data_driven')
        if any(word in content_lower for word in ['theory', 'concept', 'framework']):
            semantic_tags.append('theoretical')
        
        new_metadata = item.metadata.copy()
        new_metadata['semantic_tags'] = semantic_tags
        
        return ContextItem(
            id=item.id,
            content=item.content,
            context_type=item.context_type,
            relevance_score=item.relevance_score,
            timestamp=item.timestamp,
            metadata=new_metadata,
            source=item.source,
            embedding=item.embedding
        )
    
    def _add_relationship_indicators(self, item: ContextItem, all_items: List[ContextItem]) -> ContextItem:
        """Add relationship indicators with other context items"""
        relationships = []
        
        for other_item in all_items:
            if other_item.id == item.id:
                continue
            
            similarity = self._calculate_content_similarity(item.content, other_item.content)
            if similarity > 0.3:
                relationships.append({
                    "related_item_id": other_item.id,
                    "similarity_score": similarity,
                    "relationship_type": "content_similarity"
                })
        
        new_metadata = item.metadata.copy()
        new_metadata['relationships'] = relationships[:5]  # Limit to top 5
        
        return ContextItem(
            id=item.id,
            content=item.content,
            context_type=item.context_type,
            relevance_score=item.relevance_score,
            timestamp=item.timestamp,
            metadata=new_metadata,
            source=item.source,
            embedding=item.embedding
        )
    
    def _add_confidence_metrics(self, item: ContextItem) -> ContextItem:
        """Add confidence metrics"""
        content_quality = self._assess_content_quality(item)
        source_reliability = self._get_source_reliability_score(item.source)
        temporal_relevance = self._calculate_temporal_relevance_score(item.timestamp)
        
        confidence_score = (content_quality * 0.4 + source_reliability * 0.4 + temporal_relevance * 0.2)
        
        new_metadata = item.metadata.copy()
        new_metadata['confidence_metrics'] = {
            "overall_confidence": confidence_score,
            "content_quality": content_quality,
            "source_reliability": source_reliability,
            "temporal_relevance": temporal_relevance
        }
        
        return ContextItem(
            id=item.id,
            content=item.content,
            context_type=item.context_type,
            relevance_score=item.relevance_score,
            timestamp=item.timestamp,
            metadata=new_metadata,
            source=item.source,
            embedding=item.embedding
        )
    
    def _assess_content_quality(self, item: ContextItem) -> float:
        """Assess content quality"""
        content = item.content
        
        # Quality indicators
        length_score = min(1.0, len(content) / 200)  # Optimal around 200 chars
        structure_score = 0.5 if any(marker in content.lower() for marker in [
            'analysis', 'findings', 'evidence', 'conclusion'
        ]) else 0.0
        
        specificity_score = 0.3 if any(marker in content for marker in [
            'study', 'research', 'data', 'method'
        ]) else 0.0
        
        return min(1.0, length_score + structure_score + specificity_score)
    
    def _get_source_reliability_score(self, source: str) -> float:
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
    
    def _calculate_temporal_relevance_score(self, timestamp: str) -> float:
        """Calculate temporal relevance"""
        try:
            item_time = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            current_time = datetime.now()
            time_diff = (current_time - item_time).total_seconds()
            
            # More recent items get higher scores
            decay_factor = max(0.1, 1.0 - (time_diff / (30 * 24 * 3600)))
            return decay_factor
        except:
            return 0.5
    
    def _parse_timestamp(self, timestamp: str) -> float:
        """Parse timestamp to unix timestamp"""
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return dt.timestamp()
        except:
            return datetime.now().timestamp()
    
    def _remove_duplicates(self, items: List[ContextItem]) -> List[ContextItem]:
        """Remove duplicate items"""
        seen_content = set()
        unique_items = []
        
        for item in items:
            content_hash = hash(item.content[:100])  # Use first 100 chars for similarity
            if content_hash not in seen_content:
                seen_content.add(content_hash)
                unique_items.append(item)
        
        return unique_items
    
    def _filter_domain_relevant(self, items: List[ContextItem]) -> List[ContextItem]:
        """Filter domain-relevant items"""
        # Simple domain relevance (in real implementation, use domain-specific models)
        relevant_items = []
        
        for item in items:
            if any(keyword in item.content.lower() for keyword in [
                'research', 'analysis', 'study', 'method', 'data', 'evidence'
            ]):
                relevant_items.append(item)
        
        return relevant_items if relevant_items else items  # Fallback to all items
    
    def _calculate_content_similarity(self, content1: str, content2: str) -> float:
        """Calculate content similarity"""
        words1 = set(content1.lower().split())
        words2 = set(content2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0
    
    def _classify_source_type(self, source: str) -> str:
        """Classify source type"""
        if 'memory' in source:
            return 'memory_system'
        elif 'graph' in source:
            return 'knowledge_system'
        elif 'external' in source:
            return 'external_system'
        elif 'user' in source:
            return 'user_system'
        else:
            return 'unknown'
    
    def _calculate_cluster_coherence(self, items: List[ContextItem]) -> float:
        """Calculate cluster coherence score"""
        if len(items) <= 1:
            return 1.0
        
        # Calculate average pairwise similarity
        similarities = []
        for i, item1 in enumerate(items):
            for item2 in items[i+1:]:
                similarity = self._calculate_content_similarity(item1.content, item2.content)
                similarities.append(similarity)
        
        return sum(similarities) / len(similarities) if similarities else 0.0
    
    def _calculate_quality_score(self, items: List[ContextItem]) -> float:
        """Calculate overall quality score for processed context"""
        if not items:
            return 0.0
        
        quality_scores = []
        for item in items:
            content_quality = self._assess_content_quality(item)
            relevance = item.relevance_score
            source_reliability = self._get_source_reliability_score(item.source)
            
            item_quality = (content_quality * 0.4 + relevance * 0.4 + source_reliability * 0.2)
            quality_scores.append(item_quality)
        
        return sum(quality_scores) / len(quality_scores)
    
    def _log_processing(self, result: ProcessedContext):
        """Log processing results"""
        processing_id = str(uuid.uuid4())
        
        self.processing_history[processing_id] = {
            "timestamp": datetime.now().isoformat(),
            "original_count": len(result.original_items),
            "processed_count": len(result.processed_items),
            "quality_score": result.quality_score,
            "transformations": result.transformations_applied,
            "filters": result.filters_applied,
            "enrichments": result.enrichments_added
        }
    
    def get_processing_statistics(self) -> Dict[str, Any]:
        """Get processing statistics"""
        if not self.processing_history:
            return {"total_processing_sessions": 0}
        
        sessions = list(self.processing_history.values())
        
        return {
            "total_processing_sessions": len(sessions),
            "average_reduction_ratio": sum(
                1 - (s["processed_count"] / s["original_count"]) 
                for s in sessions if s["original_count"] > 0
            ) / len(sessions),
            "average_quality_score": sum(s["quality_score"] for s in sessions) / len(sessions),
            "most_used_transformations": self._get_most_used_operations([s["transformations"] for s in sessions]),
            "most_used_filters": self._get_most_used_operations([s["filters"] for s in sessions]),
            "most_used_enrichments": self._get_most_used_operations([s["enrichments"] for s in sessions])
        }
    
    def _get_most_used_operations(self, operation_lists: List[List[str]]) -> Dict[str, int]:
        """Get most frequently used operations"""
        operation_counts = {}
        
        for operations in operation_lists:
            for operation in operations:
                operation_counts[operation] = operation_counts.get(operation, 0) + 1
        
        return dict(sorted(operation_counts.items(), key=lambda x: x[1], reverse=True)[:5])