# pygame.freetype module
# https://www.pygame.org/docs/ref/freetype.html
#
# pygame text gets out of the window if increases to much
# https://stackoverflow.com/questions/77550093/pygame-text-gets-out-of-the-window-if-increases-to-much/77550769#77550769
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Align text and text size
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md

import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
coins = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    coins += 1
    text_surf = font.render(str(coins), True, "black")
    rect = window.get_rect().inflate(-110, -110)
    
    window.fill("white")
    pygame.draw.rect(window, "red", window.get_rect().inflate(-100, -100), 5)
    window.blit(text_surf, text_surf.get_rect(topleft = rect.topleft))
    window.blit(text_surf, text_surf.get_rect(midtop = rect.midtop))
    window.blit(text_surf, text_surf.get_rect(topright = rect.topright))
    window.blit(text_surf, text_surf.get_rect(midleft = rect.midleft))
    window.blit(text_surf, text_surf.get_rect(center = rect.center))
    window.blit(text_surf, text_surf.get_rect(midright = rect.midright))
    window.blit(text_surf, text_surf.get_rect(bottomleft = rect.bottomleft))
    window.blit(text_surf, text_surf.get_rect(midbottom = rect.midbottom))
    window.blit(text_surf, text_surf.get_rect(bottomright = rect.bottomright))
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()