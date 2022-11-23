from settings import *
import pygame

def Help(sc, text_pos, font):
        sc.fill((255, 255, 255))
        render = font.render("Help", 0, RED)
        sc.blit(render, text_pos)
        run = True
        pygame.display.flip()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        print(3)
                        run = False


        pygame.display.flip()