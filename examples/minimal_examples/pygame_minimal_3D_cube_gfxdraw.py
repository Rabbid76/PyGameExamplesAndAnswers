# pygame.math.Vector3 object
# https://www.pygame.org/docs/ref/math.html
#
# Pygame won't draw quads in the right order
# https://stackoverflow.com/questions/67143657/pygame-wont-draw-quads-in-the-right-order/67146073#67146073
#
# GitHub - PyGameExamplesAndAnswers - Draw 3D
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_3D.md

import os
os.environ["SDL_VIDEO_CENTERED"] = '1'
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'
import pygame
from pygame import gfxdraw
import math
import random

pygame.init()
pygame.display.set_caption("Hexahedron")
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 23)

fill, outline, auto_rotate = True, False, True
euler_angles = [0, 0, 0]
translation = [0, 0, 0]
scale, speed, mov_speed = 300, 0.001, 0.001
text = None
class Hexahedron:
    verts = [
        (1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
    faces = [[0, 4, 6, 2], [3, 2, 6, 7], [7, 6, 4, 5], [5, 1, 3, 7], [1, 0, 2, 3], [5, 4, 0, 1]]

mesh = Hexahedron()
points = [[[i] for i in j] for j in mesh.verts]
colors = [[random.randint(0, 255) for _ in range(3)] for i in range(len(Hexahedron.faces))]

def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)
    
    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix
        
    else:
        print("columns of the first matrix must be equal to the rows of the second matrix")
        return None

def distToCam(i):
    a = [0, 0, distance]
    b = [sum(new_points[mesh.faces[i][pi]][j][0] for pi in range(4)) / 4 for j in range(3)]
    return math.dist(a, b)

run, frame_count = True, 0
while run:
    dt = clock.tick()
    fps = clock.get_fps()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fill = not fill
                if not fill:
                    outline = True
            if event.key == pygame.K_o:
                outline = not outline
                if not outline:
                    fill = True
            if event.key == pygame.K_SPACE:
                auto_rotate = not auto_rotate
            if event.key == pygame.K_r:
                euler_angles = [0, 0, 0]
                translation = [0, 0, 0]

    keys = pygame.key.get_pressed()
    euler_angles[0] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed * dt
    euler_angles[1] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed * dt
    euler_angles[2] += (keys[pygame.K_HOME] - keys[pygame.K_END]) * speed * dt
    translation[0] += (keys[pygame.K_d] - keys[pygame.K_a]) * mov_speed * dt
    translation[1] += (keys[pygame.K_s] - keys[pygame.K_w]) * mov_speed * dt
    translation[2] += (keys[pygame.K_q] - keys[pygame.K_e]) * mov_speed * dt

    if auto_rotate:
        euler_angles[0] += 2*speed * dt
        euler_angles[1] += speed * dt

    projected_points = [j for j in range(len(points))]

    rotation_x = [[1, 0, 0],
                  [0, math.cos(euler_angles[0]), -math.sin(euler_angles[0])],
                  [0, math.sin(euler_angles[0]), math.cos(euler_angles[0])]]
    rotation_y = [[math.cos(euler_angles[1]), 0, -math.sin(euler_angles[1])],
                  [0, 1, 0],
                  [math.sin(euler_angles[1]), 0, math.cos(euler_angles[1])]]
    rotation_z = [[math.cos(euler_angles[2]), -math.sin(euler_angles[2]), 0],
                  [math.sin(euler_angles[2]), math.cos(euler_angles[2]), 0],
                  [0, 0, 1]]

    center_x, center_y, distance = *screen.get_rect().center, 5
    new_points = []
    for index, point in enumerate(points):
        rotated_2d = matrix_multiplication(rotation_y, point)
        rotated_2d = matrix_multiplication(rotation_x, rotated_2d)
        rotated_2d = matrix_multiplication(rotation_z, rotated_2d)
        
        new_point = [[rotated_2d[i][0] + translation[i]] for i in range(3)]
        new_points.append(new_point)
        
        z = 1 / (distance - new_point[2][0])
        projection_matrix = [[z, 0, 0], [0, z, 0]]
        projected_2d = matrix_multiplication(projection_matrix, new_point)
        
        x = round(projected_2d[0][0] * scale) + center_x
        y = round(projected_2d[1][0] * scale) + center_y
        projected_points[index] = [x, y]
 
    zs = [[distToCam(i), i] for i in range(len(mesh.faces))]
    zs.sort(reverse = True)
    faces = [[mesh.faces[zs[i][1]], zs[i][1]] for i in range(len(mesh.faces))]
    
    if text == None or frame_count % 100 == 0:
        text = font.render(str(round(fps, 1)), False, (20, 20, 20))    
    frame_count += 1

    screen.fill((230, 230, 230))
    for fi, f in enumerate(faces):
        if fill:
            gfxdraw.filled_polygon(screen, [projected_points[pi] for pi in f[0]], colors[f[1]])
        if outline:
            gfxdraw.aapolygon(screen, [projected_points[pi] for pi in f[0]], (0, 0, 0))
    screen.blit(text, (0, 0))
    pygame.display.update()

pygame.quit()