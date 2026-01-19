"""
HonorHero Simple Console UI
Expressive UI focused on self-improvement, not competition
Enhanced with visual identity and gamification features
"""

import time
import sys
from honorhero import HonorHero
from typing import Dict
import config
from themes import get_theme, get_score_color, Icons, VisualFeedback, format_with_theme, Colors
from achievements import AchievementSystem


class HonorHeroUI:
    """Simple expressive console UI for HonorHero with visual identity"""
    
    def __init__(self, profile: str = None, mode: str = None, theme: str = None):
        self.profile_name = profile or config.DEFAULT_PROFILE
        self.mode_name = mode or config.DEFAULT_MODE
        
        # Load profile settings
        if self.profile_name not in config.PROFILES:
            print(f"Warning: Profile '{self.profile_name}' not found, using default.")
            self.profile_name = config.DEFAULT_PROFILE
        
        self.profile = config.PROFILES[self.profile_name]
        
        # Load mode settings
        if self.mode_name not in config.SESSION_MODES:
            print(f"Warning: Mode '{self.mode_name}' not found, using default.")
            self.mode_name = config.DEFAULT_MODE
        
        self.mode = config.SESSION_MODES[self.mode_name]
        
        # Apply profile settings to config
        config.PITCH_TOLERANCE = self.profile['PITCH_TOLERANCE']
        config.TIMING_TOLERANCE = self.profile['TIMING_TOLERANCE']
        config.RHYTHM_TOLERANCE = self.profile['RHYTHM_TOLERANCE']
        config.DYNAMICS_TOLERANCE = self.profile['DYNAMICS_TOLERANCE']
        config.CONSISTENCY_THRESHOLD = self.profile['CONSISTENCY_THRESHOLD']
        
        # Load theme (profile-specific or explicit)
        self.theme = get_theme(theme_name=theme, profile=self.profile_name)
        
        # Initialize achievement system
        self.achievements = AchievementSystem()
        
        self.engine = HonorHero()
        self.last_update_time = 0
        self.previous_score = 0
        
    def clear_screen(self):
        """Clear console screen"""
        print('\033[2J\033[H', end='')
    
    def draw_bar(self, value: float, width: int = 40) -> str:
        """Draw a smooth progress bar using theme"""
        return VisualFeedback.smooth_bar(value, width)
    
    def get_color(self, score: float) -> str:
        """Get color code for score using theme"""
        return get_score_color(score, self.theme)
    
    def display_update(self, metrics: Dict):
        """Display real-time metrics update with visual feedback"""
        current_time = time.time()
        
        # Throttle updates to every 0.5 seconds
        if current_time - self.last_update_time < 0.5:
            return
        
        self.last_update_time = current_time
        self.clear_screen()
        
        honor_score = metrics.get('honor_score', 0)
        tier = metrics.get('tier', 'N/A')
        components = metrics.get('components', {})
        
        # Calculate improvement for visual feedback
        score_delta = honor_score - self.previous_score
        self.previous_score = honor_score
        
        # Header with theme colors
        print(format_with_theme("=" * 70, self.theme.primary))
        print(format_with_theme(f"{Icons.MUSIC}  HONORHERO  {Icons.MUSIC}".center(70), self.theme.accent + Colors.BOLD))
        print(format_with_theme("Interpretación consciente, no perfección vacía".center(70), self.theme.dim_text))
        print(format_with_theme("=" * 70, self.theme.primary))
        # Use raw profile and mode names without color codes for centering
        profile_mode_text = f"Perfil: {self.profile['name']} | Modo: {self.mode['name']}"
        print(profile_mode_text.center(70))
        print()
        
        # Honor Score (large display) with theme colors
        color = self.get_color(honor_score)
        reset = Colors.RESET
        
        # Add visual feedback for improvements
        feedback_icon = ""
        if score_delta > 2:
            feedback_icon = f" {VisualFeedback.particle_effect()} {Icons.ARROW_UP}"
        elif score_delta < -2:
            feedback_icon = f" {Icons.ARROW_DOWN}"
        
        print(f"{color}╔{'═' * 68}╗{reset}")
        print(f"{color}║{'  HONOR SCORE':^68}║{reset}")
        print(f"{color}║{f'{honor_score:.1f}{feedback_icon}':^68}║{reset}")
        print(f"{color}║{tier:^68}║{reset}")
        print(f"{color}╚{'═' * 68}╝{reset}")
        print()
        
        # Component scores with themed colors
        print(format_with_theme("┌─ COMPONENTES " + "─" * 54 + "┐", self.theme.primary))
        
        for name, score in components.items():
            label = name.upper().ljust(12)
            bar = self.draw_bar(score, width=35)
            color = self.get_color(score)
            print(f"│ {label} │ {color}{bar}{reset} {score:>5.1f}% │")
        
        print(format_with_theme("└" + "─" * 68 + "┘", self.theme.primary))
        print()
        
        # Human-friendly feedback with icon
        human_feedback = metrics.get('human_feedback', '')
        if human_feedback:
            print(format_with_theme(f"{Icons.SPARKLES} {human_feedback}", self.theme.info))
        else:
            # Fallback to default message
            message = metrics.get('message', '')
            print(format_with_theme(f"{Icons.SPARKLES} {message}", self.theme.info))
        print()
        print(format_with_theme("Presiona Ctrl+C para detener la evaluación...", self.theme.dim_text))
    
    def display_final_results(self, results: Dict):
        """Display final performance summary with achievements"""
        self.clear_screen()
        
        print(format_with_theme("=" * 70, self.theme.primary))
        print(format_with_theme(f"{Icons.TROPHY}  RESUMEN FINAL  {Icons.TROPHY}".center(70), self.theme.accent + Colors.BOLD))
        print(format_with_theme("=" * 70, self.theme.primary))
        print()
        
        honor_score = results.get('final_honor_score', 0)
        tier = results.get('tier', 'N/A')
        message = results.get('message', '')
        human_summary = results.get('human_summary', '')
        components = results.get('components', {})
        progress = results.get('progress', {})
        comparison = results.get('comparison', {})
        duration = results.get('duration', 0)
        
        color = self.get_color(honor_score)
        reset = Colors.RESET
        
        # Final score with visual flair
        print(f"{color}╔{'═' * 68}╗{reset}")
        print(f"{color}║{'  HONOR SCORE FINAL':^68}║{reset}")
        print(f"{color}║{f'{honor_score:.1f}':^68}║{reset}")
        print(f"{color}║{tier:^68}║{reset}")
        print(f"{color}╚{'═' * 68}╝{reset}")
        print()
        
        # Human-friendly summary
        if human_summary:
            print(format_with_theme(f"{Icons.SPARKLES} {human_summary}", self.theme.info))
        else:
            print(format_with_theme(f"{Icons.SPARKLES} {message}", self.theme.info))
        print()
        
        # Check for achievements
        history_stats = self.engine.get_session_statistics()
        newly_unlocked = self.achievements.check_session_achievements(results, history_stats)
        
        if newly_unlocked:
            print()
            print(format_with_theme(f"{'═' * 70}", self.theme.accent))
            print(format_with_theme(f"{Icons.STAR}  ¡NUEVOS LOGROS DESBLOQUEADOS!  {Icons.STAR}".center(70), 
                                   self.theme.accent + Colors.BOLD))
            print(format_with_theme(f"{'═' * 70}", self.theme.accent))
            for achievement in newly_unlocked:
                print(format_with_theme(
                    f"{achievement.icon}  {achievement.name}: {achievement.description}",
                    self.theme.success
                ))
            print()
        
        # Comparison with history
        if comparison and comparison.get('has_history'):
            print(format_with_theme(f"{Icons.CHART} {comparison.get('message', '')}", self.theme.secondary))
            print()
        
        # Component breakdown
        print(format_with_theme("┌─ DESGLOSE DE COMPONENTES " + "─" * 41 + "┐", self.theme.primary))
        for name, score in components.items():
            label = name.upper().ljust(12)
            bar = self.draw_bar(score, width=35)
            comp_color = self.get_color(score)
            print(f"│ {label} │ {comp_color}{bar}{reset} {score:>5.1f}% │")
        print(format_with_theme("└" + "─" * 68 + "┘", self.theme.primary))
        print()
        
        # Session info
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        print(format_with_theme("┌─ INFORMACIÓN DE SESIÓN " + "─" * 43 + "┐", self.theme.primary))
        print(f"│ Duración:             {minutes:02d}:{seconds:02d} min{' ' * 40} │")
        print(f"│ Evaluaciones totales: {progress.get('total_evaluations', 0):<43} │")
        print(f"│ Puntuación promedio:  {progress.get('average_score', 0):<43.1f} │")
        print(f"│ Tendencia:            {progress.get('trend', 'N/A'):<43} │")
        print(format_with_theme("└" + "─" * 68 + "┘", self.theme.primary))
        print()
        
        # Show achievement progress
        achievement_progress = self.achievements.get_progress()
        unlocked_count = achievement_progress['unlocked']
        total_count = achievement_progress['total']
        print(format_with_theme(
            f"{Icons.MEDAL} Logros: {unlocked_count}/{total_count} ({achievement_progress['percentage']:.0f}%)",
            self.theme.accent
        ))
        print()
        
        print(format_with_theme(f"{Icons.SPARKLES} Cada práctica te acerca más a la maestría. ¡Sigue adelante! {Icons.SPARKLES}", 
                               self.theme.success))
        print()
    
    def run(self, duration: int = None):
        """
        Run HonorHero with UI
        
        Args:
            duration: Performance duration in seconds (None = use mode default or until interrupted)
        """
        # Use mode duration if not explicitly provided
        if duration is None:
            duration = self.mode['duration']
        
        try:
            # Start engine
            self.engine.start_performance(self.display_update)
            
            # Run for specified duration or until interrupted
            if duration:
                time.sleep(duration)
            else:
                print("Performance en curso... (Ctrl+C para detener)")
                while True:
                    time.sleep(0.1)
                    
        except KeyboardInterrupt:
            print("\n\nDeteniendo evaluación...")
            
        finally:
            # Stop and show results
            results = self.engine.stop_performance()
            self.display_final_results(results)


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='HonorHero - Human-centered music performance evaluation'
    )
    parser.add_argument(
        '--duration',
        type=int,
        default=None,
        help='Performance duration in seconds (overrides mode default)'
    )
    parser.add_argument(
        '--profile',
        type=str,
        choices=['beginner', 'intermediate', 'advanced', 'therapy'],
        default=None,
        help='User profile: beginner (más tolerante) | intermediate | advanced (más estricto) | therapy (terapéutico)'
    )
    parser.add_argument(
        '--mode',
        type=str,
        choices=['short', 'focus', 'free'],
        default=None,
        help='Session mode: short (3 min) | focus (10 min) | free (sin límite)'
    )
    parser.add_argument(
        '--theme',
        type=str,
        choices=['warm', 'cool', 'colorblind', 'monochrome', 'dark', 'light'],
        default=None,
        help='Visual theme: warm (cálido) | cool (frío) | colorblind (accesible) | monochrome | dark | light'
    )
    
    args = parser.parse_args()
    
    # Get theme for welcome screen
    profile = args.profile or config.DEFAULT_PROFILE
    theme = get_theme(theme_name=args.theme, profile=profile)
    
    print()
    print(format_with_theme("=" * 70, theme.primary))
    print(format_with_theme(f"{Icons.MUSIC}  Bienvenido a HONORHERO  {Icons.MUSIC}".center(70), theme.accent + Colors.BOLD))
    print(format_with_theme("=" * 70, theme.primary))
    print()
    print("HonorHero es un sistema de evaluación de música centrado en el ser humano.")
    print("Captura audio en vivo y analiza:")
    print(f"  {Icons.MUSIC} Afinación (Pitch)")
    print(f"  {Icons.MUSIC} Timing y Ritmo")
    print(f"  {Icons.MUSIC} Dinámica")
    print(f"  {Icons.MUSIC} Consistencia")
    print()
    print("La performance nunca se detiene: los errores se miden, no se castigan.")
    print("Obtén un Honor Score (0-100) con niveles cualitativos:")
    print(f"  {format_with_theme('●', theme.success)} Íntegro (80-100)")
    print(f"  {format_with_theme('●', theme.info)} Firme (60-79)")
    print(f"  {format_with_theme('●', theme.warning)} Inestable (40-59)")
    print(f"  {format_with_theme('●', theme.error)} Fragmentado (0-39)")
    print()
    print(format_with_theme("Enfoque en auto-mejora, no en competencia.", theme.accent))
    print()
    
    # Show profile and mode selection
    mode = args.mode or config.DEFAULT_MODE
    
    profile_info = config.PROFILES[profile]
    mode_info = config.SESSION_MODES[mode]
    
    print(format_with_theme(f"{Icons.CHART} Perfil seleccionado: {profile_info['name']}", theme.primary))
    print(f"   {profile_info['description']}")
    print()
    print(format_with_theme(f"{Icons.ROCKET} Modo de sesión: {mode_info['name']}", theme.primary))
    print(f"   {mode_info['description']}")
    if mode_info['duration']:
        minutes = mode_info['duration'] // 60
        print(f"   Duración: {minutes} minutos")
    print()
    
    # Show theme info if explicitly selected
    if args.theme:
        print(format_with_theme(f"{Icons.SPARKLES} Tema visual: {theme.name}", theme.accent))
        print()
    
    print(format_with_theme("-" * 70, theme.dim_text))
    print()
    
    input("Presiona Enter para comenzar...")
    print()
    
    ui = HonorHeroUI(profile=profile, mode=mode, theme=args.theme)
    ui.run(duration=args.duration)


if __name__ == '__main__':
    main()
