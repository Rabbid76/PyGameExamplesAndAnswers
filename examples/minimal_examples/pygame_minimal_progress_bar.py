# How can I display a smooth loading bar in pygame?
# https://stackoverflow.com/questions/54502683/how-can-i-display-a-smooth-loading-bar-in-pygame/54502953#54502953 
#
# GitHub - PyGameExamplesAndAnswers - UI elements - Progress bar and health bar
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_ui_elements.md

import pygame
import pygame.font
pygame.init()

def drawBar(surf, pos, size, borderC, barC, progress):
    pygame.draw.rect(surf, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+3, pos[1]+3)
    innerSize = ((size[0]-6) * progress, size[1]-6)
    pygame.draw.rect(surf, barC, (*innerPos, *innerSize))

window = pygame.display.set_mode((300, 80))
clock = pygame.time.Clock()

max_a = 100
a = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    drawBar(window, (20, 20), (window.get_width()-40, 40), (0, 0, 0), (0, 128, 0), a/max_a)
    pygame.display.flip()

    a += 1
    if a >= max_a:
        a = 0 

pygame.quit()
exit()