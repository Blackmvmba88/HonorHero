# HonorHero Quick Start Guide

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Blackmvmba88/HonorHero.git
   cd HonorHero
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

### Option 1: View Juan's Inspiring Story

Perfect for understanding what HonorHero can do:

```bash
python juan_story.py
```

See how Juan improved from a score of 42 to 82 in just one week of 5-minute daily practice sessions!

### Option 2: Run the Demo (No Microphone Required)

Perfect for testing the system without audio input:

```bash
python demo.py
```

Or specify duration:
```bash
python demo.py --duration 15
```

### Option 3: Run with Live Audio

If you have a microphone:

```bash
python ui.py
```

Press Ctrl+C to stop and see results. Your session will be automatically saved.

### Option 4: View Your Progress

After completing some sessions:

```bash
python view_stats.py
```

This shows your practice history, improvement trends, and statistics.

### Option 5: Run Examples

```bash
python examples.py
```

Choose from interactive examples.

## Understanding Your Results

### Honor Score Tiers

- **Íntegro (80-100)**: Excellent! Your performance shows integrity and mastery
- **Firme (60-79)**: Very good! Your performance is solid and consistent
- **Inestable (40-59)**: Good attempt. Keep practicing for more stability
- **Fragmentado (0-39)**: Keep practicing. Each attempt brings you closer

### Component Breakdown

Your Honor Score is calculated from:

1. **Pitch (25%)**: How accurately you hit the intended notes
2. **Timing (20%)**: How well you time your note entrances
3. **Rhythm (20%)**: How consistently you maintain rhythm patterns
4. **Dynamics (15%)**: How well you control volume and expression
5. **Consistency (20%)**: Overall stability across all metrics

### Session History

Every session is automatically saved to `~/.honorhero/sessions.json`. You can:
- Track your progress over time
- See improvement trends
- Compare today's performance with previous sessions
- Build practice streaks

### Human-Friendly Feedback

Instead of just numbers, HonorHero gives you context:
- "Good control, although you sped up a bit"
- "Your pitch improved but dynamics dropped"
- "Today you're better than yesterday in rhythm"

This is coaching, not just measurement.

## Tips for Better Scores

1. **Practice in a quiet environment**: Background noise affects analysis
2. **Use a good microphone**: Better audio quality = better analysis
3. **Focus on consistency**: Consistent mistakes are better than erratic perfection
4. **Don't chase perfect scores**: Focus on improving your weakest areas
5. **Track your progress**: Use multiple sessions to see improvement over time

## Customization

Edit `config.py` to adjust:

- Tolerance thresholds (make evaluation more/less forgiving)
- Component weights (emphasize different aspects)
- Audio settings (sample rate, buffer size)

Example - Make evaluation more forgiving:
```python
PITCH_TOLERANCE = 75  # From 50 to 75 cents
TIMING_TOLERANCE = 0.25  # From 0.15 to 0.25 seconds
```

## Troubleshooting

### "No audio input detected"
- Check microphone permissions
- Verify microphone is plugged in
- Try running `python -c "import sounddevice; print(sounddevice.query_devices())"`

### "Module not found" errors
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.8+)

### Low scores despite good performance
- Adjust tolerances in `config.py`
- Check for background noise
- Ensure microphone is close enough

## Next Steps

- Read `DOCUMENTATION.md` for technical details
- Explore the code to understand how it works
- Customize thresholds for your needs
- Add new analysis dimensions
- Share your progress!

## Philosophy

Remember: **The performance never stops. Mistakes are measured, not punished.**

HonorHero is about self-improvement, not competition. Each session is an opportunity to learn and grow.

¡Buena suerte! 🎵
