"""
Demo script for Piano Roll UI
Simulates notes being played to showcase the piano roll visualization
"""

import time
import random
import traceback
from collections import deque
from piano_roll_ui import PianoRollUI
import librosa


def simulate_piano_roll_demo():
    """Simulate a piano roll demonstration without actual audio"""
    print()
    print("=" * 90)
    print("🎹  PIANO ROLL UI DEMO  🎹".center(90))
    print("=" * 90)
    print()
    print("This demo simulates notes being played to showcase the piano roll interface.")
    print("In actual use, the interface captures real audio from your microphone.")
    print()
    print("The piano roll shows:")
    print("  • Your past performance (left side)")
    print("  • Your present performance (right side)")
    print("  • Performance trends (improving, stable, or declining)")
    print()
    print("Velocity is shown with different characters: █ (forte), ▓ (mezzo), ▒ (piano), ░ (pianissimo)")
    print()
    
    input("Press Enter to start the demo...")
    print()
    
    # Create UI instance
    ui = PianoRollUI(profile='intermediate', mode='short', window_seconds=3)
    
    # Simulate a musical phrase
    # Let's play a simple C major scale up and down with varying dynamics
    scale_notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 
                   'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4']
    
    print("Simulating a C major scale performance...")
    print()
    
    start_time = time.time()
    note_index = 0
    
    # Simulate performance for 15 seconds
    while time.time() - start_time < 15:
        current_time = time.time()
        
        # Add a new note every 0.5 seconds
        if note_index < len(scale_notes) * 2:  # Play the scale twice
            note_name = scale_notes[note_index % len(scale_notes)]
            
            # Convert note to frequency
            midi_note = librosa.note_to_midi(note_name)
            frequency = librosa.midi_to_hz(midi_note)
            
            # Vary dynamics: crescendo up, diminuendo down
            position = note_index % len(scale_notes)
            if position < len(scale_notes) / 2:
                velocity = 0.4 + (position / len(scale_notes)) * 0.5
            else:
                velocity = 0.9 - ((position - len(scale_notes) / 2) / len(scale_notes)) * 0.5
            
            # Add some randomness for realism
            velocity += random.uniform(-0.1, 0.1)
            velocity = max(0.2, min(0.95, velocity))
            
            # Score improves as we progress (simulating learning)
            base_score = 60 + (note_index / (len(scale_notes) * 2)) * 30
            score = base_score + random.uniform(-5, 5)
            
            # Add note to buffer
            ui.note_buffer.append({
                'timestamp': current_time,
                'note': note_name,
                'frequency': frequency,
                'score': score,
                'velocity': velocity
            })
            
            # Add score to recent scores for trend
            ui.recent_scores.append(score)
            
            note_index += 1
        
        # Create mock metrics
        avg_score = sum(list(ui.recent_scores)[-10:]) / min(len(ui.recent_scores), 10) if ui.recent_scores else 60
        
        metrics = {
            'honor_score': avg_score,
            'tier': 'Íntegro' if avg_score >= 80 else 'Firme' if avg_score >= 60 else 'Inestable',
            'components': {
                'pitch': avg_score + random.uniform(-5, 5),
                'timing': avg_score + random.uniform(-5, 5),
                'rhythm': avg_score + random.uniform(-5, 5),
                'dynamics': avg_score + random.uniform(-5, 5),
                'consistency': avg_score + random.uniform(-5, 5)
            }
        }
        
        # Display frame
        ui.display_frame(metrics)
        
        time.sleep(0.5)
    
    # Show final summary
    print()
    print("=" * 90)
    print("Demo completed!".center(90))
    print("=" * 90)
    print()
    print("In actual use, the piano roll UI would capture your live performance")
    print("and show your notes as you play them in real-time.")
    print()
    print(f"Notes simulated: {len(ui.note_buffer)}")
    if ui.recent_scores:
        print(f"Average score: {sum(ui.recent_scores) / len(ui.recent_scores):.1f}")
        print(f"Score range: {min(ui.recent_scores):.1f} - {max(ui.recent_scores):.1f}")
    print()
    print("To use with real audio:")
    print("  python piano_roll_ui.py")
    print()


if __name__ == '__main__':
    try:
        simulate_piano_roll_demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
        print("Thank you for trying the Piano Roll UI demo!")
    except Exception as e:
        print(f"\nError during demo: {e}")
        traceback.print_exc()
