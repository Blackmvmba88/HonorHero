#!/usr/bin/env python3
"""
Display HonorHero Examples
Interactive viewer for example sessions and scenarios
"""

import json
import sys
from pathlib import Path


def print_header(text, char="═"):
    """Print a formatted header"""
    width = 70
    print("\n" + char * width)
    print(text.center(width))
    print(char * width + "\n")


def print_console_output(output_lines):
    """Print console output with proper formatting"""
    for line in output_lines:
        print(line)


def display_example1():
    """Display Example 1: Juan's Beginner Guitar Session"""
    print_header("Example 1: Juan's Beginner Guitar Session")
    
    with open('examples/example1_juan_beginner.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    session = data['session']
    
    print(f"📖 Scenario: {data['scenario']}\n")
    
    # Display console output
    print_console_output(data['console_output'])
    
    print()
    print("Component Breakdown:")
    for comp, score in session['components'].items():
        bar_length = int(score / 5)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        print(f"  {comp.capitalize():12} [{bar}] {score:.0f}/100")
    
    print()
    print(f"💡 Key Insight: {session['encouragement']}")
    print(f"📌 Next Steps: {session['next_steps']}")
    print()


def display_example2():
    """Display Example 2: Daily Practice Tracking"""
    print_header("Example 2: Daily Practice Tracking")
    
    print("📖 Scenario: Juan practices 5 minutes a day for a week.\n")
    print("After several sessions, he runs: python view_stats.py\n")
    print("HonorHero shows:\n")
    
    days = [1, 4, 7]
    progress_data = []
    
    for day in days:
        with open(f'examples/example2_daily_tracking_day{day}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            session = data['session']
            progress_data.append({
                'day': day,
                'score': session['honor_score'],
                'tier': session['tier'],
                'notes': session.get('notes', '')
            })
    
    print("┌─ PROGRESO SEMANAL " + "─" * 48 + "┐")
    print("│ " + "Día".ljust(6) + "Score".ljust(10) + "Tier".ljust(15) + 
          "Notas".ljust(30) + "│")
    print("├" + "─" * 68 + "┤")
    
    for p in progress_data:
        day_str = f"Day {p['day']}"
        score_str = str(p['score'])
        tier_str = p['tier']
        notes_str = p['notes'][:28] + ".." if len(p['notes']) > 30 else p['notes']
        
        print(f"│ {day_str.ljust(6)}{score_str.ljust(10)}{tier_str.ljust(15)}{notes_str.ljust(30)}│")
    
    print("└" + "─" * 68 + "┘")
    
    # Calculate improvement
    improvement = progress_data[-1]['score'] - progress_data[0]['score']
    
    print()
    print(f"📈 Improvement: +{improvement} points in 7 days")
    print(f"🎯 From {progress_data[0]['tier']} to {progress_data[-1]['tier']}")
    print()
    print("💡 Key Insight: Progress is visible, measurable, and motivating — without pressure.")
    print()


def display_example3():
    """Display Example 3: Shy Vocalist"""
    print_header("Example 3: Vocal Practice (Shy Vocalist)")
    
    with open('examples/example3_shy_vocalist.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    session = data['session']
    
    print(f"📖 Scenario: {data['scenario']}\n")
    
    # Display console output
    print_console_output(data['console_output'])
    
    print()
    print("HonorHero Adapts:")
    behavior = session['system_behavior']
    print(f"  • Pitch Tolerance:      {behavior['pitch_tolerance']}")
    print(f"  • Dynamics Analysis:    {behavior['dynamics_analysis']}")
    print(f"  • Stability Penalties:  {behavior['stability_penalties']}")
    print(f"  • Coaching Style:       {behavior['coaching_style']}")
    
    print()
    print("💡 Key Insight: The system acts like a supportive coach, not a judge.")
    print()


def display_example4():
    """Display Example 4: Programmatic Use"""
    print_header("Example 4: Programmatic Use (Developers)")
    
    with open('examples/example4_programmatic_use.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"📖 Scenario: {data['scenario']}\n")
    
    print("Use Cases:")
    for use_case in data['use_cases']:
        print(f"  • {use_case}")
    
    print("\n" + "─" * 70)
    print("Example Code:")
    print("─" * 70)
    
    for line in data['code_example']['snippet']:
        print(line)
    
    print("─" * 70)
    
    print("\nSample Callback Data:")
    callback = data['sample_callback_data']
    print(f"  Timestamp:    {callback['timestamp']}s")
    print(f"  Honor Score:  {callback['metrics']['honor_score']}")
    print(f"  Tier:         {callback['metrics']['tier']}")
    print(f"  Feedback:     {callback['metrics']['human_feedback']}")
    
    print("\nIntegration Scenarios:")
    for name, scenario in data['integration_scenarios'].items():
        print(f"\n  {name.replace('_', ' ').title()}:")
        print(f"    {scenario['description']}")
    
    print()
    print(f"💡 Key Insight: {data['note']}")
    print()


def display_example5():
    """Display Example 5: What HonorHero Is NOT"""
    print_header("Example 5: What HonorHero Is NOT")
    
    with open('examples/example5_what_honorhero_is_not.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"🎯 Philosophy: {data['philosophy']}\n")
    
    print("HonorHero does NOT:")
    for key, item in data['what_honorhero_does_not_do'].items():
        print(f"\n  ❌ {item['description']}")
        print(f"     {item['explanation']}")
        print(f"     ✅ Alternative: {item['alternative']}")
    
    print("\n" + "─" * 70)
    print("\nHonorHero EXISTS TO:")
    for purpose in data['honorhero_exists_to']:
        print(f"  ✨ {purpose}")
    
    print("\n" + "─" * 70)
    print("\nComparison Table:")
    print("─" * 70)
    
    comparison = data['comparison_table']
    
    aspects = ['focus', 'feedback', 'competition', 'mistakes', 'goal']
    
    print(f"{'Aspect'.ljust(15)} {'Traditional Grading'.ljust(30)} {'HonorHero'.ljust(30)}")
    print("─" * 75)
    
    for aspect in aspects:
        trad = comparison['traditional_grading'][aspect]
        honor = comparison['honorhero'][aspect]
        
        # Truncate if too long
        trad_short = trad[:28] + ".." if len(trad) > 30 else trad
        honor_short = honor[:28] + ".." if len(honor) > 30 else honor
        
        print(f"{aspect.capitalize().ljust(15)} {trad_short.ljust(30)} {honor_short.ljust(30)}")
    
    print()
    print("💡 Testimonials:")
    for role, quote in data['testimonials'].items():
        print(f"  {role.capitalize()}: \"{quote}\"")
    
    print()


def display_menu():
    """Display main menu"""
    print_header("🎵 HonorHero Examples", "═")
    
    print("Choose an example to view:\n")
    print("  1. Juan's Beginner Guitar Session")
    print("     → First-time practice, Score: 42 (Inestable)")
    print()
    print("  2. Daily Practice Tracking")
    print("     → Week-long journey from 42 to 82")
    print()
    print("  3. Shy Vocalist (Nighttime Practice)")
    print("     → Tolerant, supportive feedback, Score: 71 (Firme)")
    print()
    print("  4. Programmatic Use for Developers")
    print("     → Embedding HonorHero in custom applications")
    print()
    print("  5. What HonorHero Is NOT")
    print("     → Philosophy and comparison with traditional grading")
    print()
    print("  6. View All Examples")
    print()
    print("  0. Exit")
    print()


def main():
    """Main entry point"""
    
    # Check if we're in the right directory
    if not Path('examples').exists():
        print("Error: 'examples' directory not found.")
        print("Please run this script from the HonorHero root directory.")
        sys.exit(1)
    
    examples = {
        '1': display_example1,
        '2': display_example2,
        '3': display_example3,
        '4': display_example4,
        '5': display_example5,
    }
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (0-6): ").strip()
            
            if choice == '0':
                print("\n✨ Keep practicing! ¡Sigue tocando! 🎵\n")
                break
            elif choice == '6':
                for example_func in examples.values():
                    example_func()
                    input("\nPress Enter to continue to next example...")
            elif choice in examples:
                examples[choice]()
                input("\nPress Enter to return to menu...")
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n✨ Keep practicing! ¡Sigue tocando! 🎵\n")
            break
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")


if __name__ == '__main__':
    main()
