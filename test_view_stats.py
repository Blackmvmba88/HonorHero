"""
Test view_stats.py enhancements
"""

import sys
import os
from datetime import datetime, timedelta

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from session_history import SessionHistory
from view_stats import format_duration, get_tier_for_score, print_weekly_view


def test_format_duration():
    """Test enhanced duration formatting"""
    print("Testing format_duration...")
    
    # Test seconds only
    assert format_duration(45) == "45s"
    
    # Test minutes and seconds
    assert format_duration(125) == "2m 5s"
    
    # Test hours and minutes
    assert format_duration(3665) == "1h 1m"
    assert format_duration(7200) == "2h 0m"
    
    print("  ✓ Duration formatting works correctly")
    print(f"    45s -> {format_duration(45)}")
    print(f"    125s -> {format_duration(125)}")
    print(f"    3665s -> {format_duration(3665)}")
    print()


def test_get_tier_for_score():
    """Test tier calculation"""
    print("Testing get_tier_for_score...")
    
    assert get_tier_for_score(85) == "Íntegro"
    assert get_tier_for_score(70) == "Firme"
    assert get_tier_for_score(50) == "Inestable"
    assert get_tier_for_score(30) == "Fragmentado"
    
    # Boundary tests
    assert get_tier_for_score(80) == "Íntegro"
    assert get_tier_for_score(79) == "Firme"
    assert get_tier_for_score(60) == "Firme"
    assert get_tier_for_score(59) == "Inestable"
    assert get_tier_for_score(40) == "Inestable"
    assert get_tier_for_score(39) == "Fragmentado"
    
    print("  ✓ Tier calculation works correctly")
    print(f"    85 -> {get_tier_for_score(85)}")
    print(f"    70 -> {get_tier_for_score(70)}")
    print(f"    50 -> {get_tier_for_score(50)}")
    print(f"    30 -> {get_tier_for_score(30)}")
    print()


def test_weekly_view_with_mock_data():
    """Test weekly view with mock session data"""
    print("Testing weekly view with mock data...")
    
    # Create temporary history
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name
    
    try:
        history = SessionHistory(storage_path=temp_path)
        
        # Add some mock sessions over the last week
        today = datetime.now()
        
        for i in range(7):
            date = today - timedelta(days=i)
            session_data = {
                'timestamp': date.isoformat(),
                'date': date.strftime('%Y-%m-%d'),
                'time': date.strftime('%H:%M:%S'),
                'final_honor_score': 60 + i * 3,  # Increasing scores
                'tier': 'Firme',
                'components': {
                    'pitch': 65,
                    'timing': 70,
                    'rhythm': 68,
                    'dynamics': 72,
                    'consistency': 75
                },
                'duration': 300,
                'notes': f'Test session {i}'
            }
            history.add_session(session_data)
        
        print("  ✓ Created 7 mock sessions")
        
        # Test that print_weekly_view doesn't crash
        print("  ✓ Testing weekly view rendering...")
        print()
        print_weekly_view(history)
        
        print("  ✓ Weekly view rendered successfully")
        print()
        
    finally:
        # Clean up
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)


def test_stats_with_streak():
    """Test statistics display with streak calculation"""
    print("Testing statistics with streak...")
    
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name
    
    try:
        history = SessionHistory(storage_path=temp_path)
        
        # Add sessions for consecutive days
        today = datetime.now()
        
        for i in range(5):
            date = today - timedelta(days=i)
            session_data = {
                'final_honor_score': 75,
                'tier': 'Firme',
                'components': {},
                'duration': 300
            }
            # Manually set date/time
            session = {
                'timestamp': date.isoformat(),
                'date': date.strftime('%Y-%m-%d'),
                'time': date.strftime('%H:%M:%S'),
                'honor_score': session_data['final_honor_score'],
                'tier': session_data['tier'],
                'components': session_data['components'],
                'duration': session_data['duration'],
                'notes': ''
            }
            history.sessions.append(session)
        
        history._save_sessions()
        
        stats = history.get_statistics()
        
        assert stats['total_sessions'] == 5
        assert stats['current_streak'] >= 3, f"Expected streak >= 3, got {stats['current_streak']}"
        
        print(f"  ✓ Streak calculation: {stats['current_streak']} days")
        print(f"  ✓ Total practice time: {format_duration(stats['total_practice_time'])}")
        print(f"  ✓ Best score: {stats['highest_score']}")
        print()
        
    finally:
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)


def run_all_tests():
    """Run all view_stats tests"""
    print("=" * 70)
    print("🧪  TESTING VIEW_STATS ENHANCEMENTS")
    print("=" * 70)
    print()
    
    tests = [
        test_format_duration,
        test_get_tier_for_score,
        test_weekly_view_with_mock_data,
        test_stats_with_streak,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ {test.__name__} ERROR: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("=" * 70)
    print(f"Tests passed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Tests failed: {failed}/{len(tests)}")
        return False
    else:
        print("✨ All tests passed! ✨")
        return True


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
