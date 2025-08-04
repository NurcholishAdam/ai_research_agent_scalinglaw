#!/usr/bin/env python3
"""
Practical Implementation: Running Scaling Law Experiments on AI Research Agent
Example experiments and analysis for measuring scientific discovery scaling laws
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scaling_measurement_framework import (
    ScalingLawMeasurement, ScalingExperiment, ScalingDimension, 
    DiscoveryMetric, OrchestrationStrategy
)
from agent.research_agent import create_agent
import numpy as np
import json

def create_sample_experiments() -> list[ScalingExperiment]:
    """Create a comprehensive set of scaling experiments"""
    
    # Standard research questions across different domains and complexities
    research_questions = [
        # Simple factual questions
        "What is machine learning?",
        "How does photosynthesis work?",
        "What are the main causes of climate change?",
        
        # Medium complexity analytical questions
        "How do neural networks learn and what are the key mechanisms?",
        "What are the relationships between economic growth and environmental sustainability?",
        "How does quantum computing differ from classical computing in problem-solving approaches?",
        
        # Complex research questions
        "What are the emerging patterns in AI safety research and how do they relate to alignment problems?",
        "How do complex systems theory principles apply to understanding ecosystem resilience?",
        "What are the interdisciplinary connections between cognitive science, AI, and neuroscience in understanding consciousness?"
    ]
    
    experiments = []
    
    # Experiment 1: Compute Resources Scaling
    experiments.append(ScalingExperiment(
        experiment_id="compute_scaling_2024",
        scaling_dimension=ScalingDimension.COMPUTE_RESOURCES,
        resource_levels=[0.5, 1.0, 1.5, 2.0, 3.0, 4.0],  # 0.5x to 4x compute
        discovery_metrics=[
            DiscoveryMetric.HYPOTHESIS_GENERATION_RATE,
            DiscoveryMetric.HYPOTHESIS_QUALITY_SCORE,
            DiscoveryMetric.RESEARCH_DEPTH_SCORE,
            DiscoveryMetric.RESEARCH_EFFICIENCY
        ],
        research_questions=research_questions[:6],  # Use subset for faster testing
        repetitions=3,
        max_time_per_experiment=300,  # 5 minutes per experiment
        quality_threshold=0.7
    ))
    
    # Experiment 2: Memory Capacity Scaling
    experiments.append(ScalingExperiment(
        experiment_id="memory_scaling_2024",
        scaling_dimension=ScalingDimension.MEMORY_CAPACITY,
        resource_levels=[0.5, 1.0, 2.0, 4.0, 8.0],  # 0.5x to 8x memory
        discovery_metrics=[
            DiscoveryMetric.KNOWLEDGE_INTEGRATION_SCORE,
            DiscoveryMetric.CROSS_DOMAIN_CONNECTIONS,
            DiscoveryMetric.EVIDENCE_SYNTHESIS_QUALITY,
            DiscoveryMetric.RESEARCH_REPRODUCIBILITY
        ],
        research_questions=research_questions[3:],  # Use more complex questions
        repetitions=3,
        max_time_per_experiment=400,
        quality_threshold=0.7
    ))
    
    # Experiment 3: Context Size Scaling
    experiments.append(ScalingExperiment(
        experiment_id="context_scaling_2024",
        scaling_dimension=ScalingDimension.CONTEXT_SIZE,
        resource_levels=[0.5, 1.0, 1.5, 2.0, 3.0],  # 0.5x to 3x context
        discovery_metrics=[
            DiscoveryMetric.NOVEL_INSIGHT_COUNT,
            DiscoveryMetric.CROSS_DOMAIN_CONNECTIONS,
            DiscoveryMetric.KNOWLEDGE_INTEGRATION_SCORE,
            DiscoveryMetric.HYPOTHESIS_QUALITY_SCORE
        ],
        research_questions=research_questions,
        repetitions=2,
        max_time_per_experiment=350,
        quality_threshold=0.6
    ))
    
    # Experiment 4: Tool Count Scaling
    experiments.append(ScalingExperiment(
        experiment_id="tool_scaling_2024",
        scaling_dimension=ScalingDimension.TOOL_COUNT,
        resource_levels=[0.5, 1.0, 1.5, 2.0],  # 0.5x to 2x tools
        discovery_metrics=[
            DiscoveryMetric.RESEARCH_EFFICIENCY,
            DiscoveryMetric.EVIDENCE_SYNTHESIS_QUALITY,
            DiscoveryMetric.DISCOVERY_BREAKTHROUGH_RATE,
            DiscoveryMetric.RESEARCH_DEPTH_SCORE
        ],
        research_questions=research_questions[:7],
        repetitions=3,
        max_time_per_experiment=300,
        quality_threshold=0.7
    ))
    
    # Experiment 5: Data Volume Scaling
    experiments.append(ScalingExperiment(
        experiment_id="data_volume_scaling_2024",
        scaling_dimension=ScalingDimension.DATA_VOLUME,
        resource_levels=[1.0, 2.0, 4.0, 6.0],  # 1x to 6x data access
        discovery_metrics=[
            DiscoveryMetric.EVIDENCE_SYNTHESIS_QUALITY,
            DiscoveryMetric.RESEARCH_REPRODUCIBILITY,
            DiscoveryMetric.KNOWLEDGE_INTEGRATION_SCORE,
            DiscoveryMetric.NOVEL_INSIGHT_COUNT
        ],
        research_questions=research_questions[2:8],
        repetitions=2,
        max_time_per_experiment=450,
        quality_threshold=0.6
    ))
    
    return experiments

def run_comprehensive_scaling_analysis():
    """Run comprehensive scaling law analysis"""
    
    print("🚀 Starting Comprehensive Scaling Law Analysis for AI Research Agent")
    print("=" * 80)
    
    # Initialize measurement framework
    try:
        # Try to use actual research agent
        research_agent = create_agent()
        print("✅ Using actual research agent for experiments")
    except Exception as e:
        print(f"⚠️ Could not initialize research agent: {e}")
        print("📊 Using simulation mode for scaling experiments")
        research_agent = None
    
    scaling_measurement = ScalingLawMeasurement(research_agent)
    
    # Create experiments
    experiments = create_sample_experiments()
    print(f"📋 Created {len(experiments)} scaling experiments")
    
    all_results = []
    
    # Run each experiment
    for i, experiment in enumerate(experiments, 1):
        print(f"\n🧪 Running Experiment {i}/{len(experiments)}: {experiment.experiment_id}")
        print(f"   Scaling Dimension: {experiment.scaling_dimension.value}")
        print(f"   Resource Levels: {experiment.resource_levels}")
        print(f"   Discovery Metrics: {[m.value for m in experiment.discovery_metrics]}")
        
        try:
            results = scaling_measurement.run_scaling_experiment(experiment)
            all_results.extend(results)
            print(f"✅ Experiment completed: {len(results)} results collected")
            
        except Exception as e:
            print(f"❌ Experiment failed: {e}")
            continue
    
    print(f"\n📊 Total Results Collected: {len(all_results)}")
    
    # Analyze scaling laws
    print("\n📈 Analyzing Scaling Laws...")
    scaling_laws = scaling_measurement.analyze_scaling_laws(all_results)
    
    print(f"🔍 Discovered {len(scaling_laws)} scaling laws:")
    for law in scaling_laws:
        print(f"   • {law.discovery_metric.value} ∝ {law.scaling_dimension.value}^{law.power_law_exponent:.3f} "
              f"(R²={law.correlation_coefficient**2:.3f})")
    
    # Generate comprehensive report
    print("\n📋 Generating Scaling Laws Report...")
    report = scaling_measurement.generate_scaling_report("scaling_laws_analysis_report.json")
    
    # Create visualizations
    print("\n📊 Creating Visualizations...")
    try:
        scaling_measurement.visualize_scaling_laws("scaling_plots/")
        print("✅ Visualizations created successfully")
    except Exception as e:
        print(f"⚠️ Visualization creation failed: {e}")
    
    # Print key findings
    print_key_findings(report)
    
    return scaling_measurement, report

def print_key_findings(report: dict):
    """Print key findings from scaling analysis"""
    
    print("\n" + "=" * 80)
    print("🔍 KEY FINDINGS: SCALING LAWS FOR SCIENTIFIC DISCOVERY")
    print("=" * 80)
    
    # Summary statistics
    summary = report["experiment_summary"]
    print(f"📊 Experiments Conducted: {summary['total_experiments']}")
    print(f"🔬 Scaling Dimensions Tested: {len(summary['scaling_dimensions_tested'])}")
    print(f"📈 Discovery Metrics Measured: {len(summary['discovery_metrics_measured'])}")
    print(f"⚖️ Scaling Laws Discovered: {summary['total_scaling_laws_discovered']}")
    
    # Scaling laws analysis
    if report["scaling_laws"]:
        print(f"\n🏆 TOP SCALING LAWS DISCOVERED:")
        
        # Sort by correlation strength
        sorted_laws = sorted(report["scaling_laws"], 
                           key=lambda x: abs(x["correlation_coefficient"]), 
                           reverse=True)
        
        for i, law in enumerate(sorted_laws[:5], 1):  # Top 5
            print(f"\n{i}. {law['discovery_metric'].upper()} vs {law['scaling_dimension'].upper()}")
            print(f"   📐 Equation: {law['equation']}")
            print(f"   📊 Exponent: {law['power_law_exponent']:.3f}")
            print(f"   🎯 Correlation: {law['correlation_coefficient']:.3f} (R²={law['correlation_coefficient']**2:.3f})")
            print(f"   💡 Interpretation: {law['interpretation']}")
        
        # Identify strongest scaling relationships
        super_linear = [law for law in report["scaling_laws"] if law["power_law_exponent"] > 1.0]
        if super_linear:
            print(f"\n🚀 SUPER-LINEAR SCALING DISCOVERED ({len(super_linear)} relationships):")
            for law in super_linear:
                print(f"   • {law['discovery_metric']} shows accelerating returns with {law['scaling_dimension']}")
                print(f"     Exponent: {law['power_law_exponent']:.3f} (>1.0 = accelerating returns)")
        
        # Identify diminishing returns
        diminishing = [law for law in report["scaling_laws"] if 0 < law["power_law_exponent"] < 0.5]
        if diminishing:
            print(f"\n📉 DIMINISHING RETURNS IDENTIFIED ({len(diminishing)} relationships):")
            for law in diminishing:
                print(f"   • {law['discovery_metric']} shows diminishing returns with {law['scaling_dimension']}")
                print(f"     Exponent: {law['power_law_exponent']:.3f} (<0.5 = diminishing returns)")
    
    # Recommendations
    if report["recommendations"]:
        print(f"\n💡 SCALING RECOMMENDATIONS:")
        for i, rec in enumerate(report["recommendations"], 1):
            print(f"{i}. {rec}")
    
    print("\n" + "=" * 80)
    print("🎯 IMPLICATIONS FOR AI RESEARCH AGENT OPTIMIZATION:")
    print("=" * 80)
    
    print("Based on the scaling law analysis, consider these optimization strategies:")
    print("• Focus resources on dimensions showing super-linear scaling")
    print("• Optimize efficiency for dimensions with diminishing returns")
    print("• Use scaling laws to predict performance at different resource levels")
    print("• Design adaptive resource allocation based on discovered scaling patterns")
    print("• Monitor scaling law evolution as the system improves")

def run_quick_scaling_test():
    """Run a quick scaling test for demonstration"""
    
    print("⚡ Running Quick Scaling Test (Demonstration Mode)")
    print("=" * 60)
    
    # Create a simple experiment
    quick_experiment = ScalingExperiment(
        experiment_id="quick_test_2024",
        scaling_dimension=ScalingDimension.COMPUTE_RESOURCES,
        resource_levels=[0.5, 1.0, 2.0, 3.0],
        discovery_metrics=[
            DiscoveryMetric.HYPOTHESIS_GENERATION_RATE,
            DiscoveryMetric.RESEARCH_EFFICIENCY
        ],
        research_questions=[
            "What is artificial intelligence?",
            "How does machine learning work?",
            "What are neural networks?"
        ],
        repetitions=2,
        max_time_per_experiment=120,  # 2 minutes
        quality_threshold=0.6
    )
    
    # Run experiment
    scaling_measurement = ScalingLawMeasurement(None)  # Use simulation
    results = scaling_measurement.run_scaling_experiment(quick_experiment)
    
    # Analyze results
    scaling_laws = scaling_measurement.analyze_scaling_laws(results)
    
    print(f"\n📊 Quick Test Results:")
    print(f"   Experiments Run: {len(results)}")
    print(f"   Scaling Laws Found: {len(scaling_laws)}")
    
    for law in scaling_laws:
        print(f"   • {law.discovery_metric.value} ∝ compute^{law.power_law_exponent:.3f}")
    
    return scaling_measurement

def analyze_existing_results(results_file: str):
    """Analyze existing scaling experiment results"""
    
    print(f"📊 Analyzing Existing Results from: {results_file}")
    
    try:
        with open(results_file, 'r') as f:
            data = json.load(f)
        
        # Process and analyze the data
        print("✅ Results loaded successfully")
        # Add analysis logic here
        
    except FileNotFoundError:
        print(f"❌ Results file not found: {results_file}")
    except Exception as e:
        print(f"❌ Error analyzing results: {e}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run scaling law experiments on AI Research Agent")
    parser.add_argument("--mode", choices=["full", "quick", "analyze"], default="quick",
                       help="Experiment mode: full analysis, quick test, or analyze existing results")
    parser.add_argument("--results-file", type=str, help="Results file to analyze (for analyze mode)")
    
    args = parser.parse_args()
    
    if args.mode == "full":
        scaling_measurement, report = run_comprehensive_scaling_analysis()
        print("\n🎉 Comprehensive scaling analysis completed!")
        print("📁 Check 'scaling_laws_analysis_report.json' for detailed results")
        print("📊 Check 'scaling_plots/' directory for visualizations")
        
    elif args.mode == "quick":
        scaling_measurement = run_quick_scaling_test()
        print("\n⚡ Quick scaling test completed!")
        
    elif args.mode == "analyze":
        if not args.results_file:
            print("❌ Please provide --results-file for analyze mode")
        else:
            analyze_existing_results(args.results_file)
    
    print("\n🔬 Scaling law analysis framework ready for scientific discovery research!")