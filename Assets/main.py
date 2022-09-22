import pygame
import math
from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.minimap(player)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick(FPS)