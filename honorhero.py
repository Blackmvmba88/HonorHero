"""
HonorHero Main Engine
Coordinates all analysis modules and provides real-time evaluation
"""

import numpy as np
import time
from typing import Dict, Optional
from audio_capture import AudioCapture
from pitch_analyzer import PitchAnalyzer
from timing_analyzer import TimingAnalyzer
from dynamics_analyzer import DynamicsAnalyzer
from consistency_analyzer import ConsistencyAnalyzer
from scoring_system import ScoringSystem
import config


class HonorHero:
    """
    Main HonorHero performance evaluation engine
    
    Human-centered music performance evaluation inspired by Guitar Hero.
    Performance never stops - mistakes are measured, not punished.
    """
    
    def __init__(self):
        # Initialize modules
        self.audio_capture = AudioCapture()
        self.pitch_analyzer = PitchAnalyzer()
        self.timing_analyzer = TimingAnalyzer()
        self.dynamics_analyzer = DynamicsAnalyzer()
        self.consistency_analyzer = ConsistencyAnalyzer()
        self.scoring_system = ScoringSystem()
        
        # State
        self.is_running = False
        self.start_time = None
        self.current_metrics = {}
        self.update_callback = None
        
    def start_performance(self, update_callback=None):
        """
        Start evaluating performance
        
        Args:
            update_callback: Optional callback function for real-time updates
        """
        self.is_running = True
        self.start_time = time.time()
        self.update_callback = update_callback
        
        print("🎵 HonorHero iniciado - ¡Comienza a tocar!")
        print("La performance nunca se detiene. Los errores se miden, no se castigan.")
        print("-" * 60)
        
        # Start audio capture
        self.audio_capture.start(self._process_audio_chunk)
        
    def stop_performance(self) -> Dict:
        """
        Stop evaluating and return final results
        
        Returns:
            Final performance summary
        """
        self.is_running = False
        self.audio_capture.stop()
        
        # Calculate final scores
        final_results = self._calculate_final_scores()
        
        print("\n" + "=" * 60)
        print("🏆 Performance finalizada")
        print("=" * 60)
        
        return final_results
    
    def _process_audio_chunk(self, audio_chunk: np.ndarray, sample_rate: int):
        """Process incoming audio data"""
        if not self.is_running:
            return
        
        current_time = time.time() - self.start_time
        
        # Analyze pitch
        pitch_result = self.pitch_analyzer.analyze(audio_chunk, sample_rate)
        
        # Detect timing/rhythm
        timing_result = self.timing_analyzer.detect_onset(
            audio_chunk, sample_rate, current_time
        )
        
        # Analyze dynamics
        dynamics_result = self.dynamics_analyzer.analyze(audio_chunk)
        
        # Update metrics periodically
        if int(current_time * 2) % 2 == 0:  # Every ~0.5 seconds
            self._update_metrics()
    
    def _update_metrics(self):
        """Calculate and update current metrics"""
        # Get component scores
        pitch_score = self.pitch_analyzer.get_average_score()
        timing_analysis = self.timing_analyzer.analyze_timing()
        rhythm_analysis = self.timing_analyzer.analyze_rhythm()
        dynamics_score = self.dynamics_analyzer.get_average_score()
        
        # Update consistency
        self.consistency_analyzer.add_metrics(
            pitch_score,
            timing_analysis['score'],
            rhythm_analysis['score'],
            dynamics_score
        )
        
        consistency_analysis = self.consistency_analyzer.analyze()
        
        # Calculate Honor Score
        metrics = {
            'pitch': pitch_score,
            'timing': timing_analysis['score'],
            'rhythm': rhythm_analysis['score'],
            'dynamics': dynamics_score,
            'consistency': consistency_analysis['score']
        }
        
        honor_result = self.scoring_system.calculate_honor_score(metrics)
        
        # Store current metrics
        self.current_metrics = {
            'honor_score': honor_result['honor_score'],
            'tier': honor_result['tier'],
            'message': honor_result['message'],
            'components': metrics
        }
        
        # Call update callback if provided
        if self.update_callback:
            self.update_callback(self.current_metrics)
    
    def _calculate_final_scores(self) -> Dict:
        """Calculate final performance summary"""
        # Get final component scores
        pitch_score = self.pitch_analyzer.get_average_score()
        timing_analysis = self.timing_analyzer.analyze_timing()
        rhythm_analysis = self.timing_analyzer.analyze_rhythm()
        dynamics_score = self.dynamics_analyzer.get_average_score()
        consistency_analysis = self.consistency_analyzer.analyze()
        
        # Calculate final Honor Score
        metrics = {
            'pitch': pitch_score,
            'timing': timing_analysis['score'],
            'rhythm': rhythm_analysis['score'],
            'dynamics': dynamics_score,
            'consistency': consistency_analysis['score']
        }
        
        honor_result = self.scoring_system.calculate_honor_score(metrics)
        progress_summary = self.scoring_system.get_progress_summary()
        
        return {
            'final_honor_score': honor_result['honor_score'],
            'tier': honor_result['tier'],
            'message': honor_result['message'],
            'components': metrics,
            'progress': progress_summary
        }
    
    def get_current_status(self) -> Dict:
        """Get current performance status"""
        return self.current_metrics
    
    def reset(self):
        """Reset all analyzers for a new performance"""
        self.pitch_analyzer.reset()
        self.timing_analyzer.reset()
        self.dynamics_analyzer.reset()
        self.consistency_analyzer.reset()
        self.scoring_system.reset()
        self.current_metrics = {}
