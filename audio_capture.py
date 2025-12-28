"""
Audio Capture Module
Handles real-time audio input from microphone or instrument
"""

import numpy as np
from typing import Callable, Optional
import config

# Try to import sounddevice, but allow graceful degradation
try:
    import sounddevice as sd
    AUDIO_AVAILABLE = True
except (OSError, ImportError) as e:
    AUDIO_AVAILABLE = False
    print(f"Warning: Audio input not available ({e})")
    print("Audio capture will not work, but other modules can still be used.")


class AudioCapture:
    """Real-time audio capture with continuous streaming"""
    
    def __init__(self, sample_rate: int = config.SAMPLE_RATE,
                 buffer_size: int = config.BUFFER_SIZE,
                 channels: int = config.CHANNELS):
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.channels = channels
        self.stream: Optional[sd.InputStream] = None
        self.is_capturing = False
        self.audio_buffer = []
        
    def start(self, callback: Callable[[np.ndarray, int], None]):
        """
        Start capturing audio
        
        Args:
            callback: Function to call with audio data (audio_chunk, sample_rate)
        """
        if not AUDIO_AVAILABLE:
            raise RuntimeError("Audio input is not available. sounddevice/PortAudio not properly installed.")
        
        def audio_callback(indata, frames, time_info, status):
            if status:
                print(f"Audio status: {status}")
            # Convert to mono if needed
            audio_data = indata[:, 0] if self.channels == 1 and indata.shape[1] > 1 else indata
            callback(audio_data.copy(), self.sample_rate)
        
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            blocksize=self.buffer_size,
            callback=audio_callback
        )
        self.stream.start()
        self.is_capturing = True
        
    def stop(self):
        """Stop capturing audio"""
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.stream = None
        self.is_capturing = False
        
    def get_devices(self):
        """Get available audio input devices"""
        if not AUDIO_AVAILABLE:
            return []
        return sd.query_devices()
