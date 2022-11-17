import pygame
from settings import *
from player import Player
from ray_casting import ray_casting
from sprites_obj import *
from drawing import Drawing
from collections import Counter
from map import win_map
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
drawing = Drawing(sc, sc_map)
number_of_sprites = len(sprites.list_of_objects)
count = len(sprites.list_of_objects)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    drawing.background()
    walls = ray_casting(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    [obj.sprite_movement(player) for obj in sprites.list_of_objects]
    sprites_pos = [tuple(obj.mpos) for obj in sprites.list_of_objects]
    #print(Counter(sprites_pos + win_map))
    #sprite_counter = number_of_sprites - Counter(sprites_pos + win_map)
    for key in Counter(sprites_pos + win_map):
        c = 1
        if Counter(sprites_pos + win_map)[key] > 1:
            count = number_of_sprites - c
            c += 1
            #print(Counter(sprites_pos + win_map), sprites_pos)
    drawing.minimap(player, sprites)
    drawing.fps(clock)
    drawing.couner(count)


    pygame.display.flip()
    clock.tick(FPS)