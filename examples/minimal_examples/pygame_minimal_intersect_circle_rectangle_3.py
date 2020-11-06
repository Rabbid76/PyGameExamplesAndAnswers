# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Detect collision between textbox and circle in pygame
# https://stackoverflow.com/questions/58305721/detect-collision-between-textbox-and-circle-in-pygame/58306368#58306368
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Rectangle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
import math

pygame.init()
window = pygame.display.set_mode((500, 500))

run = False
while not run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = True

    rect = pygame.Rect(0, 0, 20, 40)
    rect.center = pygame.mouse.get_pos()
    cpt = window.get_rect().center
    radius = min(*window.get_size()) * 4 // 10
    
    corners = [rect.bottomleft, rect.bottomright, rect.topleft, rect.topright]
    dist    = [math.hypot(p[0]-cpt[0], p[1]-cpt[1]) for p in corners] 
    p_out   = [i for i, d in enumerate(dist) if d > radius]
    p_in    = [i for i, d in enumerate(dist) if d < radius]

    rect_color = (0, 0, 0)
    if any(p_in) and any(p_out):
        rect_color = (128, 128, 0)
    elif len(p_in) == 4:
        rect_color = (0, 255, 0)
    elif len(p_out) == 4:
        rect_color = (255, 0, 0)

    window.fill((255,255,255))
    pygame.draw.rect(window, rect_color, rect)
    pygame.draw.circle(window, (0, 0, 0), cpt, radius, 5)
    pygame.display.flip()

pygame.quit()
quit()