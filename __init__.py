"""
HonorHero Package Initializer
"""

from honorhero import HonorHero
from audio_capture import AudioCapture
from pitch_analyzer import PitchAnalyzer
from timing_analyzer import TimingAnalyzer
from dynamics_analyzer import DynamicsAnalyzer
from consistency_analyzer import ConsistencyAnalyzer
from scoring_system import ScoringSystem

__version__ = '1.0.0'
__all__ = [
    'HonorHero',
    'AudioCapture',
    'PitchAnalyzer',
    'TimingAnalyzer',
    'DynamicsAnalyzer',
    'ConsistencyAnalyzer',
    'ScoringSystem'
]
