# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# How To Create A Checkered Background Using Pygame Surfarrays?
# https://stackoverflow.com/questions/73277963/how-to-create-a-checkered-background-using-pygame-surfarrays/73278096#73278096  
#
# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Checkered background
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import pygame
import numpy as np

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

w, h, ts = *window.get_size(), 50
c = np.fromfunction(lambda x, y: (x//ts + y//ts) % 2, (w, h))
checkered = np.full((w, h, 3), (128, 128, 128))
checkered[c == 1] = (64, 64, 64)
background = pygame.surfarray.make_surface(checkered)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()