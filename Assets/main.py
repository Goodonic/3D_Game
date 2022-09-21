import pygame
import math
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    pygame.draw.rect(sc, BLUE, (0, 0, 1520, 380))
    pygame.draw.rect(sc, DARKGRAY, (0, 380, 1520, 380))
    ray_casting(sc,player.pos, player.angle)

    # pygame.draw.circle(sc, GREEN,(int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                          player.y + WIDTH * math.sin(player.angle)))
    # for x, y in world_map:
    #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)