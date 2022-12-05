from settings import *
import pygame
from help import Help

def Menu(sc, text_pos, font):
    buttonImg = pygame.image.load('Sprites/Not_a_Button.png')
    start = font.render("Start", 0, WHITE)
    help = font.render("Help", 0, WHITE)
    developer = font.render("Developer Nikita Orehov", 0, BLACK)
    projectName = font.render(PROJECTNAME, 0, RED)
    run = True

    while run:
        sc.fill((255, 255, 255))
        sc.blit(projectName, (HALF_WIDTH - 185, HALF_HEIGHT - 320))
        sc.blit(buttonImg, (HALF_WIDTH - 135, HALF_HEIGHT - 205))
        sc.blit(start, (text_pos[0], text_pos[1] - 100))
        sc.blit(buttonImg, (HALF_WIDTH - 135, HALF_HEIGHT - 5))
        sc.blit(help, (text_pos[0] + 20, text_pos[1] + 100))
        sc.blit(developer, (text_pos[0] - 400, text_pos[1] + 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and 626 <= event.pos[0] <= 924 and 175 <= event.pos[1] <= 273:
                    run = False
                elif event.button == 1 and 626 <= event.pos[0] <= 924 and 376 <= event.pos[1] <= 474:
                    Help(sc, HELP_TEXT_POS, HELP_FONT)
        pygame.display.flip()