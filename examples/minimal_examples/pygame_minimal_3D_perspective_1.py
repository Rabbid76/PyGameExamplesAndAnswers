# Why is there distortion when the cube is on the edge of the screen?
# https://stackoverflow.com/questions/69731067/why-is-there-distortion-when-the-cube-is-on-the-edge-of-the-screen/70415341#70415341
#
# GitHub - PyGameE# How to rotate a square around x-axis in a 3D spacexamplesAndAnswers - Draw 3D
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_3D.md

import pygame

pygame.init()
window = pygame.display.set_mode((600, 400))
width, height = window.get_size()
clock = pygame.time.Clock()

cube = [-1, -1, -1], [1, -1, -1], [1, -1, 1], [-1, -1, 1], [-1, 1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
cam_coord, cam_speed = [0, 0, 0], 0.5
scale = 200

translate = [4, 0, 0]
for i in range(len(cube)):
    for e in range(3):
        cube[i][e] += translate[e]

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    cam_coord[1] -= (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * cam_speed
    cam_coord[2] -= (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * cam_speed

    cube_coords = []
    for point in cube:
        x = (width / 2) + scale * (point[2] - cam_coord[2]) / (point[0] - cam_coord[0])
        y = (height / 2) +  scale * (point[1] - cam_coord[1]) / (point[0] - cam_coord[0])
        cube_coords.append((x, y))

    window.fill((255, 255, 255))
    for edge in edges:
        pygame.draw.line(window, (0, 0, 0), cube_coords[edge[0]], cube_coords[edge[1]], 2)
    for coord in cube_coords:
        pygame.draw.circle(window, (255, 0, 0), coord, 5)
    pygame.display.update()
    
pygame.quit()
exit()