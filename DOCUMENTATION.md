# HonorHero Technical Documentation

## System Architecture

HonorHero is built with a modular, event-driven architecture that processes audio in real-time and provides continuous feedback.

### Core Components

#### 1. Audio Capture Module (`audio_capture.py`)

**Purpose**: Captures live audio input from microphone or instrument

**Key Features**:
- Non-blocking audio stream
- Configurable sample rate and buffer size
- Device selection support
- Mono/stereo handling

**Usage**:
```python
from audio_capture import AudioCapture

capture = AudioCapture()
capture.start(callback=process_audio)
# ... audio is processed ...
capture.stop()
```

#### 2. Pitch Analyzer (`pitch_analyzer.py`)

**Purpose**: Analyzes pitch accuracy and deviation

**Algorithm**:
1. Uses librosa's piptrack for pitch detection
2. Identifies most prominent pitch frequencies
3. Converts to MIDI note numbers
4. Calculates deviation in cents
5. Scores based on tolerance threshold

**Scoring**:
- Within tolerance (±50 cents): 100 points
- Beyond tolerance: Score decreases linearly

**Key Methods**:
- `analyze(audio_chunk, sample_rate)`: Analyze pitch in chunk
- `get_average_score()`: Get average pitch score
- `reset()`: Clear history

#### 3. Timing Analyzer (`timing_analyzer.py`)

**Purpose**: Evaluates timing accuracy and rhythm consistency

**Algorithm**:
1. Energy-based onset detection
2. Tracks intervals between note onsets
3. Calculates timing variance
4. Measures rhythm consistency (coefficient of variation)

**Scoring**:
- Low variance (≤0.15s): 100 points
- High variance: Score decreases
- Rhythm: Based on interval consistency

**Key Methods**:
- `detect_onset(audio_chunk, sample_rate, timestamp)`: Detect note onsets
- `analyze_timing()`: Analyze timing accuracy
- `analyze_rhythm()`: Analyze rhythm consistency

#### 4. Dynamics Analyzer (`dynamics_analyzer.py`)

**Purpose**: Assesses volume control and expression

**Algorithm**:
1. Calculates RMS amplitude
2. Converts to dB scale
3. Tracks dynamic range
4. Evaluates expressive variation

**Scoring**:
- Optimal range (5-15 dB): 100 points
- Too flat (<5 dB): Lower score
- Too variable (>15 dB): Lower score

**Key Methods**:
- `analyze(audio_chunk)`: Analyze dynamics
- `get_average_score()`: Get average dynamics score

#### 5. Consistency Analyzer (`consistency_analyzer.py`)

**Purpose**: Measures overall performance consistency

**Algorithm**:
1. Tracks all component scores over time
2. Calculates coefficient of variation for each
3. Computes overall consistency metric
4. Scores based on stability threshold

**Scoring**:
- High consistency (≥70%): 100 points
- Lower consistency: Proportional score

**Key Methods**:
- `add_metrics(pitch, timing, rhythm, dynamics)`: Add scores
- `analyze()`: Compute consistency
- `reset()`: Clear history

#### 6. Scoring System (`scoring_system.py`)

**Purpose**: Calculates Honor Score and assigns tiers

**Algorithm**:
1. Weighted average of components:
   - Pitch: 25%
   - Timing: 20%
   - Rhythm: 20%
   - Dynamics: 15%
   - Consistency: 20%
2. Maps score to qualitative tier
3. Provides encouraging message

**Tiers**:
- **Íntegro** (80-100): Excellent performance
- **Firme** (60-79): Good performance
- **Inestable** (40-59): Needs improvement
- **Fragmentado** (0-39): Keep practicing

**Key Methods**:
- `calculate_honor_score(metrics)`: Calculate score
- `get_average_score()`: Average over session
- `get_progress_summary()`: Trend analysis

#### 7. Main Engine (`honorhero.py`)

**Purpose**: Coordinates all modules for real-time evaluation

**Flow**:
1. Initialize all analyzer modules
2. Start audio capture with callback
3. Process each audio chunk:
   - Pitch analysis
   - Onset detection
   - Dynamics analysis
4. Periodically (every ~0.5s):
   - Calculate component scores
   - Update consistency
   - Compute Honor Score
   - Trigger UI update
5. On stop:
   - Calculate final scores
   - Generate summary

**Key Methods**:
- `start_performance(callback)`: Begin evaluation
- `stop_performance()`: End and get results
- `get_current_status()`: Get real-time status
- `reset()`: Reset for new session

#### 8. User Interface (`ui.py`)

**Purpose**: Provides expressive, encouraging console UI

**Features**:
- Real-time score display
- Color-coded progress bars
- Qualitative tier display
- Component breakdown
- Encouraging messages
- Final summary with trends

**Display Elements**:
- Large Honor Score display
- Component bars with colors
- Progress information
- Motivational messages

## Data Flow

```
Microphone → Audio Capture → Audio Chunks
                               ↓
                    ┌──────────┴──────────┐
                    ↓                     ↓
            Pitch Analysis         Dynamics Analysis
            Timing/Rhythm                 ↓
                    ↓                     ↓
                    └──────────┬──────────┘
                               ↓
                      Consistency Analysis
                               ↓
                        Scoring System
                               ↓
                          Honor Score
                               ↓
                          UI Display
```

## Configuration

All thresholds and parameters are defined in `config.py`:

### Audio Settings
- `SAMPLE_RATE = 22050`: Audio sample rate (Hz)
- `BUFFER_SIZE = 2048`: Audio buffer size
- `CHANNELS = 1`: Mono audio

### Tolerance Thresholds
- `PITCH_TOLERANCE = 50`: ±50 cents (quarter tone)
- `TIMING_TOLERANCE = 0.15`: ±150ms
- `RHYTHM_TOLERANCE = 0.20`: 20% variation
- `DYNAMICS_TOLERANCE = 15`: ±15 dB
- `CONSISTENCY_THRESHOLD = 0.7`: 70% consistency

### Component Weights
```python
WEIGHTS = {
    'pitch': 0.25,      # 25% of score
    'timing': 0.20,     # 20% of score
    'rhythm': 0.20,     # 20% of score
    'dynamics': 0.15,   # 15% of score
    'consistency': 0.20 # 20% of score
}
```

## Extending HonorHero

### Adding a New Analyzer

1. Create new module (e.g., `articulation_analyzer.py`):
```python
class ArticulationAnalyzer:
    def analyze(self, audio_chunk, sample_rate):
        # Implement analysis
        return {'score': score}
    
    def get_average_score(self):
        # Return average
        return score
    
    def reset(self):
        # Clear history
        pass
```

2. Add to main engine (`honorhero.py`):
```python
self.articulation_analyzer = ArticulationAnalyzer()
```

3. Update weights in `config.py`:
```python
WEIGHTS = {
    'pitch': 0.20,
    'timing': 0.15,
    'rhythm': 0.15,
    'dynamics': 0.15,
    'articulation': 0.15,
    'consistency': 0.20
}
```

### Customizing Tolerances

Edit `config.py` to make evaluation more or less forgiving:

```python
# More forgiving
PITCH_TOLERANCE = 75  # 75 cents
TIMING_TOLERANCE = 0.25  # 250ms

# More strict
PITCH_TOLERANCE = 25  # 25 cents
TIMING_TOLERANCE = 0.10  # 100ms
```

### Adding New Tiers

Modify `SCORE_TIERS` in `config.py`:

```python
SCORE_TIERS = {
    'Maestro': (90, 100),
    'Íntegro': (75, 89),
    'Firme': (60, 74),
    'Inestable': (40, 59),
    'Fragmentado': (0, 39)
}
```

## Performance Optimization

### Audio Processing
- Use appropriate buffer sizes (1024-4096 samples)
- Minimize processing in audio callback
- Use efficient NumPy operations

### Real-time Updates
- Throttle UI updates (default: 500ms)
- Cache calculated scores
- Use efficient console rendering

### Memory Management
- Limit history buffer sizes
- Periodically clear old data
- Use circular buffers for streaming

## Testing

### Manual Testing
```bash
# Test with live microphone
python ui.py --duration 30

# Test programmatically
python examples.py
```

### Component Testing
```python
# Test individual analyzer
from pitch_analyzer import PitchAnalyzer
import numpy as np

analyzer = PitchAnalyzer()
# Generate test audio (A4 = 440 Hz)
t = np.linspace(0, 1, 22050)
audio = np.sin(2 * np.pi * 440 * t)
result = analyzer.analyze(audio, 22050)
print(result)  # Should detect ~A4
```

## Troubleshooting

### No Audio Input
- Check microphone permissions
- Verify device with `AudioCapture.get_devices()`
- Test with system audio settings

### Low Scores
- Check microphone quality
- Adjust tolerances in `config.py`
- Ensure quiet environment

### Performance Issues
- Reduce sample rate in `config.py`
- Increase buffer size
- Close other audio applications

## Future Enhancements

- Visual waveform display
- Recording and playback
- Target pitch/rhythm patterns
- Progress tracking over sessions
- Multi-user support
- Web-based UI
- Mobile app
- Integration with music notation software