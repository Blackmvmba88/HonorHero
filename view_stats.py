#!/usr/bin/env python3
"""
Session Statistics Viewer
View your practice history and progress
"""

from session_history import SessionHistory
from pathlib import Path


def format_duration(seconds):
    """Format duration in a human-readable way"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}h {minutes}m"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    return f"{secs}s"


def print_statistics():
    """Print session statistics"""
    history = SessionHistory()
    
    stats = history.get_statistics()
    
    if stats['total_sessions'] == 0:
        print("=" * 70)
        print("📊  ESTADÍSTICAS DE PRÁCTICA")
        print("=" * 70)
        print()
        print("No hay sesiones registradas todavía.")
        print("¡Comienza tu primera práctica con 'python ui.py'!")
        print()
        return
    
    print("=" * 70)
    print("📊  ESTADÍSTICAS DE PRÁCTICA")
    print("=" * 70)
    print()
    
    # Overall stats
    print("┌─ RESUMEN GENERAL " + "─" * 50 + "┐")
    print(f"│ Total de sesiones:    {stats['total_sessions']:<47} │")
    print(f"│ Tiempo total:         {format_duration(stats['total_practice_time']):<47} │")
    print(f"│ Puntuación promedio:  {stats['average_score']:<47.1f} │")
    print(f"│ 🏆 Mejor puntuación:  {stats['highest_score']:<47.1f} │")
    print(f"│ Tier más común:       {stats['most_common_tier']:<47} │")
    
    # Streak display with emoji
    streak = stats['current_streak']
    if streak > 0:
        streak_emoji = "🔥" if streak >= 7 else "⭐"
        print(f"│ {streak_emoji} Racha actual:      {streak} día{'s' if streak != 1 else ''}{' ' * (44 - len(str(streak)))} │")
    else:
        print(f"│ Racha actual:         {streak} días (¡empieza hoy!){' ' * 23} │")
    
    print("└" + "─" * 68 + "┘")
    print()
    
    # Weekly view - last 7 days
    print_weekly_view(history)
    
    # Recent sessions
    recent = history.get_recent_sessions(5)
    
    if recent:
        print("┌─ ÚLTIMAS 5 SESIONES " + "─" * 46 + "┐")
        print("│ " + "Fecha".ljust(12) + "Hora".ljust(10) + "Score".ljust(8) + 
              "Tier".ljust(15) + "Duración".ljust(12) + "│")
        print("├" + "─" * 68 + "┤")
        
        for session in reversed(recent):
            date = session.get('date', 'N/A')
            time = session.get('time', 'N/A')[:8]  # HH:MM:SS
            score = session.get('honor_score', 0)
            tier = session.get('tier', 'N/A')
            duration = format_duration(session.get('duration', 0))
            
            print(f"│ {date.ljust(12)}{time.ljust(10)}{str(int(score)).ljust(8)}"
                  f"{tier.ljust(15)}{duration.ljust(12)}│")
        
        print("└" + "─" * 68 + "┘")
        print()
    
    # Progress trend
    if stats['total_sessions'] >= 3:
        evolution = history.get_evolution_data()
        
        # Get first 3 and last 3 scores
        first_scores = [e['score'] for e in evolution[:3]]
        last_scores = [e['score'] for e in evolution[-3:]]
        
        avg_first = sum(first_scores) / len(first_scores)
        avg_last = sum(last_scores) / len(last_scores)
        improvement = avg_last - avg_first
        
        print("┌─ PROGRESO " + "─" * 56 + "┐")
        print(f"│ Promedio inicial:  {avg_first:<50.1f} │")
        print(f"│ Promedio reciente: {avg_last:<50.1f} │")
        
        if improvement > 0:
            print(f"│ Mejora:            +{improvement:.1f} puntos {' ' * 35}│")
            print(f"│ {' ' * 66} │")
            print(f"│ 📈 ¡Estás mejorando! Sigue practicando.{' ' * 27} │")
        elif improvement < 0:
            print(f"│ Cambio:            {improvement:.1f} puntos {' ' * 36}│")
            print(f"│ {' ' * 66} │")
            print(f"│ 💪 No te desanimes. La consistencia es la clave.{' ' * 18} │")
        else:
            print(f"│ {' ' * 66} │")
            print(f"│ ⚖️  Te mantienes estable. Busca nuevos desafíos.{' ' * 19} │")
        
        print("└" + "─" * 68 + "┘")
        print()
    
    print("✨ Cada sesión cuenta. ¡Sigue tocando! ✨")
    print()
    
    # Storage location
    storage_path = history.storage_path
    print(f"Datos guardados en: {storage_path}")
    print()


def print_weekly_view(history):
    """Print a weekly view of practice sessions"""
    from datetime import datetime, timedelta
    from collections import defaultdict
    
    # Get all sessions
    sessions = history.get_all_sessions()
    
    if not sessions:
        return
    
    # Group sessions by date
    sessions_by_date = defaultdict(list)
    for session in sessions:
        date = session.get('date')
        if date:
            sessions_by_date[date].append(session)
    
    # Get last 7 days
    today = datetime.now().date()
    week_dates = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6, -1, -1)]
    day_names = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    
    print("┌─ TU SEMANA " + "─" * 55 + "┐")
    
    for i, date in enumerate(week_dates):
        # Get day name
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        day_name = day_names[date_obj.weekday()]
        
        if date in sessions_by_date:
            # Get average score for the day
            day_sessions = sessions_by_date[date]
            avg_score = sum(s['honor_score'] for s in day_sessions) / len(day_sessions)
            tier = get_tier_for_score(avg_score)
            
            # Format with color indicator
            score_str = f"{int(avg_score)}"
            session_count = f"({len(day_sessions)} sesión{'es' if len(day_sessions) > 1 else ''})"
            
            print(f"│ {day_name}: {score_str.rjust(3)} ({tier}) {session_count.ljust(35)} │")
        else:
            print(f"│ {day_name}: {'---'.rjust(3)} (Sin práctica){' ' * 36} │")
    
    print("└" + "─" * 68 + "┘")
    print()


def get_tier_for_score(score):
    """Get the tier name for a given score"""
    if score >= 80:
        return "Íntegro"
    elif score >= 60:
        return "Firme"
    elif score >= 40:
        return "Inestable"
    else:
        return "Fragmentado"


def main():
    """Main entry point"""
    try:
        print_statistics()
    except Exception as e:
        print(f"Error al cargar estadísticas: {e}")
        print("Asegúrate de haber completado al menos una sesión.")


if __name__ == '__main__':
    main()
