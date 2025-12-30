"""
Session History Module
Tracks and persists practice sessions for progress tracking
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path


class SessionHistory:
    """
    Manages practice session history and persistence
    
    Sessions are stored locally as JSON for privacy and simplicity.
    """
    
    def __init__(self, storage_path: str = None):
        """
        Initialize session history manager
        
        Args:
            storage_path: Path to JSON storage file (default: ~/.honorhero/sessions.json)
        """
        if storage_path is None:
            home = Path.home()
            storage_dir = home / '.honorhero'
            storage_dir.mkdir(exist_ok=True)
            storage_path = storage_dir / 'sessions.json'
        
        self.storage_path = Path(storage_path)
        self.sessions = self._load_sessions()
    
    def _load_sessions(self) -> List[Dict]:
        """Load sessions from JSON file"""
        if not self.storage_path.exists():
            return []
        
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    
    def _save_sessions(self):
        """Save sessions to JSON file"""
        try:
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(self.sessions, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Warning: Could not save session history: {e}")
    
    def add_session(self, session_data: Dict):
        """
        Add a new practice session
        
        Args:
            session_data: Dictionary containing session information
                Required keys: final_honor_score, tier, components
                Optional keys: duration, notes
        """
        session = {
            'timestamp': datetime.now().isoformat(),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'honor_score': session_data.get('final_honor_score', 0),
            'tier': session_data.get('tier', 'N/A'),
            'components': session_data.get('components', {}),
            'duration': session_data.get('duration', 0),
            'notes': session_data.get('notes', '')
        }
        
        self.sessions.append(session)
        self._save_sessions()
    
    def get_recent_sessions(self, count: int = 10) -> List[Dict]:
        """Get most recent sessions"""
        return self.sessions[-count:] if self.sessions else []
    
    def get_sessions_by_date(self, date: str) -> List[Dict]:
        """
        Get all sessions from a specific date
        
        Args:
            date: Date string in format 'YYYY-MM-DD'
        """
        return [s for s in self.sessions if s.get('date') == date]
    
    def get_all_sessions(self) -> List[Dict]:
        """Get all sessions"""
        return self.sessions
    
    def get_statistics(self) -> Dict:
        """
        Calculate overall statistics
        
        Returns:
            Dictionary with statistics
        """
        if not self.sessions:
            return {
                'total_sessions': 0,
                'total_practice_time': 0,
                'average_score': 0,
                'highest_score': 0,
                'lowest_score': 0,
                'current_streak': 0
            }
        
        scores = [s['honor_score'] for s in self.sessions]
        total_time = sum(s.get('duration', 0) for s in self.sessions)
        
        # Calculate streak
        streak = self._calculate_streak()
        
        return {
            'total_sessions': len(self.sessions),
            'total_practice_time': total_time,
            'average_score': sum(scores) / len(scores),
            'highest_score': max(scores),
            'lowest_score': min(scores),
            'current_streak': streak,
            'most_common_tier': self._get_most_common_tier()
        }
    
    def _calculate_streak(self) -> int:
        """Calculate current practice streak (consecutive days)"""
        if not self.sessions:
            return 0
        
        # Get unique dates
        dates = sorted(set(s['date'] for s in self.sessions), reverse=True)
        
        if not dates:
            return 0
        
        # Check if practiced today or yesterday
        today = datetime.now().date()
        last_practice = datetime.fromisoformat(dates[0]).date()
        
        days_diff = (today - last_practice).days
        if days_diff > 1:
            return 0
        
        # Count consecutive days
        streak = 1
        for i in range(len(dates) - 1):
            current = datetime.fromisoformat(dates[i]).date()
            next_date = datetime.fromisoformat(dates[i + 1]).date()
            
            if (current - next_date).days == 1:
                streak += 1
            else:
                break
        
        return streak
    
    def _get_most_common_tier(self) -> str:
        """Get the most frequently achieved tier"""
        if not self.sessions:
            return 'N/A'
        
        tiers = [s['tier'] for s in self.sessions]
        return max(set(tiers), key=tiers.count)
    
    def compare_with_previous(self, current_score: float, 
                             current_components: Dict) -> Dict:
        """
        Compare current session with previous sessions
        
        Args:
            current_score: Current Honor Score
            current_components: Current component scores
        
        Returns:
            Dictionary with comparison data
        """
        if len(self.sessions) < 1:
            return {
                'has_history': False,
                'message': '¡Primera sesión! Establece tu línea base.'
            }
        
        # Get last session
        last_session = self.sessions[-1]
        last_score = last_session['honor_score']
        score_diff = current_score - last_score
        
        # Get average of recent sessions
        recent = self.get_recent_sessions(5)
        avg_recent = sum(s['honor_score'] for s in recent) / len(recent)
        
        # Find improved components
        improved = []
        declined = []
        
        if 'components' in last_session:
            for comp, score in current_components.items():
                if comp in last_session['components']:
                    diff = score - last_session['components'][comp]
                    if diff > 5:
                        improved.append(comp)
                    elif diff < -5:
                        declined.append(comp)
        
        # Generate message
        if score_diff > 5:
            message = f"¡Mejoraste! +{score_diff:.1f} puntos desde la última sesión."
        elif score_diff < -5:
            message = f"Bajaste un poco ({score_diff:.1f}), pero es parte del proceso."
        else:
            message = "Mantuviste tu nivel. La consistencia es clave."
        
        if improved:
            message += f" Destacas en: {', '.join(improved)}."
        if declined:
            message += f" Practica más: {', '.join(declined)}."
        
        return {
            'has_history': True,
            'last_score': last_score,
            'score_difference': score_diff,
            'average_recent': avg_recent,
            'improved_components': improved,
            'declined_components': declined,
            'message': message
        }
    
    def get_evolution_data(self, component: str = None) -> List[Dict]:
        """
        Get evolution data for plotting
        
        Args:
            component: Specific component to track, or None for Honor Score
        
        Returns:
            List of {date, time, score} dictionaries
        """
        evolution = []
        
        for session in self.sessions:
            if component and component in session.get('components', {}):
                score = session['components'][component]
            else:
                score = session['honor_score']
            
            evolution.append({
                'date': session['date'],
                'time': session['time'],
                'timestamp': session['timestamp'],
                'score': score
            })
        
        return evolution
    
    def clear_all(self):
        """Clear all session history"""
        self.sessions = []
        self._save_sessions()
