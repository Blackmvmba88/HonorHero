"""
Test script for themes and achievements system
"""

import sys
from themes import (
    get_theme, get_score_color, Icons, VisualFeedback,
    format_with_theme, Colors, THEMES, PROFILE_THEMES
)
from achievements import AchievementSystem, ACHIEVEMENT_DEFINITIONS


def test_themes():
    """Test theme system"""
    print("=" * 70)
    print("Testing Theme System")
    print("=" * 70)
    print()
    
    # Test all themes
    for theme_name in THEMES.keys():
        theme = get_theme(theme_name=theme_name)
        print(f"Theme: {format_with_theme(theme.name, theme.accent + Colors.BOLD)}")
        print(f"  Primary: {format_with_theme('██████', theme.primary)}")
        print(f"  Success: {format_with_theme('██████', theme.success)}")
        print(f"  Warning: {format_with_theme('██████', theme.warning)}")
        print(f"  Error: {format_with_theme('██████', theme.error)}")
        print()
    
    # Test profile-based themes
    print("Profile-based themes:")
    for profile, theme_name in PROFILE_THEMES.items():
        theme = get_theme(profile=profile)
        print(f"  {profile}: {theme.name}")
    print()
    
    # Test visual feedback
    print("Visual Feedback Elements:")
    print(f"  Particles: {VisualFeedback.particle_effect(3)}")
    print(f"  Wave (low): {VisualFeedback.wave_effect(0.2)}")
    print(f"  Wave (high): {VisualFeedback.wave_effect(0.8)}")
    print(f"  Progress: {VisualFeedback.progress_indicator(7, 10, 20)}")
    print(f"  Smooth bar (50%): {VisualFeedback.smooth_bar(50, 30)}")
    print(f"  Smooth bar (75%): {VisualFeedback.smooth_bar(75, 30)}")
    print()
    
    print(format_with_theme(f"{Icons.CHECK} Theme system working!", Colors.GREEN + Colors.BOLD))
    print()


def test_achievements():
    """Test achievement system"""
    print("=" * 70)
    print("Testing Achievement System")
    print("=" * 70)
    print()
    
    # Create achievement system
    achv = AchievementSystem(data_file='/tmp/test_achievements.json')
    
    print(f"Total achievements defined: {len(achv.achievements)}")
    print()
    
    # List all achievements by category
    categories = set(a.category for a in achv.achievements.values())
    for category in categories:
        achievements = achv.get_achievements_by_category(category)
        print(f"Category: {category.upper()}")
        for achievement in achievements:
            status = Icons.CHECK if achievement.unlocked else Icons.CROSS
            print(f"  {status} {achievement.icon} {achievement.name}: {achievement.description}")
        print()
    
    # Test simulated session to unlock achievements
    print("Simulating session data to test achievement unlocking...")
    session_data = {
        'final_honor_score': 85,
        'components': {
            'pitch': 80,
            'timing': 75,
            'rhythm': 78,
            'dynamics': 82,
            'consistency': 88
        }
    }
    
    history_data = {
        'total_sessions': 1,
        'streak': 0,
        'total_time': 600,
        'first_score': 50
    }
    
    newly_unlocked = achv.check_session_achievements(session_data, history_data)
    
    if newly_unlocked:
        print(f"\n{Icons.STAR} Newly unlocked achievements:")
        for achievement in newly_unlocked:
            print(f"  {achievement.icon} {achievement.name}: {achievement.description}")
    else:
        print(f"\n{Icons.SPARKLES} No new achievements unlocked (as expected for first session)")
    
    print()
    
    # Show progress
    progress = achv.get_progress()
    print(f"Achievement Progress:")
    print(f"  Total: {progress['unlocked']}/{progress['total']} ({progress['percentage']:.1f}%)")
    print()
    
    print(format_with_theme(f"{Icons.CHECK} Achievement system working!", Colors.GREEN + Colors.BOLD))
    print()


def test_score_colors():
    """Test score color mapping"""
    print("=" * 70)
    print("Testing Score Color Mapping")
    print("=" * 70)
    print()
    
    theme = get_theme('cool')
    
    scores = [95, 75, 55, 25]
    tiers = ['Íntegro', 'Firme', 'Inestable', 'Fragmentado']
    
    for score, tier in zip(scores, tiers):
        color = get_score_color(score, theme)
        bar = VisualFeedback.smooth_bar(score, 40)
        print(f"{tier:15} ({score:>3}): {color}{bar}{Colors.RESET}")
    
    print()
    print(format_with_theme(f"{Icons.CHECK} Score color mapping working!", Colors.GREEN + Colors.BOLD))
    print()


def main():
    """Run all tests"""
    try:
        test_themes()
        test_achievements()
        test_score_colors()
        
        print("=" * 70)
        print(format_with_theme(f"{Icons.TROPHY} All tests passed!", Colors.GREEN + Colors.BOLD))
        print("=" * 70)
        
    except Exception as e:
        print(f"{Icons.CROSS} Test failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
