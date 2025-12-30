"""
Dynamics Analysis Module
Analyzes volume dynamics and expression
"""

import numpy as np
from typing import List
import config


class DynamicsAnalyzer:
    """Analyzes dynamics and expressive volume control"""
    
    def __init__(self, tolerance: float = config.DYNAMICS_TOLERANCE):
        self.tolerance = tolerance  # dB
        self.amplitude_history = []
        self.db_history = []
        
    def analyze(self, audio_chunk: np.ndarray) -> dict:
        """
        Analyze dynamics from audio chunk
        
        Args:
            audio_chunk: Audio data
            
        Returns:
            Dictionary with dynamics analysis
        """
        # Calculate RMS amplitude
        rms = np.sqrt(np.mean(audio_chunk ** 2))
        
        # Convert to dB (with floor to avoid log(0))
        if rms > 1e-10:
            db = 20 * np.log10(rms)
        else:
            db = -100  # Very quiet
        
        self.amplitude_history.append(rms)
        self.db_history.append(db)
        
        # Calculate dynamic range
        if len(self.db_history) > 1:
            dynamic_range = max(self.db_history) - min(self.db_history)
        else:
            dynamic_range = 0
        
        # Score based on dynamic control
        # Good dynamics show variation but not excessive
        if 5 <= dynamic_range <= self.tolerance:
            score = 100
        elif dynamic_range < 5:
            # Too flat
            score = 60 + (dynamic_range * 8)
        else:
            # Too much variation
            excess = dynamic_range - self.tolerance
            score = max(0, 100 - (excess * 2))
        
        return {
            'amplitude': rms,
            'db': db,
            'dynamic_range': dynamic_range,
            'score': score
        }
    
    def get_average_score(self) -> float:
        """Get average dynamics score"""
        if len(self.db_history) < 2:
            return 70.0  # Default good score
        
        dynamic_range = max(self.db_history) - min(self.db_history)
        
        if 5 <= dynamic_range <= self.tolerance:
            return 100.0
        elif dynamic_range < 5:
            return 60.0 + (dynamic_range * 8)
        else:
            excess = dynamic_range - self.tolerance
            return max(0, 100 - (excess * 2))
    
    def reset(self):
        """Reset dynamics history"""
        self.amplitude_history = []
        self.db_history = []
