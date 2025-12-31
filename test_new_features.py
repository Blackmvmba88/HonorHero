"""
Test script for new HonorHero features
Tests session history and feedback generation without audio dependencies
"""

from session_history import SessionHistory
from feedback_generator import FeedbackGenerator
import tempfile
import os


def test_session_history():
    """Test session history functionality"""
    print("Testing Session History...")
    print("-" * 50)
    
    # Create temporary storage
    temp_file = tempfile.mktemp(suffix='.json')
    
    try:
        history = SessionHistory(temp_file)
        
        # Add multiple sessions
        sessions_data = [
            {'final_honor_score': 42, 'tier': 'Fragmentado', 
             'components': {'pitch': 50, 'timing': 40, 'rhythm': 38, 'dynamics': 45, 'consistency': 42},
             'duration': 300},
            {'final_honor_score': 58, 'tier': 'Inestable',
             'components': {'pitch': 60, 'timing': 55, 'rhythm': 52, 'dynamics': 60, 'consistency': 58},
             'duration': 300},
            {'final_honor_score': 72, 'tier': 'Firme',
             'components': {'pitch': 75, 'timing': 70, 'rhythm': 68, 'dynamics': 72, 'consistency': 75},
             'duration': 300},
        ]
        
        for session in sessions_data:
            history.add_session(session)
        
        # Get statistics
        stats = history.get_statistics()
        print(f"✓ Total sessions: {stats['total_sessions']}")
        print(f"✓ Average score: {stats['average_score']:.1f}")
        print(f"✓ Score range: {stats['lowest_score']:.1f} - {stats['highest_score']:.1f}")
        
        # Test comparison
        comparison = history.compare_with_previous(75, {
            'pitch': 78, 'timing': 72, 'rhythm': 70, 'dynamics': 75, 'consistency': 73
        })
        print(f"✓ Comparison message: {comparison['message']}")
        
        # Test evolution data
        evolution = history.get_evolution_data()
        print(f"✓ Evolution data points: {len(evolution)}")
        
        print("✅ Session History: PASSED\n")
        
    finally:
        # Cleanup
        if os.path.exists(temp_file):
            os.remove(temp_file)


def test_feedback_generator():
    """Test feedback generator functionality"""
    print("Testing Feedback Generator...")
    print("-" * 50)
    
    generator = FeedbackGenerator()
    
    # Test real-time feedback
    current_metrics = {
        'honor_score': 65,
        'tier': 'Firme',
        'components': {
            'pitch': 70,
            'timing': 60,
            'rhythm': 65,
            'dynamics': 68,
            'consistency': 62
        }
    }
    
    feedback = generator.generate_realtime_feedback(current_metrics)
    print(f"✓ Real-time feedback: '{feedback}'")
    assert feedback, "Should generate feedback"
    
    # Test with previous metrics
    previous_metrics = {
        'components': {
            'pitch': 65,
            'timing': 55,
            'rhythm': 60,
            'dynamics': 70,
            'consistency': 60
        }
    }
    
    feedback_with_comparison = generator.generate_realtime_feedback(
        current_metrics, previous_metrics
    )
    print(f"✓ Comparative feedback: '{feedback_with_comparison}'")
    
    # Test component-specific feedback
    component_feedback = generator.generate_component_feedback('pitch', 85, 70)
    print(f"✓ Component feedback: '{component_feedback}'")
    assert 'pitch' in component_feedback or 'afinación' in component_feedback
    
    # Test session summary
    results = {
        'final_honor_score': 82,
        'tier': 'Íntegro',
        'components': current_metrics['components']
    }
    
    comparison = {
        'has_history': True,
        'score_difference': 10,
        'improved_components': ['pitch', 'timing'],
        'declined_components': []
    }
    
    summary = generator.generate_session_summary(results, comparison)
    print(f"✓ Session summary: '{summary}'")
    assert summary, "Should generate summary"
    
    # Test achievement messages
    achievement = generator.generate_achievement_message('first_integro')
    print(f"✓ Achievement message: '{achievement}'")
    assert '🎉' in achievement or 'Íntegro' in achievement
    
    print("✅ Feedback Generator: PASSED\n")


def test_tier_messages():
    """Test feedback for different tiers"""
    print("Testing Tier-Specific Messages...")
    print("-" * 50)
    
    generator = FeedbackGenerator()
    
    tiers = [
        ('Íntegro', 85),
        ('Firme', 70),
        ('Inestable', 50),
        ('Fragmentado', 35)
    ]
    
    for tier, score in tiers:
        metrics = {
            'honor_score': score,
            'tier': tier,
            'components': {
                'pitch': score,
                'timing': score,
                'rhythm': score,
                'dynamics': score,
                'consistency': score
            }
        }
        
        feedback = generator.generate_realtime_feedback(metrics)
        print(f"✓ {tier:12} ({score:2}): {feedback}")
    
    print("✅ Tier Messages: PASSED\n")


def run_all_tests():
    """Run all feature tests"""
    print("=" * 60)
    print("HonorHero New Features Test Suite")
    print("=" * 60)
    print()
    
    try:
        test_session_history()
        test_feedback_generator()
        test_tier_messages()
        
        print("=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        return True
        
    except Exception as e:
        print("=" * 60)
        print(f"❌ TEST FAILED: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
