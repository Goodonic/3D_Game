## Imports
import random
import time
from settings import player_pos

# Найти количество окружающих ячеек
def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0] - 1][rand_wall[1]] == '.'):
        s_cells += 1
    if (maze[rand_wall[0] + 1][rand_wall[1]] == '.'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] - 1] == '.'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] + 1] == '.'):
        s_cells += 1

    return s_cells


## Основной код
# Переменные инициализации
wall = '1'
cell = '.'
unvisited = 'u'
height = 10
width = 20
maze = []



# Denote all cells as unvisited
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(unvisited)
    maze.append(line)

# Рандомизируйте начальную точку и задайте ей ячейку
starting_height = height//2
starting_width = width//2
if (starting_height == 0):
    starting_height += 1
if (starting_height == height - 1):
    starting_height -= 1
if (starting_width == 0):
    starting_width += 1
if (starting_width == width - 1):
    starting_width -= 1

# Отметьте его как ячейку и добавьте окружающие стены в список
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Обозначить стены в лабиринте
maze[starting_height - 1][starting_width] = '1'
maze[starting_height][starting_width - 1] = '1'
maze[starting_height][starting_width + 1] = '1'
maze[starting_height + 1][starting_width] = '1'

while (walls):
    # Выберите случайную стену
    rand_wall = walls[int(random.random() * len(walls)) - 1]

    # Проверьте, является ли это левой стеной
    if (rand_wall[1] != 0):
        if (maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == '.'):
            # Найдите количество окружающих ячеек
            s_cells = surroundingCells(rand_wall)

            if (s_cells < 2):
                # Обозначить новый путь
                maze[rand_wall[0]][rand_wall[1]] = '.'

                # Отметьте новые стены
                # Верхняя ячейка
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0] - 1][rand_wall[1]] != '.'):
                        maze[rand_wall[0] - 1][rand_wall[1]] = '1'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Нижняя ячейка
                if (rand_wall[0] != height - 1):
                    if (maze[rand_wall[0] + 1][rand_wall[1]] != '.'):
                        maze[rand_wall[0] + 1][rand_wall[1]] = '1'
                    if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] + 1, rand_wall[1]])

                # Крайняя левая ячейка
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1] - 1] != '.'):
                        maze[rand_wall[0]][rand_wall[1] - 1] = '1'
                    if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] - 1])

            # Удалить стену
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Проверьте, является ли это верхней стеной
    if (rand_wall[0] != 0):
        if (maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == '.'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Обозначить новый путь
                maze[rand_wall[0]][rand_wall[1]] = '.'

                # Mark the new walls
                # Upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0] - 1][rand_wall[1]] != '.'):
                        maze[rand_wall[0] - 1][rand_wall[1]] = '1'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1] - 1] != '.'):
                        maze[rand_wall[0]][rand_wall[1] - 1] = '1'
                    if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] - 1])

                # Rightmost cell
                if (rand_wall[1] != width - 1):
                    if (maze[rand_wall[0]][rand_wall[1] + 1] != '.'):
                        maze[rand_wall[0]][rand_wall[1] + 1] = '1'
                    if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] + 1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check the bottom wall
    if (rand_wall[0] != height - 1):
        if (maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] - 1][rand_wall[1]] == '.'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = '.'

                # Mark the new walls
                if (rand_wall[0] != height - 1):
                    if (maze[rand_wall[0] + 1][rand_wall[1]] != '.'):
                        maze[rand_wall[0] + 1][rand_wall[1]] = '1'
                    if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] + 1, rand_wall[1]])
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1] - 1] != '.'):
                        maze[rand_wall[0]][rand_wall[1] - 1] = '1'
                    if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] - 1])
                if (rand_wall[1] != width - 1):
                    if (maze[rand_wall[0]][rand_wall[1] + 1] != '.'):
                        maze[rand_wall[0]][rand_wall[1] + 1] = '1'
                    if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] + 1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check the right wall
    if (rand_wall[1] != width - 1):
        if (maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == '.'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = '.'

                # Mark the new walls
                if (rand_wall[1] != width - 1):
                    if (maze[rand_wall[0]][rand_wall[1] + 1] != '.'):
                        maze[rand_wall[0]][rand_wall[1] + 1] = '1'
                    if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] + 1])
                if (rand_wall[0] != height - 1):
                    if (maze[rand_wall[0] + 1][rand_wall[1]] != '.'):
                        maze[rand_wall[0] + 1][rand_wall[1]] = '1'
                    if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] + 1, rand_wall[1]])
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0] - 1][rand_wall[1]] != '.'):
                        maze[rand_wall[0] - 1][rand_wall[1]] = '1'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Delete the wall from the list anyway
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)

# Mark the remaining unvisited cells as walls
for i in range(0, height):
    for j in range(0, width):
        if (maze[i][j] == 'u'):
            maze[i][j] = '1'

# Set entrance and exit
for i in range(0, width):
    if (maze[1][i] == '.'):
        maze[1][i] = '.'
        break

for i in range(width - 1, 0, -1):
    if (maze[height - 2][i] == '.'):
        maze[height - 2][i] = '.'
        break

