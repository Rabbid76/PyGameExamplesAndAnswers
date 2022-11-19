# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Issue finding side of collision for Circle-Rectangle collision
# https://stackoverflow.com/questions/61718259/issue-finding-side-of-collision-for-circle-rectangle-collision/61719115#61719115
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Rectangle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-NearestPointOnRectangle

import pygame
import math

def intersectRectangleCircle(r_cpt, r_size, c_cpt, c_rad):

    v2_c_cpt = pygame.math.Vector2(c_cpt)
    v2_r_cpt = pygame.math.Vector2(r_cpt)

    offset = v2_c_cpt - v2_r_cpt
    if offset.x == 0 and offset.y == 0:
        return [v2_c_cpt, v2_r_cpt]

    if offset.x == 0:   
        ratio = r_size[1] / abs(offset.y)
    elif offset.y == 0: 
        ratio = r_size[0] / abs(offset.x)
    else:
        ratio  = min(r_size[0] / abs(offset.x), r_size[1] / abs(offset.y))
    ratio *= 0.5

    p1 = v2_r_cpt + (offset * ratio)
    offset.scale_to_length(c_rad)
    p2 = v2_c_cpt - offset

    return [p1, p2]

def inBetween(p1, p2, px):

    v = pygame.math.Vector2(p2) - pygame.math.Vector2(p1)
    d = v.length()
    if d == 0:
        return False
    v.normalize_ip()

    vx = pygame.math.Vector2(px) - pygame.math.Vector2(p1)
    dx = v.dot(vx)
    
    return dx >= 0 and dx <= d

pygame.init()
window = pygame.display.set_mode((500, 500))

run = False
while not run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = True

    rect_center     = window.get_rect().center
    rect_size       = window.get_width() // 5, window.get_height() // 10
    rect            = pygame.Rect(rect_center[0] - rect_size[0] // 2, rect_center[1] - rect_size[1] // 2, *rect_size)
    circle_center   = pygame.mouse.get_pos()
    circle_diameter = min(*window.get_size()) // 5

    isect_pts = intersectRectangleCircle(rect_center, rect_size, circle_center, circle_diameter/2)
    dx, dy = isect_pts[0].x - rect_center[0], isect_pts[1].y - rect_center[1] 

    window.fill((255,255,255))
    pygame.draw.rect(window, (0, 0, 0), rect, 3)
    pygame.draw.circle(window, (0, 0, 0), circle_center, circle_diameter // 2, 3)

    pygame.draw.line(window, (0, 0, 255), rect_center, circle_center, 1)
    pygame.draw.line(window, (255, 0, 255), rect_center, (round(isect_pts[0].x), round(isect_pts[0].y)), 3)
    for i in range(2):
        px, py = round(isect_pts[i].x), round(isect_pts[i].y)
        col = (255, 0, 0) if inBetween(rect_center, circle_center, (px, py)) else (0, 255, 0)
        pygame.draw.line(window, col, (px-5, py), (px+5, py), 3)
        pygame.draw.line(window, col, (px, py-5), (px, py+5), 3)

    pygame.display.flip()

pygame.quit()
quit()