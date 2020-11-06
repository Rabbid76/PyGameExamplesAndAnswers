# pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
#
# How to rotate a triangle to a certain angle in pygame?
# https://stackoverflow.com/questions/58100335/how-to-rotate-a-triangle-to-a-certain-angle-in-pygame
#
# GitHub - PyGameExamplesAndAnswers - Rotate towards target or mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_rotate_towards_target.md

import pygame
import math

def rotate_triangle_Vector2(center, scale, mouse_pos):
    
    vMouse  = pygame.math.Vector2(mouse_pos)
    vCenter = pygame.math.Vector2(center)
    angle   = pygame.math.Vector2().angle_to(vMouse - vCenter)
    
    points = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
    rotated_point = [pygame.math.Vector2(p).rotate(angle) for p in points]

    triangle_points = [(vCenter + p*scale) for p in rotated_point]
    return triangle_points

def rotate_triangle(center, scale, mouse_pos):
    
    dx = mouse_pos[0] - center[0]
    dy = mouse_pos[1] - center[1]
    len = math.hypot(dx, dy)
    if len > 0:
        dx, dy = (dx*scale/len, dy*scale/len) if len > 0 else (1, 0)

    pts = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
    pts = [(center[0] + p[0]*dx + p[1]*dy, center[1] + p[0]*dy - p[1]*dx) for p in pts]
    return pts

window = pygame.display.set_mode((200, 200))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    mouse_position = pygame.mouse.get_pos()
    points = rotate_triangle(window.get_rect().center, 20, mouse_position)
    
    pygame.Surface.fill(window, (255,255,255))
    pygame.draw.polygon(window, (0,0,0), points)
    pygame.display.update()

pygame.quit()
exit()