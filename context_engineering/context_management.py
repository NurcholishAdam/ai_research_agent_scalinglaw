#!/usr/bin/env python3
"""
Layer 3: Context Management System for AI Research Agent
Advanced context lifecycle management, prioritization, and optimization
"""

import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, asdict
from .context_retrieval import ContextItem, ContextType
from .context_processing import ProcessedContext, ContextCluster

class ContextScope(Enum):
    SESSION = "session"
    GLOBAL = "global"
    DOMAIN = "domain"
    TEMPORAL = "temporal"
    USER = "user"

class ContextPriority(Enum):
    CRITICAL = 5
    HIGH = 4
    MEDIUM = 3
    LOW = 2
    MINIMAL = 1

@dataclass
class ContextSession:
    id: str
    research_question: str
    context_items: List[ContextItem]
    processed_context: Optional[ProcessedContext]
    priority_scores: Dict[str, float]
    session_metadata: Dict[str, Any]
    created_at: str
    last_accessed: str
    scope: ContextScope

@dataclass
class ContextPolicy:
    max_items_per_session: int
    retention_period_days: int
    priority_threshold: float
    auto_cleanup_enabled: bool
    scope_preferences: Dict[ContextScope, float]

class ContextManager:
    """Layer 3: Advanced context lifecycle management system"""
    
    def __init__(self, policy: Optional[ContextPolicy] = None):
        self.active_sessions: Dict[str, ContextSession] = {}
        self.context_cache: Dict[str, List[ContextItem]] = {}
        self.priority_matrix: Dict[str, Dict[str, float]] = {}
        self.access_patterns: Dict[str, List[Dict[str, Any]]] = {}
        self.policy = policy or self._default_policy()
        self.management_history: List[Dict[str, Any]] = []
        print("🎛️ Layer 3: Context Manager initialized")
    
    def create_session(
        self,
        research_question: str,
        context_items: List[ContextItem],
        scope: ContextScope = ContextScope.SESSION,
        priority: ContextPriority = ContextPriority.MEDIUM
    ) -> str:
        """Create a new context management session"""
        
        session_id = str(uuid.uuid4())
        
        # Calculate initial priority scores
        priority_scores = self._calculate_priority_scores(context_items, priority)
        
        # Create session metadata
        session_metadata = {
            "priority_level": priority.value,
            "scope": scope.value,
            "item_count": len(context_items),
            "average_relevance": sum(item.relevance_score for item in context_items) / len(context_items) if context_items else 0,
            "context_types": list(set(item.context_type.value for item in context_items)),
            "creation_timestamp": datetime.now().isoformat()
        }
        
        session = ContextSession(
            id=session_id,
            research_question=research_question,
            context_items=context_items,
            processed_context=None,
            priority_scores=priority_scores,
            session_metadata=session_metadata,
            created_at=datetime.now().isoformat(),
            last_accessed=datetime.now().isoformat(),
            scope=scope
        )
        
        self.active_sessions[session_id] = session
        
        # Initialize access pattern tracking
        self.access_patterns[session_id] = []
        
        print(f"🎛️ Created context session: {session_id[:8]}... ({len(context_items)} items, {scope.value} scope)")
        
        return session_id
    
    def manage_context(
        self,
        session_id: str,
        processed_context: ProcessedContext,
        optimization_goals: List[str] = None
    ) -> Dict[str, Any]:
        """Comprehensive context management with optimization"""
        
        if session_id not in self.active_sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.active_sessions[session_id]
        session.processed_context = processed_context
        session.last_accessed = datetime.now().isoformat()
        
        # Layer 3.1: Priority Management
        priority_updates = self._manage_priorities(session, optimization_goals or [])
        
        # Layer 3.2: Context Optimization
        optimization_results = self._optimize_context(session)
        
        # Layer 3.3: Lifecycle Management
        lifecycle_actions = self._manage_lifecycle(session)
        
        # Layer 3.4: Performance Monitoring
        performance_metrics = self._monitor_performance(session)
        
        # Update access patterns
        self._track_access_pattern(session_id, {
            "action": "manage_context",
            "timestamp": datetime.now().isoformat(),
            "optimization_goals": optimization_goals,
            "performance_metrics": performance_metrics
        })
        
        management_result = {
            "session_id": session_id,
            "priority_updates": priority_updates,
            "optimization_results": optimization_results,
            "lifecycle_actions": lifecycle_actions,
            "performance_metrics": performance_metrics,
            "session_health": self._assess_session_health(session)
        }
        
        # Log management action
        self._log_management_action(management_result)
        
        print(f"🎛️ Managed context session: {session_id[:8]}... (health: {management_result['session_health']:.3f})")
        
        return management_result
    
    def _manage_priorities(
        self,
        session: ContextSession,
        optimization_goals: List[str]
    ) -> Dict[str, Any]:
        """Layer 3.1: Advanced priority management"""
        
        priority_updates = {
            "items_promoted": [],
            "items_demoted": [],
            "priority_adjustments": {},
            "goal_alignments": {}
        }
        
        if not session.processed_context:
            return priority_updates
        
        # Analyze current priorities
        current_priorities = session.priority_scores.copy()
        
        # Goal-based priority adjustment
        for goal in optimization_goals:
            goal_alignment = self._calculate_goal_alignment(session, goal)
            priority_updates["goal_alignments"][goal] = goal_alignment
            
            # Adjust priorities based on goal alignment
            for item in session.processed_context.processed_items:
                alignment_score = self._calculate_item_goal_alignment(item, goal)
                if alignment_score > 0.7:
                    current_priorities[item.id] = min(1.0, current_priorities.get(item.id, 0.5) + 0.2)
                    priority_updates["items_promoted"].append(item.id)
        
        # Performance-based priority adjustment
        for item in session.processed_context.processed_items:
            performance_score = self._calculate_item_performance(item, session)
            
            if performance_score > 0.8:
                current_priorities[item.id] = min(1.0, current_priorities.get(item.id, 0.5) + 0.1)
                if item.id not in priority_updates["items_promoted"]:
                    priority_updates["items_promoted"].append(item.id)
            elif performance_score < 0.3:
                current_priorities[item.id] = max(0.1, current_priorities.get(item.id, 0.5) - 0.1)
                priority_updates["items_demoted"].append(item.id)
        
        # Update session priorities
        session.priority_scores = current_priorities
        priority_updates["priority_adjustments"] = {
            item_id: current_priorities[item_id] - session.priority_scores.get(item_id, 0.5)
            for item_id in current_priorities
        }
        
        return priority_updates
    
    def _optimize_context(self, session: ContextSession) -> Dict[str, Any]:
        """Layer 3.2: Context optimization strategies"""
        
        optimization_results = {
            "memory_optimization": {},
            "access_optimization": {},
            "quality_optimization": {},
            "size_optimization": {}
        }
        
        if not session.processed_context:
            return optimization_results
        
        # Memory optimization
        memory_usage = self._calculate_memory_usage(session)
        if memory_usage > self.policy.max_items_per_session:
            optimization_results["memory_optimization"] = self._optimize_memory(session)
        
        # Access pattern optimization
        access_patterns = self.access_patterns.get(session.id, [])
        if len(access_patterns) > 5:
            optimization_results["access_optimization"] = self._optimize_access_patterns(session)
        
        # Quality optimization
        quality_score = session.processed_context.quality_score
        if quality_score < self.policy.priority_threshold:
            optimization_results["quality_optimization"] = self._optimize_quality(session)
        
        # Size optimization
        if len(session.processed_context.processed_items) > self.policy.max_items_per_session:
            optimization_results["size_optimization"] = self._optimize_size(session)
        
        return optimization_results
    
    def _manage_lifecycle(self, session: ContextSession) -> Dict[str, Any]:
        """Layer 3.3: Context lifecycle management"""
        
        lifecycle_actions = {
            "cleanup_performed": False,
            "items_archived": [],
            "items_expired": [],
            "retention_applied": False
        }
        
        # Check retention policy
        created_time = datetime.fromisoformat(session.created_at)
        retention_cutoff = datetime.now() - timedelta(days=self.policy.retention_period_days)
        
        if created_time < retention_cutoff:
            if self.policy.auto_cleanup_enabled:
                lifecycle_actions["cleanup_performed"] = True
                lifecycle_actions["retention_applied"] = True
                # In a real implementation, this would archive or remove old items
        
        # Identify expired items
        if session.processed_context:
            for item in session.processed_context.processed_items:
                item_time = datetime.fromisoformat(item.timestamp)
                if item_time < retention_cutoff:
                    lifecycle_actions["items_expired"].append(item.id)
        
        # Archive low-priority items
        low_priority_threshold = 0.3
        for item_id, priority in session.priority_scores.items():
            if priority < low_priority_threshold:
                lifecycle_actions["items_archived"].append(item_id)
        
        return lifecycle_actions
    
    def _monitor_performance(self, session: ContextSession) -> Dict[str, Any]:
        """Layer 3.4: Performance monitoring and metrics"""
        
        performance_metrics = {
            "session_efficiency": 0.0,
            "context_utilization": 0.0,
            "access_frequency": 0.0,
            "quality_trend": "stable",
            "memory_efficiency": 0.0
        }
        
        # Session efficiency
        if session.processed_context:
            original_count = len(session.processed_context.original_items)
            processed_count = len(session.processed_context.processed_items)
            performance_metrics["session_efficiency"] = processed_count / original_count if original_count > 0 else 0
        
        # Context utilization
        access_count = len(self.access_patterns.get(session.id, []))
        performance_metrics["access_frequency"] = access_count / max(1, self._get_session_age_hours(session))
        
        # Quality trend analysis
        if session.processed_context:
            performance_metrics["quality_trend"] = self._analyze_quality_trend(session)
        
        # Memory efficiency
        performance_metrics["memory_efficiency"] = self._calculate_memory_efficiency(session)
        
        # Context utilization
        performance_metrics["context_utilization"] = self._calculate_context_utilization(session)
        
        return performance_metrics
    
    def get_session_context(
        self,
        session_id: str,
        priority_filter: Optional[float] = None,
        max_items: Optional[int] = None
    ) -> List[ContextItem]:
        """Retrieve context items from session with filtering"""
        
        if session_id not in self.active_sessions:
            return []
        
        session = self.active_sessions[session_id]
        session.last_accessed = datetime.now().isoformat()
        
        # Track access
        self._track_access_pattern(session_id, {
            "action": "get_context",
            "timestamp": datetime.now().isoformat(),
            "priority_filter": priority_filter,
            "max_items": max_items
        })
        
        if not session.processed_context:
            return session.context_items
        
        items = session.processed_context.processed_items
        
        # Apply priority filter
        if priority_filter is not None:
            items = [
                item for item in items
                if session.priority_scores.get(item.id, 0.5) >= priority_filter
            ]
        
        # Sort by priority
        items.sort(
            key=lambda x: session.priority_scores.get(x.id, 0.5),
            reverse=True
        )
        
        # Apply max items limit
        if max_items is not None:
            items = items[:max_items]
        
        return items
    
    def update_context_priorities(
        self,
        session_id: str,
        priority_updates: Dict[str, float]
    ) -> bool:
        """Update context item priorities"""
        
        if session_id not in self.active_sessions:
            return False
        
        session = self.active_sessions[session_id]
        
        for item_id, new_priority in priority_updates.items():
            session.priority_scores[item_id] = max(0.0, min(1.0, new_priority))
        
        session.last_accessed = datetime.now().isoformat()
        
        return True
    
    def cleanup_sessions(self, force: bool = False) -> Dict[str, Any]:
        """Clean up expired or unused sessions"""
        
        cleanup_results = {
            "sessions_cleaned": 0,
            "items_archived": 0,
            "memory_freed": 0,
            "cleanup_timestamp": datetime.now().isoformat()
        }
        
        sessions_to_remove = []
        
        for session_id, session in self.active_sessions.items():
            should_cleanup = False
            
            # Check retention policy
            created_time = datetime.fromisoformat(session.created_at)
            retention_cutoff = datetime.now() - timedelta(days=self.policy.retention_period_days)
            
            if created_time < retention_cutoff or force:
                should_cleanup = True
            
            # Check access patterns
            last_accessed = datetime.fromisoformat(session.last_accessed)
            if datetime.now() - last_accessed > timedelta(days=7):  # 7 days inactive
                should_cleanup = True
            
            if should_cleanup:
                sessions_to_remove.append(session_id)
                cleanup_results["sessions_cleaned"] += 1
                if session.processed_context:
                    cleanup_results["items_archived"] += len(session.processed_context.processed_items)
        
        # Remove sessions
        for session_id in sessions_to_remove:
            del self.active_sessions[session_id]
            if session_id in self.access_patterns:
                del self.access_patterns[session_id]
        
        cleanup_results["memory_freed"] = len(sessions_to_remove)
        
        print(f"🧹 Cleaned up {cleanup_results['sessions_cleaned']} sessions")
        
        return cleanup_results
    
    def get_management_statistics(self) -> Dict[str, Any]:
        """Get comprehensive management statistics"""
        
        stats = {
            "active_sessions": len(self.active_sessions),
            "total_context_items": sum(
                len(session.context_items) for session in self.active_sessions.values()
            ),
            "average_session_age_hours": self._calculate_average_session_age(),
            "memory_usage": self._calculate_total_memory_usage(),
            "access_patterns": self._analyze_access_patterns(),
            "priority_distribution": self._analyze_priority_distribution(),
            "scope_distribution": self._analyze_scope_distribution(),
            "performance_summary": self._calculate_performance_summary()
        }
        
        return stats
    
    # Helper methods
    
    def _default_policy(self) -> ContextPolicy:
        """Create default context management policy"""
        return ContextPolicy(
            max_items_per_session=20,
            retention_period_days=30,
            priority_threshold=0.6,
            auto_cleanup_enabled=True,
            scope_preferences={
                ContextScope.CRITICAL: 1.0,
                ContextScope.SESSION: 0.8,
                ContextScope.DOMAIN: 0.7,
                ContextScope.GLOBAL: 0.6,
                ContextScope.USER: 0.5
            }
        )
    
    def _calculate_priority_scores(
        self,
        context_items: List[ContextItem],
        base_priority: ContextPriority
    ) -> Dict[str, float]:
        """Calculate initial priority scores for context items"""
        
        priority_scores = {}
        base_score = base_priority.value / 5.0  # Normalize to 0-1
        
        for item in context_items:
            # Combine base priority with item relevance
            item_score = (base_score * 0.6) + (item.relevance_score * 0.4)
            priority_scores[item.id] = min(1.0, item_score)
        
        return priority_scores
    
    def _calculate_goal_alignment(self, session: ContextSession, goal: str) -> float:
        """Calculate how well session aligns with optimization goal"""
        
        goal_keywords = {
            "accuracy": ["accurate", "precise", "correct", "verified"],
            "speed": ["fast", "quick", "efficient", "rapid"],
            "comprehensiveness": ["complete", "thorough", "comprehensive", "detailed"],
            "relevance": ["relevant", "pertinent", "applicable", "related"]
        }
        
        if goal not in goal_keywords:
            return 0.5
        
        keywords = goal_keywords[goal]
        alignment_scores = []
        
        if session.processed_context:
            for item in session.processed_context.processed_items:
                content_lower = item.content.lower()
                keyword_matches = sum(1 for keyword in keywords if keyword in content_lower)
                alignment_scores.append(keyword_matches / len(keywords))
        
        return sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0.5
    
    def _calculate_item_goal_alignment(self, item: ContextItem, goal: str) -> float:
        """Calculate item alignment with specific goal"""
        
        goal_indicators = {
            "accuracy": ["verified", "confirmed", "validated", "peer-reviewed"],
            "speed": ["quick", "fast", "immediate", "real-time"],
            "comprehensiveness": ["detailed", "complete", "thorough", "extensive"],
            "relevance": ["relevant", "applicable", "pertinent", "related"]
        }
        
        if goal not in goal_indicators:
            return 0.5
        
        indicators = goal_indicators[goal]
        content_lower = item.content.lower()
        
        matches = sum(1 for indicator in indicators if indicator in content_lower)
        return matches / len(indicators)
    
    def _calculate_item_performance(self, item: ContextItem, session: ContextSession) -> float:
        """Calculate item performance score"""
        
        # Base performance from relevance
        base_performance = item.relevance_score
        
        # Boost from metadata quality
        metadata_quality = 0.5
        if item.metadata:
            metadata_quality = min(1.0, len(item.metadata) / 5)  # Normalize to 5 metadata fields
        
        # Source reliability factor
        source_reliability = self._get_source_reliability(item.source)
        
        return (base_performance * 0.5 + metadata_quality * 0.3 + source_reliability * 0.2)
    
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
    
    def _calculate_memory_usage(self, session: ContextSession) -> int:
        """Calculate memory usage for session"""
        if not session.processed_context:
            return len(session.context_items)
        return len(session.processed_context.processed_items)
    
    def _optimize_memory(self, session: ContextSession) -> Dict[str, Any]:
        """Optimize memory usage"""
        return {
            "strategy": "priority_based_reduction",
            "items_removed": max(0, self._calculate_memory_usage(session) - self.policy.max_items_per_session),
            "memory_saved": "estimated_bytes"
        }
    
    def _optimize_access_patterns(self, session: ContextSession) -> Dict[str, Any]:
        """Optimize based on access patterns"""
        patterns = self.access_patterns.get(session.id, [])
        return {
            "pattern_analysis": "frequent_access_optimization",
            "optimizations_applied": len(patterns),
            "efficiency_gain": "estimated_percentage"
        }
    
    def _optimize_quality(self, session: ContextSession) -> Dict[str, Any]:
        """Optimize context quality"""
        return {
            "quality_improvements": "content_filtering_and_enhancement",
            "items_enhanced": self._calculate_memory_usage(session),
            "quality_boost": "estimated_improvement"
        }
    
    def _optimize_size(self, session: ContextSession) -> Dict[str, Any]:
        """Optimize context size"""
        current_size = self._calculate_memory_usage(session)
        target_size = self.policy.max_items_per_session
        
        return {
            "size_reduction": max(0, current_size - target_size),
            "compression_ratio": target_size / current_size if current_size > 0 else 1.0,
            "items_compressed": current_size - target_size
        }
    
    def _assess_session_health(self, session: ContextSession) -> float:
        """Assess overall session health"""
        
        health_factors = []
        
        # Quality factor
        if session.processed_context:
            health_factors.append(session.processed_context.quality_score)
        else:
            health_factors.append(0.5)
        
        # Access frequency factor
        access_count = len(self.access_patterns.get(session.id, []))
        session_age_hours = self._get_session_age_hours(session)
        access_frequency = access_count / max(1, session_age_hours)
        health_factors.append(min(1.0, access_frequency))
        
        # Priority distribution factor
        if session.priority_scores:
            avg_priority = sum(session.priority_scores.values()) / len(session.priority_scores)
            health_factors.append(avg_priority)
        else:
            health_factors.append(0.5)
        
        return sum(health_factors) / len(health_factors)
    
    def _get_session_age_hours(self, session: ContextSession) -> float:
        """Get session age in hours"""
        created_time = datetime.fromisoformat(session.created_at)
        age_delta = datetime.now() - created_time
        return age_delta.total_seconds() / 3600
    
    def _analyze_quality_trend(self, session: ContextSession) -> str:
        """Analyze quality trend"""
        # Simplified trend analysis
        if session.processed_context and session.processed_context.quality_score > 0.8:
            return "improving"
        elif session.processed_context and session.processed_context.quality_score < 0.5:
            return "declining"
        else:
            return "stable"
    
    def _calculate_memory_efficiency(self, session: ContextSession) -> float:
        """Calculate memory efficiency"""
        if not session.processed_context:
            return 0.5
        
        original_count = len(session.processed_context.original_items)
        processed_count = len(session.processed_context.processed_items)
        
        if original_count == 0:
            return 1.0
        
        return 1.0 - (processed_count / original_count)
    
    def _calculate_context_utilization(self, session: ContextSession) -> float:
        """Calculate context utilization rate"""
        access_count = len(self.access_patterns.get(session.id, []))
        item_count = self._calculate_memory_usage(session)
        
        if item_count == 0:
            return 0.0
        
        return min(1.0, access_count / item_count)
    
    def _track_access_pattern(self, session_id: str, access_info: Dict[str, Any]):
        """Track access patterns for optimization"""
        if session_id not in self.access_patterns:
            self.access_patterns[session_id] = []
        
        self.access_patterns[session_id].append(access_info)
        
        # Keep only recent access patterns (last 50)
        if len(self.access_patterns[session_id]) > 50:
            self.access_patterns[session_id] = self.access_patterns[session_id][-50:]
    
    def _log_management_action(self, result: Dict[str, Any]):
        """Log management actions for analysis"""
        self.management_history.append({
            "timestamp": datetime.now().isoformat(),
            "action": "manage_context",
            "result": result
        })
        
        # Keep only recent history (last 100 actions)
        if len(self.management_history) > 100:
            self.management_history = self.management_history[-100:]
    
    def _calculate_average_session_age(self) -> float:
        """Calculate average session age in hours"""
        if not self.active_sessions:
            return 0.0
        
        total_age = sum(
            self._get_session_age_hours(session)
            for session in self.active_sessions.values()
        )
        
        return total_age / len(self.active_sessions)
    
    def _calculate_total_memory_usage(self) -> int:
        """Calculate total memory usage across all sessions"""
        return sum(
            self._calculate_memory_usage(session)
            for session in self.active_sessions.values()
        )
    
    def _analyze_access_patterns(self) -> Dict[str, Any]:
        """Analyze access patterns across all sessions"""
        total_accesses = sum(
            len(patterns) for patterns in self.access_patterns.values()
        )
        
        return {
            "total_accesses": total_accesses,
            "average_accesses_per_session": total_accesses / max(1, len(self.access_patterns)),
            "most_active_session": max(
                self.access_patterns.keys(),
                key=lambda x: len(self.access_patterns[x])
            ) if self.access_patterns else None
        }
    
    def _analyze_priority_distribution(self) -> Dict[str, Any]:
        """Analyze priority distribution across sessions"""
        all_priorities = []
        for session in self.active_sessions.values():
            all_priorities.extend(session.priority_scores.values())
        
        if not all_priorities:
            return {"distribution": "no_data"}
        
        return {
            "average_priority": sum(all_priorities) / len(all_priorities),
            "high_priority_items": sum(1 for p in all_priorities if p > 0.7),
            "low_priority_items": sum(1 for p in all_priorities if p < 0.3),
            "total_items": len(all_priorities)
        }
    
    def _analyze_scope_distribution(self) -> Dict[str, int]:
        """Analyze scope distribution"""
        scope_counts = {}
        for session in self.active_sessions.values():
            scope = session.scope.value
            scope_counts[scope] = scope_counts.get(scope, 0) + 1
        
        return scope_counts
    
    def _calculate_performance_summary(self) -> Dict[str, float]:
        """Calculate overall performance summary"""
        if not self.active_sessions:
            return {"overall_performance": 0.0}
        
        health_scores = [
            self._assess_session_health(session)
            for session in self.active_sessions.values()
        ]
        
        return {
            "overall_performance": sum(health_scores) / len(health_scores),
            "best_session_health": max(health_scores),
            "worst_session_health": min(health_scores),
            "performance_variance": max(health_scores) - min(health_scores)
        }