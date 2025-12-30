"""
Storytelling Example: Juan's Musical Journey
A week-long practice story showing HonorHero in action
"""

from datetime import datetime, timedelta
import json


def generate_juan_story():
    """
    Generate Juan's week-long practice story with simulated data
    
    This demonstrates how HonorHero tracks progress over time
    """
    
    story = {
        "title": "Juan's Musical Journey: 7 Days with HonorHero",
        "subtitle": "A beginner guitarist discovers the power of consistent practice",
        "character": {
            "name": "Juan",
            "instrument": "Guitar",
            "experience": "3 months",
            "goal": "Learn to play a simple song smoothly"
        },
        "sessions": []
    }
    
    # Day 1: Monday - Nervous beginning
    story["sessions"].append({
        "day": 1,
        "date": "Monday",
        "narrative": "Juan sits down, nervous. His fingers fumble on the frets. He knows the chords but can't switch between them smoothly. The metronome feels like an enemy.",
        "duration": "5 minutes",
        "honor_score": 42,
        "tier": "Fragmentado",
        "components": {
            "pitch": 55,
            "timing": 35,
            "rhythm": 38,
            "dynamics": 48,
            "consistency": 42
        },
        "feedback": "Performance fragmentada. Tu afinación va bien, pero timing y ritmo necesitan trabajo. No te preocupes—es tu primera sesión.",
        "juan_thoughts": "Solo 42 puntos... pero al menos HonorHero no me juzgó. Dice que mi afinación está bien. Eso me da algo para trabajar."
    })
    
    # Day 2: Tuesday - Small adjustment
    story["sessions"].append({
        "day": 2,
        "date": "Tuesday",
        "narrative": "Juan slows down. Instead of rushing through, he focuses on each chord change. Still clumsy, but there's a rhythm emerging.",
        "duration": "5 minutes",
        "honor_score": 48,
        "tier": "Inestable",
        "components": {
            "pitch": 58,
            "timing": 42,
            "rhythm": 45,
            "dynamics": 50,
            "consistency": 48
        },
        "feedback": "Control irregular, pero mejoraste 6 puntos. Tu timing y ritmo están subiendo. Sigue con esa velocidad pausada.",
        "juan_thoughts": "¡48! Subí. HonorHero notó que mejoré el timing. Ir despacio funciona."
    })
    
    # Day 3: Wednesday - Breakthrough moment
    story["sessions"].append({
        "day": 3,
        "date": "Wednesday",
        "narrative": "Something clicks. Juan's fingers find the strings with less hesitation. The transitions aren't perfect, but they flow. For the first time, it sounds like music.",
        "duration": "5 minutes",
        "honor_score": 61,
        "tier": "Firme",
        "components": {
            "pitch": 65,
            "timing": 58,
            "rhythm": 60,
            "dynamics": 62,
            "consistency": 60
        },
        "feedback": "¡Buen salto! Performance sólida. Tu consistencia mejoró mucho. Ahora estás en nivel Firme—sigue así.",
        "juan_thoughts": "¿61? ¡Firme! Esta es la primera vez que suena a canción y no a accidente. Me siento... músico."
    })
    
    # Day 4: Thursday - Plateau
    story["sessions"].append({
        "day": 4,
        "date": "Thursday",
        "narrative": "Juan tries to push faster, to prove yesterday wasn't a fluke. But rushing makes him sloppy. Mistakes creep back in. Frustration builds.",
        "duration": "5 minutes",
        "honor_score": 58,
        "tier": "Inestable",
        "components": {
            "pitch": 60,
            "timing": 52,
            "rhythm": 55,
            "dynamics": 65,
            "dynamics": 58
        },
        "feedback": "Bajaste un poco, pero es parte del proceso. Tu dinámica mejoró, pero timing bajó. ¿Estás yendo muy rápido?",
        "juan_thoughts": "Bajé a 58. Me frustré... pero HonorHero dice que es parte del proceso. Y mi dinámica mejoró, eso no lo había notado."
    })
    
    # Day 5: Friday - Learning patience
    story["sessions"].append({
        "day": 5,
        "date": "Friday",
        "narrative": "Juan takes the feedback to heart. He returns to the slower tempo. No rushing. Just presence. Each note matters.",
        "duration": "5 minutes",
        "honor_score": 65,
        "tier": "Firme",
        "components": {
            "pitch": 68,
            "timing": 62,
            "rhythm": 64,
            "dynamics": 67,
            "consistency": 64
        },
        "feedback": "Volviste al camino. Performance estable. Mejoraste +7 puntos. La paciencia funciona.",
        "juan_thoughts": "65. De vuelta en Firme. Aprendí algo: ir lento no es debilidad, es control."
    })
    
    # Day 6: Saturday - Flow state
    story["sessions"].append({
        "day": 6,
        "date": "Saturday",
        "narrative": "Juan isn't thinking anymore. His fingers know where to go. The music flows through him. He closes his eyes and just... plays.",
        "duration": "5 minutes",
        "honor_score": 74,
        "tier": "Firme",
        "components": {
            "pitch": 76,
            "timing": 72,
            "rhythm": 73,
            "dynamics": 75,
            "consistency": 74
        },
        "feedback": "¡Excelente! Mejoraste 9 puntos. Tu performance muestra cohesión. Casi rozas Íntegro.",
        "juan_thoughts": "74... Esto ya no se siente como práctica. Se siente como tocar."
    })
    
    # Day 7: Sunday - Milestone
    story["sessions"].append({
        "day": 7,
        "date": "Sunday",
        "narrative": "One week. Seven sessions. Juan plays the song one more time. Smooth, confident, alive. The guitar isn't separate from him anymore—it's part of him.",
        "duration": "5 minutes",
        "honor_score": 82,
        "tier": "Íntegro",
        "components": {
            "pitch": 84,
            "timing": 80,
            "rhythm": 82,
            "dynamics": 83,
            "consistency": 81
        },
        "feedback": "🎉 ¡Primera vez en nivel Íntegro! Tu interpretación muestra integridad y maestría. Celebra este logro.",
        "juan_thoughts": "82. Íntegro. En una semana pasé de 42 a 82. No porque sea talentoso, sino porque practiqué. Cinco minutos cada día. Eso es todo lo que tomó."
    })
    
    # Summary
    story["summary"] = {
        "total_practice_time": "35 minutes",
        "initial_score": 42,
        "final_score": 82,
        "improvement": "+40 points",
        "key_lesson": "Consistency and patience over intensity",
        "juan_reflection": "HonorHero didn't make me perfect. It made me present. Every day, it showed me where I was, without judgment. The numbers weren't threats—they were mirrors. And when I looked in that mirror, I saw someone becoming a musician."
    }
    
    return story


def print_juan_story():
    """Print Juan's story in a beautiful narrative format"""
    story = generate_juan_story()
    
    print("=" * 70)
    print(f"  {story['title']}")
    print(f"  {story['subtitle']}")
    print("=" * 70)
    print()
    
    char = story['character']
    print(f"Meet {char['name']}")
    print(f"  Instrument: {char['instrument']}")
    print(f"  Experience: {char['experience']}")
    print(f"  Goal: {char['goal']}")
    print()
    print("-" * 70)
    print()
    
    # Print each day
    for session in story['sessions']:
        print(f"DAY {session['day']}: {session['date'].upper()}")
        print("─" * 70)
        print()
        print(session['narrative'])
        print()
        print(f"Duration: {session['duration']}")
        print(f"Honor Score: {session['honor_score']} — {session['tier']}")
        print()
        print("Components:")
        for comp, score in session['components'].items():
            bar = "█" * int(score / 5) + "░" * (20 - int(score / 5))
            print(f"  {comp:12} [{bar}] {score}")
        print()
        print(f"💬 HonorHero says: \"{session['feedback']}\"")
        print()
        print(f"🤔 Juan thinks: \"{session['juan_thoughts']}\"")
        print()
        print("-" * 70)
        print()
    
    # Summary
    summary = story['summary']
    print("WEEK SUMMARY")
    print("=" * 70)
    print()
    print(f"Total Practice Time: {summary['total_practice_time']}")
    print(f"Score Journey: {summary['initial_score']} → {summary['final_score']} ({summary['improvement']})")
    print(f"Key Lesson: {summary['key_lesson']}")
    print()
    print("Juan's Reflection:")
    print()
    print(f'  "{summary["juan_reflection"]}"')
    print()
    print("=" * 70)
    print()
    print("✨ This could be your story. Start with just 5 minutes a day. ✨")
    print()


def save_juan_story_json(filename='juan_story.json'):
    """Save Juan's story as JSON for external use"""
    story = generate_juan_story()
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(story, f, indent=2, ensure_ascii=False)
    print(f"Story saved to {filename}")


if __name__ == '__main__':
    print_juan_story()
