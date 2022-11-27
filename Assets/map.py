from settings import *
import pygame
collision_walls = []
text_map = [['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','.','.','.','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','.','.','.','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','.','.','.','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','.','.','.','.','.','.','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','.','1','.','1','1','.','1','1','1','1','1','1','2','2','2','2','1'],
            ['1','.','.','.','1','.','1','1','.','1','1','1','1','1','2','.','.','3','3','2'],
            ['1','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','3','3','2'],
            ['1','1','1','1','1','.','1','1','1','.','1','.','1','1','2','.','.','3','3','2'],
            ['1','1','1','1','1','.','.','.','.','.','1','.','1','1','1','2','2','2','2','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ]

world_map = {}
mini_map = set()
win_map = []
collision_walls_list_for_sprites = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
                mini_map.add((i * MAP_TILE, j * MAP_TILE, '1'))
                collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
                collision_walls_list_for_sprites.append((i+1, j+1))
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'
                mini_map.add((i * MAP_TILE, j * MAP_TILE, '2'))
                collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
                collision_walls_list_for_sprites.append((i+1, j+1))
            elif char == '3':
                mini_map.add((i * MAP_TILE, j * MAP_TILE, '3'))
                win_map.append((i+1, j+1))
