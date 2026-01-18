#!/usr/bin/env python3
"""
Visual demonstration of different profiles and their tolerances
"""

import config

def show_profile_comparison():
    """Show a comparison table of all profiles"""
    
    print("=" * 100)
    print("PROFILE COMPARISON TABLE".center(100))
    print("=" * 100)
    print()
    
    # Header
    headers = ["Profile", "Pitch±", "Timing±", "Rhythm±", "Dynamics±", "Consistency%"]
    col_widths = [25, 12, 12, 12, 12, 15]
    
    header_line = "│"
    for i, header in enumerate(headers):
        header_line += f" {header.ljust(col_widths[i])} │"
    
    print("┌" + "─" * 98 + "┐")
    print(header_line)
    print("├" + "─" * 98 + "┤")
    
    # Rows
    profiles_order = ['therapy', 'beginner', 'intermediate', 'advanced']
    
    for profile_key in profiles_order:
        profile = config.PROFILES[profile_key]
        
        row = f"│ {profile['name'].ljust(col_widths[0])} │"
        row += f" {str(profile['PITCH_TOLERANCE']) + ' cents'.ljust(col_widths[1])} │"
        row += f" {(str(profile['TIMING_TOLERANCE']) + 's').ljust(col_widths[2])} │"
        row += f" {(str(int(profile['RHYTHM_TOLERANCE'] * 100)) + '%').ljust(col_widths[3])} │"
        row += f" {(str(profile['DYNAMICS_TOLERANCE']) + ' dB').ljust(col_widths[4])} │"
        row += f" {(str(int(profile['CONSISTENCY_THRESHOLD'] * 100)) + '%').ljust(col_widths[5])} │"
        
        print(row)
    
    print("└" + "─" * 98 + "┘")
    print()
    
    print("Legend:")
    print("  • Pitch±     : Pitch tolerance in cents (100 cents = 1 semitone)")
    print("  • Timing±    : Timing tolerance in seconds")
    print("  • Rhythm±    : Rhythm variance tolerance as percentage")
    print("  • Dynamics±  : Dynamic range tolerance in decibels")
    print("  • Consistency: Minimum consistency threshold as percentage")
    print()
    print("Higher values = More tolerant | Lower values = More strict")
    print()


def show_mode_comparison():
    """Show a comparison of session modes"""
    
    print("=" * 80)
    print("SESSION MODE COMPARISON".center(80))
    print("=" * 80)
    print()
    
    for mode_key in ['short', 'focus', 'free']:
        mode = config.SESSION_MODES[mode_key]
        
        duration_str = f"{mode['duration'] // 60} minutes" if mode['duration'] else "Unlimited"
        
        print(f"┌─ {mode['name'].upper()} " + "─" * (75 - len(mode['name'])) + "┐")
        print(f"│ Duration:    {duration_str.ljust(64)} │")
        print(f"│ Description: {mode['description'].ljust(64)} │")
        
        if mode_key == 'short':
            print(f"│ Best for:    Quick warmups, busy schedules{' ' * 26} │")
        elif mode_key == 'focus':
            print(f"│ Best for:    Daily practice, skill development{' ' * 21} │")
        else:
            print(f"│ Best for:    Exploratory practice, jam sessions{' ' * 19} │")
        
        print("└" + "─" * 78 + "┘")
        print()


def show_use_case_examples():
    """Show practical use case examples"""
    
    print("=" * 80)
    print("USE CASE EXAMPLES".center(80))
    print("=" * 80)
    print()
    
    examples = [
        {
            'scenario': 'Absolute Beginner - First Day',
            'profile': 'beginner',
            'mode': 'short',
            'command': 'python ui.py --profile beginner --mode short',
            'why': 'Low pressure, short session to build confidence'
        },
        {
            'scenario': 'Regular Daily Practice',
            'profile': 'intermediate',
            'mode': 'focus',
            'command': 'python ui.py --profile intermediate --mode focus',
            'why': 'Balanced evaluation with focused 10-min session'
        },
        {
            'scenario': 'Pre-Performance Refinement',
            'profile': 'advanced',
            'mode': 'focus',
            'command': 'python ui.py --profile advanced --mode focus',
            'why': 'Strict evaluation to ensure performance readiness'
        },
        {
            'scenario': 'Music Therapy Session',
            'profile': 'therapy',
            'mode': 'free',
            'command': 'python ui.py --profile therapy --mode free',
            'why': 'Maximum tolerance with no time pressure'
        },
        {
            'scenario': 'Quick Morning Warmup',
            'profile': 'beginner',
            'mode': 'short',
            'command': 'python ui.py --profile beginner --mode short',
            'why': 'Gentle start to the day, builds consistency'
        },
        {
            'scenario': 'Jam Session / Exploration',
            'profile': 'intermediate',
            'mode': 'free',
            'command': 'python ui.py --profile intermediate --mode free',
            'why': 'Freedom to explore without strict time limits'
        }
    ]
    
    for i, ex in enumerate(examples, 1):
        print(f"{i}. {ex['scenario']}")
        print(f"   Profile: {ex['profile']}  |  Mode: {ex['mode']}")
        print(f"   Command: {ex['command']}")
        print(f"   Why:     {ex['why']}")
        print()


def main():
    print()
    print("╔" + "═" * 98 + "╗")
    print("║" + "HONORHERO - PROFILES & MODES VISUAL GUIDE".center(98) + "║")
    print("╚" + "═" * 98 + "╝")
    print()
    
    show_profile_comparison()
    show_mode_comparison()
    show_use_case_examples()
    
    print("=" * 80)
    print("For detailed documentation, see NEW_FEATURES.md")
    print("=" * 80)
    print()


if __name__ == '__main__':
    main()
