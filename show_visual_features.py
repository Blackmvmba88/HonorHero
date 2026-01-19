"""
Generate visual output samples showing the new UI features
"""

from themes import get_theme, get_score_color, Icons, VisualFeedback, format_with_theme, Colors


def show_standard_ui_sample():
    """Show a sample of the standard UI with themes"""
    theme = get_theme('warm')
    
    print()
    print(format_with_theme("=" * 70, theme.primary))
    print(format_with_theme(f"{Icons.MUSIC}  HONORHERO  {Icons.MUSIC}".center(70), theme.accent + Colors.BOLD))
    print(format_with_theme("Interpretación consciente, no perfección vacía".center(70), theme.dim_text))
    print(format_with_theme("=" * 70, theme.primary))
    print(f"Perfil: {format_with_theme('Súper Principiante', theme.secondary)} | Modo: {format_with_theme('Sesión Corta', theme.secondary)}".center(90))
    print()
    
    # Mock honor score
    honor_score = 78
    tier = "Firme"
    color = get_score_color(honor_score, theme)
    
    print(f"{color}╔{'═' * 68}╗{Colors.RESET}")
    print(f"{color}║{'  HONOR SCORE':^68}║{Colors.RESET}")
    print(f"{color}║{f'{honor_score:.1f} {VisualFeedback.particle_effect(2)} {Icons.ARROW_UP}':^78}║{Colors.RESET}")
    print(f"{color}║{tier:^68}║{Colors.RESET}")
    print(f"{color}╚{'═' * 68}╝{Colors.RESET}")
    print()
    
    # Mock components
    components = {
        'pitch': 80,
        'timing': 75,
        'rhythm': 78,
        'dynamics': 76,
        'consistency': 82
    }
    
    print(format_with_theme("┌─ COMPONENTES " + "─" * 54 + "┐", theme.primary))
    
    for name, score in components.items():
        label = name.upper().ljust(12)
        bar = VisualFeedback.smooth_bar(score, width=35)
        comp_color = get_score_color(score, theme)
        print(f"│ {label} │ {comp_color}{bar}{Colors.RESET} {score:>5.1f}% │")
    
    print(format_with_theme("└" + "─" * 68 + "┘", theme.primary))
    print()
    
    print(format_with_theme(f"{Icons.SPARKLES} ¡Excelente! Tu afinación sigue mejorando. Sigue así.", theme.info))
    print()
    print(format_with_theme("Presiona Ctrl+C para detener la evaluación...", theme.dim_text))
    print()


def show_piano_roll_sample():
    """Show a sample of the piano roll UI"""
    theme = get_theme('cool')
    
    print()
    print(format_with_theme("═" * 90, theme.primary))
    print(format_with_theme(f"{Icons.MUSIC}  HONORHERO PIANO ROLL  {Icons.MUSIC}".center(90), 
                           theme.accent + Colors.BOLD))
    print(format_with_theme("Espejo temporal de tu interpretación".center(90), theme.dim_text))
    print(format_with_theme("═" * 90, theme.primary))
    print(f"Perfil: {format_with_theme('Intermedio', theme.secondary)} | Modo: {format_with_theme('Sesión Profunda', theme.secondary)}".center(100))
    print()
    
    # Mock piano roll
    print(format_with_theme("┌" + "─" * 4 + "┬" + "─" * 80 + "┐", theme.primary))
    print(f"│{'NOTA':^4}│{format_with_theme('← PASADO', theme.dim_text):^40}{format_with_theme('PRESENTE →', theme.accent):^50}│")
    print(format_with_theme("├" + "─" * 4 + "┼" + "─" * 80 + "┤", theme.primary))
    
    # Mock notes
    notes = ['C5', 'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4']
    for i, note in enumerate(notes):
        row = f"{note:>4} │"
        # Add some visual notes
        for j in range(80):
            if (i + j) % 7 == 0 and j > 20:
                row += format_with_theme('█', theme.info)
            elif (i + j) % 9 == 0 and j > 40:
                row += format_with_theme('▓', theme.success)
            else:
                row += ' '
        row += "│"
        print(row)
    
    print(format_with_theme("└" + "─" * 4 + "┴" + "─" * 80 + "┘", theme.primary))
    print()
    
    # Score display
    honor_score = 82
    tier = "Íntegro"
    color = get_score_color(honor_score, theme)
    print(f"{color}╔{'═' * 88}╗{Colors.RESET}")
    print(f"{color}║{f'HONOR SCORE: {honor_score:.1f} - {tier}':^88}║{Colors.RESET}")
    print(f"{color}╚{'═' * 88}╝{Colors.RESET}")
    print()
    
    print(format_with_theme(f"Tendencia: {Icons.ARROW_UP} Mejorando", theme.success))
    print()
    
    print(format_with_theme(f"{Icons.CHART} PITCH: 85  TIMING: 80  RHYTHM: 82  DYNAMICS: 83  CONSISTENCY: 80", theme.info))
    print()


def show_achievement_unlock():
    """Show achievement unlock notification"""
    theme = get_theme('cool')
    
    print()
    print(format_with_theme(f"{'═' * 70}", theme.accent))
    print(format_with_theme(f"{Icons.STAR}  ¡NUEVOS LOGROS DESBLOQUEADOS!  {Icons.STAR}".center(70), 
                           theme.accent + Colors.BOLD))
    print(format_with_theme(f"{'═' * 70}", theme.accent))
    print(format_with_theme(f"🚀 Primer Paso: Completaste tu primera sesión", theme.success))
    print(format_with_theme(f"🏆 Primera Integridad: Alcanzaste el tier Íntegro (80+) por primera vez", theme.success))
    print(format_with_theme(f"⚖️ Intérprete Equilibrado: Alcanzaste 70+ en todos los componentes", theme.success))
    print()


def show_theme_comparison():
    """Show comparison of different themes"""
    themes_to_show = [
        ('warm', 'Warm (Therapeutic)'),
        ('cool', 'Cool (Precision)'),
        ('colorblind', 'Colorblind Accessible')
    ]
    
    print()
    print(format_with_theme("Theme Comparison".center(70), Colors.BOLD + Colors.CYAN))
    print("=" * 70)
    print()
    
    score = 75
    
    for theme_name, display_name in themes_to_show:
        theme = get_theme(theme_name=theme_name)
        color = get_score_color(score, theme)
        bar = VisualFeedback.smooth_bar(score, 40)
        
        print(f"{display_name:30} {color}{bar}{Colors.RESET} {score}%")
    
    print()


def main():
    """Generate all visual samples"""
    print("\n" + "=" * 70)
    print("HONORHERO - Visual Identity Feature Showcase".center(70))
    print("=" * 70 + "\n")
    
    print("\n### 1. Standard UI with Warm Theme (Beginner Profile)")
    show_standard_ui_sample()
    
    print("\n### 2. Piano Roll UI with Cool Theme (Intermediate Profile)")
    show_piano_roll_sample()
    
    print("\n### 3. Achievement Unlock Notification")
    show_achievement_unlock()
    
    print("\n### 4. Theme Color Comparison")
    show_theme_comparison()
    
    print("\n" + "=" * 70)
    print("Feature Summary:".center(70))
    print("=" * 70)
    print()
    print("✓ 6 Visual Themes (warm, cool, colorblind, dark, light, monochrome)")
    print("✓ Profile-specific theming (beginner=warm, intermediate/advanced=cool, therapy=warm)")
    print("✓ 17+ Non-competitive achievements")
    print("✓ Animated real-time feedback (particles, arrows, smooth progress bars)")
    print("✓ Accessibility support (colorblind mode)")
    print("✓ Icons and visual landmarks throughout the UI")
    print()
    print("Usage:")
    print("  python ui.py --theme warm --profile beginner")
    print("  python ui.py --theme colorblind")
    print("  python piano_roll_ui.py --theme dark --mode focus")
    print()


if __name__ == '__main__':
    main()
