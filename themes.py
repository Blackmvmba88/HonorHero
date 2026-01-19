"""
HonorHero Theme System
Visual identity and aesthetic configuration for different profiles and modes
Provides color palettes, icons, and visual feedback elements
"""

# ANSI Color Codes
class Colors:
    """ANSI color codes for terminal output"""
    # Reset
    RESET = '\033[0m'
    
    # Standard colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Dark colors
    DARK_RED = '\033[31m'
    DARK_GREEN = '\033[32m'
    DARK_YELLOW = '\033[33m'
    DARK_BLUE = '\033[34m'
    DARK_MAGENTA = '\033[35m'
    DARK_CYAN = '\033[36m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'


# Icon and Symbol Sets
class Icons:
    """Visual icons for different UI elements"""
    # Emojis and symbols
    MUSIC = '🎵'
    MICROPHONE = '🎤'
    TROPHY = '🏆'
    FIRE = '🔥'
    STAR = '⭐'
    SPARKLES = '✨'
    MEDAL = '🏅'
    CHART = '📊'
    ROCKET = '🚀'
    HEART = '❤️'
    CROWN = '👑'
    GEM = '💎'
    
    # Progress indicators
    CHECK = '✓'
    CROSS = '✗'
    ARROW_UP = '↑'
    ARROW_DOWN = '↓'
    ARROW_RIGHT = '→'
    
    # Animations
    PARTICLES = ['✨', '⭐', '💫', '🌟']
    WAVES = ['~', '≈', '∼', '≋']
    PROGRESS = ['▱', '▰']
    
    # Bars
    BAR_FULL = '█'
    BAR_SEVEN_EIGHTHS = '▉'
    BAR_THREE_QUARTERS = '▊'
    BAR_FIVE_EIGHTHS = '▋'
    BAR_HALF = '▌'
    BAR_THREE_EIGHTHS = '▍'
    BAR_QUARTER = '▎'
    BAR_EIGHTH = '▏'
    BAR_EMPTY = '░'


# Theme Palettes
class ThemePalette:
    """Color palette for a specific theme"""
    
    def __init__(self, name, colors_dict):
        self.name = name
        self.primary = colors_dict.get('primary', Colors.CYAN)
        self.secondary = colors_dict.get('secondary', Colors.BLUE)
        self.success = colors_dict.get('success', Colors.GREEN)
        self.warning = colors_dict.get('warning', Colors.YELLOW)
        self.error = colors_dict.get('error', Colors.RED)
        self.info = colors_dict.get('info', Colors.CYAN)
        self.accent = colors_dict.get('accent', Colors.MAGENTA)
        self.text = colors_dict.get('text', Colors.WHITE)
        self.dim_text = colors_dict.get('dim_text', Colors.DIM + Colors.WHITE)
        self.background = colors_dict.get('background', Colors.BLACK)


# Pre-defined Theme Palettes
THEMES = {
    'warm': ThemePalette('Warm (Therapeutic)', {
        'primary': Colors.YELLOW,
        'secondary': '\033[38;5;214m',  # Orange
        'success': Colors.GREEN,
        'warning': Colors.YELLOW,
        'error': '\033[38;5;209m',  # Soft pink/coral
        'info': Colors.CYAN,
        'accent': Colors.MAGENTA,
        'text': Colors.WHITE,
        'dim_text': Colors.DIM + Colors.WHITE
    }),
    
    'cool': ThemePalette('Cool (Precision)', {
        'primary': Colors.CYAN,
        'secondary': Colors.BLUE,
        'success': Colors.GREEN,
        'warning': Colors.YELLOW,
        'error': Colors.RED,
        'info': Colors.CYAN,
        'accent': '\033[38;5;147m',  # Light blue
        'text': Colors.WHITE,
        'dim_text': Colors.DIM + Colors.WHITE
    }),
    
    'colorblind': ThemePalette('Colorblind Accessible', {
        'primary': Colors.BOLD + Colors.WHITE,
        'secondary': Colors.CYAN,
        'success': Colors.BLUE,  # Blue instead of green
        'warning': Colors.BOLD + Colors.YELLOW,
        'error': Colors.BOLD + Colors.MAGENTA,  # Magenta instead of red
        'info': Colors.CYAN,
        'accent': Colors.BOLD + Colors.CYAN,
        'text': Colors.WHITE,
        'dim_text': Colors.DIM + Colors.WHITE
    }),
    
    'monochrome': ThemePalette('Monochrome', {
        'primary': Colors.BOLD + Colors.WHITE,
        'secondary': Colors.WHITE,
        'success': Colors.BOLD + Colors.WHITE,
        'warning': Colors.DIM + Colors.WHITE,
        'error': Colors.BOLD + Colors.WHITE,
        'info': Colors.WHITE,
        'accent': Colors.UNDERLINE + Colors.WHITE,
        'text': Colors.WHITE,
        'dim_text': Colors.DIM + Colors.WHITE
    }),
    
    'dark': ThemePalette('Dark Mode', {
        'primary': Colors.CYAN,
        'secondary': Colors.BLUE,
        'success': Colors.GREEN,
        'warning': Colors.YELLOW,
        'error': Colors.RED,
        'info': Colors.CYAN,
        'accent': Colors.MAGENTA,
        'text': Colors.WHITE,
        'dim_text': Colors.DIM + Colors.WHITE
    }),
    
    'light': ThemePalette('Light Mode', {
        'primary': Colors.DARK_CYAN,
        'secondary': Colors.DARK_BLUE,
        'success': Colors.DARK_GREEN,
        'warning': Colors.DARK_YELLOW,
        'error': Colors.DARK_RED,
        'info': Colors.DARK_CYAN,
        'accent': Colors.DARK_MAGENTA,
        'text': Colors.BLACK,
        'dim_text': Colors.DIM + Colors.BLACK
    })
}


# Profile-specific themes
PROFILE_THEMES = {
    'beginner': 'warm',       # Warm colors for comfort and encouragement
    'intermediate': 'cool',   # Cool colors for balanced focus
    'advanced': 'cool',       # Precise, technical feel
    'therapy': 'warm'         # Soft, comforting colors
}


class VisualFeedback:
    """
    Visual feedback elements for real-time performance feedback
    """
    
    @staticmethod
    def particle_effect(count=3):
        """Generate particle effect string"""
        import random
        particles = random.sample(Icons.PARTICLES, min(count, len(Icons.PARTICLES)))
        return ' '.join(particles)
    
    @staticmethod
    def wave_effect(intensity=0.5):
        """Generate wave effect based on intensity"""
        wave_char = Icons.WAVES[int(intensity * (len(Icons.WAVES) - 1))]
        return wave_char * 5
    
    @staticmethod
    def progress_indicator(current, total, width=20):
        """Generate progress bar indicator"""
        filled = int((current / total) * width)
        return Icons.BAR_FULL * filled + Icons.BAR_EMPTY * (width - filled)
    
    @staticmethod
    def trend_arrow(value):
        """Get trend arrow based on value"""
        if value > 0:
            return Icons.ARROW_UP
        elif value < 0:
            return Icons.ARROW_DOWN
        else:
            return Icons.ARROW_RIGHT
    
    @staticmethod
    def smooth_bar(value, width=40):
        """
        Generate smooth progress bar with partial characters
        value: 0-100
        width: bar width in characters
        """
        bars = [
            Icons.BAR_EMPTY,
            Icons.BAR_EIGHTH,
            Icons.BAR_QUARTER,
            Icons.BAR_THREE_EIGHTHS,
            Icons.BAR_HALF,
            Icons.BAR_FIVE_EIGHTHS,
            Icons.BAR_THREE_QUARTERS,
            Icons.BAR_SEVEN_EIGHTHS,
            Icons.BAR_FULL
        ]
        
        # Calculate filled portion
        filled_exact = (value / 100) * width
        filled_full = int(filled_exact)
        remainder = filled_exact - filled_full
        
        # Select partial character
        partial_index = int(remainder * (len(bars) - 1))
        
        # Build bar
        bar = Icons.BAR_FULL * filled_full
        if filled_full < width and partial_index > 0:
            bar += bars[partial_index]
            bar += Icons.BAR_EMPTY * (width - filled_full - 1)
        else:
            bar += Icons.BAR_EMPTY * (width - filled_full)
        
        return bar


def get_theme(theme_name=None, profile=None):
    """
    Get theme palette by name or profile
    
    Args:
        theme_name: Explicit theme name ('warm', 'cool', 'colorblind', etc.)
        profile: Profile name to get default theme for
    
    Returns:
        ThemePalette instance
    """
    if theme_name and theme_name in THEMES:
        return THEMES[theme_name]
    elif profile and profile in PROFILE_THEMES:
        return THEMES[PROFILE_THEMES[profile]]
    else:
        return THEMES['cool']  # Default


def get_score_color(score, theme):
    """
    Get color for a score value based on theme
    
    Args:
        score: Score value (0-100)
        theme: ThemePalette instance
    
    Returns:
        ANSI color code
    """
    if score >= 80:
        return theme.success
    elif score >= 60:
        return theme.info
    elif score >= 40:
        return theme.warning
    else:
        return theme.error


def format_with_theme(text, color, reset=True):
    """
    Format text with color and optional reset
    
    Args:
        text: Text to format
        color: ANSI color code
        reset: Whether to append reset code
    
    Returns:
        Formatted string
    """
    if reset:
        return f"{color}{text}{Colors.RESET}"
    else:
        return f"{color}{text}"
