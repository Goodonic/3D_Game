import pygame
from settings import *
from map import world_map
from player import Player

# def ray_casting(sc, player_pos, player_angle):
#     cur_angle = player_angle - HALF_FOV
#     xo, yo = player_pos
#     for ray in range(NUM_RAYS):
#         sin_a = math.sin(cur_angle)
#         cos_a = math.cos(cur_angle)
#         for depth in range(MAX_DEPTH):
#             x = xo + depth * cos_a
#             y = yo + depth * sin_a
#             #pygame.draw.line(sc, DARKGRAY, player_pos, (x,y), 2)
#             if (x // TILE * TILE, y // TILE * TILE) in world_map:
#                 depth *= math.cos(player_angle - cur_angle)
#
#                 proj_height = PROJ_COEFF / depth
#
#                 c = 255 / (1 + depth * depth * 0.0000029)
#                 color = (c, c // 2, c // 3)
#                 pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
#                 break
#         cur_angle += DELTA_ANGLE

def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE
def ray_casting(sc, player_pos, player_angle):
    xo, yo = player_pos
    xm, ym = mapping(xo, yo)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # Пересечение с вертикалью
        x, dx = (xm + TILE,1 ) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - xo) / cos_a
            y = yo + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        # Пересечение с горизонталью
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WIDTH, TILE):
            depth_h = (y - yo) / sin_a
            x = xo + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE

        # Проекция
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        proj_height = PROJ_COEFF / depth
        c = 255 / (1 + depth * depth * 0.0000029)
        color = (c, c // 2, c // 3)
        pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE

