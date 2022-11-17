import pygame
from settings import *
from map import world_map
from player import Player

def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE

def ray_casting(player, textures):
    walls = []
    xo, yo = player.pos
    texture_v, texture_h = '1', '1'
    xm, ym = mapping(xo, yo)
    cur_angle = player.angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # Пересечение с вертикалью
        x, dx = (xm + TILE,1 ) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - xo) / cos_a
            yv = yo + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        # Пересечение с горизонталью
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WIDTH, TILE):
            depth_h = (y - yo) / sin_a
            xh = xo + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        # Пересечение со спрайтом
        # Горизонталь TODO сделать также как рейкастинг только проверять пересечение с ректом спрайта


        # Проекция
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % TILE
        depth *= math.cos(player.angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(PROJ_COEFF / depth), HEIGHT * 2)

        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column,(SCALE, proj_height))
        wall_pos = ray * SCALE,HALF_HEIGHT - proj_height // 2
        walls.append((depth, wall_column, wall_pos))
        cur_angle += DELTA_ANGLE
        
    return walls
