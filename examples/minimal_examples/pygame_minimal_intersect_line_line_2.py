# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Problem with calculating line intersections
# https://stackoverflow.com/questions/56312503/problem-with-calculating-line-intersections/56312654#56312654
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Line and line
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-IntersectAndCutLines#main.py

import pygame
import math
import random

def intersect(obstacles, P0, P1):
    bestdist = 1000000000000000000
    endpoint = P1
    for Q0, Q1 in obstacles:
        d = (P1[0]-P0[0]) * (Q1[1]-Q0[1]) + (P1[1]-P0[1]) * (Q0[0]-Q1[0]) 
        if d != 0:
            t = ((Q0[0]-P0[0]) * (Q1[1]-Q0[1]) + (Q0[1]-P0[1]) * (Q0[0]-Q1[0])) / d
            u = ((Q0[0]-P0[0]) * (P1[1]-P0[1]) + (Q0[1]-P0[1]) * (P0[0]-P1[0])) / d
            if 0 <= t <= 1 and 0 <= u <= 1:
                vx, vy = (P1[0]-P0[0]) * t, (P1[1]-P0[1]) * t
                dist = vx*vx + vy*vy
                if dist < bestdist:
                    px, py = round(Q1[0] * u + Q0[0] * (1-u)), round(Q1[1] * u + Q0[1] * (1-u))
                    bestdist = dist
                    endpoint = (px, py)
    return endpoint

def createRays(center):
    return [(center[0] + 1200 * math.cos(angle), center[1] + 1200 * math.sin(angle)) for angle in range(0, 360, 10)]

def createObstacles(surface):
    w, h = surface.get_size()
    return [((random.randrange(w), random.randrange(h)), (random.randrange(w), random.randrange(h))) for _ in range(5)]

window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

origin = window.get_rect().center
rays = createRays(origin)
obstacles = createObstacles(window)

move_center = True
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            obstacles = createObstacles(window) 
        if event.type == pygame.KEYDOWN:
            move_center = not move_center

    if move_center:
        origin = pygame.mouse.get_pos()
        rays = createRays(origin) 
        
    window.fill(0)
    for endpoint in rays:
        endpoint = intersect(obstacles, origin, endpoint)
        pygame.draw.line(window, (128, 128, 128), origin, endpoint)
    pygame.draw.circle(window, (255, 255, 255), origin, 10)
    for start, end in obstacles:
        pygame.draw.line(window, (255, 0, 0), start, end)
    pygame.display.flip()

pygame.quit()
exit()