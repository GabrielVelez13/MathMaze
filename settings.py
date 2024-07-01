import math
import pygame as pg
import sys


# Screen settings
RES = WIDTH, HEIGHT = 1600, 900
FPS = 60

# Player settings
PLAYER_POS = (1.5, 1.5)
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.005
PLAYER_ROTATION = 0.002

# Raycast settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
DElTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 25
SCREEM_DIST = WIDTH // 2 / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS