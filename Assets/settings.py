import math
import pygame

# Настройки игры
WIDTH = 1520
HEIGHT = 760
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
FPS_POS = WIDTH - 65, 5
TILE = 76

# Настройки лучей
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 1520
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (3 * math.tan(HALF_FOV))
PROJ_COEFF = 6 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# Настройка спрайтов
DOUBLE_PI = 2 * math.pi
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
# Настройки текстур (1520 x 1520)
TEXTURE_WIDTH = 1000
TEXTURE_HEIGHT = 1000
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# Настройки препятствий
BLOCK_WIDTH = 700
BLOCK_HEIGHT = 700
BLOCK_SCALE = TEXTURE_WIDTH // TILE

# Настройки игрока
player_pos = (HALF_WIDTH + 25, HALF_HEIGHT)
player_angle = 0
player_speed = 1.25

# Настройки миникарты
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# Настройки мыши
SENSETIVITY = 0.0009

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
YELLOW = (255, 255, 102)