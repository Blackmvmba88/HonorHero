"""
HonorHero Piano Roll Console UI
A temporal mirror of musical performance - showing the journey, not judging it
"""

import time
import sys
from collections import deque
from typing import Dict, List, Tuple
import librosa
from honorhero import HonorHero
import config


class PianoRollUI:
    """
    Console-based piano-roll visualization
    
    Shows a temporal window of the musician's performance:
    - Past: What happened 3 seconds ago
    - Present: What's happening now
    - Trend: Where the performance is moving
    """
    
    def __init__(self, profile: str = None, mode: str = None, window_seconds: int = 3):
        self.profile_name = profile or config.DEFAULT_PROFILE
        self.mode_name = mode or config.DEFAULT_MODE
        self.window_seconds = window_seconds
        
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
        
        # Temporal buffer for notes
        # Each entry: {'timestamp': float, 'note': str, 'frequency': float, 'score': float, 'velocity': float}
        self.note_buffer = deque(maxlen=100)  # Keep last 100 notes
        
        # Piano roll display configuration
        self.octave_range = (2, 6)  # C2 to C6
        self.notes_per_octave = 12
        self.total_rows = (self.octave_range[1] - self.octave_range[0] + 1) * self.notes_per_octave
        self.display_width = 80  # Width of the piano roll
        
        # Note names for display
        self.note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        # Performance metrics for trend display
        self.recent_scores = deque(maxlen=30)  # Last 30 evaluations
        self.last_update_time = 0
        
    def clear_screen(self):
        """Clear console screen"""
        print('\033[2J\033[H', end='')
        
    def get_note_row(self, note_name: str) -> int:
        """Convert note name to row index in the piano roll"""
        try:
            # Parse note (e.g., "C4" -> note="C", octave=4)
            note = note_name[:-1]
            octave = int(note_name[-1])
            
            if octave < self.octave_range[0] or octave > self.octave_range[1]:
                return -1  # Out of range
            
            note_index = self.note_names.index(note)
            row = (self.octave_range[1] - octave) * self.notes_per_octave + (11 - note_index)
            return row
        except (ValueError, IndexError):
            return -1
    
    def get_color_for_score(self, score: float) -> str:
        """Get ANSI color code based on score"""
        if score >= 80:
            return '\033[92m'  # Green - Íntegro
        elif score >= 60:
            return '\033[94m'  # Blue - Firme
        elif score >= 40:
            return '\033[93m'  # Yellow - Inestable
        else:
            return '\033[91m'  # Red - Fragmentado
    
    def get_velocity_char(self, velocity: float) -> str:
        """Get character representing velocity/dynamics"""
        if velocity >= 0.8:
            return '█'
        elif velocity >= 0.6:
            return '▓'
        elif velocity >= 0.4:
            return '▒'
        else:
            return '░'
    
    def draw_piano_roll(self, current_time: float):
        """Draw the piano roll visualization"""
        # Create empty piano roll grid
        grid = [[' ' for _ in range(self.display_width)] for _ in range(self.total_rows)]
        
        # Time window (past window_seconds)
        time_start = current_time - self.window_seconds
        time_end = current_time
        time_range = time_end - time_start
        
        # Plot notes in the buffer
        for note_entry in self.note_buffer:
            timestamp = note_entry['timestamp']
            if timestamp < time_start or timestamp > time_end:
                continue
            
            # Calculate x position (time axis)
            x = int(((timestamp - time_start) / time_range) * (self.display_width - 1))
            x = max(0, min(x, self.display_width - 1))
            
            # Calculate y position (pitch axis)
            y = self.get_note_row(note_entry['note'])
            if y < 0 or y >= self.total_rows:
                continue
            
            # Draw note with character representing velocity
            char = self.get_velocity_char(note_entry.get('velocity', 0.5))
            grid[y][x] = char
        
        # Convert grid to colored output
        lines = []
        for row_idx, row in enumerate(grid):
            # Get note name for this row
            octave = self.octave_range[1] - (row_idx // self.notes_per_octave)
            note_idx = 11 - (row_idx % self.notes_per_octave)
            note_name = f"{self.note_names[note_idx]}{octave}"
            
            # Build row string with colors
            row_str = f"{note_name:>4} │"
            for char in row:
                if char != ' ':
                    # Color based on recent average score
                    avg_score = sum(self.recent_scores) / len(self.recent_scores) if self.recent_scores else 50
                    color = self.get_color_for_score(avg_score)
                    row_str += f"{color}{char}\033[0m"
                else:
                    row_str += char
            row_str += "│"
            lines.append(row_str)
        
        return lines
    
    def draw_trend_indicator(self) -> str:
        """Draw trend indicator showing performance direction"""
        if len(self.recent_scores) < 3:
            return "Trend: ━━ Gathering data..."
        
        # Calculate trend (simple linear regression)
        scores = list(self.recent_scores)
        n = len(scores)
        x = list(range(n))
        
        x_mean = sum(x) / n
        y_mean = sum(scores) / n
        
        numerator = sum((x[i] - x_mean) * (scores[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
        
        if denominator == 0:
            slope = 0
        else:
            slope = numerator / denominator
        
        # Visualize trend
        if slope > 1:
            trend = "↗↗ Mejorando rápidamente"
            color = '\033[92m'
        elif slope > 0.3:
            trend = "↗ Mejorando"
            color = '\033[94m'
        elif slope > -0.3:
            trend = "→ Estable"
            color = '\033[93m'
        elif slope > -1:
            trend = "↘ Bajando"
            color = '\033[93m'
        else:
            trend = "↘↘ Bajando rápidamente"
            color = '\033[91m'
        
        return f"{color}Tendencia: {trend}\033[0m"
    
    def display_frame(self, metrics: Dict):
        """Display a frame of the piano roll UI"""
        current_time = time.time()
        
        # Throttle updates
        if current_time - self.last_update_time < 0.1:  # 10 FPS max
            return
        
        self.last_update_time = current_time
        
        # Clear screen
        self.clear_screen()
        
        # Header
        print("═" * 90)
        print("🎹  HONORHERO PIANO ROLL  🎹".center(90))
        print("Espejo temporal de tu interpretación".center(90))
        print("═" * 90)
        print(f"Perfil: {self.profile['name']} | Modo: {self.mode['name']}".center(90))
        print()
        
        # Piano roll visualization
        print("┌" + "─" * 4 + "┬" + "─" * 80 + "┐")
        print(f"│{'NOTA':^4}│{'← PASADO':^30}{'PRESENTE →':^50}│")
        print("├" + "─" * 4 + "┼" + "─" * 80 + "┤")
        
        # Draw the piano roll
        roll_lines = self.draw_piano_roll(current_time)
        for line in roll_lines:
            print(line)
        
        print("└" + "─" * 4 + "┴" + "─" * 80 + "┘")
        print()
        
        # Current metrics
        honor_score = metrics.get('honor_score', 0)
        tier = metrics.get('tier', 'N/A')
        components = metrics.get('components', {})
        
        # Score display
        color = self.get_color_for_score(honor_score)
        print(f"{color}╔{'═' * 88}╗\033[0m")
        print(f"{color}║{f'HONOR SCORE: {honor_score:.1f} - {tier}':^88}║\033[0m")
        print(f"{color}╚{'═' * 88}╝\033[0m")
        print()
        
        # Trend indicator
        print(self.draw_trend_indicator())
        print()
        
        # Mini component display
        comp_str = "  ".join([f"{name.upper()}: {score:.0f}" for name, score in components.items()])
        print(f"📊 {comp_str}")
        print()
        
        # Legend
        print("Leyenda: █ fuerte  ▓ medio  ▒ suave  ░ muy suave")
        print()
        print("Presiona Ctrl+C para detener...")
        
        # Store score for trend calculation
        self.recent_scores.append(honor_score)
    
    def on_update(self, metrics: Dict):
        """Callback for real-time updates from HonorHero engine"""
        # Extract note information from the pitch analyzer
        # This is called by the engine with current metrics
        current_time = time.time()
        
        # Get pitch information if available
        components = metrics.get('components', {})
        pitch_score = components.get('pitch', 50)
        
        # Try to get note from engine's pitch analyzer
        if hasattr(self.engine.pitch_analyzer, 'pitch_history') and self.engine.pitch_analyzer.pitch_history:
            recent_pitch = self.engine.pitch_analyzer.pitch_history[-1]
            frequency = recent_pitch.get('frequency', 0)
            
            if frequency > 0:
                # Convert frequency to note
                try:
                    note_number = librosa.hz_to_midi(frequency)
                    closest_note = round(note_number)
                    note_name = librosa.midi_to_note(closest_note)
                    
                    # Get velocity from dynamics
                    velocity = components.get('dynamics', 50) / 100.0
                    
                    # Add to buffer
                    self.note_buffer.append({
                        'timestamp': current_time,
                        'note': note_name,
                        'frequency': frequency,
                        'score': pitch_score,
                        'velocity': velocity
                    })
                except:
                    pass
        
        # Display the frame
        self.display_frame(metrics)
    
    def display_final_results(self, results: Dict):
        """Display final performance summary"""
        self.clear_screen()
        
        print("=" * 90)
        print("🏆  RESUMEN FINAL  🏆".center(90))
        print("=" * 90)
        print()
        
        honor_score = results.get('final_honor_score', 0)
        tier = results.get('tier', 'N/A')
        message = results.get('message', '')
        human_summary = results.get('human_summary', '')
        components = results.get('components', {})
        duration = results.get('duration', 0)
        
        color = self.get_color_for_score(honor_score)
        
        # Final score
        print(f"{color}╔{'═' * 88}╗\033[0m")
        print(f"{color}║{'HONOR SCORE FINAL':^88}║\033[0m")
        print(f"{color}║{f'{honor_score:.1f}':^88}║\033[0m")
        print(f"{color}║{tier:^88}║\033[0m")
        print(f"{color}╚{'═' * 88}╝\033[0m")
        print()
        
        # Human-friendly summary
        if human_summary:
            print(f"💬 {human_summary}")
        else:
            print(f"💬 {message}")
        print()
        
        # Component breakdown
        print("┌─ COMPONENTES " + "─" * 73 + "┐")
        for name, score in components.items():
            label = name.upper().ljust(15)
            bar_width = 50
            filled = int((score / 100) * bar_width)
            bar = '█' * filled + '░' * (bar_width - filled)
            comp_color = self.get_color_for_score(score)
            print(f"│ {label} │ {comp_color}{bar}\033[0m {score:>5.1f}% │")
        print("└" + "─" * 88 + "┘")
        print()
        
        # Session info
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        print(f"⏱️  Duración: {minutes:02d}:{seconds:02d}")
        print(f"🎵 Notas tocadas: {len(self.note_buffer)}")
        print()
        
        print("✨ La música es el viaje, no el destino. ¡Sigue explorando! ✨")
        print()
    
    def run(self, duration: int = None):
        """
        Run HonorHero with piano roll UI
        
        Args:
            duration: Performance duration in seconds (None = use mode default or until interrupted)
        """
        # Use mode duration if not explicitly provided
        if duration is None:
            duration = self.mode['duration']
        
        try:
            # Start engine with our callback
            self.engine.start_performance(self.on_update)
            
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
    """Main entry point for piano roll UI"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='HonorHero Piano Roll - Temporal mirror of your musical performance'
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
        help='User profile: beginner | intermediate | advanced | therapy'
    )
    parser.add_argument(
        '--mode',
        type=str,
        choices=['short', 'focus', 'free'],
        default=None,
        help='Session mode: short (3 min) | focus (10 min) | free (sin límite)'
    )
    parser.add_argument(
        '--window',
        type=int,
        default=3,
        help='Time window in seconds to display (default: 3)'
    )
    
    args = parser.parse_args()
    
    print()
    print("=" * 90)
    print("🎹  Bienvenido a HONORHERO PIANO ROLL  🎹".center(90))
    print("=" * 90)
    print()
    print("Un espejo temporal de tu interpretación musical.")
    print("Ver tu música fluir en tiempo real - sin juicios, solo reflexión.")
    print()
    print("El piano roll muestra:")
    print("  • Tu pasado reciente (últimos 3 segundos)")
    print("  • Tu presente (lo que estás tocando ahora)")
    print("  • Tu tendencia (hacia dónde te mueves)")
    print()
    print("Cada nota es un paso en tu viaje musical. 🎶")
    print()
    
    # Show profile and mode selection
    profile = args.profile or config.DEFAULT_PROFILE
    mode = args.mode or config.DEFAULT_MODE
    
    profile_info = config.PROFILES[profile]
    mode_info = config.SESSION_MODES[mode]
    
    print(f"📋 Perfil: {profile_info['name']}")
    print(f"   {profile_info['description']}")
    print()
    print(f"⏱️  Modo: {mode_info['name']}")
    print(f"   {mode_info['description']}")
    if mode_info['duration']:
        minutes = mode_info['duration'] // 60
        print(f"   Duración: {minutes} minutos")
    print()
    print("-" * 90)
    print()
    
    input("Presiona Enter para comenzar...")
    print()
    
    ui = PianoRollUI(profile=profile, mode=mode, window_seconds=args.window)
    ui.run(duration=args.duration)


if __name__ == '__main__':
    main()
