# New Features Guide

## User Profiles

HonorHero now supports different user profiles to accommodate musicians at various skill levels and use cases.

### Available Profiles

#### 1. Beginner (Súper Principiante)
**Perfect for:** Complete beginners, first-time musicians, exploratory practice
- Most tolerant pitch detection (±70 cents)
- Generous timing tolerance (±0.20 seconds)
- Flexible rhythm variance (±25%)
- Wide dynamics range (±20 dB)
- Lower consistency threshold (60%)

**Use when:** Starting your musical journey, trying a new instrument, or practicing in a non-judgmental way.

```bash
python ui.py --profile beginner
```

#### 2. Intermediate (Intermedio) - DEFAULT
**Perfect for:** Regular practitioners, developing musicians
- Balanced pitch tolerance (±50 cents)
- Moderate timing tolerance (±0.15 seconds)
- Standard rhythm variance (±20%)
- Moderate dynamics range (±15 dB)
- Standard consistency threshold (70%)

**Use when:** You have some experience and want a balanced evaluation.

```bash
python ui.py --profile intermediate
# or simply
python ui.py
```

#### 3. Advanced (Avanzado)
**Perfect for:** Experienced musicians, performance preparation
- Strict pitch tolerance (±30 cents)
- Tight timing tolerance (±0.10 seconds)
- Precise rhythm variance (±15%)
- Narrow dynamics range (±10 dB)
- High consistency threshold (80%)

**Use when:** Preparing for performances, refining technique, or challenging yourself.

```bash
python ui.py --profile advanced
```

#### 4. Therapy (Terapia / Rehabilitación)
**Perfect for:** Music therapy, rehabilitation, adaptive music education
- Maximum pitch tolerance (±100 cents)
- Very generous timing tolerance (±0.30 seconds)
- Very flexible rhythm variance (±35%)
- Widest dynamics range (±25 dB)
- Lowest consistency threshold (50%)

**Use when:** Using music for therapeutic purposes, rehabilitation, or adaptive needs.

```bash
python ui.py --profile therapy
```

## Session Modes

Control the duration of your practice sessions with predefined modes.

### Available Modes

#### 1. Short (Sesión Corta)
**Duration:** 3 minutes
**Perfect for:** Quick warmups, busy schedules, focused micro-practice

```bash
python ui.py --mode short
```

#### 2. Focus (Sesión Profunda)
**Duration:** 10 minutes
**Perfect for:** Concentrated practice, skill development, daily routine

```bash
python ui.py --mode focus
```

#### 3. Free (Sesión Libre) - DEFAULT
**Duration:** Unlimited (until Ctrl+C)
**Perfect for:** Exploratory practice, jam sessions, extended practice

```bash
python ui.py --mode free
# or simply
python ui.py
```

### Combining Profiles and Modes

You can combine profiles and modes for customized practice sessions:

```bash
# Quick beginner practice
python ui.py --profile beginner --mode short

# Advanced focused session
python ui.py --profile advanced --mode focus

# Therapeutic free session
python ui.py --profile therapy --mode free
```

### Custom Duration Override

You can override the mode's default duration with `--duration`:

```bash
# 60-second intermediate practice
python ui.py --profile intermediate --duration 60

# 5-minute advanced practice (300 seconds)
python ui.py --profile advanced --duration 300
```

## Enhanced Statistics View

The `view_stats.py` script now includes enhanced features:

### New Features

1. **🔥 Streak Tracking with Emoji**
   - Shows your current practice streak in days
   - 🔥 emoji for streaks ≥7 days
   - ⭐ emoji for shorter streaks

2. **🏆 Best Honor Score Highlighting**
   - Your all-time best score is clearly marked

3. **📅 Weekly View**
   - Shows last 7 days of practice
   - Daily average scores with tier classification
   - Identifies gaps in practice schedule

4. **⏱️ Improved Time Formatting**
   - Shows hours, minutes, and seconds
   - Examples: "1h 15m", "25m 30s", "45s"

### Usage

```bash
python view_stats.py
```

### Example Output

```
======================================================================
📊  ESTADÍSTICAS DE PRÁCTICA
======================================================================

┌─ RESUMEN GENERAL ──────────────────────────────────────────────────┐
│ Total de sesiones:    12                                           │
│ Tiempo total:         1h 15m                                       │
│ Puntuación promedio:  68.5                                         │
│ 🏆 Mejor puntuación:  82.0                                         │
│ Tier más común:       Firme                                        │
│ 🔥 Racha actual:      5 días                                       │
└────────────────────────────────────────────────────────────────────┘

┌─ TU SEMANA ────────────────────────────────────────────────────────┐
│ Lun:  65 (Firme) (1 sesión)                                       │
│ Mar:  70 (Firme) (2 sesiónes)                                     │
│ Mié: --- (Sin práctica)                                           │
│ Jue:  72 (Firme) (1 sesión)                                       │
│ Vie:  68 (Firme) (1 sesión)                                       │
│ Sáb:  75 (Firme) (2 sesiónes)                                     │
│ Dom:  82 (Íntegro) (1 sesión)                                     │
└────────────────────────────────────────────────────────────────────┘
```

## Philosophy Alignment

All new features align with HonorHero's core philosophy:

✅ **Interpretación consciente, no perfección vacía**
- Profiles encourage progress without comparison
- Therapy mode validates adaptive music-making
- Modes support different practice needs

✅ **Auto-mejora, no competencia**
- No leaderboards or external comparisons
- Streak tracking celebrates consistency, not perfection
- Weekly view shows personal progress

✅ **Los errores se miden, no se castigan**
- Tolerant profiles for beginners and therapeutic use
- Advanced profiles for those ready to be challenged
- All profiles maintain encouraging feedback

## Quick Reference

### Full Command Syntax

```bash
python ui.py [--profile {beginner|intermediate|advanced|therapy}] \
             [--mode {short|focus|free}] \
             [--duration SECONDS]
```

### Common Use Cases

```bash
# Daily practice routine
python ui.py --profile intermediate --mode focus

# Morning warmup
python ui.py --profile beginner --mode short

# Performance preparation
python ui.py --profile advanced --mode focus

# Music therapy session
python ui.py --profile therapy --mode free

# Quick check-in (1 minute)
python ui.py --duration 60
```

## Testing

Run the new feature tests:

```bash
# Test profiles and modes
python test_profiles_and_modes.py

# Test enhanced statistics
python test_view_stats.py

# Test all existing functionality
python test_honorhero.py
```
