import pygame
from settings import *
from player import Player
from ray_casting import ray_casting
from sprites_obj import *
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
drawing = Drawing(sc, sc_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    drawing.background()
    walls = ray_casting(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    [obj.sprite_movement(player) for obj in sprites.list_of_objects]
    drawing.minimap(player, sprites)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick(FPS)