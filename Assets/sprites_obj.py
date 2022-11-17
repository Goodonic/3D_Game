import math
import pygame
from settings import *
import time
from map import collision_walls
class Sprites:
    def __init__(self):
        self.sprite_types = {
            'box': [pygame.image.load(f'Sprites/Box/{i}.png').convert_alpha() for i in range(8)]
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['box'], False, (8, 4), 0.1, 2),
            SpriteObject(self.sprite_types['box'], False, (8, 5), 0.1, 2),
            SpriteObject(self.sprite_types['box'], False, (6, 3), 0.1, 2),
            SpriteObject(self.sprite_types['box'], False, (6, 5), 0.1, 2),
            SpriteObject(self.sprite_types['box'], False, (6, 8), 0.1, 2),
            SpriteObject(self.sprite_types['box'], False, (3, 8), 0.1, 2),

        ]

class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.blocked = True
        self.side = 60
        self.x, self.y = (pos[0] - 0.5) * TILE, (pos[1] - 0.5) * TILE
        self.mx, self.my = (pos[0] - 1) * MAP_TILE, (pos[1] - 1) * MAP_TILE
        self.pos = [self.x - self.side // 2, self.y - self.side // 2]
        self.mpos = list(pos)
        self.shift = shift
        self.scale = scale

        if not static:
            self.spite_angles = [frozenset(range(i, i+45)) for i in range(0, 360, 45)]
            self.spite_position = {angle: pos for angle, pos in zip(self.spite_angles, self.object)}

    def object_locate(self, player, walls):
        fake_walls0 = [walls[0] for i in range(FAKE_RAYS)]
        fake_walls1 = [walls[-1] for i in range(FAKE_RAYS)]
        fake_walls = fake_walls0 + walls + fake_walls1

        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprites = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 100 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprites *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        if 0 <= fake_ray <= NUM_RAYS - 1 + 2 * FAKE_RAYS and distance_to_sprites < fake_walls[fake_ray][0]:
            proj_height = min(int(PROJ_COEFF / distance_to_sprites * self.scale), HEIGHT * 3)
            half_proj_haight = proj_height // 2
            shift = half_proj_haight * self.shift

            if not self.static:
                if theta < 0:
                    theta += DOUBLE_PI
                theta = 360 - int(math.degrees(theta))

                for angles in self.spite_angles:
                    if theta in angles:
                        self.object = self.spite_position[angles]
                        break

            sprite_pos = (current_ray * SCALE - half_proj_haight, HALF_HEIGHT - half_proj_haight + shift)
            sprite = pygame.transform.scale(self.object, (proj_height-10, proj_height-10))
            return (distance_to_sprites, sprite, sprite_pos)
        else:
            return (False, )

    def collision_sprites_update(self, player):
        collision_sprites = [pygame.Rect(*obj.pos, obj.side, obj.side) for obj in player.sprites.list_of_objects if obj.blocked]
        player.collision_list = collision_walls + collision_sprites

    def sprite_movement(self, player):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprites = math.sqrt(dx ** 2 + dy ** 2)
        if player.keys_control() == True and distance_to_sprites <= 100:
            # TODO Сделать логику передвижения спрайта отностильно игрока ИСПРАВЬ!
            #print(player.x, player.y)
            #print(self.x, self.y)
            # Сверху
            if player.y <= self.y and self.x + TILE-20 >= player.x >= self.x-20:
                self.y += TILE
                self.my += MAP_TILE
                self.mpos[1] += 1
                self.pos[1] += TILE
                self.collision_sprites_update(player)
                time.sleep(0.2)
            # Снизу
            elif player.y >= self.y and self.x + TILE-20 > player.x >= self.x-20:
                self.y -= TILE
                self.my -= MAP_TILE
                self.mpos[1] -= 1
                self.pos[1] -= TILE
                self.collision_sprites_update(player)
                time.sleep(0.2)
            # Слево
            elif player.x <= self.x and self.y + TILE-20 > player.y >= self.y-20:
                self.x += TILE
                self.mx += MAP_TILE
                self.mpos[0] += 1
                print(self.mpos)
                self.pos[0] += TILE
                self.collision_sprites_update(player)
                time.sleep(0.2)
            # Справо
            elif player.x >= self.x and self.y + TILE-20 > player.y >= self.y-20:
                self.x -= TILE
                self.mx -= MAP_TILE
                self.mpos[0] -= 1
                self.pos[0] -= TILE
                self.collision_sprites_update(player)
                time.sleep(0.2)

            #print("I'm working!")
            #print(distance_to_sprites, dx, dy)