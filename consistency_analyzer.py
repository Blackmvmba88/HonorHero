"""
Consistency Analysis Module
Measures overall performance consistency over time
"""

import numpy as np
from typing import List, Dict
import config


class ConsistencyAnalyzer:
    """Analyzes consistency across all performance metrics"""
    
    def __init__(self, threshold: float = config.CONSISTENCY_THRESHOLD):
        self.threshold = threshold
        self.metric_history = {
            'pitch': [],
            'timing': [],
            'rhythm': [],
            'dynamics': []
        }
        
    def add_metrics(self, pitch_score: float, timing_score: float,
                   rhythm_score: float, dynamics_score: float):
        """
        Add metrics to history
        
        Args:
            pitch_score: Pitch score (0-100)
            timing_score: Timing score (0-100)
            rhythm_score: Rhythm score (0-100)
            dynamics_score: Dynamics score (0-100)
        """
        self.metric_history['pitch'].append(pitch_score)
        self.metric_history['timing'].append(timing_score)
        self.metric_history['rhythm'].append(rhythm_score)
        self.metric_history['dynamics'].append(dynamics_score)
    
    def analyze(self) -> dict:
        """
        Analyze consistency across all metrics
        
        Returns:
            Dictionary with consistency analysis
        """
        if not self.metric_history['pitch']:
            return {
                'score': 70,  # Default good score
                'overall_consistency': self.threshold,
                'metric_consistency': {}
            }
        
        metric_consistencies = {}
        total_consistency = 0
        
        for metric_name, values in self.metric_history.items():
            if len(values) < 2:
                consistency = 1.0
            else:
                # Calculate coefficient of variation
                mean_val = np.mean(values)
                if mean_val > 0:
                    cv = np.std(values) / mean_val
                    consistency = max(0, 1 - cv)
                else:
                    consistency = 0.5
            
            metric_consistencies[metric_name] = consistency
            total_consistency += consistency
        
        # Average consistency
        overall_consistency = total_consistency / len(self.metric_history)
        
        # Score based on consistency
        if overall_consistency >= self.threshold:
            score = 100
        else:
            # Score decreases below threshold
            score = (overall_consistency / self.threshold) * 100
        
        return {
            'score': score,
            'overall_consistency': overall_consistency,
            'metric_consistency': metric_consistencies
        }
    
    def reset(self):
        """Reset consistency history"""
        for metric in self.metric_history:
            self.metric_history[metric] = []
