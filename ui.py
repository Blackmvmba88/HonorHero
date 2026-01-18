"""
HonorHero Simple Console UI
Expressive UI focused on self-improvement, not competition
"""

import time
import sys
from honorhero import HonorHero
from typing import Dict
import config


class HonorHeroUI:
    """Simple expressive console UI for HonorHero"""
    
    def __init__(self, profile: str = None, mode: str = None):
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
        
        self.engine = HonorHero()
        self.last_update_time = 0
        
    def clear_screen(self):
        """Clear console screen"""
        print('\033[2J\033[H', end='')
    
    def draw_bar(self, value: float, width: int = 40, char: str = '█') -> str:
        """Draw a progress bar"""
        filled = int((value / 100) * width)
        bar = char * filled + '░' * (width - filled)
        return bar
    
    def get_color(self, score: float) -> str:
        """Get color code for score"""
        if score >= 80:
            return '\033[92m'  # Green
        elif score >= 60:
            return '\033[94m'  # Blue
        elif score >= 40:
            return '\033[93m'  # Yellow
        else:
            return '\033[91m'  # Red
    
    def display_update(self, metrics: Dict):
        """Display real-time metrics update"""
        current_time = time.time()
        
        # Throttle updates to every 0.5 seconds
        if current_time - self.last_update_time < 0.5:
            return
        
        self.last_update_time = current_time
        self.clear_screen()
        
        honor_score = metrics.get('honor_score', 0)
        tier = metrics.get('tier', 'N/A')
        components = metrics.get('components', {})
        
        # Header
        print("=" * 70)
        print("🎵  HONORHERO  🎵".center(70))
        print("Interpretación consciente, no perfección vacía".center(70))
        print("=" * 70)
        print(f"Perfil: {self.profile['name']} | Modo: {self.mode['name']}".center(70))
        print()
        
        # Honor Score (large display)
        color = self.get_color(honor_score)
        reset = '\033[0m'
        
        print(f"{color}╔{'═' * 68}╗{reset}")
        print(f"{color}║{'  HONOR SCORE':^68}║{reset}")
        print(f"{color}║{f'{honor_score:.1f}':^68}║{reset}")
        print(f"{color}║{tier:^68}║{reset}")
        print(f"{color}╚{'═' * 68}╝{reset}")
        print()
        
        # Component scores
        print("┌─ COMPONENTES " + "─" * 54 + "┐")
        
        for name, score in components.items():
            label = name.upper().ljust(12)
            bar = self.draw_bar(score, width=35)
            color = self.get_color(score)
            print(f"│ {label} │ {color}{bar}{reset} {score:>5.1f}% │")
        
        print("└" + "─" * 68 + "┘")
        print()
        
        # Human-friendly feedback
        human_feedback = metrics.get('human_feedback', '')
        if human_feedback:
            print(f"💬 {human_feedback}")
        else:
            # Fallback to default message
            message = metrics.get('message', '')
            print(f"💬 {message}")
        print()
        print("Presiona Ctrl+C para detener la evaluación...")
    
    def display_final_results(self, results: Dict):
        """Display final performance summary"""
        self.clear_screen()
        
        print("=" * 70)
        print("🏆  RESUMEN FINAL  🏆".center(70))
        print("=" * 70)
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
        reset = '\033[0m'
        
        # Final score
        print(f"{color}╔{'═' * 68}╗{reset}")
        print(f"{color}║{'  HONOR SCORE FINAL':^68}║{reset}")
        print(f"{color}║{f'{honor_score:.1f}':^68}║{reset}")
        print(f"{color}║{tier:^68}║{reset}")
        print(f"{color}╚{'═' * 68}╝{reset}")
        print()
        
        # Human-friendly summary
        if human_summary:
            print(f"💬 {human_summary}")
        else:
            print(f"💬 {message}")
        print()
        
        # Comparison with history
        if comparison and comparison.get('has_history'):
            print(f"📊 {comparison.get('message', '')}")
            print()
        
        # Component breakdown
        print("┌─ DESGLOSE DE COMPONENTES " + "─" * 41 + "┐")
        for name, score in components.items():
            label = name.upper().ljust(12)
            bar = self.draw_bar(score, width=35)
            comp_color = self.get_color(score)
            print(f"│ {label} │ {comp_color}{bar}{reset} {score:>5.1f}% │")
        print("└" + "─" * 68 + "┘")
        print()
        
        # Session info
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        print("┌─ INFORMACIÓN DE SESIÓN " + "─" * 43 + "┐")
        print(f"│ Duración:             {minutes:02d}:{seconds:02d} min{' ' * 40} │")
        print(f"│ Evaluaciones totales: {progress.get('total_evaluations', 0):<43} │")
        print(f"│ Puntuación promedio:  {progress.get('average_score', 0):<43.1f} │")
        print(f"│ Tendencia:            {progress.get('trend', 'N/A'):<43} │")
        print("└" + "─" * 68 + "┘")
        print()
        
        print("✨ Cada práctica te acerca más a la maestría. ¡Sigue adelante! ✨")
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
    
    args = parser.parse_args()
    
    print()
    print("=" * 70)
    print("🎵  Bienvenido a HONORHERO  🎵".center(70))
    print("=" * 70)
    print()
    print("HonorHero es un sistema de evaluación de música centrado en el ser humano.")
    print("Captura audio en vivo y analiza:")
    print("  • Afinación (Pitch)")
    print("  • Timing y Ritmo")
    print("  • Dinámica")
    print("  • Consistencia")
    print()
    print("La performance nunca se detiene: los errores se miden, no se castigan.")
    print("Obtén un Honor Score (0-100) con niveles cualitativos:")
    print("  • Íntegro (80-100)")
    print("  • Firme (60-79)")
    print("  • Inestable (40-59)")
    print("  • Fragmentado (0-39)")
    print()
    print("Enfoque en auto-mejora, no en competencia.")
    print()
    
    # Show profile and mode selection
    profile = args.profile or config.DEFAULT_PROFILE
    mode = args.mode or config.DEFAULT_MODE
    
    profile_info = config.PROFILES[profile]
    mode_info = config.SESSION_MODES[mode]
    
    print(f"📋 Perfil seleccionado: {profile_info['name']}")
    print(f"   {profile_info['description']}")
    print()
    print(f"⏱️  Modo de sesión: {mode_info['name']}")
    print(f"   {mode_info['description']}")
    if mode_info['duration']:
        minutes = mode_info['duration'] // 60
        print(f"   Duración: {minutes} minutos")
    print()
    print("-" * 70)
    print()
    
    input("Presiona Enter para comenzar...")
    print()
    
    ui = HonorHeroUI(profile=profile, mode=mode)
    ui.run(duration=args.duration)


if __name__ == '__main__':
    main()
