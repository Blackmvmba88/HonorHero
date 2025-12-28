"""
Audio Capture Module
Handles real-time audio input from microphone or instrument
"""

import numpy as np
import sounddevice as sd
from typing import Callable, Optional
import config


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
        return sd.query_devices()
