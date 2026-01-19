"""
Unit tests for Piano Roll UI
"""

import numpy as np
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from piano_roll_ui import PianoRollUI
import librosa  # Used for note-to-MIDI conversion in tests


def test_piano_roll_initialization():
    """Test piano roll UI initialization"""
    print("Testing PianoRollUI initialization...")
    
    ui = PianoRollUI(profile='beginner', mode='short', window_seconds=3)
    
    assert ui.profile_name == 'beginner', "Profile should be set to beginner"
    assert ui.mode_name == 'short', "Mode should be set to short"
    assert ui.window_seconds == 3, "Window should be 3 seconds"
    assert len(ui.note_buffer) == 0, "Note buffer should be empty initially"
    
    print("  ✓ Piano roll UI initialized correctly")
    print()


def test_note_row_conversion():
    """Test note name to row conversion"""
    print("Testing note row conversion...")
    
    ui = PianoRollUI()
    
    # Test valid notes
    row_c4 = ui.get_note_row('C4')
    assert row_c4 >= 0, "C4 should have valid row"
    
    row_c5 = ui.get_note_row('C5')
    assert row_c5 >= 0, "C5 should have valid row"
    assert row_c5 < row_c4, "C5 should be above C4 (smaller row number)"
    
    # Test out of range notes
    row_out = ui.get_note_row('C1')
    assert row_out == -1, "C1 should be out of range"
    
    print(f"  ✓ C4 row: {row_c4}")
    print(f"  ✓ C5 row: {row_c5}")
    print(f"  ✓ Out of range handling works")
    print()


def test_color_selection():
    """Test color selection based on score"""
    print("Testing color selection...")
    
    ui = PianoRollUI()
    
    # Test different score ranges
    color_high = ui.get_color_for_score(85)
    assert color_high == '\033[92m', "High score should be green"
    
    color_mid = ui.get_color_for_score(65)
    assert color_mid == '\033[94m', "Mid score should be blue"
    
    color_low = ui.get_color_for_score(45)
    assert color_low == '\033[93m', "Low score should be yellow"
    
    color_very_low = ui.get_color_for_score(25)
    assert color_very_low == '\033[91m', "Very low score should be red"
    
    print("  ✓ Color selection works for all score ranges")
    print()


def test_velocity_character():
    """Test velocity character selection"""
    print("Testing velocity character selection...")
    
    ui = PianoRollUI()
    
    char_strong = ui.get_velocity_char(0.9)
    assert char_strong == '█', "Strong velocity should use solid block"
    
    char_medium = ui.get_velocity_char(0.7)
    assert char_medium == '▓', "Medium velocity should use medium shade"
    
    char_soft = ui.get_velocity_char(0.5)
    assert char_soft == '▒', "Soft velocity should use light shade"
    
    char_very_soft = ui.get_velocity_char(0.2)
    assert char_very_soft == '░', "Very soft velocity should use very light shade"
    
    print("  ✓ Velocity characters assigned correctly")
    print()


def test_note_buffer():
    """Test note buffer functionality"""
    print("Testing note buffer...")
    
    ui = PianoRollUI()
    
    # Simulate adding notes
    import time
    current_time = time.time()
    
    for i in range(5):
        ui.note_buffer.append({
            'timestamp': current_time + i * 0.5,
            'note': f'C{4 + (i % 2)}',
            'frequency': 440 + i * 10,
            'score': 80 + i,
            'velocity': 0.5 + i * 0.1
        })
    
    assert len(ui.note_buffer) == 5, "Should have 5 notes in buffer"
    
    # Test that buffer has correct structure
    first_note = ui.note_buffer[0]
    assert 'timestamp' in first_note, "Note should have timestamp"
    assert 'note' in first_note, "Note should have note name"
    assert 'frequency' in first_note, "Note should have frequency"
    assert 'score' in first_note, "Note should have score"
    assert 'velocity' in first_note, "Note should have velocity"
    
    print(f"  ✓ Note buffer contains {len(ui.note_buffer)} notes")
    print("  ✓ Note structure is correct")
    print()


def test_trend_calculation():
    """Test trend indicator calculation"""
    print("Testing trend calculation...")
    
    ui = PianoRollUI()
    
    # Not enough data
    trend = ui.draw_trend_indicator()
    assert "Gathering data" in trend, "Should indicate gathering data with few points"
    
    # Add improving scores
    for score in [50, 55, 60, 65, 70]:
        ui.recent_scores.append(score)
    
    trend = ui.draw_trend_indicator()
    assert "↗" in trend or "Mejorando" in trend, "Should indicate improving trend"
    
    # Add declining scores
    ui.recent_scores.clear()
    for score in [70, 65, 60, 55, 50]:
        ui.recent_scores.append(score)
    
    trend = ui.draw_trend_indicator()
    assert "↘" in trend or "Bajando" in trend, "Should indicate declining trend"
    
    print("  ✓ Trend calculation works")
    print("  ✓ Improving trend detected")
    print("  ✓ Declining trend detected")
    print()


def test_piano_roll_drawing():
    """Test piano roll drawing function"""
    print("Testing piano roll drawing...")
    
    ui = PianoRollUI()
    
    # Add some notes
    import time
    current_time = time.time()
    
    for i in range(10):
        ui.note_buffer.append({
            'timestamp': current_time - 2 + i * 0.3,
            'note': f'C{4}',
            'frequency': 261.63,
            'score': 75,
            'velocity': 0.6
        })
        ui.recent_scores.append(75)
    
    # Draw the piano roll
    lines = ui.draw_piano_roll(current_time)
    
    assert len(lines) > 0, "Should generate piano roll lines"
    assert len(lines) == ui.total_rows, f"Should have {ui.total_rows} rows"
    
    # Check that lines contain note labels
    has_note_labels = any('C' in line or 'D' in line or 'E' in line for line in lines)
    assert has_note_labels, "Piano roll should contain note labels"
    
    print(f"  ✓ Piano roll generated with {len(lines)} rows")
    print("  ✓ Note labels present")
    print()


def run_all_tests():
    """Run all tests"""
    print("=" * 70)
    print("Piano Roll UI Unit Tests")
    print("=" * 70)
    print()
    
    try:
        test_piano_roll_initialization()
        test_note_row_conversion()
        test_color_selection()
        test_velocity_character()
        test_note_buffer()
        test_trend_calculation()
        test_piano_roll_drawing()
        
        print("=" * 70)
        print("✅ All tests passed!")
        print("=" * 70)
        return True
        
    except Exception as e:
        print("=" * 70)
        print(f"❌ Test failed: {e}")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
