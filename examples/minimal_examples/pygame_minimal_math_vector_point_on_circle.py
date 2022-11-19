# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# How Do I Find The Coordinates of the Edge of a Circle
# https://stackoverflow.com/questions/67197763/how-do-i-find-the-coordinates-of-the-edge-of-a-circle/67198226#67198226
#
# GitHub - PyGameExamplesAndAnswers - Vector - Angle between vectors
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_math_vector_and_reflection.md

import pygame
import math

def point_on_circle_1(cpt, radius, angle):
    angle_rad = math.radians(angle)
    pt_x = cpt[0] + radius * math.sin(angle_rad)
    pt_y = cpt[1] - radius * math.cos(angle_rad) 
    return pt_x, pt_y

def point_on_circle_2(cpt, radius, angle):
    vec = pygame.math.Vector2(0, -radius).rotate(angle)
    return cpt[0] + vec.x, cpt[0] + vec.y

pygame.init()
window = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
cpt = window.get_rect().center
angle = 0
radius = 100

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

  
    pt_x, pt_y = point_on_circle_1(cpt, radius, angle)
    #pt_x, pt_y = point_on_circle_2(cpt, radius, angle)
    
    angle += 1     
    if angle >= 360:
        angle = 0

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), cpt, radius, 2)
    pygame.draw.line(window, (0, 0, 255), cpt, (pt_x, pt_y), 2)
    pygame.draw.line(window, (0, 0, 255), cpt, (cpt[0], cpt[1]-radius), 2)
    text = font.render(str(angle), True, (255, 0, 0))
    window.blit(text, text.get_rect(center = cpt))
    pygame.display.flip()

pygame.quit()
exit()