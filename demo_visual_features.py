"""
Demo script showcasing HonorHero's visual identity and gamification features
"""

import time
import sys
from themes import (
    get_theme, get_score_color, Icons, VisualFeedback,
    format_with_theme, Colors, THEMES
)
from achievements import AchievementSystem


def print_header(text, theme):
    """Print a styled header"""
    print()
    print(format_with_theme("=" * 70, theme.primary))
    print(format_with_theme(text.center(70), theme.accent + Colors.BOLD))
    print(format_with_theme("=" * 70, theme.primary))
    print()


def demo_themes():
    """Demonstrate all available themes"""
    print()
    print(format_with_theme("🎨 VISUAL IDENTITY DEMO 🎨".center(70), Colors.BOLD + Colors.CYAN))
    print("=" * 70)
    print()
    
    for theme_name in ['warm', 'cool', 'colorblind', 'dark', 'light', 'monochrome']:
        theme = get_theme(theme_name=theme_name)
        
        print_header(f"Theme: {theme.name}", theme)
        
        # Show color palette
        print("Color Palette:")
        print(f"  Primary:   {format_with_theme('████████████', theme.primary)}")
        print(f"  Secondary: {format_with_theme('████████████', theme.secondary)}")
        print(f"  Success:   {format_with_theme('████████████', theme.success)}")
        print(f"  Warning:   {format_with_theme('████████████', theme.warning)}")
        print(f"  Error:     {format_with_theme('████████████', theme.error)}")
        print(f"  Info:      {format_with_theme('████████████', theme.info)}")
        print(f"  Accent:    {format_with_theme('████████████', theme.accent)}")
        print()
        
        # Show score tiers
        print("Score Tiers:")
        for score, tier in [(95, 'Íntegro'), (70, 'Firme'), (50, 'Inestable'), (25, 'Fragmentado')]:
            color = get_score_color(score, theme)
            bar = VisualFeedback.smooth_bar(score, 30)
            print(f"  {tier:15} ({score:>3}): {color}{bar}{Colors.RESET}")
        print()
        
        # Show animated feedback
        print("Animated Feedback:")
        print(f"  Particles:  {VisualFeedback.particle_effect(4)}")
        print(f"  Improvement: {format_with_theme(f'{Icons.ARROW_UP} Score increasing!', theme.success)}")
        print(f"  Stable:      {format_with_theme(f'{Icons.ARROW_RIGHT} Maintaining level', theme.info)}")
        print(f"  Decline:     {format_with_theme(f'{Icons.ARROW_DOWN} Score decreasing', theme.warning)}")
        print()
        
        input("Press Enter to continue...")


def demo_profile_themes():
    """Demonstrate profile-specific theming"""
    print()
    print(format_with_theme("👤 PROFILE-SPECIFIC THEMES 👤".center(70), Colors.BOLD + Colors.MAGENTA))
    print("=" * 70)
    print()
    
    profiles = {
        'beginner': 'Warm, encouraging colors for comfort',
        'intermediate': 'Cool, balanced colors for focus',
        'advanced': 'Precise, technical colors',
        'therapy': 'Soft, gentle colors for healing'
    }
    
    for profile, description in profiles.items():
        theme = get_theme(profile=profile)
        
        print(format_with_theme(f"Profile: {profile.upper()}", theme.accent + Colors.BOLD))
        print(f"Description: {description}")
        print(f"Theme: {theme.name}")
        print()
        
        # Mock UI preview
        mock_score = 75
        mock_components = {
            'pitch': 78,
            'timing': 72,
            'rhythm': 75,
            'dynamics': 76,
            'consistency': 74
        }
        
        print(format_with_theme("┌─ MOCK UI PREVIEW " + "─" * 50 + "┐", theme.primary))
        
        # Honor score display
        color = get_score_color(mock_score, theme)
        print(f"│ {color}Honor Score: {mock_score:.1f}{Colors.RESET}{'':>51}│")
        print("│" + " " * 68 + "│")
        
        # Components
        for name, score in mock_components.items():
            bar = VisualFeedback.smooth_bar(score, 30)
            comp_color = get_score_color(score, theme)
            print(f"│ {name:12} {comp_color}{bar}{Colors.RESET} {score:>5.1f}%{'':>7}│")
        
        print(format_with_theme("└" + "─" * 68 + "┘", theme.primary))
        print()
        
        input("Press Enter to continue...")


def demo_achievements():
    """Demonstrate achievement system"""
    print()
    print(format_with_theme("🏆 ACHIEVEMENT SYSTEM DEMO 🏆".center(70), Colors.BOLD + Colors.YELLOW))
    print("=" * 70)
    print()
    
    achv = AchievementSystem(data_file='/tmp/demo_achievements.json')
    
    # Show categories
    print(format_with_theme("Achievement Categories:", Colors.BOLD + Colors.CYAN))
    print()
    
    categories = {
        'filosofico': ('Philosophical', '🌱', 'Focus on intrinsic values of learning'),
        'medalla': ('Soft Medals', '✨', 'Gentle recognition of technical progress'),
        'hito': ('Milestones', '🚀', 'Time-based celebration of dedication')
    }
    
    for cat_id, (cat_name, icon, description) in categories.items():
        achievements = achv.get_achievements_by_category(cat_id)
        
        print(format_with_theme(f"{icon} {cat_name}", Colors.BOLD + Colors.GREEN))
        print(f"   {description}")
        print(f"   {len(achievements)} achievements")
        print()
        
        for achievement in achievements[:3]:  # Show first 3
            status = Icons.CHECK if achievement.unlocked else Icons.CROSS
            print(f"   {status} {achievement.icon} {achievement.name}")
            print(f"      {achievement.description}")
        
        if len(achievements) > 3:
            print(f"   ... and {len(achievements) - 3} more")
        print()
    
    # Simulate unlocking
    print(format_with_theme("Simulating achievement unlock...", Colors.BOLD + Colors.YELLOW))
    print()
    
    session_data = {
        'final_honor_score': 85,
        'components': {'pitch': 80, 'timing': 75, 'rhythm': 78, 'dynamics': 82, 'consistency': 88}
    }
    history_data = {'total_sessions': 1, 'streak': 0, 'total_time': 600, 'first_score': 50}
    
    newly_unlocked = achv.check_session_achievements(session_data, history_data)
    
    if newly_unlocked:
        print(format_with_theme("=" * 70, Colors.GREEN))
        print(format_with_theme(f"{Icons.STAR}  ACHIEVEMENTS UNLOCKED!  {Icons.STAR}".center(70), 
                               Colors.GREEN + Colors.BOLD))
        print(format_with_theme("=" * 70, Colors.GREEN))
        print()
        
        for achievement in newly_unlocked:
            print(format_with_theme(f"{achievement.icon} {achievement.name}", Colors.GREEN + Colors.BOLD))
            print(f"   {achievement.description}")
            print()
    
    progress = achv.get_progress()
    print(f"Achievement Progress: {progress['unlocked']}/{progress['total']} ({progress['percentage']:.0f}%)")
    print()
    
    input("Press Enter to continue...")


def demo_visual_feedback():
    """Demonstrate animated visual feedback"""
    print()
    print(format_with_theme("✨ ANIMATED FEEDBACK DEMO ✨".center(70), Colors.BOLD + Colors.MAGENTA))
    print("=" * 70)
    print()
    
    theme = get_theme('cool')
    
    print("Real-time Score Animation:")
    print()
    
    scores = [45, 52, 58, 65, 70, 75, 78, 82, 85]
    
    for i, score in enumerate(scores):
        print(f"\033[2J\033[H", end='')  # Clear screen
        
        print_header(f"Performance Update #{i+1}", theme)
        
        color = get_score_color(score, theme)
        bar = VisualFeedback.smooth_bar(score, 40)
        
        print(f"{color}╔{'═' * 68}╗{Colors.RESET}")
        print(f"{color}║{'HONOR SCORE':^68}║{Colors.RESET}")
        print(f"{color}║{f'{score:.1f}':^68}║{Colors.RESET}")
        print(f"{color}╚{'═' * 68}╝{Colors.RESET}")
        print()
        
        # Show feedback based on improvement
        if i > 0:
            delta = score - scores[i-1]
            if delta > 3:
                print(format_with_theme(f"{VisualFeedback.particle_effect()} {Icons.ARROW_UP} Great improvement!", 
                                       theme.success))
            elif delta > 0:
                print(format_with_theme(f"{Icons.ARROW_UP} Keep going!", theme.info))
            else:
                print(format_with_theme(f"{Icons.ARROW_RIGHT} Stable performance", theme.warning))
        
        print()
        print(f"Progress: {color}{bar}{Colors.RESET}")
        print()
        
        time.sleep(0.8)
    
    print()
    print(format_with_theme(f"{Icons.SPARKLES} Demo complete! Your score improved from 45 to 85! {Icons.SPARKLES}", 
                           theme.success + Colors.BOLD))
    print()
    
    input("Press Enter to continue...")


def main():
    """Run the complete demo"""
    try:
        print("\033[2J\033[H")  # Clear screen
        print()
        print(format_with_theme("╔" + "═" * 68 + "╗", Colors.CYAN))
        print(format_with_theme("║" + " " * 68 + "║", Colors.CYAN))
        print(format_with_theme("║" + f"{Icons.MUSIC} HONORHERO VISUAL IDENTITY & GAMIFICATION DEMO {Icons.MUSIC}".center(78) + "║", 
                               Colors.CYAN + Colors.BOLD))
        print(format_with_theme("║" + " " * 68 + "║", Colors.CYAN))
        print(format_with_theme("╚" + "═" * 68 + "╝", Colors.CYAN))
        print()
        print("This demo showcases HonorHero's new visual identity and gamification features:")
        print()
        print("  🎨 6 distinct visual themes")
        print("  👤 Profile-specific aesthetics")
        print("  🏆 17+ non-competitive achievements")
        print("  ✨ Animated real-time feedback")
        print()
        print("Press Enter to begin the demo...")
        input()
        
        demo_themes()
        demo_profile_themes()
        demo_achievements()
        demo_visual_feedback()
        
        print("\033[2J\033[H")  # Clear screen
        print()
        print(format_with_theme("=" * 70, Colors.GREEN))
        print(format_with_theme(f"{Icons.TROPHY} DEMO COMPLETE! {Icons.TROPHY}".center(70), 
                               Colors.GREEN + Colors.BOLD))
        print(format_with_theme("=" * 70, Colors.GREEN))
        print()
        print("HonorHero now features:")
        print()
        print(f"  {format_with_theme('✓', Colors.GREEN)} 6 visual themes (warm, cool, colorblind, dark, light, monochrome)")
        print(f"  {format_with_theme('✓', Colors.GREEN)} Profile-specific theming for optimal learning")
        print(f"  {format_with_theme('✓', Colors.GREEN)} 17+ achievements celebrating personal growth")
        print(f"  {format_with_theme('✓', Colors.GREEN)} Real-time animated feedback")
        print(f"  {format_with_theme('✓', Colors.GREEN)} Smooth progress bars and visual indicators")
        print(f"  {format_with_theme('✓', Colors.GREEN)} Accessibility support (colorblind mode)")
        print()
        print("Try it yourself:")
        print(f"  python ui.py --theme warm --profile beginner")
        print(f"  python ui.py --theme colorblind --mode focus")
        print(f"  python piano_roll_ui.py --theme dark")
        print()
        print(format_with_theme("¡Que disfrutes tu viaje musical! 🎵", Colors.MAGENTA + Colors.BOLD))
        print()
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted.")
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
