# Line is detected as diagonal of rectangle while using collidepoint function in pygame
# https://stackoverflow.com/questions/67372361/line-is-detected-as-diagonal-of-rectangle-while-using-collidepoint-function-in-p/67372647#67372647
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Point and line
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
import math

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

def distance_point_line_2(pt, l1, l2):
    nx, ny = l1[1] - l2[1], l2[0] - l1[0]
    nlen = math.hypot(nx, ny)
    nx /= nlen
    ny /= nlen
    vx, vy = pt[0] - l1[0],  pt[1] - l1[1]
    dist = abs(nx*vx + ny*vy)
    return dist

def distance_point_line(pt, l1, l2):
    NV = pygame.math.Vector2(l1[1] - l2[1], l2[0] - l1[0])
    LP = pygame.math.Vector2(l1)
    P = pygame.math.Vector2(pt)
    return abs(NV.normalize().dot(P -LP))

lines = [
    {"clicked" : False, "line": ((50, 50), (350, 350)), "thickness": 10},
    {"clicked" : False, "line": ((350, 100), (50, 300)), "thickness": 20},
    {"clicked" : False, "line": ((100, 50), (300, 200)), "thickness": 15},
    {"clicked" : False, "line": ((50, 250), (350, 300)), "thickness": 15}
]

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            for line in lines:
                l = line["line"]
                line_rect = pygame.Rect(*l[0], l[1][0]-l[0][0], l[1][1]+l[0][1])
                line_rect.normalize()
                if (line_rect.collidepoint(event.pos) and 
                    distance_point_line(event.pos, *l) < line["thickness"] / 2):
                    line["clicked"] = not line["clicked"]

    window.fill((0, 0, 0))
    for line in lines:
        pygame.draw.line(window, (255, 0, 0) if line["clicked"] else (164, 164, 164), *line["line"], line["thickness"])
    pygame.display.update()
        
pygame.quit()
exit()
