# HonorHero 🎵

> *Interpretación consciente, no perfección vacía*

HonorHero is a human-centered music performance evaluation system inspired by Guitar Hero. It captures live audio (voice or instrument) and analyzes your performance in real-time, providing constructive feedback focused on self-improvement rather than competition.

## Who is HonorHero for? 🎯

HonorHero was created for anyone who wants to grow as a musician without the pressure of competition or judgment:

- **🎸 The beginner musician** who's tired of feeling inadequate when comparing themselves to others
- **🎤 The shy vocalist** who needs private, encouraging feedback to build confidence
- **🥁 The instrumentalist who hates metronomes** but still wants to develop better timing
- **👨‍🏫 The music teacher** seeking a compassionate tool that encourages students instead of grading them
- **🎹 The self-taught learner** who wants to track progress without the stress of formal evaluation
- **🎵 The experienced musician** exploring new styles or recovering from injury
- **💆 Anyone using music for therapy or mindfulness** who values process over perfection

If you believe that **mistakes are part of learning**, not failures to be punished, HonorHero is for you.

## Philosophy

**The performance never stops.** Mistakes are measured, not punished. HonorHero embraces the learning journey and celebrates progress over perfection.

Read our full philosophy in the [MANIFESTO](MANIFESTO.md).

## Features

- 🎤 **Real-time Audio Capture**: Captures live audio from microphone or instrument
- 🎼 **Multi-Dimensional Analysis**:
  - **Pitch**: Analyzes pitch accuracy with tolerant thresholds
  - **Timing**: Measures note timing accuracy
  - **Rhythm**: Evaluates rhythm consistency and patterns
  - **Dynamics**: Assesses volume control and expression
  - **Consistency**: Tracks overall performance consistency
- 🏆 **Honor Score (0-100)**: Weighted score with qualitative tiers
- 📊 **Qualitative Tiers**:
  - **Íntegro** (80-100): Complete, integrated performance
  - **Firme** (60-79): Firm, solid performance
  - **Inestable** (40-59): Unstable, inconsistent
  - **Fragmentado** (0-39): Fragmented performance
- 🗣️ **Human-Friendly Feedback**: Natural language coaching, not just numbers
- 💾 **Session History**: Track your progress over days and weeks
- 🎨 **Expressive UI**: Simple console interface focused on encouragement
- 🔧 **Modular Architecture**: Clean separation of concerns for easy extension

## Installation

### Prerequisites

- Python 3.8 or higher
- A microphone or audio input device

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Blackmvmba88/HonorHero.git
cd HonorHero
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the UI Application

```bash
python ui.py
```

This launches the interactive console UI that displays real-time performance metrics.

### Command-line Options

```bash
# Run for a specific duration (in seconds)
python ui.py --duration 30

# Run until interrupted (Ctrl+C)
python ui.py
```

### Programmatic Usage

```python
from honorhero import HonorHero

# Create engine
engine = HonorHero()

# Define callback for real-time updates
def on_update(metrics):
    print(f"Score: {metrics['honor_score']:.1f}")
    print(f"Tier: {metrics['tier']}")

# Start performance evaluation
engine.start_performance(on_update)

# ... perform music ...

# Stop and get final results
results = engine.stop_performance()
print(f"Final Score: {results['final_honor_score']:.1f}")
```

See `examples.py` for more usage examples.

## Architecture

HonorHero uses a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────┐
│                  HonorHero                      │
│              (Main Engine)                      │
└──────────┬─────────────────────────────┬────────┘
           │                             │
┌──────────▼──────────┐       ┌─────────▼─────────┐
│   Audio Capture     │       │  Scoring System   │
└──────────┬──────────┘       └─────────▲─────────┘
           │                             │
           ├─────────────────────────────┤
           │                             │
    ┌──────▼──────┐              ┌──────┴────────┐
    │   Pitch     │              │  Consistency  │
    │  Analyzer   │              │   Analyzer    │
    └─────────────┘              └───────────────┘
           │
    ┌──────▼──────┐              ┌───────────────┐
    │   Timing    │              │   Dynamics    │
    │  Analyzer   │              │   Analyzer    │
    └─────────────┘              └───────────────┘
```

### Modules

- **`audio_capture.py`**: Real-time audio input handling
- **`pitch_analyzer.py`**: Pitch detection and accuracy analysis
- **`timing_analyzer.py`**: Timing and rhythm evaluation
- **`dynamics_analyzer.py`**: Volume and expression analysis
- **`consistency_analyzer.py`**: Overall consistency tracking
- **`scoring_system.py`**: Honor Score calculation and tier assignment
- **`honorhero.py`**: Main engine coordinating all modules
- **`ui.py`**: Console user interface
- **`config.py`**: Configuration and tolerant thresholds

## Configuration

Edit `config.py` to adjust thresholds and weights:

```python
# Tolerances (more forgiving values)
PITCH_TOLERANCE = 50  # cents
TIMING_TOLERANCE = 0.15  # seconds
RHYTHM_TOLERANCE = 0.20  # ratio
DYNAMICS_TOLERANCE = 15  # dB

# Component weights
WEIGHTS = {
    'pitch': 0.25,
    'timing': 0.20,
    'rhythm': 0.20,
    'dynamics': 0.15,
    'consistency': 0.20
}
```

## Design Principles

1. **Human-Centered**: Focuses on the learner's journey, not competition
2. **Tolerant Thresholds**: Forgiving ranges that encourage rather than discourage
3. **Continuous Evaluation**: Performance never stops for mistakes
4. **Constructive Feedback**: Qualitative tiers with encouraging messages
5. **Modular Design**: Easy to extend and customize
6. **Self-Improvement Focus**: Progress tracking and trend analysis

## Honor Score Calculation

The Honor Score is calculated as a weighted average of component scores:

```
Honor Score = (Pitch × 0.25) + (Timing × 0.20) + (Rhythm × 0.20) 
            + (Dynamics × 0.15) + (Consistency × 0.20)
```

Each component is scored 0-100 based on tolerant thresholds that encourage learning.

## Examples

Run the example scripts:

```bash
python examples.py
```

This provides interactive examples of using HonorHero both with callbacks and programmatically.

### Juan's Story: A Week-Long Journey

Want to see HonorHero in action? Read about Juan's transformation:

```bash
python juan_story.py
```

Juan, a beginner guitarist, practiced just 5 minutes a day for a week. His Honor Score went from 42 to 82. This isn't about talent—it's about consistent, mindful practice. The story shows how HonorHero tracks progress, provides encouragement, and celebrates growth.

## Requirements

- numpy: Numerical operations
- librosa: Audio analysis and pitch detection
- sounddevice: Audio capture
- scipy: Signal processing
- pyaudio: Audio I/O (alternative backend)

## Contributing

Contributions are welcome! This project embraces:
- More tolerant evaluation algorithms
- Additional analysis dimensions
- Better UI/UX for encouragement
- Multi-language support
- Recording and playback features

See our [ROADMAP](ROADMAP.md) for planned features and how you can help.

**Please review our [ethical guidelines](ETHICS.md) before contributing.** All contributions must align with HonorHero's philosophy of encouragement over competition.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Ethical Use**: While this is open source software, we encourage all users to review our [ETHICS.md](ETHICS.md) guidelines. HonorHero is designed for learning and self-improvement, not for competitive ranking or punitive evaluation.

## Roadmap 🚢

We're actively developing HonorHero! Check out our [ROADMAP](ROADMAP.md) to see:
- **v0.2**: Session persistence and history tracking
- **v0.3**: Visualization and insights
- **v1.0**: GUI and standalone application

Want to contribute? Pick a feature from the roadmap and join us!

## Credits

Inspired by Guitar Hero's engaging gameplay, but focused on real musical skill development and self-improvement rather than competition.

---

*"La música es el arte de organizar el sonido en el tiempo. HonorHero es el arte de celebrar ese viaje."*
