# Piano Roll UI - Temporal Mirror Interface

## Overview

The Piano Roll UI is HonorHero's visual interface that acts as a **temporal mirror** of your musical performance. Unlike traditional rhythm games that throw notes at you, this interface reflects what **you** are creating in real-time.

## Philosophy

> "Si el músico genera notas, entonces la UI es un espejo temporal de su ejecución."

The Piano Roll UI embodies HonorHero's core philosophy:
- **The music comes from you** - There's no backing track to follow
- **The UI accompanies, not judges** - It shows your journey without criticism
- **Presence over perfection** - It measures your musical presence, not perfection

## What It Shows

The piano roll displays three temporal dimensions of your performance:

1. **Past (Left side)** - What you played 3 seconds ago
2. **Present (Right side)** - What you're playing now  
3. **Trend (Bottom indicator)** - Where your performance is heading

```
┌────┬────────────────────────────────────────────────────────────────┐
│NOTA│           ← PASADO                    PRESENTE →                │
├────┼────────────────────────────────────────────────────────────────┤
  C5 │                                                  █              │
  B4 │                                          ▓                      │
  A4 │                                  ▓                              │
  G4 │                          ▒                                      │
  F4 │                  ▒                                              │
  E4 │          ░                                                      │
  D4 │  ░                                                              │
  C4 │                                                                 │
└────┴────────────────────────────────────────────────────────────────┘
```

## Visual Elements

### Note Representation

Notes are displayed with characters that represent their velocity/dynamics:
- `█` - **Forte** (strong, loud)
- `▓` - **Mezzo** (medium)
- `▒` - **Piano** (soft)
- `░` - **Pianissimo** (very soft)

### Color Coding

Performance quality is indicated with colors based on the Honor Score:
- 🟢 **Green** (80-100) - Íntegro (integrated, complete)
- 🔵 **Blue** (60-79) - Firme (firm, solid)
- 🟡 **Yellow** (40-59) - Inestable (unstable)
- 🔴 **Red** (0-39) - Fragmentado (fragmented)

### Trend Indicators

The trend line shows where your performance is heading:
- `↗↗` - Improving rapidly
- `↗` - Improving
- `→` - Stable
- `↘` - Declining
- `↘↘` - Declining rapidly

## Usage

### Basic Usage

```bash
# Launch with default settings
python piano_roll_ui.py

# Quick practice session
python piano_roll_ui.py --profile beginner --mode short

# Extended practice with custom time window
python piano_roll_ui.py --mode focus --window 5
```

### Command-Line Options

- `--profile` - User profile: `beginner`, `intermediate`, `advanced`, `therapy`
- `--mode` - Session mode: `short` (3 min), `focus` (10 min), `free` (unlimited)
- `--duration` - Custom duration in seconds (overrides mode)
- `--window` - Time window to display in seconds (default: 3)

### Examples

```bash
# Beginner practicing for 3 minutes
python piano_roll_ui.py --profile beginner --mode short

# Intermediate with 5-second time window
python piano_roll_ui.py --profile intermediate --window 5

# Therapeutic session with no time limit
python piano_roll_ui.py --profile therapy --mode free

# Custom 2-minute session
python piano_roll_ui.py --duration 120
```

## Features

### Temporal Buffer
- Stores recent notes (up to 100)
- Automatically manages note history
- Displays notes within the configurable time window

### Real-Time Analysis
- Pitch detection and mapping to musical notes
- Velocity/dynamics tracking
- Score calculation and trend analysis
- Component metrics (pitch, timing, rhythm, dynamics, consistency)

### Performance Feedback
- Honor Score with qualitative tiers
- Trend indicators showing improvement/decline
- Component breakdowns
- Human-friendly messages

## Display Range

The piano roll covers a range of 5 octaves:
- **Lowest note**: C2 (65.41 Hz)
- **Highest note**: B6 (1975.53 Hz)
- **Total rows**: 60 (12 notes × 5 octaves)

This range accommodates most vocal and instrumental performances.

## How It Works

1. **Audio Capture**: Your microphone captures live audio
2. **Analysis**: HonorHero's engine analyzes pitch, timing, dynamics
3. **Note Extraction**: Detected pitches are converted to musical notes
4. **Temporal Buffer**: Notes are stored with timestamps
5. **Visualization**: The piano roll displays notes within the time window
6. **Updates**: Display refreshes at ~10 FPS for smooth visualization

## Technical Details

### Dependencies
- Python 3.8+
- NumPy - Numerical operations
- Librosa - Audio analysis and note conversion
- SoundDevice - Audio capture
- HonorHero engine modules

### Architecture

```
PianoRollUI
├── Temporal buffer (deque)
├── Display configuration
│   ├── Octave range (C2-C6)
│   ├── Display width (80 chars)
│   └── Update throttling (10 FPS)
├── HonorHero engine integration
└── Real-time rendering
```

## Comparison: Standard UI vs Piano Roll UI

| Feature | Standard UI | Piano Roll UI |
|---------|-------------|---------------|
| Display | Metrics & scores | Visual note timeline |
| Focus | Current performance | Temporal journey |
| Feedback | Numbers & text | Visual patterns |
| Best for | Tracking scores | Seeing musical flow |

Both interfaces use the same HonorHero engine and can be used interchangeably based on your preference.

## Use Cases

### Practice Sessions
- **Warm-ups**: See your range and dynamics visually
- **Technical practice**: Track consistency in scales and arpeggios
- **Expression work**: Visualize dynamic variations

### Learning
- **Beginner musicians**: Visual feedback on note accuracy
- **Pitch training**: See how close you are to target notes
- **Rhythm work**: Observe timing patterns

### Therapy & Mindfulness
- **Music therapy**: Non-judgmental visual feedback
- **Stress relief**: Focus on the flowing patterns
- **Meditation**: Use music as a mindful practice

## Tips for Best Experience

1. **Start with longer time windows** (5 seconds) to see more context
2. **Use beginner profile** initially - more forgiving thresholds
3. **Watch the trend indicator** - it shows your improvement over time
4. **Experiment with dynamics** - try playing softly and loudly
5. **Don't chase perfection** - embrace the journey

## Demo Mode

Try the demo to see the interface without needing audio setup:

```bash
python demo_piano_roll.py
```

This simulates a C major scale performance to showcase the visualization.

## Philosophy in Practice

The Piano Roll UI is designed for **accompaniment, not judgment**:

- ✅ Shows your musical expression
- ✅ Reflects your journey in real-time
- ✅ Celebrates presence and effort
- ✅ Encourages exploration

- ❌ Doesn't punish mistakes
- ❌ Doesn't compare to others
- ❌ Doesn't impose external standards

## Future Enhancements

Potential additions being considered:
- Multiple instrument views (vocal range, guitar fretboard, etc.)
- Note duration visualization (sustained notes)
- Chord detection and display
- Recording and playback with piano roll
- Export as MIDI or sheet music

---

*"La música es el viaje, no el destino. El piano roll es tu mapa temporal."*

**The performance never stops. The mirror simply reflects.**
