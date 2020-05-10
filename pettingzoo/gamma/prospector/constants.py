import math

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1280, 720)
BACKGROUND_COLOR = (217, 151, 106)
FPS = 15

# FENCE_WIDTH = 100
FENCE_WIDTH = 22
WATER_HEIGHT = 100

# AGENT_RADIUS = 16.5
AGENT_RADIUS = 15
AGENT_DIAMETER = AGENT_RADIUS * 2
# The 3 is for RBG values
OBSERVATION_SIDE_LENGTH = 5 * AGENT_DIAMETER
OBSERVATION_SHAPE = (OBSERVATION_SIDE_LENGTH, OBSERVATION_SIDE_LENGTH, 3)

MAX_SPRITE_ROTATION = math.pi / 4

NUM_PROSPECTORS = 4
NUM_BANKERS = 3
NUM_AGENTS = NUM_PROSPECTORS + NUM_BANKERS

PROSPECTOR_SPEED = 150
BANKER_SPEED = 100
BANKER_HANDOFF_TOLERANCE = math.pi / 4
TWO_PI = math.pi * 2.0

FENCE_COLLISION_BUFFER = AGENT_DIAMETER
VERT_FENCE_HEIGHT = SCREEN_HEIGHT - WATER_HEIGHT
# VERT_FENCE_WIDTH =

# For the left and right fences
FENCE_VERT_VERTICES = (
    (0, 0),
    (FENCE_WIDTH + FENCE_COLLISION_BUFFER, 0),
    (FENCE_WIDTH + FENCE_COLLISION_BUFFER, VERT_FENCE_HEIGHT),
    (0, VERT_FENCE_HEIGHT),
)

# For the top fence
FENCE_HORIZ_VERTICES = (
    (0, 0),
    (SCREEN_WIDTH, 0),
    (SCREEN_WIDTH, FENCE_WIDTH + FENCE_COLLISION_BUFFER),
    (0, FENCE_WIDTH + FENCE_COLLISION_BUFFER),
)

FENCE_INFO = [
    ("left", [0, 0], [0, 0], FENCE_VERT_VERTICES),  # left boundary
    ("top", [0, 0], [0, 0], FENCE_HORIZ_VERTICES),  # top boundary
    (
        "right",
        [SCREEN_WIDTH - FENCE_WIDTH, 0],
        [SCREEN_WIDTH - (FENCE_WIDTH + FENCE_COLLISION_BUFFER), 0],
        FENCE_VERT_VERTICES,
    ),
]

BANK_SIZE = BANK_WIDTH, BANK_HEIGHT = 184, 100

BANK_VERTS = (
    (0, 0),
    (BANK_WIDTH, 0),
    (BANK_WIDTH, BANK_HEIGHT),
    (0, BANK_HEIGHT),
)

BANK_INFO = [
    ([184 * 1, 50], BANK_VERTS),
    ([184 * 3, 50], BANK_VERTS),
    ([184 * 5, 50], BANK_VERTS),
]

WATER_INFO = [
    (0, SCREEN_HEIGHT - WATER_HEIGHT),  # position
    (  # vertices
        (0, 0),
        (SCREEN_WIDTH, 0),
        (SCREEN_WIDTH, WATER_HEIGHT),
        (0, WATER_HEIGHT),
    ),
]
