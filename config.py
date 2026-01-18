"""
HonorHero Configuration
Tolerant thresholds focused on encouragement and self-improvement
"""

# Audio capture settings
SAMPLE_RATE = 22050  # Hz
BUFFER_SIZE = 2048
CHANNELS = 1

# Performance evaluation thresholds (tolerant ranges)
PITCH_TOLERANCE = 50  # cents (half semitone)
TIMING_TOLERANCE = 0.15  # seconds
RHYTHM_TOLERANCE = 0.20  # ratio variance
DYNAMICS_TOLERANCE = 15  # dB range
CONSISTENCY_THRESHOLD = 0.7  # 70% consistency is acceptable

# Honor Score tiers (0-100)
SCORE_TIERS = {
    'Íntegro': (80, 100),      # 80-100: Complete, integrated performance
    'Firme': (60, 79),          # 60-79: Firm, solid performance
    'Inestable': (40, 59),      # 40-59: Unstable, inconsistent
    'Fragmentado': (0, 39)      # 0-39: Fragmented performance
}

# Component weights for overall score
WEIGHTS = {
    'pitch': 0.25,
    'timing': 0.20,
    'rhythm': 0.20,
    'dynamics': 0.15,
    'consistency': 0.20
}

# Analysis parameters
MIN_CONFIDENCE = 0.5  # Minimum confidence for pitch detection
WINDOW_SIZE = 0.5  # seconds for analysis windows

# User Profiles - Different tolerance levels for different skill levels and needs
PROFILES = {
    'beginner': {
        'name': 'Súper Principiante',
        'description': 'Tolerancias amplias para empezar sin presión',
        'PITCH_TOLERANCE': 70,
        'TIMING_TOLERANCE': 0.20,
        'RHYTHM_TOLERANCE': 0.25,
        'DYNAMICS_TOLERANCE': 20,
        'CONSISTENCY_THRESHOLD': 0.6
    },
    'intermediate': {
        'name': 'Intermedio',
        'description': 'Balance entre apoyo y desafío',
        'PITCH_TOLERANCE': 50,
        'TIMING_TOLERANCE': 0.15,
        'RHYTHM_TOLERANCE': 0.20,
        'DYNAMICS_TOLERANCE': 15,
        'CONSISTENCY_THRESHOLD': 0.7
    },
    'advanced': {
        'name': 'Avanzado',
        'description': 'Estándares más altos para músicos experimentados',
        'PITCH_TOLERANCE': 30,
        'TIMING_TOLERANCE': 0.10,
        'RHYTHM_TOLERANCE': 0.15,
        'DYNAMICS_TOLERANCE': 10,
        'CONSISTENCY_THRESHOLD': 0.8
    },
    'therapy': {
        'name': 'Terapia / Rehabilitación',
        'description': 'Máxima tolerancia para uso terapéutico',
        'PITCH_TOLERANCE': 100,
        'TIMING_TOLERANCE': 0.30,
        'RHYTHM_TOLERANCE': 0.35,
        'DYNAMICS_TOLERANCE': 25,
        'CONSISTENCY_THRESHOLD': 0.5
    }
}

DEFAULT_PROFILE = 'intermediate'

# Session modes - Different durations for different practice styles
SESSION_MODES = {
    'short': {
        'name': 'Sesión Corta',
        'duration': 180,  # 3 minutes
        'description': 'Práctica rápida y enfocada'
    },
    'focus': {
        'name': 'Sesión Profunda',
        'duration': 600,  # 10 minutes
        'description': 'Práctica concentrada y extendida'
    },
    'free': {
        'name': 'Sesión Libre',
        'duration': None,  # No limit
        'description': 'Sin límite de tiempo'
    }
}

DEFAULT_MODE = 'free'
