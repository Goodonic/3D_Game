from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWW',
    'W..................W',
    'W..................W',
    'W....W.............W',
    'W..WWW.............W',
    'W...W......W.......W',
    'W..........W.......W',
    'W........WWW.......W',
    'W..................W',
    'WWWWWWWWWWWWWWWWWWWW'
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))