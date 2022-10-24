from settings import *
import pygame
from ray_casting import ray_casting
from map import world_map, mini_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.Font('Fonts/Button_Font/Elfboyclassic.ttf', 24)
        self.textures = {'1':pygame.image.load('Sprites/wall.jpg').convert(),
                         '2':pygame.image.load('Sprites/wall2.jpg').convert()
                         }
    def background(self):
        pygame.draw.rect(self.sc, BLUE, (0, 0, 1520, 380))
        pygame.draw.rect(self.sc, DARKGRAY, (0, 380, 1520, 380))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, WHITE)
        self.sc.blit(render, FPS_POS)

    def minimap(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, GREEN, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)))
        pygame.draw.circle(self.sc_map, GREEN, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, GREEN, (x, y, MAP_TILE, MAP_TILE), 1)
        self.sc.blit(self.sc_map, MAP_POS)