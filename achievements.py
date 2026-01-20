"""
HonorHero Achievement System
Non-competitive rewards and philosophical achievements
Focus on personal growth, not competition
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class Achievement:
    """Represents a single achievement"""
    
    def __init__(self, id: str, name: str, description: str, icon: str, category: str):
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon
        self.category = category
        self.unlocked = False
        self.unlocked_date = None
    
    def unlock(self):
        """Unlock this achievement"""
        if not self.unlocked:
            self.unlocked = True
            self.unlocked_date = datetime.now().isoformat()
            return True
        return False
    
    def to_dict(self):
        """Convert to dictionary for serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon': self.icon,
            'category': self.category,
            'unlocked': self.unlocked,
            'unlocked_date': self.unlocked_date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Achievement from dictionary"""
        achievement = cls(
            data['id'],
            data['name'],
            data['description'],
            data['icon'],
            data['category']
        )
        achievement.unlocked = data.get('unlocked', False)
        achievement.unlocked_date = data.get('unlocked_date')
        return achievement


# Define all achievements
ACHIEVEMENT_DEFINITIONS = [
    # Philosophical Achievements (focusing on journey and growth)
    Achievement(
        'persistence',
        'Persistencia',
        'Completaste 3 sesiones seguidas sin rendirte',
        '🌱',
        'filosofico'
    ),
    Achievement(
        'constancy',
        'Constancia',
        'Practicaste durante 7 días seguidos',
        '🔥',
        'filosofico'
    ),
    Achievement(
        'listening',
        'Escucha',
        'Mejoraste tu afinación en 20 puntos',
        '👂',
        'filosofico'
    ),
    Achievement(
        'vocal_courage',
        'Valentía Vocal',
        'Completaste 10 sesiones de práctica',
        '🎤',
        'filosofico'
    ),
    Achievement(
        'rhythmic_heart',
        'Corazón Rítmico',
        'Mantuviste un ritmo estable durante 5 minutos',
        '❤️',
        'filosofico'
    ),
    Achievement(
        'expression',
        'Expresión',
        'Alcanzaste excelencia en dinámica (80+)',
        '🎨',
        'filosofico'
    ),
    
    # Soft Medals (gentle recognition of progress)
    Achievement(
        'stable_pitch_5min',
        'Afinación Estable',
        'Mantuviste afinación estable por 5 minutos',
        '✨',
        'medalla'
    ),
    Achievement(
        'stable_pitch_7min',
        'Afinación Sólida',
        'Mantuviste afinación estable por 7 minutos',
        '⭐',
        'medalla'
    ),
    Achievement(
        'balanced_performer',
        'Intérprete Equilibrado',
        'Alcanzaste 70+ en todos los componentes',
        '⚖️',
        'medalla'
    ),
    Achievement(
        'integro_first',
        'Primera Integridad',
        'Alcanzaste el tier Íntegro (80+) por primera vez',
        '🏆',
        'medalla'
    ),
    Achievement(
        'integro_streak',
        'Maestría Consistente',
        'Alcanzaste Íntegro en 3 sesiones consecutivas',
        '👑',
        'medalla'
    ),
    
    # Temporal Milestones (time-based achievements)
    Achievement(
        'first_session',
        'Primer Paso',
        'Completaste tu primera sesión',
        '🚀',
        'hito'
    ),
    Achievement(
        'streak_5days',
        'Dedicación Semanal',
        'Practicaste 5 días seguidos',
        '📅',
        'hito'
    ),
    Achievement(
        'streak_30days',
        'Músico Dedicado',
        'Practicaste 30 días seguidos',
        '💎',
        'hito'
    ),
    Achievement(
        'total_10hours',
        'Viajero Musical',
        'Acumulaste 10 horas de práctica total',
        '🎵',
        'hito'
    ),
    Achievement(
        'total_50hours',
        'Explorador Sonoro',
        'Acumulaste 50 horas de práctica total',
        '🌟',
        'hito'
    ),
    Achievement(
        'improvement_journey',
        'Viaje de Mejora',
        'Mejoraste tu Honor Score en 30 puntos desde tu primera sesión',
        '📈',
        'hito'
    )
]


class AchievementSystem:
    """
    Manages achievements and tracks progress
    Non-competitive, focused on personal growth
    """
    
    def __init__(self, data_file='achievements.json'):
        self.data_file = data_file
        self.achievements = {}
        
        # Initialize achievements
        for achievement_def in ACHIEVEMENT_DEFINITIONS:
            self.achievements[achievement_def.id] = achievement_def
        
        # Load saved progress
        self.load()
    
    def load(self):
        """Load achievement progress from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for achievement_data in data.get('achievements', []):
                        achievement = Achievement.from_dict(achievement_data)
                        if achievement.id in self.achievements:
                            self.achievements[achievement.id] = achievement
            except Exception as e:
                print(f"Warning: Could not load achievements: {e}")
    
    def save(self):
        """Save achievement progress to file"""
        try:
            data = {
                'achievements': [a.to_dict() for a in self.achievements.values()],
                'last_updated': datetime.now().isoformat()
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save achievements: {e}")
    
    def check_and_unlock(self, achievement_id: str) -> bool:
        """
        Check if achievement can be unlocked and unlock it
        
        Returns:
            True if newly unlocked, False otherwise
        """
        if achievement_id in self.achievements:
            achievement = self.achievements[achievement_id]
            if achievement.unlock():
                self.save()
                return True
        return False
    
    def get_achievement(self, achievement_id: str) -> Optional[Achievement]:
        """Get achievement by ID"""
        return self.achievements.get(achievement_id)
    
    def get_unlocked_achievements(self) -> List[Achievement]:
        """Get all unlocked achievements"""
        return [a for a in self.achievements.values() if a.unlocked]
    
    def get_locked_achievements(self) -> List[Achievement]:
        """Get all locked achievements"""
        return [a for a in self.achievements.values() if not a.unlocked]
    
    def get_achievements_by_category(self, category: str) -> List[Achievement]:
        """Get all achievements in a category"""
        return [a for a in self.achievements.values() if a.category == category]
    
    def get_progress(self) -> Dict:
        """Get overall achievement progress"""
        total = len(self.achievements)
        unlocked = len(self.get_unlocked_achievements())
        
        categories = {}
        for achievement in self.achievements.values():
            if achievement.category not in categories:
                categories[achievement.category] = {'total': 0, 'unlocked': 0}
            categories[achievement.category]['total'] += 1
            if achievement.unlocked:
                categories[achievement.category]['unlocked'] += 1
        
        return {
            'total': total,
            'unlocked': unlocked,
            'percentage': (unlocked / total * 100) if total > 0 else 0,
            'categories': categories
        }
    
    def check_session_achievements(self, session_data: Dict, history_data: Dict):
        """
        Check for achievements based on session data
        
        Args:
            session_data: Current session data
            history_data: Historical session data
        
        Returns:
            List of newly unlocked achievements
        """
        newly_unlocked = []
        
        # First session - check if this achievement hasn't been unlocked yet
        if history_data.get('total_sessions', 0) >= 1:
            if self.check_and_unlock('first_session'):
                newly_unlocked.append(self.achievements['first_session'])
        
        # Vocal courage - 10 sessions
        if history_data.get('total_sessions', 0) >= 10:
            if self.check_and_unlock('vocal_courage'):
                newly_unlocked.append(self.achievements['vocal_courage'])
        
        # Streak achievements
        streak = history_data.get('streak', 0)
        if streak >= 3:
            if self.check_and_unlock('persistence'):
                newly_unlocked.append(self.achievements['persistence'])
        if streak >= 5:
            if self.check_and_unlock('streak_5days'):
                newly_unlocked.append(self.achievements['streak_5days'])
        if streak >= 7:
            if self.check_and_unlock('constancy'):
                newly_unlocked.append(self.achievements['constancy'])
        if streak >= 30:
            if self.check_and_unlock('streak_30days'):
                newly_unlocked.append(self.achievements['streak_30days'])
        
        # Time-based achievements
        total_time = history_data.get('total_time', 0)
        if total_time >= 36000:  # 10 hours
            if self.check_and_unlock('total_10hours'):
                newly_unlocked.append(self.achievements['total_10hours'])
        if total_time >= 180000:  # 50 hours
            if self.check_and_unlock('total_50hours'):
                newly_unlocked.append(self.achievements['total_50hours'])
        
        # Score-based achievements
        honor_score = session_data.get('final_honor_score', 0)
        if honor_score >= 80:
            if self.check_and_unlock('integro_first'):
                newly_unlocked.append(self.achievements['integro_first'])
        
        # Component achievements
        components = session_data.get('components', {})
        if components.get('dynamics', 0) >= 80:
            if self.check_and_unlock('expression'):
                newly_unlocked.append(self.achievements['expression'])
        
        # Balanced performer
        if all(score >= 70 for score in components.values() if score > 0):
            if self.check_and_unlock('balanced_performer'):
                newly_unlocked.append(self.achievements['balanced_performer'])
        
        # Improvement journey
        first_score = history_data.get('first_score', 0)
        if first_score > 0 and honor_score >= first_score + 30:
            if self.check_and_unlock('improvement_journey'):
                newly_unlocked.append(self.achievements['improvement_journey'])
        
        return newly_unlocked
    
    def format_achievement_notification(self, achievement: Achievement) -> str:
        """Format achievement unlock notification"""
        return f"\n{achievement.icon}  ¡Logro Desbloqueado: {achievement.name}!\n   {achievement.description}\n"
