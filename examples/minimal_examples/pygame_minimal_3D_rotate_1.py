# pygame.math.Vector3 object
# https://www.pygame.org/docs/ref/math.html
#
# 3D Projection in pygame
# https://stackoverflow.com/questions/63944055/3d-projection-in-pygame/63944641#63944641
#
# GitHub - PyGameExamplesAndAnswers - Draw 3D
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_3D.md

import pygame
import numpy as np
import math

window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

points = [np.matrix([-0.5+i*0.5, -0.5+j*0.5, 1]) for i in range(3) for j in range(3)]
angle = 0
w, h = window.get_rect().size
projection_matrix = np.matrix([[h/2, 0, w/2], [0, h/2, h/2]])

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    s, c = math.sin(angle), math.cos(angle)
    angle += 0.01
    rotation = np.matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])

    window.fill((0,0,0))
    for point in points:
        projected2d = projection_matrix * rotation * point.reshape((3, 1))
        cpt = int(projected2d[0][0]), int(projected2d[1][0])
        pygame.draw.circle(window, (255, 255, 255), cpt, 5)

    pygame.display.update()

pygame.quit()
exit()