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
