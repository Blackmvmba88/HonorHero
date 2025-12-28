"""
HonorHero Demo Script
Demonstrates the system without requiring audio input
"""

import numpy as np
import time
import sys

from pitch_analyzer import PitchAnalyzer
from timing_analyzer import TimingAnalyzer
from dynamics_analyzer import DynamicsAnalyzer
from consistency_analyzer import ConsistencyAnalyzer
from scoring_system import ScoringSystem


def simulate_performance(duration_seconds=10):
    """
    Simulate a musical performance without real audio input
    
    Args:
        duration_seconds: Duration of simulated performance
    """
    print("=" * 70)
    print("🎵  HonorHero Demo - Simulated Performance  🎵".center(70))
    print("=" * 70)
    print()
    print("This demo simulates a musical performance without requiring")
    print("actual audio input. It demonstrates the HonorHero system.")
    print()
    print("-" * 70)
    print()
    
    # Initialize analyzers
    pitch = PitchAnalyzer()
    timing = TimingAnalyzer()
    dynamics = DynamicsAnalyzer()
    consistency = ConsistencyAnalyzer()
    scorer = ScoringSystem()
    
    sample_rate = 22050
    chunk_duration = 0.1  # 100ms chunks
    chunks_per_second = int(1.0 / chunk_duration)
    total_chunks = int(duration_seconds * chunks_per_second)
    
    print(f"Simulating {duration_seconds} second performance...")
    print()
    
    # Simulate performance with varying quality
    for chunk_idx in range(total_chunks):
        current_time = chunk_idx * chunk_duration
        
        # Generate synthetic audio with some variation
        # Simulating a melody with occasional pitch drift
        base_frequency = 440  # A4
        pitch_variation = np.sin(current_time * 0.5) * 20  # Slight pitch variation
        frequency = base_frequency + pitch_variation
        
        t = np.linspace(0, chunk_duration, int(sample_rate * chunk_duration))
        audio = 0.5 * np.sin(2 * np.pi * frequency * t)
        
        # Add some noise (simulating non-perfect performance)
        noise_level = 0.05 + 0.02 * np.sin(current_time * 0.3)
        audio += np.random.randn(len(t)) * noise_level
        
        # Vary amplitude (simulating dynamics)
        amplitude_variation = 0.7 + 0.3 * np.sin(current_time * 0.7)
        audio *= amplitude_variation
        
        # Analyze
        pitch.analyze(audio, sample_rate)
        timing.detect_onset(audio, sample_rate, current_time)
        dynamics.analyze(audio)
        
        # Update every second
        if chunk_idx > 0 and chunk_idx % chunks_per_second == 0:
            # Calculate scores
            pitch_score = pitch.get_average_score()
            timing_result = timing.analyze_timing()
            rhythm_result = timing.analyze_rhythm()
            dynamics_score = dynamics.get_average_score()
            
            consistency.add_metrics(
                pitch_score,
                timing_result['score'],
                rhythm_result['score'],
                dynamics_score
            )
            consistency_result = consistency.analyze()
            
            # Calculate honor score
            metrics = {
                'pitch': pitch_score,
                'timing': timing_result['score'],
                'rhythm': rhythm_result['score'],
                'dynamics': dynamics_score,
                'consistency': consistency_result['score']
            }
            
            honor_result = scorer.calculate_honor_score(metrics)
            
            # Display progress
            progress = int((chunk_idx / total_chunks) * 100)
            bar_length = 40
            filled = int((progress / 100) * bar_length)
            bar = '█' * filled + '░' * (bar_length - filled)
            
            print(f"[{bar}] {progress}%")
            print(f"  Honor Score: {honor_result['honor_score']:.1f} - {honor_result['tier']}")
            print()
    
    # Final results
    print()
    print("=" * 70)
    print("🏆  Final Results  🏆".center(70))
    print("=" * 70)
    print()
    
    # Calculate final scores
    pitch_score = pitch.get_average_score()
    timing_result = timing.analyze_timing()
    rhythm_result = timing.analyze_rhythm()
    dynamics_score = dynamics.get_average_score()
    consistency.add_metrics(
        pitch_score,
        timing_result['score'],
        rhythm_result['score'],
        dynamics_score
    )
    consistency_result = consistency.analyze()
    
    metrics = {
        'pitch': pitch_score,
        'timing': timing_result['score'],
        'rhythm': rhythm_result['score'],
        'dynamics': dynamics_score,
        'consistency': consistency_result['score']
    }
    
    honor_result = scorer.calculate_honor_score(metrics)
    progress_summary = scorer.get_progress_summary()
    
    # Display results
    score = honor_result['honor_score']
    tier = honor_result['tier']
    
    print(f"╔{'═' * 68}╗")
    print(f"║{'  HONOR SCORE':^68}║")
    print(f"║{f'{score:.1f}':^68}║")
    print(f"║{tier:^68}║")
    print(f"╚{'═' * 68}╝")
    print()
    
    print(f"💬 {honor_result['message']}")
    print()
    
    print("Component Scores:")
    for name, value in metrics.items():
        print(f"  • {name.capitalize()}: {value:.1f}/100")
    
    print()
    print("Progress Summary:")
    print(f"  • Total Evaluations: {progress_summary['total_evaluations']}")
    print(f"  • Average Score: {progress_summary['average_score']:.1f}")
    print(f"  • Trend: {progress_summary['trend']}")
    print()
    
    print("=" * 70)
    print("✨ Demo completed successfully! ✨".center(70))
    print("=" * 70)
    print()


def main():
    """Main demo entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='HonorHero Demo')
    parser.add_argument(
        '--duration',
        type=int,
        default=10,
        help='Duration of simulated performance in seconds (default: 10)'
    )
    
    args = parser.parse_args()
    
    try:
        simulate_performance(args.duration)
    except KeyboardInterrupt:
        print("\n\nDemo interrupted.")
        sys.exit(0)


if __name__ == '__main__':
    main()
