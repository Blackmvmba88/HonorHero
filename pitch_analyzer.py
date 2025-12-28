"""
Pitch Analysis Module
Analyzes pitch accuracy and deviation from expected notes
"""

import numpy as np
import librosa
from typing import Tuple, Optional
import config


class PitchAnalyzer:
    """Analyzes pitch accuracy with tolerant thresholds"""
    
    def __init__(self, tolerance: float = config.PITCH_TOLERANCE):
        self.tolerance = tolerance  # cents
        self.pitch_history = []
        
    def analyze(self, audio_chunk: np.ndarray, sample_rate: int) -> dict:
        """
        Analyze pitch from audio chunk
        
        Args:
            audio_chunk: Audio data
            sample_rate: Sample rate in Hz
            
        Returns:
            Dictionary with pitch analysis results
        """
        # Extract pitch using librosa
        pitches, magnitudes = librosa.piptrack(
            y=audio_chunk,
            sr=sample_rate,
            fmin=librosa.note_to_hz('C2'),
            fmax=librosa.note_to_hz('C7')
        )
        
        # Get the most prominent pitch
        pitch_values = []
        for t in range(pitches.shape[1]):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            if pitch > 0:
                pitch_values.append(pitch)
        
        if not pitch_values:
            return {
                'detected': False,
                'frequency': 0,
                'note': None,
                'deviation': 0,
                'score': 50  # Neutral score when no pitch detected
            }
        
        # Calculate average pitch
        avg_pitch = np.mean(pitch_values)
        
        # Convert to note
        note_number = librosa.hz_to_midi(avg_pitch)
        closest_note = round(note_number)
        note_name = librosa.midi_to_note(closest_note)
        
        # Calculate deviation in cents
        deviation = 100 * (note_number - closest_note)
        
        # Store in history
        self.pitch_history.append({
            'frequency': avg_pitch,
            'deviation': deviation
        })
        
        # Calculate score (0-100) based on deviation
        # Within tolerance = 100, outside tolerance decreases score
        if abs(deviation) <= self.tolerance:
            score = 100
        else:
            # Score decreases as deviation increases beyond tolerance
            excess = abs(deviation) - self.tolerance
            score = max(0, 100 - (excess * 2))  # 2 points per cent deviation
        
        return {
            'detected': True,
            'frequency': avg_pitch,
            'note': note_name,
            'deviation': deviation,
            'score': score
        }
    
    def get_average_score(self) -> float:
        """Get average pitch score from history"""
        if not self.pitch_history:
            return 50.0
        
        scores = []
        for entry in self.pitch_history:
            dev = abs(entry['deviation'])
            if dev <= self.tolerance:
                score = 100
            else:
                excess = dev - self.tolerance
                score = max(0, 100 - (excess * 2))
            scores.append(score)
        
        return np.mean(scores)
    
    def reset(self):
        """Reset pitch history"""
        self.pitch_history = []
