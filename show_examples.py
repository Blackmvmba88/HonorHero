#!/usr/bin/env python3
"""
Quick viewer for HonorHero examples
Non-interactive version for automated display
"""

import json
from pathlib import Path


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(text.center(70))
    print("=" * 70 + "\n")


def show_all_examples():
    """Display all examples in sequence"""
    
    print_header("🎵 HonorHero Examples Showcase")
    
    # Example 1: Juan's Beginner Session
    print("\n" + "─" * 70)
    print("EXAMPLE 1: Juan's Beginner Guitar Session")
    print("─" * 70)
    with open('examples/example1_juan_beginner.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    session = data['session']
    print(f"\nScenario: {data['scenario']}")
    print(f"\nHonor Score: {session['honor_score']}")
    print(f"Tier: {session['tier']}")
    print(f"\nKey Insight: {session['encouragement']}")
    
    # Example 2: Daily Tracking
    print("\n" + "─" * 70)
    print("EXAMPLE 2: Daily Practice Tracking")
    print("─" * 70)
    print("\nJuan's Weekly Progress:\n")
    for day in [1, 4, 7]:
        with open(f'examples/example2_daily_tracking_day{day}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            s = data['session']
            print(f"Day {day}: {s['honor_score']} ({s['tier']})")
            print(f"  {s['notes']}\n")
    
    # Example 3: Shy Vocalist
    print("─" * 70)
    print("EXAMPLE 3: Shy Vocalist")
    print("─" * 70)
    with open('examples/example3_shy_vocalist.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    session = data['session']
    print(f"\nScenario: {data['scenario']}")
    print(f"\nHonor Score: {session['honor_score']}")
    print(f"Tier: {session['tier']}")
    print(f"\nFeedback Highlights:")
    for highlight in session['feedback']['highlights']:
        print(f"  • {highlight}")
    
    # Example 4: Programmatic Use
    print("\n" + "─" * 70)
    print("EXAMPLE 4: Programmatic Use for Developers")
    print("─" * 70)
    with open('examples/example4_programmatic_use.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\nScenario: {data['scenario']}")
    print("\nUse Cases:")
    for use_case in data['use_cases']:
        print(f"  • {use_case}")
    
    # Example 5: What HonorHero Is NOT
    print("\n" + "─" * 70)
    print("EXAMPLE 5: What HonorHero Is NOT")
    print("─" * 70)
    with open('examples/example5_what_honorhero_is_not.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\nPhilosophy: {data['philosophy']}")
    print("\nHonorHero does NOT:")
    for key, item in list(data['what_honorhero_does_not_do'].items())[:3]:
        print(f"  ❌ {item['description']}")
    print("\nHonorHero EXISTS TO:")
    for purpose in data['honorhero_exists_to'][:3]:
        print(f"  ✨ {purpose}")
    
    print("\n" + "=" * 70)
    print("For full details, see EXAMPLES.md or run: python display_examples.py")
    print("=" * 70 + "\n")


if __name__ == '__main__':
    # Check if we're in the right directory
    if not Path('examples').exists():
        print("Error: 'examples' directory not found.")
        print("Please run this script from the HonorHero root directory.")
        exit(1)
    
    show_all_examples()
