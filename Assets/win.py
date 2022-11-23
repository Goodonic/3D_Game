from settings import *
import pygame

def Win(win_pos, sprites_pos):
    res = 0
    for i in sprites_pos:
        if i in win_pos:
            res += 1
    return res

def WinDisplay(sc, text_pos, font):
    sc.fill((255, 255, 255))
    render = font.render("YOU WIN!", 0, RED)
    sc.blit(render, text_pos)