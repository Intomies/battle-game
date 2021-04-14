
# Main settings
BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

# Fighter settings
FIGHTER_START_POSITIONS = {
    "Knight": [
        300,
        200,
        100
    ],
    "Bandit": [
        500,
        600,
        700
    ]
}
FIGHTER_HEIGHT = {
    "Knight": 260,
    "Bandit": 270
}
FIGHTER_IMAGE_SCALE = 3
FIGHTER_ACTIONS = [
    "attack", 
    "death", 
    "hurt", 
    "idle"
]
MAX_AMOUNT_OF_ENEMIES = 3
MIN_AMOUNT_OF_ENEMIES = 1

# Interface settings

HEALTH_BAR_POSITIONS_X = {
    "Knight": 100,
    "Bandit": 500
}
HEALTH_BAR_POSITIONS_Y = [
    SCREEN_HEIGHT - BOTTOM_PANEL + 30,
    SCREEN_HEIGHT - BOTTOM_PANEL + 70,
    SCREEN_HEIGHT - BOTTOM_PANEL + 110
]
HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 150

# Colors settings

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
