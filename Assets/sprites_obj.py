import math

import pygame
from settings import *

class Sprites:
    def __init__(self):
        self.sprite_types = {
            'box' : pygame.image.load('Sprites/Box/2.png').convert_alpha()
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['box'], True, (9.5, 7.5), 0.1, 2)
        ]
class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.shift = shift
        self.scale = scale

    def object_locate(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprites = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 100 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprites *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        if 0 <= current_ray <= NUM_RAYS - 1 and distance_to_sprites < walls[current_ray][0]:
            proj_height = int(PROJ_COEFF / distance_to_sprites * self.scale)
            half_proj_haight = proj_height // 2
            shift = half_proj_haight * self.shift

            sprite_pos = (current_ray * SCALE - half_proj_haight, HALF_HEIGHT - half_proj_haight + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (distance_to_sprites, sprite, sprite_pos)
        else:
            return (False, )