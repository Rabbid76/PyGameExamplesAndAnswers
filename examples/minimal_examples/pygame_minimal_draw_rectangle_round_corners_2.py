# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Is there a way to turn a rectangle into a circle in pygame?
# https://stackoverflow.com/questions/71058033/is-there-a-way-to-turn-a-rectangle-into-a-circle-in-pygame/71060513#71060513
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame

pygame.init()
window = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

radius = 0
step = 1

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    pygame.draw.rect(window, (255, 255, 0), (100, 100, 200, 200), border_radius = radius)
    pygame.display.flip()

    radius += step
    if radius <= 0 or radius >= 100:
        step *= -1

pygame.quit()
exit()