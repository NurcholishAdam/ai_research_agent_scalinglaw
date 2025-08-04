#!/usr/bin/env python3
"""
Scaling Laws Measurement Framework for AI Research Agent
Comprehensive framework for measuring how scientific discovery capabilities scale with resources
"""

import json
import time
import uuid
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import logging

class ScalingDimension(Enum):
    """Different dimensions along which to measure scaling"""
    COMPUTE_RESOURCES = "compute_resources"
    MEMORY_CAPACITY = "memory_capacity"
    CONTEXT_SIZE = "context_size"
    TOOL_COUNT = "tool_count"
    DATA_VOLUME = "data_volume"
    RESEARCH_COMPLEXITY = "research_complexity"
    TIME_ALLOCATION = "time_allocation"
    AGENT_COUNT = "agent_count"

class DiscoveryMetric(Enum):
    """Metrics for measuring scientific discovery capability"""
    HYPOTHESIS_GENERATION_RATE = "hypothesis_generation_rate"
    HYPOTHESIS_QUALITY_SCORE = "hypothesis_quality_score"
    NOVEL_INSIGHT_COUNT = "novel_insight_count"
    RESEARCH_DEPTH_SCORE = "research_depth_score"
    CROSS_DOMAIN_CONNECTIONS = "cross_domain_connections"
    EVIDENCE_SYNTHESIS_QUALITY = "evidence_synthesis_quality"
    RESEARCH_EFFICIENCY = "research_efficiency"
    DISCOVERY_BREAKTHROUGH_RATE = "discovery_breakthrough_rate"
    KNOWLEDGE_INTEGRATION_SCORE = "knowledge_integration_score"
    RESEARCH_REPRODUCIBILITY = "research_reproducibility"

@dataclass
class ScalingExperiment:
    """Configuration for a scaling experiment"""
    experiment_id: str
    scaling_dimension: ScalingDimension
    resource_levels: List[float]  # Different resource levels to test
    discovery_metrics: List[DiscoveryMetric]
    research_questions: List[str]
    repetitions: int
    max_time_per_experiment: int  # seconds
    quality_threshold: float

@dataclass
class ExperimentResult:
    """Results from a single scaling experiment run"""
    experiment_id: str
    resource_level: float
    scaling_dimension: ScalingDimension
    discovery_metrics: Dict[DiscoveryMetric, float]
    execution_time: float
    memory_usage: float
    research_outputs: Dict[str, Any]
    quality_scores: Dict[str, float]
    timestamp: str

@dataclass
class ScalingLaw:
    """Discovered scaling law relationship"""
    scaling_dimension: ScalingDimension
    discovery_metric: DiscoveryMetric
    power_law_exponent: float
    correlation_coefficient: float
    confidence_interval: Tuple[float, float]
    data_points: List[Tuple[float, float]]
    equation: str

class ScalingLawMeasurement:
    """Framework for measuring scaling laws in scientific discovery"""
    
    def __init__(self, research_agent=None):
        self.research_agent = research_agent
        self.experiment_results: List[ExperimentResult] = []
        self.discovered_scaling_laws: List[ScalingLaw] = []
        self.baseline_performance: Dict[str, float] = {}
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        print("📏 Scaling Laws Measurement Framework initialized")
    
    def run_scaling_experiment(self, experiment: ScalingExperiment) -> List[ExperimentResult]:
        """Run a complete scaling experiment across resource levels"""
        
        print(f"🧪 Running scaling experiment: {experiment.scaling_dimension.value}")
        print(f"   Resource levels: {experiment.resource_levels}")
        print(f"   Metrics: {[m.value for m in experiment.discovery_metrics]}")
        
        results = []
        
        for resource_level in experiment.resource_levels:
            print(f"\n📊 Testing resource level: {resource_level}")
            
            level_results = []
            for rep in range(experiment.repetitions):
                print(f"   Repetition {rep + 1}/{experiment.repetitions}")
                
                result = self._run_single_experiment(
                    experiment, resource_level, rep
                )
                level_results.append(result)
                results.append(result)
            
            # Calculate average performance at this resource level
            avg_metrics = self._calculate_average_metrics(level_results)
            print(f"   Average performance: {avg_metrics}")
        
        self.experiment_results.extend(results)
        return results
    
    def _run_single_experiment(
        self, 
        experiment: ScalingExperiment, 
        resource_level: float, 
        repetition: int
    ) -> ExperimentResult:
        """Run a single experiment at a specific resource level"""
        
        start_time = time.time()
        
        # Configure agent for this resource level
        agent_config = self._configure_agent_for_resource_level(
            experiment.scaling_dimension, resource_level
        )
        
        # Run research on sample questions
        research_outputs = {}
        quality_scores = {}
        discovery_metrics = {}
        
        for i, question in enumerate(experiment.research_questions):
            if time.time() - start_time > experiment.max_time_per_experiment:
                break
            
            try:
                # Run research with configured resources
                research_result = self._run_research_with_config(
                    question, agent_config, experiment.scaling_dimension, resource_level
                )
                
                research_outputs[f"question_{i}"] = research_result
                
                # Calculate discovery metrics for this research
                metrics = self._calculate_discovery_metrics(
                    research_result, experiment.discovery_metrics
                )
                
                # Aggregate metrics
                for metric, value in metrics.items():
                    if metric not in discovery_metrics:
                        discovery_metrics[metric] = []
                    discovery_metrics[metric].append(value)
                
                # Calculate quality scores
                quality_scores[f"question_{i}"] = self._calculate_quality_score(research_result)
                
            except Exception as e:
                self.logger.error(f"Experiment failed for question {i}: {e}")
                continue
        
        # Average the metrics across questions
        averaged_metrics = {
            metric: np.mean(values) for metric, values in discovery_metrics.items()
        }
        
        execution_time = time.time() - start_time
        memory_usage = self._estimate_memory_usage(agent_config)
        
        return ExperimentResult(
            experiment_id=experiment.experiment_id,
            resource_level=resource_level,
            scaling_dimension=experiment.scaling_dimension,
            discovery_metrics=averaged_metrics,
            execution_time=execution_time,
            memory_usage=memory_usage,
            research_outputs=research_outputs,
            quality_scores=quality_scores,
            timestamp=datetime.now().isoformat()
        )
    
    def _configure_agent_for_resource_level(
        self, 
        scaling_dimension: ScalingDimension, 
        resource_level: float
    ) -> Dict[str, Any]:
        """Configure agent parameters for specific resource level"""
        
        base_config = {
            "max_iterations": 10,
            "context_items": 15,
            "tool_count": 10,
            "memory_capacity": 1000,
            "agent_count": 1,
            "time_limit": 300,
            "quality_threshold": 0.7
        }
        
        if scaling_dimension == ScalingDimension.COMPUTE_RESOURCES:
            # Scale computational resources (iterations, parallel processing)
            base_config["max_iterations"] = int(10 * resource_level)
            base_config["parallel_processing"] = resource_level > 1.5
            
        elif scaling_dimension == ScalingDimension.MEMORY_CAPACITY:
            # Scale memory-related parameters
            base_config["memory_capacity"] = int(1000 * resource_level)
            base_config["context_items"] = int(15 * resource_level)
            
        elif scaling_dimension == ScalingDimension.CONTEXT_SIZE:
            # Scale context window size
            base_config["context_items"] = int(15 * resource_level)
            base_config["max_context_length"] = int(5000 * resource_level)
            
        elif scaling_dimension == ScalingDimension.TOOL_COUNT:
            # Scale number of available tools
            base_config["tool_count"] = int(10 * resource_level)
            base_config["tool_diversity"] = resource_level
            
        elif scaling_dimension == ScalingDimension.DATA_VOLUME:
            # Scale data access and processing
            base_config["data_sources"] = int(5 * resource_level)
            base_config["search_depth"] = int(3 * resource_level)
            
        elif scaling_dimension == ScalingDimension.RESEARCH_COMPLEXITY:
            # Scale research complexity handling
            base_config["hypothesis_depth"] = int(3 * resource_level)
            base_config["analysis_layers"] = int(2 * resource_level)
            
        elif scaling_dimension == ScalingDimension.TIME_ALLOCATION:
            # Scale time resources
            base_config["time_limit"] = int(300 * resource_level)
            base_config["deep_analysis_time"] = int(60 * resource_level)
            
        elif scaling_dimension == ScalingDimension.AGENT_COUNT:
            # Scale multi-agent resources
            base_config["agent_count"] = int(resource_level)
            base_config["collaboration_depth"] = resource_level
        
        return base_config
    
    def _run_research_with_config(
        self, 
        question: str, 
        config: Dict[str, Any], 
        scaling_dimension: ScalingDimension,
        resource_level: float
    ) -> Dict[str, Any]:
        """Run research with specific configuration"""
        
        if self.research_agent is None:
            # Simulate research results for testing
            return self._simulate_research_result(question, config, scaling_dimension, resource_level)
        
        # Configure the actual research agent
        original_config = self._backup_agent_config()
        self._apply_config_to_agent(config)
        
        try:
            # Run research
            result = self.research_agent.invoke({
                "research_question": question,
                "session_id": f"scaling_exp_{uuid.uuid4()}",
                "max_iterations": config.get("max_iterations", 10)
            })
            
            return {
                "final_answer": result.get("final_answer", ""),
                "research_plan": result.get("research_plan", []),
                "findings": result.get("findings", []),
                "hypotheses": result.get("hypotheses", []),
                "quality_assessment": result.get("quality_assessment", {}),
                "multi_agent_analysis": result.get("multi_agent_analysis", {}),
                "context_orchestration": result.get("context_orchestration", {}),
                "execution_metadata": {
                    "scaling_dimension": scaling_dimension.value,
                    "resource_level": resource_level,
                    "config_applied": config
                }
            }
            
        finally:
            # Restore original configuration
            self._restore_agent_config(original_config)
    
    def _simulate_research_result(
        self, 
        question: str, 
        config: Dict[str, Any], 
        scaling_dimension: ScalingDimension,
        resource_level: float
    ) -> Dict[str, Any]:
        """Simulate research results for testing purposes"""
        
        # Simulate scaling effects
        base_quality = 0.6
        scaling_factor = min(2.0, resource_level ** 0.5)  # Square root scaling
        
        simulated_quality = min(1.0, base_quality * scaling_factor)
        hypothesis_count = max(1, int(3 * scaling_factor))
        finding_count = max(2, int(5 * scaling_factor))
        
        return {
            "final_answer": f"Simulated research answer for: {question} (quality: {simulated_quality:.2f})",
            "research_plan": [f"Step {i+1}: Simulated research step" for i in range(int(3 * scaling_factor))],
            "findings": [
                {
                    "step": i,
                    "analysis": f"Simulated finding {i+1} with quality {simulated_quality:.2f}",
                    "sources_used": {"external_sources": int(2 * scaling_factor)}
                }
                for i in range(finding_count)
            ],
            "hypotheses": [
                {
                    "statement": f"Simulated hypothesis {i+1}",
                    "confidence": min(1.0, 0.5 + 0.3 * scaling_factor),
                    "supporting_evidence": [f"Evidence {j+1}" for j in range(int(2 * scaling_factor))]
                }
                for i in range(hypothesis_count)
            ],
            "quality_assessment": {
                "overall_quality_score": simulated_quality * 10,
                "confidence_assessment": simulated_quality,
                "external_sources_used": int(3 * scaling_factor),
                "source_diversity": min(4, int(2 * scaling_factor))
            },
            "multi_agent_analysis": {
                "confidence_scores": {
                    "researcher_avg": simulated_quality,
                    "critic_avg": simulated_quality * 0.9,
                    "synthesis_confidence": simulated_quality * 1.1
                }
            },
            "context_orchestration": {
                "quality_score": simulated_quality,
                "context_items_count": int(10 * scaling_factor),
                "execution_time": max(5, 30 / scaling_factor)  # Inverse scaling for time
            },
            "execution_metadata": {
                "scaling_dimension": scaling_dimension.value,
                "resource_level": resource_level,
                "simulated": True
            }
        }
    
    def _calculate_discovery_metrics(
        self, 
        research_result: Dict[str, Any], 
        metrics: List[DiscoveryMetric]
    ) -> Dict[DiscoveryMetric, float]:
        """Calculate discovery metrics from research results"""
        
        calculated_metrics = {}
        
        for metric in metrics:
            if metric == DiscoveryMetric.HYPOTHESIS_GENERATION_RATE:
                hypothesis_count = len(research_result.get("hypotheses", []))
                execution_time = research_result.get("context_orchestration", {}).get("execution_time", 60)
                calculated_metrics[metric] = hypothesis_count / max(1, execution_time / 60)  # hypotheses per minute
                
            elif metric == DiscoveryMetric.HYPOTHESIS_QUALITY_SCORE:
                hypotheses = research_result.get("hypotheses", [])
                if hypotheses:
                    avg_confidence = np.mean([h.get("confidence", 0.5) for h in hypotheses])
                    calculated_metrics[metric] = avg_confidence
                else:
                    calculated_metrics[metric] = 0.0
                    
            elif metric == DiscoveryMetric.NOVEL_INSIGHT_COUNT:
                # Count novel insights based on hypothesis novelty and cross-references
                hypotheses = research_result.get("hypotheses", [])
                findings = research_result.get("findings", [])
                novel_count = len(hypotheses) + len([f for f in findings if "novel" in f.get("analysis", "").lower()])
                calculated_metrics[metric] = novel_count
                
            elif metric == DiscoveryMetric.RESEARCH_DEPTH_SCORE:
                findings = research_result.get("findings", [])
                quality_score = research_result.get("quality_assessment", {}).get("overall_quality_score", 5)
                depth_score = len(findings) * (quality_score / 10)
                calculated_metrics[metric] = depth_score
                
            elif metric == DiscoveryMetric.CROSS_DOMAIN_CONNECTIONS:
                # Estimate cross-domain connections from multi-agent analysis
                multi_agent = research_result.get("multi_agent_analysis", {})
                connection_score = len(str(multi_agent)) / 1000  # Rough estimate
                calculated_metrics[metric] = min(10, connection_score)
                
            elif metric == DiscoveryMetric.EVIDENCE_SYNTHESIS_QUALITY:
                quality_assessment = research_result.get("quality_assessment", {})
                synthesis_quality = quality_assessment.get("overall_quality_score", 5) / 10
                calculated_metrics[metric] = synthesis_quality
                
            elif metric == DiscoveryMetric.RESEARCH_EFFICIENCY:
                quality_score = research_result.get("quality_assessment", {}).get("overall_quality_score", 5)
                execution_time = research_result.get("context_orchestration", {}).get("execution_time", 60)
                efficiency = quality_score / max(1, execution_time / 10)  # quality per 10 seconds
                calculated_metrics[metric] = efficiency
                
            elif metric == DiscoveryMetric.DISCOVERY_BREAKTHROUGH_RATE:
                # Estimate breakthrough potential from hypothesis confidence and novelty
                hypotheses = research_result.get("hypotheses", [])
                high_confidence_hypotheses = [h for h in hypotheses if h.get("confidence", 0) > 0.8]
                breakthrough_rate = len(high_confidence_hypotheses) / max(1, len(hypotheses))
                calculated_metrics[metric] = breakthrough_rate
                
            elif metric == DiscoveryMetric.KNOWLEDGE_INTEGRATION_SCORE:
                # Score based on source diversity and cross-references
                quality_assessment = research_result.get("quality_assessment", {})
                source_diversity = quality_assessment.get("source_diversity", 1)
                external_sources = quality_assessment.get("external_sources_used", 1)
                integration_score = (source_diversity * external_sources) / 10
                calculated_metrics[metric] = min(1.0, integration_score)
                
            elif metric == DiscoveryMetric.RESEARCH_REPRODUCIBILITY:
                # Estimate reproducibility from methodology and source quality
                quality_assessment = research_result.get("quality_assessment", {})
                confidence = quality_assessment.get("confidence_assessment", 0.5)
                source_reliability = min(1.0, quality_assessment.get("external_sources_used", 1) / 5)
                reproducibility = (confidence + source_reliability) / 2
                calculated_metrics[metric] = reproducibility
        
        return calculated_metrics
    
    def analyze_scaling_laws(self, results: List[ExperimentResult]) -> List[ScalingLaw]:
        """Analyze experiment results to discover scaling laws"""
        
        print("📈 Analyzing scaling laws from experiment results...")
        
        scaling_laws = []
        
        # Group results by scaling dimension and metric
        grouped_results = {}
        for result in results:
            key = (result.scaling_dimension, tuple(result.discovery_metrics.keys()))
            if key not in grouped_results:
                grouped_results[key] = []
            grouped_results[key].append(result)
        
        for (scaling_dimension, metrics), group_results in grouped_results.items():
            for metric in metrics:
                # Extract data points
                data_points = []
                for result in group_results:
                    if metric in result.discovery_metrics:
                        data_points.append((result.resource_level, result.discovery_metrics[metric]))
                
                if len(data_points) < 3:  # Need at least 3 points for meaningful analysis
                    continue
                
                # Fit power law: y = a * x^b
                scaling_law = self._fit_power_law(scaling_dimension, metric, data_points)
                if scaling_law:
                    scaling_laws.append(scaling_law)
        
        self.discovered_scaling_laws.extend(scaling_laws)
        return scaling_laws
    
    def _fit_power_law(
        self, 
        scaling_dimension: ScalingDimension, 
        metric: DiscoveryMetric, 
        data_points: List[Tuple[float, float]]
    ) -> Optional[ScalingLaw]:
        """Fit a power law to the data points"""
        
        try:
            x_values = np.array([point[0] for point in data_points])
            y_values = np.array([point[1] for point in data_points])
            
            # Remove zero or negative values for log transformation
            valid_indices = (x_values > 0) & (y_values > 0)
            x_values = x_values[valid_indices]
            y_values = y_values[valid_indices]
            
            if len(x_values) < 3:
                return None
            
            # Log-linear regression: log(y) = log(a) + b * log(x)
            log_x = np.log(x_values)
            log_y = np.log(y_values)
            
            # Linear regression on log-transformed data
            coeffs = np.polyfit(log_x, log_y, 1)
            power_law_exponent = coeffs[0]  # This is 'b' in y = a * x^b
            log_a = coeffs[1]
            
            # Calculate correlation coefficient
            correlation = np.corrcoef(log_x, log_y)[0, 1]
            
            # Calculate confidence interval (simplified)
            residuals = log_y - (log_a + power_law_exponent * log_x)
            std_error = np.std(residuals) / np.sqrt(len(residuals))
            confidence_interval = (
                power_law_exponent - 1.96 * std_error,
                power_law_exponent + 1.96 * std_error
            )
            
            # Create equation string
            a_value = np.exp(log_a)
            equation = f"{metric.value} = {a_value:.3f} * {scaling_dimension.value}^{power_law_exponent:.3f}"
            
            return ScalingLaw(
                scaling_dimension=scaling_dimension,
                discovery_metric=metric,
                power_law_exponent=power_law_exponent,
                correlation_coefficient=correlation,
                confidence_interval=confidence_interval,
                data_points=data_points,
                equation=equation
            )
            
        except Exception as e:
            self.logger.error(f"Failed to fit power law for {scaling_dimension.value} vs {metric.value}: {e}")
            return None
    
    def generate_scaling_report(self, output_file: str = "scaling_laws_report.json") -> Dict[str, Any]:
        """Generate comprehensive scaling laws report"""
        
        report = {
            "experiment_summary": {
                "total_experiments": len(self.experiment_results),
                "scaling_dimensions_tested": list(set(r.scaling_dimension.value for r in self.experiment_results)),
                "discovery_metrics_measured": list(set(
                    metric.value for r in self.experiment_results for metric in r.discovery_metrics.keys()
                )),
                "total_scaling_laws_discovered": len(self.discovered_scaling_laws)
            },
            "scaling_laws": [
                {
                    "scaling_dimension": law.scaling_dimension.value,
                    "discovery_metric": law.discovery_metric.value,
                    "power_law_exponent": law.power_law_exponent,
                    "correlation_coefficient": law.correlation_coefficient,
                    "confidence_interval": law.confidence_interval,
                    "equation": law.equation,
                    "data_points": law.data_points,
                    "interpretation": self._interpret_scaling_law(law)
                }
                for law in self.discovered_scaling_laws
            ],
            "performance_analysis": self._analyze_performance_trends(),
            "recommendations": self._generate_scaling_recommendations(),
            "timestamp": datetime.now().isoformat()
        }
        
        # Save report
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📊 Scaling laws report saved to: {output_file}")
        return report
    
    def _interpret_scaling_law(self, law: ScalingLaw) -> str:
        """Interpret the meaning of a scaling law"""
        
        exponent = law.power_law_exponent
        correlation = law.correlation_coefficient
        
        # Interpret exponent
        if exponent > 1.0:
            scaling_type = "super-linear (accelerating returns)"
        elif exponent == 1.0:
            scaling_type = "linear"
        elif exponent > 0.5:
            scaling_type = "sub-linear but positive"
        elif exponent > 0:
            scaling_type = "diminishing returns"
        else:
            scaling_type = "negative scaling"
        
        # Interpret correlation strength
        if abs(correlation) > 0.9:
            correlation_strength = "very strong"
        elif abs(correlation) > 0.7:
            correlation_strength = "strong"
        elif abs(correlation) > 0.5:
            correlation_strength = "moderate"
        else:
            correlation_strength = "weak"
        
        return f"{law.discovery_metric.value} shows {scaling_type} scaling with {law.scaling_dimension.value} " \
               f"(exponent: {exponent:.3f}, {correlation_strength} correlation: {correlation:.3f})"
    
    def _analyze_performance_trends(self) -> Dict[str, Any]:
        """Analyze overall performance trends"""
        
        if not self.experiment_results:
            return {"error": "No experiment results available"}
        
        # Calculate average performance by scaling dimension
        dimension_performance = {}
        for result in self.experiment_results:
            dim = result.scaling_dimension.value
            if dim not in dimension_performance:
                dimension_performance[dim] = {
                    "resource_levels": [],
                    "avg_quality": [],
                    "avg_efficiency": [],
                    "avg_execution_time": []
                }
            
            dimension_performance[dim]["resource_levels"].append(result.resource_level)
            
            # Calculate average quality across all metrics
            if result.discovery_metrics:
                avg_quality = np.mean(list(result.discovery_metrics.values()))
                dimension_performance[dim]["avg_quality"].append(avg_quality)
            
            dimension_performance[dim]["avg_execution_time"].append(result.execution_time)
        
        return dimension_performance
    
    def _generate_scaling_recommendations(self) -> List[str]:
        """Generate recommendations based on scaling law analysis"""
        
        recommendations = []
        
        for law in self.discovered_scaling_laws:
            if law.power_law_exponent > 1.0 and law.correlation_coefficient > 0.7:
                recommendations.append(
                    f"Strong positive scaling found for {law.discovery_metric.value} with {law.scaling_dimension.value}. "
                    f"Consider increasing {law.scaling_dimension.value} for accelerating returns."
                )
            elif law.power_law_exponent < 0.5 and law.correlation_coefficient > 0.5:
                recommendations.append(
                    f"Diminishing returns observed for {law.discovery_metric.value} with {law.scaling_dimension.value}. "
                    f"Consider optimizing efficiency rather than scaling this dimension."
                )
        
        if not recommendations:
            recommendations.append("Insufficient data for specific recommendations. Consider running more experiments.")
        
        return recommendations
    
    def visualize_scaling_laws(self, output_dir: str = "scaling_plots/"):
        """Create visualizations of discovered scaling laws"""
        
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        for law in self.discovered_scaling_laws:
            plt.figure(figsize=(10, 6))
            
            # Extract data points
            x_values = [point[0] for point in law.data_points]
            y_values = [point[1] for point in law.data_points]
            
            # Plot data points
            plt.scatter(x_values, y_values, alpha=0.7, s=50, label='Data Points')
            
            # Plot fitted power law
            x_fit = np.linspace(min(x_values), max(x_values), 100)
            # Extract coefficient from equation
            a_value = float(law.equation.split(' = ')[1].split(' * ')[0])
            y_fit = a_value * (x_fit ** law.power_law_exponent)
            plt.plot(x_fit, y_fit, 'r-', linewidth=2, label=f'Power Law Fit (exponent: {law.power_law_exponent:.3f})')
            
            plt.xlabel(law.scaling_dimension.value.replace('_', ' ').title())
            plt.ylabel(law.discovery_metric.value.replace('_', ' ').title())
            plt.title(f'Scaling Law: {law.discovery_metric.value} vs {law.scaling_dimension.value}')
            plt.legend()
            plt.grid(True, alpha=0.3)
            
            # Add correlation info
            plt.text(0.05, 0.95, f'R² = {law.correlation_coefficient**2:.3f}', 
                    transform=plt.gca().transAxes, bbox=dict(boxstyle="round", facecolor='wheat'))
            
            filename = f"{law.scaling_dimension.value}_vs_{law.discovery_metric.value}.png"
            plt.savefig(os.path.join(output_dir, filename), dpi=300, bbox_inches='tight')
            plt.close()
        
        print(f"📊 Scaling law visualizations saved to: {output_dir}")
    
    # Helper methods for agent configuration (to be implemented based on actual agent structure)
    
    def _backup_agent_config(self) -> Dict[str, Any]:
        """Backup current agent configuration"""
        return {}  # Implement based on actual agent structure
    
    def _apply_config_to_agent(self, config: Dict[str, Any]):
        """Apply configuration to research agent"""
        pass  # Implement based on actual agent structure
    
    def _restore_agent_config(self, config: Dict[str, Any]):
        """Restore agent configuration"""
        pass  # Implement based on actual agent structure
    
    def _estimate_memory_usage(self, config: Dict[str, Any]) -> float:
        """Estimate memory usage for given configuration"""
        # Simple estimation based on configuration parameters
        base_memory = 100  # MB
        memory_factor = config.get("memory_capacity", 1000) / 1000
        context_factor = config.get("context_items", 15) / 15
        
        return base_memory * (1 + memory_factor + context_factor)
    
    def _calculate_quality_score(self, research_result: Dict[str, Any]) -> float:
        """Calculate overall quality score for research result"""
        quality_assessment = research_result.get("quality_assessment", {})
        return quality_assessment.get("overall_quality_score", 5) / 10
    
    def _calculate_average_metrics(self, results: List[ExperimentResult]) -> Dict[str, float]:
        """Calculate average metrics across multiple results"""
        if not results:
            return {}
        
        all_metrics = set()
        for result in results:
            all_metrics.update(result.discovery_metrics.keys())
        
        averaged = {}
        for metric in all_metrics:
            values = [result.discovery_metrics.get(metric, 0) for result in results if metric in result.discovery_metrics]
            if values:
                averaged[metric.value] = np.mean(values)
        
        return averaged