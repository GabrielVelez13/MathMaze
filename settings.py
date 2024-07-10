import math
import pygame as pg
import sys

# Paths
DEATH_ANIMATION = "Resources/Sprites/Bringer-Of-Death/Individual Sprite/Death/"
IDLE_ANIMATION = "Resources/Sprites/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_1.png"
# Screen settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

# Player settings
PLAYER_POS = (1.5, 7.5)
PLAYER_ANGLE = 4.7
PLAYER_SPEED = 0.003
PLAYER_ROTATION = 0.002
PLAYER_SIZE_SCALE = 100

# Raycast settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
DElTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 25
SCREEM_DIST = WIDTH // 2 / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS
DELTA_ANGLE = FOV / NUM_RAYS

#textures
TEXTURE_SIZE = 260
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS