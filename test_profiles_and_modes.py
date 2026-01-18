"""
Tests for user profiles and session modes
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from ui import HonorHeroUI


def test_profiles_exist():
    """Test that all profiles are defined"""
    print("Testing profiles existence...")
    
    required_profiles = ['beginner', 'intermediate', 'advanced', 'therapy']
    
    for profile in required_profiles:
        assert profile in config.PROFILES, f"Profile '{profile}' not found"
        
        profile_data = config.PROFILES[profile]
        assert 'name' in profile_data, f"Profile '{profile}' missing 'name'"
        assert 'description' in profile_data, f"Profile '{profile}' missing 'description'"
        assert 'PITCH_TOLERANCE' in profile_data, f"Profile '{profile}' missing 'PITCH_TOLERANCE'"
        assert 'TIMING_TOLERANCE' in profile_data, f"Profile '{profile}' missing 'TIMING_TOLERANCE'"
        assert 'RHYTHM_TOLERANCE' in profile_data, f"Profile '{profile}' missing 'RHYTHM_TOLERANCE'"
        assert 'DYNAMICS_TOLERANCE' in profile_data, f"Profile '{profile}' missing 'DYNAMICS_TOLERANCE'"
        assert 'CONSISTENCY_THRESHOLD' in profile_data, f"Profile '{profile}' missing 'CONSISTENCY_THRESHOLD'"
        
        print(f"  ✓ Profile '{profile}': {profile_data['name']}")
    
    print(f"  ✓ All {len(required_profiles)} profiles defined correctly")
    print()


def test_profile_tolerance_progression():
    """Test that profiles have appropriate tolerance progression"""
    print("Testing profile tolerance progression...")
    
    # Beginner should be most tolerant, advanced should be strictest
    assert config.PROFILES['beginner']['PITCH_TOLERANCE'] > config.PROFILES['advanced']['PITCH_TOLERANCE']
    assert config.PROFILES['beginner']['TIMING_TOLERANCE'] > config.PROFILES['advanced']['TIMING_TOLERANCE']
    assert config.PROFILES['beginner']['RHYTHM_TOLERANCE'] > config.PROFILES['advanced']['RHYTHM_TOLERANCE']
    
    # Therapy should be most tolerant
    assert config.PROFILES['therapy']['PITCH_TOLERANCE'] >= config.PROFILES['beginner']['PITCH_TOLERANCE']
    assert config.PROFILES['therapy']['TIMING_TOLERANCE'] >= config.PROFILES['beginner']['TIMING_TOLERANCE']
    
    print("  ✓ Beginner more tolerant than advanced")
    print("  ✓ Therapy most tolerant")
    print()


def test_session_modes_exist():
    """Test that all session modes are defined"""
    print("Testing session modes existence...")
    
    required_modes = ['short', 'focus', 'free']
    
    for mode in required_modes:
        assert mode in config.SESSION_MODES, f"Mode '{mode}' not found"
        
        mode_data = config.SESSION_MODES[mode]
        assert 'name' in mode_data, f"Mode '{mode}' missing 'name'"
        assert 'description' in mode_data, f"Mode '{mode}' missing 'description'"
        assert 'duration' in mode_data, f"Mode '{mode}' missing 'duration'"
        
        print(f"  ✓ Mode '{mode}': {mode_data['name']} - {mode_data['duration'] or 'unlimited'}s")
    
    print(f"  ✓ All {len(required_modes)} modes defined correctly")
    print()


def test_session_mode_durations():
    """Test that session mode durations are correct"""
    print("Testing session mode durations...")
    
    assert config.SESSION_MODES['short']['duration'] == 180, "Short mode should be 180 seconds (3 min)"
    assert config.SESSION_MODES['focus']['duration'] == 600, "Focus mode should be 600 seconds (10 min)"
    assert config.SESSION_MODES['free']['duration'] is None, "Free mode should have no duration limit"
    
    print("  ✓ Short mode: 3 minutes (180s)")
    print("  ✓ Focus mode: 10 minutes (600s)")
    print("  ✓ Free mode: unlimited")
    print()


def test_ui_initialization_with_profile():
    """Test that UI can be initialized with different profiles"""
    print("Testing UI initialization with profiles...")
    
    for profile_name in ['beginner', 'intermediate', 'advanced', 'therapy']:
        try:
            ui = HonorHeroUI(profile=profile_name, mode='free')
            assert ui.profile_name == profile_name
            assert ui.profile == config.PROFILES[profile_name]
            
            # Check that config was updated
            assert config.PITCH_TOLERANCE == config.PROFILES[profile_name]['PITCH_TOLERANCE']
            
            print(f"  ✓ UI initialized with profile '{profile_name}'")
        except Exception as e:
            raise AssertionError(f"Failed to initialize UI with profile '{profile_name}': {e}")
    
    print()


def test_ui_initialization_with_mode():
    """Test that UI can be initialized with different modes"""
    print("Testing UI initialization with modes...")
    
    for mode_name in ['short', 'focus', 'free']:
        try:
            ui = HonorHeroUI(profile='intermediate', mode=mode_name)
            assert ui.mode_name == mode_name
            assert ui.mode == config.SESSION_MODES[mode_name]
            
            print(f"  ✓ UI initialized with mode '{mode_name}'")
        except Exception as e:
            raise AssertionError(f"Failed to initialize UI with mode '{mode_name}': {e}")
    
    print()


def test_default_profile_and_mode():
    """Test that default profile and mode work"""
    print("Testing default profile and mode...")
    
    # Test default initialization
    ui = HonorHeroUI()
    
    assert ui.profile_name == config.DEFAULT_PROFILE
    assert ui.mode_name == config.DEFAULT_MODE
    
    print(f"  ✓ Default profile: {config.DEFAULT_PROFILE}")
    print(f"  ✓ Default mode: {config.DEFAULT_MODE}")
    print()


def test_invalid_profile_fallback():
    """Test that invalid profile falls back to default"""
    print("Testing invalid profile fallback...")
    
    ui = HonorHeroUI(profile='nonexistent', mode='free')
    
    assert ui.profile_name == config.DEFAULT_PROFILE
    print(f"  ✓ Invalid profile falls back to {config.DEFAULT_PROFILE}")
    print()


def test_invalid_mode_fallback():
    """Test that invalid mode falls back to default"""
    print("Testing invalid mode fallback...")
    
    ui = HonorHeroUI(profile='intermediate', mode='nonexistent')
    
    assert ui.mode_name == config.DEFAULT_MODE
    print(f"  ✓ Invalid mode falls back to {config.DEFAULT_MODE}")
    print()


def run_all_tests():
    """Run all tests"""
    print("=" * 70)
    print("🧪  TESTING PROFILES AND MODES")
    print("=" * 70)
    print()
    
    tests = [
        test_profiles_exist,
        test_profile_tolerance_progression,
        test_session_modes_exist,
        test_session_mode_durations,
        test_ui_initialization_with_profile,
        test_ui_initialization_with_mode,
        test_default_profile_and_mode,
        test_invalid_profile_fallback,
        test_invalid_mode_fallback,
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
