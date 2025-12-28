"""
Timing Analysis Module
Analyzes timing accuracy and rhythm consistency
"""

import numpy as np
from typing import List
import config


class TimingAnalyzer:
    """Analyzes timing and rhythm with tolerant thresholds"""
    
    def __init__(self, timing_tolerance: float = config.TIMING_TOLERANCE,
                 rhythm_tolerance: float = config.RHYTHM_TOLERANCE):
        self.timing_tolerance = timing_tolerance
        self.rhythm_tolerance = rhythm_tolerance
        self.onset_times = []
        self.intervals = []
        
    def detect_onset(self, audio_chunk: np.ndarray, sample_rate: int,
                     timestamp: float) -> dict:
        """
        Detect note onsets for timing analysis
        
        Args:
            audio_chunk: Audio data
            sample_rate: Sample rate in Hz
            timestamp: Current timestamp
            
        Returns:
            Dictionary with onset detection results
        """
        # Simple energy-based onset detection
        energy = np.sum(audio_chunk ** 2)
        threshold = 0.01  # Tolerant threshold
        
        is_onset = energy > threshold
        
        if is_onset and (not self.onset_times or 
                        timestamp - self.onset_times[-1] > 0.1):  # Minimum 100ms between onsets
            self.onset_times.append(timestamp)
            
            # Calculate interval if we have previous onset
            if len(self.onset_times) > 1:
                interval = self.onset_times[-1] - self.onset_times[-2]
                self.intervals.append(interval)
        
        return {
            'is_onset': is_onset,
            'energy': energy,
            'timestamp': timestamp
        }
    
    def analyze_timing(self, expected_timing: float = None) -> dict:
        """
        Analyze timing accuracy
        
        Args:
            expected_timing: Expected note timing (optional)
            
        Returns:
            Dictionary with timing analysis
        """
        if len(self.onset_times) < 2:
            return {
                'score': 50,  # Neutral score
                'average_interval': 0,
                'timing_variance': 0
            }
        
        avg_interval = np.mean(self.intervals) if self.intervals else 0
        timing_variance = np.std(self.intervals) if len(self.intervals) > 1 else 0
        
        # Calculate score based on consistency
        # Low variance = high score
        if timing_variance <= self.timing_tolerance:
            score = 100
        else:
            excess = timing_variance - self.timing_tolerance
            score = max(0, 100 - (excess * 100))
        
        return {
            'score': score,
            'average_interval': avg_interval,
            'timing_variance': timing_variance
        }
    
    def analyze_rhythm(self) -> dict:
        """
        Analyze rhythm consistency
        
        Returns:
            Dictionary with rhythm analysis
        """
        if len(self.intervals) < 2:
            return {
                'score': 50,
                'consistency': 0.5,
                'pattern_strength': 0
            }
        
        # Calculate rhythm consistency
        intervals = np.array(self.intervals)
        mean_interval = np.mean(intervals)
        
        # Coefficient of variation for consistency
        if mean_interval > 0:
            cv = np.std(intervals) / mean_interval
            consistency = max(0, 1 - cv)
        else:
            consistency = 0.5
        
        # Score based on consistency
        if cv <= self.rhythm_tolerance:
            score = 100
        else:
            excess = cv - self.rhythm_tolerance
            score = max(0, 100 - (excess * 150))
        
        return {
            'score': score,
            'consistency': consistency,
            'pattern_strength': consistency
        }
    
    def reset(self):
        """Reset timing history"""
        self.onset_times = []
        self.intervals = []
