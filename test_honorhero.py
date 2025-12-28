"""
Unit tests for HonorHero modules
"""

import numpy as np
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pitch_analyzer import PitchAnalyzer
from timing_analyzer import TimingAnalyzer
from dynamics_analyzer import DynamicsAnalyzer
from consistency_analyzer import ConsistencyAnalyzer
from scoring_system import ScoringSystem


def test_pitch_analyzer():
    """Test pitch analyzer with synthetic audio"""
    print("Testing PitchAnalyzer...")
    
    analyzer = PitchAnalyzer()
    
    # Generate A4 (440 Hz) tone
    sample_rate = 22050
    duration = 0.5
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency = 440  # A4
    audio = 0.5 * np.sin(2 * np.pi * frequency * t)
    
    result = analyzer.analyze(audio, sample_rate)
    
    assert result['detected'] == True, "Should detect pitch"
    assert 430 < result['frequency'] < 450, f"Frequency should be ~440 Hz, got {result['frequency']}"
    assert result['score'] > 0, "Score should be positive"
    
    print(f"  ✓ Detected frequency: {result['frequency']:.1f} Hz")
    print(f"  ✓ Note: {result['note']}")
    print(f"  ✓ Score: {result['score']:.1f}")
    print()


def test_timing_analyzer():
    """Test timing analyzer"""
    print("Testing TimingAnalyzer...")
    
    analyzer = TimingAnalyzer()
    
    # Simulate onsets at regular intervals
    sample_rate = 22050
    for i in range(5):
        timestamp = i * 0.5  # Every 0.5 seconds
        audio = np.random.randn(2048) * 0.1  # Noise
        result = analyzer.detect_onset(audio, sample_rate, timestamp)
    
    timing_result = analyzer.analyze_timing()
    rhythm_result = analyzer.analyze_rhythm()
    
    assert timing_result['score'] >= 0, "Timing score should be valid"
    assert rhythm_result['score'] >= 0, "Rhythm score should be valid"
    
    print(f"  ✓ Timing score: {timing_result['score']:.1f}")
    print(f"  ✓ Rhythm score: {rhythm_result['score']:.1f}")
    print()


def test_dynamics_analyzer():
    """Test dynamics analyzer"""
    print("Testing DynamicsAnalyzer...")
    
    analyzer = DynamicsAnalyzer()
    
    # Test with varying amplitudes
    for amplitude in [0.1, 0.3, 0.5, 0.7]:
        audio = np.random.randn(2048) * amplitude
        result = analyzer.analyze(audio)
        assert result['score'] >= 0, "Dynamics score should be valid"
    
    avg_score = analyzer.get_average_score()
    assert 0 <= avg_score <= 100, "Average score should be in valid range"
    
    print(f"  ✓ Average dynamics score: {avg_score:.1f}")
    print()


def test_consistency_analyzer():
    """Test consistency analyzer"""
    print("Testing ConsistencyAnalyzer...")
    
    analyzer = ConsistencyAnalyzer()
    
    # Add consistent metrics
    for _ in range(5):
        analyzer.add_metrics(80, 75, 70, 85)
    
    result = analyzer.analyze()
    
    assert result['score'] >= 0, "Consistency score should be valid"
    assert 'overall_consistency' in result, "Should have overall consistency"
    
    print(f"  ✓ Consistency score: {result['score']:.1f}")
    print(f"  ✓ Overall consistency: {result['overall_consistency']:.2f}")
    print()


def test_scoring_system():
    """Test scoring system"""
    print("Testing ScoringSystem...")
    
    scorer = ScoringSystem()
    
    # Test with good metrics
    metrics = {
        'pitch': 85,
        'timing': 80,
        'rhythm': 75,
        'dynamics': 90,
        'consistency': 88
    }
    
    result = scorer.calculate_honor_score(metrics)
    
    assert 0 <= result['honor_score'] <= 100, "Honor score should be in valid range"
    assert result['tier'] in ['Íntegro', 'Firme', 'Inestable', 'Fragmentado'], "Should have valid tier"
    assert 'message' in result, "Should have message"
    
    print(f"  ✓ Honor Score: {result['honor_score']:.1f}")
    print(f"  ✓ Tier: {result['tier']}")
    print(f"  ✓ Message: {result['message']}")
    print()
    
    # Test tier boundaries
    test_cases = [
        ({'pitch': 90, 'timing': 90, 'rhythm': 90, 'dynamics': 90, 'consistency': 90}, 'Íntegro'),
        ({'pitch': 70, 'timing': 70, 'rhythm': 70, 'dynamics': 70, 'consistency': 70}, 'Firme'),
        ({'pitch': 50, 'timing': 50, 'rhythm': 50, 'dynamics': 50, 'consistency': 50}, 'Inestable'),
        ({'pitch': 30, 'timing': 30, 'rhythm': 30, 'dynamics': 30, 'consistency': 30}, 'Fragmentado'),
    ]
    
    for metrics, expected_tier in test_cases:
        result = scorer.calculate_honor_score(metrics)
        assert result['tier'] == expected_tier, f"Expected {expected_tier}, got {result['tier']}"
        print(f"  ✓ Tier test passed: Score {result['honor_score']:.1f} = {result['tier']}")
    
    print()


def test_integration():
    """Test module integration"""
    print("Testing Integration...")
    
    # Create all analyzers
    pitch = PitchAnalyzer()
    timing = TimingAnalyzer()
    dynamics = DynamicsAnalyzer()
    consistency = ConsistencyAnalyzer()
    scorer = ScoringSystem()
    
    # Simulate a short performance
    sample_rate = 22050
    duration = 0.1
    
    for i in range(10):
        # Generate test audio
        t = np.linspace(0, duration, int(sample_rate * duration))
        audio = 0.5 * np.sin(2 * np.pi * 440 * t) + np.random.randn(len(t)) * 0.05
        
        # Analyze
        pitch_result = pitch.analyze(audio, sample_rate)
        timing.detect_onset(audio, sample_rate, i * duration)
        dynamics.analyze(audio)
    
    # Get scores
    pitch_score = pitch.get_average_score()
    timing_score = timing.analyze_timing()['score']
    rhythm_score = timing.analyze_rhythm()['score']
    dynamics_score = dynamics.get_average_score()
    
    consistency.add_metrics(pitch_score, timing_score, rhythm_score, dynamics_score)
    consistency_result = consistency.analyze()
    
    # Calculate honor score
    metrics = {
        'pitch': pitch_score,
        'timing': timing_score,
        'rhythm': rhythm_score,
        'dynamics': dynamics_score,
        'consistency': consistency_result['score']
    }
    
    honor_result = scorer.calculate_honor_score(metrics)
    
    assert 0 <= honor_result['honor_score'] <= 100, "Honor score should be valid"
    
    print(f"  ✓ Integration test passed")
    print(f"  ✓ Final Honor Score: {honor_result['honor_score']:.1f}")
    print(f"  ✓ Tier: {honor_result['tier']}")
    print()


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("HonorHero Unit Tests")
    print("=" * 60)
    print()
    
    try:
        test_pitch_analyzer()
        test_timing_analyzer()
        test_dynamics_analyzer()
        test_consistency_analyzer()
        test_scoring_system()
        test_integration()
        
        print("=" * 60)
        print("✅ All tests passed!")
        print("=" * 60)
        return True
        
    except Exception as e:
        print("=" * 60)
        print(f"❌ Test failed: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
