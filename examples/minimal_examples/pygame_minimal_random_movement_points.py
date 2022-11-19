# How to plot circles every 20 pixels between two randomly generated points in Pygame?
# https://stackoverflow.com/questions/56245338/how-to-plot-circles-every-20-pixels-between-two-randomly-generated-points-in-pyg/56245525#56245525
#
# GitHub - PyGameExamplesAndAnswers - Random movement distribution
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
import math
import random

window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

radius = 10
pts = [(random.randint(radius, window.get_width()-radius), random.randint(radius, window.get_height()-radius)) for _ in range(2)]
switch = [(random.randint(radius, window.get_width()-radius), random.randint(radius, window.get_height()-radius)) for _ in range(2)]

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i, ((x, y), (x2, y2)) in enumerate(zip(pts, switch)):
        if x2 == x:
            x2 = random.randint(radius, window.get_width()-radius)
        else:
            x += 1 if x2 > x else -1
        if y2 == y:
            y2 = random.randint(radius, window.get_height()-radius)
        else:
            y += 1 if y2 > y else -1
        pts[i], switch[i] = (x, y), (x2, y2)
        
    window.fill((255, 255, 255))

    pygame.draw.line(window, (255, 0, 0), (switch[0][0], 0), (switch[0][0], window.get_height()), 1)
    pygame.draw.line(window, (255, 0, 0), (0, switch[0][1]), (window.get_width(), switch[0][1]), 1)
    pygame.draw.line(window, (0, 255, 0), (switch[1][0], 0), (switch[1][0], window.get_height()), 1)
    pygame.draw.line(window, (0, 255, 0), (0, switch[1][1]), (window.get_width(), switch[1][1]), 1)
    
    dir = pts[1][0]-pts[0][0], pts[1][1]-pts[0][1]
    dist = math.hypot(*dir)
    for i in range(1, int(dist) // 20+1):
        pt = round(pts[0][0] + dir[0] * i * 20 / dist), int(pts[0][1] + dir[1] * i * 20 / dist)
        pygame.draw.circle(window, (0, 0, 0), pt, 2)

    pygame.draw.circle(window, (127, 0, 0), pts[0], radius)
    pygame.draw.circle(window, (0, 127, 0), pts[1], radius)
        
    pygame.display.flip()

pygame.quit()
exit()