# pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
#
# player turns in wrong direction if angle is negative
# https://stackoverflow.com/questions/61817913/player-turns-in-wrong-direction-if-angle-is-negative  
#
# GitHub - PyGameExamplesAndAnswers - Rotate towards target or mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_rotate_towards_target.md

import pygame
import math

def rotate_triangle(center, scale, mouse_pos):
    
    dx = mouse_pos[0] - center[0]
    dy = mouse_pos[1] - center[1]
    len = math.hypot(dx, dy)
    if len:
        dx, dy = (dx*scale/len, dy*scale/len) if len > 0 else (1, 0)

    pts = [(-0.5, -0.866), (-0.5, 0.866), (4.0, 0.0)]
    pts = [(center[0] + p[0]*dx + p[1]*dy, center[1] + p[0]*dy - p[1]*dx) for p in pts]
    return pts

def mouse_direction():
    x, y = window.get_width()/2, window.get_height()/2
    mousex, mousey = pygame.mouse.get_pos()
    dx, dy = mousex - x, mousey - y
    return dx, dy

window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()
player_angle = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    player_dir = math.cos(math.radians(player_angle)), math.sin(math.radians(player_angle)) 
    direction = mouse_direction()
    normal_dir = -direction[1], direction[0] 
    
    dot_p_n = player_dir[0]*normal_dir[0] + player_dir[1]*normal_dir[1]
    player_angle += -1 if dot_p_n > 0 else 1

    target_pos = window.get_width()/2 + math.cos(math.radians(player_angle)), window.get_height()/2 + math.sin(math.radians(player_angle)) 
    points = rotate_triangle(window.get_rect().center, 20, target_pos)
    
    window.fill((255, 255, 255))
    pygame.draw.polygon(window, (0, 0, 0), points)
    pygame.display.update()

pygame.quit()
exit()