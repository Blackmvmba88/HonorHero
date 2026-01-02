# HonorHero Examples 🎵

This directory contains concrete examples demonstrating HonorHero in action. Each example includes simulated session data in JSON format and shows how HonorHero evaluates performance with encouragement rather than judgment.

## Overview

HonorHero exists to reflect your musical journey, not to dominate it. These examples illustrate real-world scenarios where HonorHero provides supportive, constructive feedback.

## Example Files

### Example 1: Juan's Beginner Guitar Session
**File:** `example1_juan_beginner.json`

Juan, a beginner guitarist, practices for the first time with HonorHero.

**Honor Score:** 42  
**Tier:** Inestable

**Console Output:**
```
═══════════════════════════════════════════════════════════
               🎵 HonorHero Performance Report
═══════════════════════════════════════════════════════════

        Honor Score: 42
        Tier: Inestable

Feedback:
- Timing is improving, but rhythm varies.
- Pitch accuracy is within a healthy learning range.
- Keep playing — consistency grows with time.

═══════════════════════════════════════════════════════════
```

**Key Insight:** Juan doesn't "fail". He receives a snapshot of where he is right now.

---

### Example 2: Daily Practice Tracking
**Files:** `example2_daily_tracking_day1.json`, `example2_daily_tracking_day4.json`, `example2_daily_tracking_day7.json`

Juan practices 5 minutes a day for a week. After several sessions, he runs:

```bash
python view_stats.py
```

**Progress Summary:**
```
Day 1: 42 (Inestable)
Day 4: 63 (Firme)
Day 7: 82 (Íntegro)
```

**HonorHero shows:**
- Average Honor Score per day
- Improvement trends
- Practice streaks

**Key Insight:** Progress is visible, measurable, and motivating — without pressure.

---

### Example 3: Vocal Practice (Shy Vocalist)
**File:** `example3_shy_vocalist.json`

A shy vocalist practices alone at night using a microphone.

**Honor Score:** 71  
**Tier:** Firme

**HonorHero adapts:**
- Tolerant pitch thresholds
- Gentle dynamics analysis
- No harsh penalties for instability

**Console Output:**
```
═══════════════════════════════════════════════════════════
               🎵 HonorHero Performance Report
═══════════════════════════════════════════════════════════

        Honor Score: 71
        Tier: Firme

Feedback:
- Expressive dynamics detected.
- Pitch confidence increased during sustained notes.
- Excellent emotional continuity.

The system acts like a supportive coach, not a judge.

═══════════════════════════════════════════════════════════
```

**Key Insight:** The system acts like a supportive coach, not a judge.

---

### Example 4: Programmatic Use (Developers)
**File:** `example4_programmatic_use.json`

HonorHero can be embedded into other tools or experiments.

**Use Cases:**
- Custom UI development
- Music therapy software
- Educational platforms
- Research on performance consistency

**Example Code:**
```python
from honorhero import HonorHero

# Create engine
engine = HonorHero()

# Define callback for real-time updates
def on_update(metrics):
    print(f"Score: {metrics['honor_score']:.1f}")
    print(f"Tier: {metrics['tier']}")
    # Store metrics in database
    db.save_metrics(metrics)

# Start performance evaluation
engine.start_performance(on_update)

# ... perform music ...

# Stop and get final results
results = engine.stop_performance()
print(f"Final Score: {results['final_honor_score']:.1f}")
```

**Key Insight:** Real-time metrics can be accessed through callbacks and stored for later analysis, making HonorHero suitable for musicians, educators, therapists, and developers.

---

### Example 5: What HonorHero Is NOT
**File:** `example5_what_honorhero_is_not.json`

**HonorHero does not:**
- ❌ Rank musicians against each other
- ❌ Enforce rigid "perfect" timing
- ❌ Punish mistakes
- ❌ Replace teachers or human judgment

**HonorHero exists to reflect, not to dominate.**

#### Comparison: Traditional Grading vs HonorHero

| Aspect | Traditional Grading | HonorHero |
|--------|-------------------|-----------|
| **Focus** | Absolute performance against a standard | Personal growth and consistency |
| **Feedback** | Pass/Fail, Letter grades | Qualitative tiers with encouragement |
| **Competition** | Ranked against peers | Compare with your own history |
| **Mistakes** | Penalized, subtract points | Measured as learning opportunities |
| **Goal** | Meet external standards | Improve through mindful practice |

---

## Running the Examples

### View Example Data
```bash
# View a specific example
cat examples/example1_juan_beginner.json | python -m json.tool

# View all examples
ls examples/*.json
```

### Simulate Juan's Week
To see the progression from Day 1 to Day 7:
```bash
python -c "
import json
for day in [1, 4, 7]:
    with open(f'examples/example2_daily_tracking_day{day}.json') as f:
        data = json.load(f)
        s = data['session']
        print(f\"Day {day}: {s['honor_score']} ({s['tier']})\")
"
```

Output:
```
Day 1: 42 (Inestable)
Day 4: 63 (Firme)
Day 7: 82 (Íntegro)
```

### Try Your Own Session
```bash
# Run HonorHero UI
python ui.py --duration 30

# View your stats
python view_stats.py
```

---

## Session Data Format

All example files follow this JSON structure:

```json
{
  "description": "Brief description of the scenario",
  "scenario": "Detailed context",
  "session": {
    "timestamp": "ISO 8601 timestamp",
    "date": "YYYY-MM-DD",
    "time": "HH:MM:SS",
    "honor_score": 0-100,
    "tier": "Íntegro | Firme | Inestable | Fragmentado",
    "duration": 300,
    "components": {
      "pitch": 0-100,
      "timing": 0-100,
      "rhythm": 0-100,
      "dynamics": 0-100,
      "consistency": 0-100
    },
    "feedback": {
      "summary": "Natural language summary",
      "highlights": ["Key observations"]
    }
  }
}
```

---

## Visualizing Your Journey

### ASCII Session Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Start Practice Session                   │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│              🎤 Audio Capture (Microphone)                  │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│              Real-time Analysis Every ~0.5s                 │
│  ┌────────────┬────────────┬────────────┬──────────────┐   │
│  │   Pitch    │  Timing/   │  Dynamics  │ Consistency  │   │
│  │  Analyzer  │   Rhythm   │  Analyzer  │   Analyzer   │   │
│  └────────────┴────────────┴────────────┴──────────────┘   │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│                   Calculate Honor Score                     │
│                   (Weighted Average)                        │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│                 Assign Qualitative Tier                     │
│   Íntegro (80-100) | Firme (60-79) | Inestable (40-59)    │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│            Generate Encouraging Feedback                    │
│     "Tu dinámica está sólida, pero timing necesita          │
│                      atención"                              │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│              Display to User & Save to History              │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
                 (Loop until session ends)
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│                   Final Performance Report                  │
│            • Honor Score & Tier                             │
│            • Component Breakdown                            │
│            • Progress Comparison                            │
│            • Encouragement & Next Steps                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Philosophy in Action

These examples demonstrate HonorHero's core philosophy:

1. **No Failure, Only Snapshots** - Juan's Score of 42 isn't a failure; it's a starting point.

2. **Progress Over Perfection** - The week-long journey from 42 to 82 shows measurable growth.

3. **Adaptation to Context** - The shy vocalist receives gentle, supportive feedback.

4. **Extensibility** - Developers can integrate HonorHero into therapy, education, and research.

5. **Human-Centered Design** - Every interaction reinforces growth mindset over competition.

---

## Next Steps

Want to see these examples in action?

1. **Try the interactive demo:**
   ```bash
   python examples.py
   ```

2. **Read Juan's full story:**
   ```bash
   python juan_story.py
   ```

3. **Start your own practice:**
   ```bash
   python ui.py
   ```

4. **Check your progress:**
   ```bash
   python view_stats.py
   ```

---

*"La música es el arte de organizar el sonido en el tiempo. HonorHero es el arte de celebrar ese viaje."* 🎶
