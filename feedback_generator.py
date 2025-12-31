"""
Human-Friendly Feedback Module
Generates natural language feedback based on performance metrics
"""

import random
from typing import Dict, List


class FeedbackGenerator:
    """
    Generates encouraging, human-friendly feedback messages
    
    Converts numbers into natural language that feels like a supportive coach.
    """
    
    def __init__(self):
        self.component_names = {
            'pitch': 'afinación',
            'timing': 'timing',
            'rhythm': 'ritmo',
            'dynamics': 'dinámica',
            'consistency': 'consistencia'
        }
    
    def generate_realtime_feedback(self, metrics: Dict, 
                                   previous_metrics: Dict = None) -> str:
        """
        Generate real-time natural language feedback
        
        Args:
            metrics: Current metrics dictionary
            previous_metrics: Previous metrics for comparison
        
        Returns:
            Natural language feedback string
        """
        honor_score = metrics.get('honor_score', 0)
        components = metrics.get('components', {})
        
        # Base message on tier
        tier = metrics.get('tier', '')
        base_messages = self._get_tier_base_messages(tier)
        base = random.choice(base_messages)
        
        # Add component-specific insights
        insights = []
        
        # Find strongest and weakest components
        if components:
            sorted_components = sorted(components.items(), key=lambda x: x[1], reverse=True)
            strongest = sorted_components[0]
            weakest = sorted_components[-1]
            
            # Only comment if there's significant difference
            if strongest[1] - weakest[1] > 15:
                strong_name = self.component_names.get(strongest[0], strongest[0])
                weak_name = self.component_names.get(weakest[0], weakest[0])
                
                insights.append(
                    f"Tu {strong_name} está sólida, pero {weak_name} necesita atención"
                )
        
        # Compare with previous if available
        if previous_metrics and 'components' in previous_metrics:
            changes = self._analyze_changes(components, previous_metrics['components'])
            if changes:
                insights.append(changes)
        
        # Combine base with insights
        if insights:
            return f"{base}. {' y '.join(insights)}."
        else:
            return f"{base}."
    
    def generate_component_feedback(self, component: str, 
                                   score: float, 
                                   previous_score: float = None) -> str:
        """
        Generate feedback for a specific component
        
        Args:
            component: Component name
            score: Current score
            previous_score: Previous score for comparison
        
        Returns:
            Component-specific feedback
        """
        comp_name = self.component_names.get(component, component)
        
        # Score-based feedback
        if score >= 85:
            messages = [
                f"Excelente {comp_name}",
                f"Tu {comp_name} está impecable",
                f"Dominas la {comp_name}"
            ]
        elif score >= 70:
            messages = [
                f"Buena {comp_name}",
                f"Tu {comp_name} va bien",
                f"{comp_name.capitalize()} sólida"
            ]
        elif score >= 50:
            messages = [
                f"{comp_name.capitalize()} irregular",
                f"Trabaja más tu {comp_name}",
                f"Tu {comp_name} puede mejorar"
            ]
        else:
            messages = [
                f"{comp_name.capitalize()} necesita práctica",
                f"Enfócate en {comp_name}",
                f"Dedica tiempo a {comp_name}"
            ]
        
        base = random.choice(messages)
        
        # Add comparison if available (showing actual point difference)
        if previous_score is not None:
            diff = score - previous_score
            if diff > 5:
                base += f" (↑ +{diff:.0f} puntos)"
            elif diff < -5:
                base += f" (↓ {diff:.0f} puntos)"
        
        return base
    
    def generate_session_summary(self, results: Dict, 
                                comparison: Dict = None) -> str:
        """
        Generate natural language summary for end of session
        
        Args:
            results: Final session results
            comparison: Comparison with previous sessions
        
        Returns:
            Summary message
        """
        honor_score = results.get('final_honor_score', 0)
        tier = results.get('tier', '')
        
        # Opening
        if honor_score >= 80:
            opening = "¡Sesión brillante! "
        elif honor_score >= 60:
            opening = "Buena práctica. "
        elif honor_score >= 40:
            opening = "Sesión con altibajos. "
        else:
            opening = "Sesión desafiante. "
        
        # Tier description
        tier_msg = self._get_tier_description(tier)
        
        # Comparison with history
        comparison_msg = ""
        if comparison and comparison.get('has_history'):
            score_diff = comparison.get('score_difference', 0)
            if score_diff > 10:
                comparison_msg = f" Mejoraste significativamente (+{score_diff:.1f})."
            elif score_diff > 3:
                comparison_msg = f" Progresaste un poco (+{score_diff:.1f})."
            elif score_diff < -10:
                comparison_msg = f" Bajaste algo, pero es temporal ({score_diff:.1f})."
            elif score_diff < -3:
                comparison_msg = f" Descendiste levemente ({score_diff:.1f})."
            else:
                comparison_msg = " Te mantienes estable."
        
        # Component advice
        components = results.get('components', {})
        advice = ""
        if components:
            weakest = min(components.items(), key=lambda x: x[1])
            if weakest[1] < 60:
                weak_name = self.component_names.get(weakest[0], weakest[0])
                advice = f" Próxima sesión enfócate en {weak_name}."
        
        return opening + tier_msg + comparison_msg + advice
    
    def _get_tier_base_messages(self, tier: str) -> List[str]:
        """Get base messages for a tier"""
        messages = {
            'Íntegro': [
                "¡Excelente control!",
                "Performance integrada",
                "Tocas con maestría",
                "Muy sólido"
            ],
            'Firme': [
                "Buen control general",
                "Performance estable",
                "Vas bien",
                "Mantén el rumbo"
            ],
            'Inestable': [
                "Hay inconsistencias",
                "Control irregular",
                "Trabaja la estabilidad",
                "Un poco disperso"
            ],
            'Fragmentado': [
                "Performance fragmentada",
                "Necesita más práctica",
                "Sigue trabajando",
                "Cada sesión cuenta"
            ]
        }
        return messages.get(tier, ["Sigue adelante"])
    
    def _get_tier_description(self, tier: str) -> str:
        """Get descriptive text for tier"""
        descriptions = {
            'Íntegro': "Tu interpretación muestra integridad y cohesión.",
            'Firme': "Tu performance es sólida y consistente.",
            'Inestable': "Hay potencial, pero necesitas más estabilidad.",
            'Fragmentado': "Continúa practicando para integrar todo."
        }
        return descriptions.get(tier, "")
    
    def _analyze_changes(self, current: Dict, previous: Dict) -> str:
        """Analyze changes between current and previous components"""
        changes = []
        
        for comp, score in current.items():
            if comp in previous:
                diff = score - previous[comp]
                comp_name = self.component_names.get(comp, comp)
                
                if diff > 10:
                    changes.append(f"tu {comp_name} mejoró mucho")
                elif diff < -10:
                    changes.append(f"tu {comp_name} bajó")
        
        if changes:
            if len(changes) == 1:
                return changes[0]
            else:
                return ", ".join(changes[:-1]) + f" pero {changes[-1]}"
        
        return ""
    
    def generate_achievement_message(self, achievement: str) -> str:
        """Generate celebratory message for achievements"""
        messages = {
            'first_integro': "🎉 ¡Primera vez en nivel Íntegro! ¡Celebra este logro!",
            'streak_7': "🔥 ¡7 días seguidos practicando! La consistencia es la clave.",
            'streak_30': "⭐ ¡30 días de práctica! Esto es dedicación real.",
            'improvement_20': "📈 ¡Mejoraste 20 puntos! Tu trabajo está dando frutos.",
            'all_above_70': "💪 Todos los componentes sobre 70. ¡Balance perfecto!",
            'perfect_pitch': "🎵 Afinación perfecta en esta sesión. ¡Increíble oído!",
            'perfect_rhythm': "⏱️ Ritmo impecable. Tienes el tempo en la sangre.",
        }
        return messages.get(achievement, "🌟 ¡Gran logro!")
