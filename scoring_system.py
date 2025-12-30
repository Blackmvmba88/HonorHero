"""
Scoring System Module
Calculates Honor Score and assigns qualitative tiers
"""

import config
from typing import Dict, Tuple


class ScoringSystem:
    """Calculates Honor Score (0-100) with qualitative tiers"""
    
    def __init__(self, weights: dict = None):
        self.weights = weights if weights else config.WEIGHTS
        self.score_history = []
        
    def calculate_honor_score(self, metrics: Dict[str, float]) -> Dict:
        """
        Calculate Honor Score from component metrics
        
        Args:
            metrics: Dictionary with component scores
                    - pitch: 0-100
                    - timing: 0-100
                    - rhythm: 0-100
                    - dynamics: 0-100
                    - consistency: 0-100
        
        Returns:
            Dictionary with Honor Score and tier information
        """
        # Calculate weighted average
        honor_score = 0
        for component, weight in self.weights.items():
            if component in metrics:
                honor_score += metrics[component] * weight
        
        # Ensure score is in valid range
        honor_score = max(0, min(100, honor_score))
        
        # Determine tier
        tier = self._get_tier(honor_score)
        
        # Store in history
        self.score_history.append({
            'score': honor_score,
            'tier': tier,
            'components': metrics.copy()
        })
        
        return {
            'honor_score': honor_score,
            'tier': tier,
            'components': metrics,
            'message': self._get_message(tier)
        }
    
    def _get_tier(self, score: float) -> str:
        """Get qualitative tier for score"""
        for tier_name, (min_score, max_score) in config.SCORE_TIERS.items():
            if min_score <= score <= max_score:
                return tier_name
        return 'Fragmentado'  # Default
    
    def _get_message(self, tier: str) -> str:
        """Get encouraging message for tier"""
        messages = {
            'Íntegro': '¡Excelente! Tu interpretación muestra integridad y maestría.',
            'Firme': '¡Muy bien! Tu performance es sólida y consistente.',
            'Inestable': 'Buen intento. Sigue practicando para mayor estabilidad.',
            'Fragmentado': 'Continúa practicando. Cada intento te acerca más.'
        }
        return messages.get(tier, 'Sigue adelante.')
    
    def get_average_score(self) -> float:
        """Get average Honor Score from history"""
        if not self.score_history:
            return 0.0
        
        scores = [entry['score'] for entry in self.score_history]
        return sum(scores) / len(scores)
    
    def get_progress_summary(self) -> Dict:
        """Get summary of progress over time"""
        if not self.score_history:
            return {
                'total_evaluations': 0,
                'average_score': 0,
                'trend': 'N/A'
            }
        
        total = len(self.score_history)
        avg_score = self.get_average_score()
        
        # Calculate trend (comparing first half to second half)
        if total >= 4:
            mid = total // 2
            first_half_avg = sum(e['score'] for e in self.score_history[:mid]) / mid
            second_half_avg = sum(e['score'] for e in self.score_history[mid:]) / (total - mid)
            
            if second_half_avg > first_half_avg + 5:
                trend = 'Mejorando'
            elif second_half_avg < first_half_avg - 5:
                trend = 'Descendiendo'
            else:
                trend = 'Estable'
        else:
            trend = 'Insuficiente data'
        
        return {
            'total_evaluations': total,
            'average_score': avg_score,
            'current_tier': self.score_history[-1]['tier'] if total > 0 else 'N/A',
            'trend': trend
        }
    
    def reset(self):
        """Reset score history"""
        self.score_history = []
