# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Problem with calculating line intersections
# https://stackoverflow.com/questions/56312503/problem-with-calculating-line-intersections/56312654#56312654
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Line and line
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-IntersectLines

import pygame
import math
import random

def intersect_line_line_vec2(startObs, endObs, origin, endpoint):
    P = pygame.Vector2(startObs)
    R = (endObs - P)
    Q = pygame.Vector2(origin)
    S = (endpoint - Q)
    d = R.dot((S.y, -S.x))
    if d == 0:
        return None
    t = (Q-P).dot((S.y, -S.x)) / d 
    u = (Q-P).dot((R.y, -R.x)) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        X  =  P + R * t
        return (X.x, X.y)
    return None

def intersect_line_line(P0, P1, Q0, Q1):  
    d = (P1[0]-P0[0]) * (Q1[1]-Q0[1]) + (P1[1]-P0[1]) * (Q0[0]-Q1[0]) 
    if d == 0:
        return None
    t = ((Q0[0]-P0[0]) * (Q1[1]-Q0[1]) + (Q0[1]-P0[1]) * (Q0[0]-Q1[0])) / d
    u = ((Q0[0]-P0[0]) * (P1[1]-P0[1]) + (Q0[1]-P0[1]) * (P0[0]-P1[0])) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        return P1[0] * t + P0[0] * (1-t), P1[1] * t + P0[1] * (1-t)
    return None

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
        pygame.draw.line(window, (128, 128, 128), origin, endpoint)
    pygame.draw.circle(window, (255, 255, 255), origin, 10)
    for start, end in obstacles:
        pygame.draw.line(window, (255, 0, 0), start, end)
        for endpoint in rays:
            pos = intersect_line_line(start, end, origin, endpoint)
            if pos:
                pygame.draw.circle(window, (0, 255, 0), (round(pos[0]), round(pos[1])), 3)
    pygame.display.flip()

pygame.quit()
exit()