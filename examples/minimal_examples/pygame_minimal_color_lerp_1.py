# Blending two pygame.Color objects together
# https://stackoverflow.com/questions/69426379/blending-two-pygame-color-objects-together/69426709#69426709 
# 
# GitHub - PyGameExamplesAndAnswers - Color
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_color.md

import pygame

pygame.init()
window = pygame.display.set_mode((500, 100))
clock = pygame.time.Clock()

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
pink25 = white.lerp(red, 0.25)
pink50 = white.lerp(red, 0.5)
pink75 = white.lerp(red, 0.75)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.fill(0)
    pygame.draw.circle(window, white, (50, 50), 45)
    pygame.draw.circle(window, pink25, (150, 50), 45)
    pygame.draw.circle(window, pink50, (250, 50), 45)
    pygame.draw.circle(window, pink75, (350, 50), 45)
    pygame.draw.circle(window, red, (450, 50), 45)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
