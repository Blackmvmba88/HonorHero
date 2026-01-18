#!/usr/bin/env python3
"""
Manual demonstration of new features
Shows the help text and profile/mode information
"""

import subprocess
import sys

def run_command(cmd, description):
    """Run a command and display output"""
    print("=" * 70)
    print(f"🔍 {description}")
    print("=" * 70)
    print(f"$ {cmd}")
    print()
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    print()


def main():
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + "  HONORHERO - NEW FEATURES DEMONSTRATION".center(68) + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    # Show help
    run_command(
        "cd /home/runner/work/HonorHero/HonorHero && source .venv/bin/activate && python ui.py --help",
        "UI Help - Shows new --profile and --mode options"
    )
    
    # Show different profile/mode combinations
    print()
    print("=" * 70)
    print("📋 AVAILABLE PROFILES")
    print("=" * 70)
    print()
    print("1. beginner     - Súper Principiante (más tolerante)")
    print("2. intermediate - Intermedio (balance)")
    print("3. advanced     - Avanzado (más estricto)")
    print("4. therapy      - Terapia / Rehabilitación (máxima tolerancia)")
    print()
    
    print("=" * 70)
    print("⏱️  AVAILABLE MODES")
    print("=" * 70)
    print()
    print("1. short - Sesión Corta (3 minutos)")
    print("2. focus - Sesión Profunda (10 minutos)")
    print("3. free  - Sesión Libre (sin límite)")
    print()
    
    print("=" * 70)
    print("💡 EXAMPLE COMMANDS")
    print("=" * 70)
    print()
    print("# Quick practice session for beginners:")
    print("python ui.py --profile beginner --mode short")
    print()
    print("# Focused advanced practice:")
    print("python ui.py --profile advanced --mode focus")
    print()
    print("# Therapeutic session with no time limit:")
    print("python ui.py --profile therapy --mode free")
    print()
    print("# Override duration:")
    print("python ui.py --profile intermediate --duration 60")
    print()
    
    print("=" * 70)
    print("📊 VIEW STATISTICS")
    print("=" * 70)
    print()
    print("# View your practice history and weekly progress:")
    print("python view_stats.py")
    print()
    print("Enhanced features:")
    print("  • 🔥 Streak tracking with emoji")
    print("  • 🏆 Best Honor Score highlighted")
    print("  • 📅 Weekly view showing last 7 days")
    print("  • ⏱️  Better time formatting (hours + minutes)")
    print()
    
    print("=" * 70)
    print("✨ All features implemented successfully! ✨")
    print("=" * 70)
    print()


if __name__ == '__main__':
    main()
