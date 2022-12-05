from settings import *
import pygame

def Help(sc, text_pos, font):
        with open("help.txt", 'r', encoding='utf-8') as file:
            texts = file.readlines()
        sc.fill((255, 255, 255))
        for i in range(len(texts)):
            render = font.render(texts[i].rstrip(), 0, BLACK)
            sc.blit(render, (text_pos[0], text_pos[1] + 45 * i))
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