import pygame
from settings import *
from player import Player
from ray_casting import ray_casting
from sprites_obj import *
from drawing import Drawing
from map import win_map
from win import Win, WinDisplay
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
    drawing.minimap(player, sprites)
    drawing.fps(clock)
    count_res = count - Win(win_map, sprites_pos)
    drawing.counter(count_res)
    # Перезагрузка
    if pygame.key.get_pressed()[pygame.K_r]:
        player.__init__(sprites)
        sprites.__init__()
    if count_res == 0:
        WinDisplay(sc, WIN_TEXT_POS, WIN_FONT)


    pygame.display.flip()
    clock.tick(FPS)