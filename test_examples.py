#!/usr/bin/env python3
"""
Tests for HonorHero examples
Validates JSON structure and data integrity
"""

import json
import sys
from pathlib import Path


def test_example_files_exist():
    """Test that all example files exist"""
    print("Testing example files existence...")
    
    expected_files = [
        'examples/example1_juan_beginner.json',
        'examples/example2_daily_tracking_day1.json',
        'examples/example2_daily_tracking_day4.json',
        'examples/example2_daily_tracking_day7.json',
        'examples/example3_shy_vocalist.json',
        'examples/example4_programmatic_use.json',
        'examples/example5_what_honorhero_is_not.json',
        'examples/README.md'
    ]
    
    all_exist = True
    for filepath in expected_files:
        if Path(filepath).exists():
            print(f"  ✓ {filepath}")
        else:
            print(f"  ✗ {filepath} NOT FOUND")
            all_exist = False
    
    assert all_exist, "Some example files are missing"
    print()


def test_json_validity():
    """Test that all JSON files are valid"""
    print("Testing JSON validity...")
    
    json_files = [
        'examples/example1_juan_beginner.json',
        'examples/example2_daily_tracking_day1.json',
        'examples/example2_daily_tracking_day4.json',
        'examples/example2_daily_tracking_day7.json',
        'examples/example3_shy_vocalist.json',
        'examples/example4_programmatic_use.json',
        'examples/example5_what_honorhero_is_not.json'
    ]
    
    all_valid = True
    for filepath in json_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"  ✓ {filepath} - Valid JSON")
        except json.JSONDecodeError as e:
            print(f"  ✗ {filepath} - Invalid JSON: {e}")
            all_valid = False
        except Exception as e:
            print(f"  ✗ {filepath} - Error: {e}")
            all_valid = False
    
    assert all_valid, "Some JSON files are invalid"
    print()


def test_example1_structure():
    """Test Example 1 has required fields"""
    print("Testing Example 1 structure...")
    
    with open('examples/example1_juan_beginner.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Check required top-level fields
    assert 'description' in data, "Missing 'description'"
    assert 'scenario' in data, "Missing 'scenario'"
    assert 'session' in data, "Missing 'session'"
    assert 'console_output' in data, "Missing 'console_output'"
    
    session = data['session']
    
    # Check session fields
    required_session_fields = ['timestamp', 'date', 'time', 'honor_score', 
                               'tier', 'duration', 'components', 'feedback']
    for field in required_session_fields:
        assert field in session, f"Session missing '{field}'"
    
    # Check components
    required_components = ['pitch', 'timing', 'rhythm', 'dynamics', 'consistency']
    for comp in required_components:
        assert comp in session['components'], f"Missing component '{comp}'"
        score = session['components'][comp]
        assert 0 <= score <= 100, f"Component '{comp}' score {score} out of range"
    
    # Verify score is in valid range
    assert 0 <= session['honor_score'] <= 100, "Honor score out of range"
    
    # Verify tier is valid
    valid_tiers = ['Íntegro', 'Firme', 'Inestable', 'Fragmentado']
    assert session['tier'] in valid_tiers, f"Invalid tier '{session['tier']}'"
    
    print(f"  ✓ All required fields present")
    print(f"  ✓ Honor Score: {session['honor_score']} ({session['tier']})")
    print()


def test_example2_progression():
    """Test Example 2 shows valid progression"""
    print("Testing Example 2 progression...")
    
    days = [1, 4, 7]
    scores = []
    
    for day in days:
        with open(f'examples/example2_daily_tracking_day{day}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            score = data['session']['honor_score']
            tier = data['session']['tier']
            scores.append(score)
            print(f"  Day {day}: {score} ({tier})")
    
    # Verify progression (should improve)
    assert scores[0] < scores[1], "Day 4 should be better than Day 1"
    assert scores[1] < scores[2], "Day 7 should be better than Day 4"
    
    improvement = scores[2] - scores[0]
    print(f"  ✓ Total improvement: +{improvement} points")
    print()


def test_example3_vocalist():
    """Test Example 3 shy vocalist data"""
    print("Testing Example 3 (Shy Vocalist)...")
    
    with open('examples/example3_shy_vocalist.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    session = data['session']
    
    assert 'system_behavior' in session, "Missing system_behavior"
    assert 'feedback' in session, "Missing feedback"
    
    # Check score is in Firme range (60-79)
    assert 60 <= session['honor_score'] <= 79, \
        f"Firme tier should be 60-79, got {session['honor_score']}"
    
    print(f"  ✓ Honor Score: {session['honor_score']} (Firme)")
    print(f"  ✓ System behavior documented")
    print()


def test_example4_programmatic():
    """Test Example 4 programmatic use data"""
    print("Testing Example 4 (Programmatic Use)...")
    
    with open('examples/example4_programmatic_use.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    assert 'use_cases' in data, "Missing use_cases"
    assert 'code_example' in data, "Missing code_example"
    assert 'sample_callback_data' in data, "Missing sample_callback_data"
    assert 'integration_scenarios' in data, "Missing integration_scenarios"
    
    # Verify use cases are present
    assert len(data['use_cases']) > 0, "No use cases defined"
    
    # Verify code example has snippet
    assert 'snippet' in data['code_example'], "Missing code snippet"
    assert len(data['code_example']['snippet']) > 0, "Empty code snippet"
    
    print(f"  ✓ {len(data['use_cases'])} use cases defined")
    print(f"  ✓ Code example present")
    print(f"  ✓ {len(data['integration_scenarios'])} integration scenarios")
    print()


def test_example5_philosophy():
    """Test Example 5 philosophy data"""
    print("Testing Example 5 (What HonorHero Is NOT)...")
    
    with open('examples/example5_what_honorhero_is_not.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    assert 'philosophy' in data, "Missing philosophy"
    assert 'what_honorhero_does_not_do' in data, "Missing what_honorhero_does_not_do"
    assert 'honorhero_exists_to' in data, "Missing honorhero_exists_to"
    assert 'comparison_table' in data, "Missing comparison_table"
    
    # Verify at least 3 items in each category
    assert len(data['what_honorhero_does_not_do']) >= 3, \
        "Should have at least 3 'does not' items"
    assert len(data['honorhero_exists_to']) >= 3, \
        "Should have at least 3 'exists to' items"
    
    print(f"  ✓ Philosophy documented")
    print(f"  ✓ {len(data['what_honorhero_does_not_do'])} 'does not' items")
    print(f"  ✓ {len(data['honorhero_exists_to'])} 'exists to' items")
    print()


def test_documentation_files():
    """Test that documentation files exist and are not empty"""
    print("Testing documentation files...")
    
    doc_files = [
        'EXAMPLES.md',
        'examples/README.md',
        'display_examples.py',
        'show_examples.py'
    ]
    
    for filepath in doc_files:
        path = Path(filepath)
        assert path.exists(), f"{filepath} does not exist"
        
        size = path.stat().st_size
        assert size > 0, f"{filepath} is empty"
        
        print(f"  ✓ {filepath} ({size} bytes)")
    
    print()


def run_all_tests():
    """Run all tests"""
    print("=" * 70)
    print("HonorHero Examples Test Suite")
    print("=" * 70)
    print()
    
    tests = [
        test_example_files_exist,
        test_json_validity,
        test_example1_structure,
        test_example2_progression,
        test_example3_vocalist,
        test_example4_programmatic,
        test_example5_philosophy,
        test_documentation_files
    ]
    
    failed = 0
    passed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ FAILED: {e}\n")
            failed += 1
        except Exception as e:
            print(f"  ✗ ERROR: {e}\n")
            failed += 1
    
    print("=" * 70)
    print(f"Tests passed: {passed}/{len(tests)}")
    print(f"Tests failed: {failed}/{len(tests)}")
    print("=" * 70)
    
    if failed > 0:
        sys.exit(1)
    else:
        print("\n✓ All tests passed!")


if __name__ == '__main__':
    run_all_tests()
