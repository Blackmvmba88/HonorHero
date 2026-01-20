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
- 👤 **User Profiles**: 4 profiles for different skill levels and needs (beginner, intermediate, advanced, therapy)
- ⏱️ **Session Modes**: Predefined durations (short 3min, focus 10min, free unlimited)
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
- 🔥 **Enhanced Statistics**: Streak tracking, weekly view, best score highlighting
- 🎨 **Visual Identity System**: 6 themes with profile-specific aesthetics
  - **Warm Theme**: Encouraging colors for beginners and therapy
  - **Cool Theme**: Precise colors for intermediate/advanced practice
  - **Colorblind Accessible**: High-contrast, accessible color palette
  - **Dark/Light Modes**: Optimized for different lighting conditions
  - **Monochrome**: Minimal distraction, pure focus
  - **Animated Feedback**: Particles, arrows, and smooth progress bars
- 🎮 **Non-Competitive Gamification**: Achievement system focused on personal growth
  - **Philosophical Achievements**: Persistence, Constancy, Listening, Expression
  - **Soft Medals**: Gentle recognition of technical progress
  - **Temporal Milestones**: Time-based celebration of dedication
  - **17+ Achievements**: No rankings, no competition, just personal celebration
- 🎨 **Expressive UI**: Two interface modes available
  - **Standard UI**: Real-time metrics display with component scores and themed visuals
  - **Piano Roll UI**: Temporal mirror showing your musical journey as it unfolds
- 🎹 **Piano Roll Visualization**: Console-based piano-roll interface that shows:
  - Your past performance (what you played 3 seconds ago)
  - Your present performance (what you're playing now)
  - Performance trends (where you're heading)
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

HonorHero offers two interface modes:

#### 1. Standard Console UI (Metrics Display)

```bash
# Basic usage with default settings (intermediate profile, unlimited time)
python ui.py

# Quick beginner practice (3 minutes)
python ui.py --profile beginner --mode short

# Daily intermediate practice (10 minutes)
python ui.py --profile intermediate --mode focus

# Advanced performance preparation
python ui.py --profile advanced --mode focus

# Therapeutic session (no time limit)
python ui.py --profile therapy --mode free

# Custom duration override
python ui.py --profile intermediate --duration 60

# Use specific visual theme
python ui.py --theme warm           # Encouraging, warm colors
python ui.py --theme cool           # Precise, cool colors
python ui.py --theme colorblind     # Accessible for color vision deficiency
python ui.py --theme dark           # Dark mode for low light
python ui.py --theme light          # Light mode for bright environments
python ui.py --theme monochrome     # Pure grayscale
```

This launches the interactive console UI that displays real-time performance metrics with beautiful themed visuals, animated feedback, and saves your session history automatically. Achievements are unlocked as you progress!

#### 2. Piano Roll UI (Temporal Mirror)

```bash
# Launch piano roll interface with default settings
python piano_roll_ui.py

# Quick practice with visual feedback
python piano_roll_ui.py --profile beginner --mode short

# Extended practice with 5-second time window
python piano_roll_ui.py --profile intermediate --mode focus --window 5

# Therapeutic session with piano roll visualization
python piano_roll_ui.py --profile therapy --mode free

# Piano roll with specific theme
python piano_roll_ui.py --theme dark --mode focus
```

The **Piano Roll UI** is a temporal mirror of your performance with themed colors - it shows:
- **Your past** (what you played 3 seconds ago)
- **Your present** (what you're playing now)
- **Your trend** (where your performance is heading)

This interface embraces the HonorHero philosophy: the music comes from you, and the UI reflects your journey without judgment. Unlike Guitar Hero, notes aren't thrown at you - instead, you see your own musical expression unfold in real-time with beautiful visual feedback.

### Visual Themes & Achievements

HonorHero now features a comprehensive visual identity system with 6 themes and a non-competitive achievement system. See [VISUAL_IDENTITY.md](VISUAL_IDENTITY.md) for complete details.

**Quick Theme Guide:**
- `warm` - Encouraging, therapeutic (auto-selected for beginner/therapy)
- `cool` - Precise, focused (auto-selected for intermediate/advanced)
- `colorblind` - Accessible for color vision deficiency
- `dark` / `light` - Optimized for different lighting
- `monochrome` - Minimal visual distraction

**Achievements:**
Unlock 17+ achievements as you practice, including:
- 🌱 Philosophical achievements (Persistence, Constancy, Listening)
- ✨ Soft medals (Stable Pitch, Balanced Performer)
- 🚀 Temporal milestones (First Step, Week Streak, 10 Hours)

No rankings, no competition - just personal celebration of your musical journey!

### User Profiles

Choose a profile that matches your skill level and needs:

- **`beginner`**: Most tolerant settings for beginners and exploratory practice
- **`intermediate`**: Balanced evaluation for regular practice (default)
- **`advanced`**: Strict standards for experienced musicians
- **`therapy`**: Maximum tolerance for therapeutic and adaptive use

### Session Modes

Select a practice duration that fits your schedule:

- **`short`**: 3 minutes - Perfect for quick warmups and busy schedules
- **`focus`**: 10 minutes - Ideal for daily concentrated practice
- **`free`**: Unlimited - Continue until you stop (default)

### View Your Progress

After completing sessions, view your statistics with enhanced features:

```bash
python view_stats.py
```

This shows:
- 🔥 Practice streak with emoji (🔥 for 7+ days)
- 🏆 Your best Honor Score
- 📅 Weekly view of last 7 days
- ⏱️ Total practice time with better formatting
- 📊 Progress trends and improvements

### Command-line Options

```bash
# Show all available options
python ui.py --help

# Combine profile and mode
python ui.py --profile beginner --mode short

# Override duration (in seconds)
python ui.py --duration 30

# Run until interrupted (Ctrl+C)
python ui.py
```

For detailed information about profiles and modes, see [NEW_FEATURES.md](NEW_FEATURES.md).

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

HonorHero includes comprehensive examples demonstrating real-world scenarios and use cases. See [EXAMPLES.md](EXAMPLES.md) for detailed documentation with console output and visual storytelling.

### Interactive Example Viewer

```bash
python display_examples.py
```

This launches an interactive menu to explore:
- **Example 1:** Juan's beginner guitar session (Score: 42, Inestable)
- **Example 2:** Daily practice tracking - week-long journey from 42 to 82
- **Example 3:** Shy vocalist with gentle, supportive feedback
- **Example 4:** Programmatic use for developers and custom applications
- **Example 5:** What HonorHero is NOT - philosophy and principles

### Example Data Files

All examples include simulated session data in JSON format in the `examples/` directory:

```bash
# View example data
cat examples/example1_juan_beginner.json | python -m json.tool

# Simulate Juan's weekly progress
ls examples/example2_daily_tracking_*.json
```

### Juan's Story: A Week-Long Journey

Want to see HonorHero in action? Read about Juan's transformation:

```bash
python juan_story.py
```

Juan, a beginner guitarist, practiced just 5 minutes a day for a week. His Honor Score went from 42 to 82. This isn't about talent—it's about consistent, mindful practice. The story shows how HonorHero tracks progress, provides encouragement, and celebrates growth.

### Programmatic Usage Examples

```bash
python examples.py
```

This provides interactive examples of using HonorHero both with callbacks and programmatically, including integration scenarios for music therapy, educational platforms, and research applications.

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
