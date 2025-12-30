"""
HonorHero Simple Console UI
Expressive UI focused on self-improvement, not competition
"""

import time
import sys
from honorhero import HonorHero
from typing import Dict


class HonorHeroUI:
    """Simple expressive console UI for HonorHero"""
    
    def __init__(self):
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
            duration: Performance duration in seconds (None = until interrupted)
        """
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
        help='Performance duration in seconds (default: until interrupted)'
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
    print("-" * 70)
    print()
    
    input("Presiona Enter para comenzar...")
    print()
    
    ui = HonorHeroUI()
    ui.run(duration=args.duration)


if __name__ == '__main__':
    main()
