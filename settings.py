
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
# FIGHTER_ACTIONS = {
#     "Attack": "Attack",
#     "Death": "Death",
#     "Hurt": "Hurt",
#     "Idle": "Idle"
# }

FIGHTER_ACTIONS = ["Attack", "Death", "Hurt", "Idle"]
