# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Is there anyway to do this recursively in pygame?
# https://stackoverflow.com/questions/59455641/is-there-anyway-to-do-this-recursively-in-pygame/59456232#59456232
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Fractal
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame
import math

def innerCircles(surf, cpt, radius, depth):
    if depth == 4:
        return

    sin60    = math.sin(math.pi/3) # math.sqrt(3) / 2
    tri_pt   = [[-sin60, 0.5], [sin60, 0.5], [0, -1]]
    in_r     = radius * sin60 / (sin60+1)
    in_cpt_d = radius - in_r

    colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
    for pt, color in zip(tri_pt, colors):
        in_cpt = (cpt[0] + pt[0] * in_cpt_d), (cpt[1] + pt[1] * in_cpt_d)
        pygame.draw.circle(surf, color, (round(in_cpt[0]), round(in_cpt[1])), round(in_r), 1)
        innerCircles(surf, in_cpt, in_r, depth+1)

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

cpt = (250, 250)
radius = 200

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    pygame.draw.circle(window, (255, 255, 255), cpt, radius+1, 3)
    innerCircles(window, cpt, radius, 0)
    pygame.display.flip()

pygame.quit()
exit()