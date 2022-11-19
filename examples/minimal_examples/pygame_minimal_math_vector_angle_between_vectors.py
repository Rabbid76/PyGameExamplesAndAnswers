# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# How to know the angle between two vectors?
# https://stackoverflow.com/questions/42258637/how-to-know-the-angle-between-two-vectors/64563327#64563327
#
# GitHub - PyGameExamplesAndAnswers - Vector - Angle between vectors
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_math_vector_and_reflection.md

import pygame
import math

def angle_between_vectors(x1, y1, x2, y2):
    return pygame.math.Vector2(x1, y1).angle_to((x2, y2))

def angle_of_vector(x, y):
    return pygame.math.Vector2(x, y).angle_to((1, 0))    
    
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

angle = 0
radius = 150
vec1 = (radius, 0)
vec2 = (radius, 0)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    cpt = window.get_rect().center
    pt1 = cpt[0] + vec1[0], cpt[1] + vec1[1]
    pt2 = cpt[0] + vec2[0], cpt[1] + vec2[1]
    angle = angle_between_vectors(*vec2, *vec1)

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), cpt, radius, 1)
    pygame.draw.line(window, (0, 255, 0), cpt, pt1, 3)
    pygame.draw.line(window, (255, 0, 0), cpt, pt2, 3)
    text_surf = font.render(str(round(angle/5)*5) + "°", True, (255, 0, 0))
    text_surf.set_alpha(127)
    window.blit(text_surf, text_surf.get_rect(bottomleft = (cpt[0]+20, cpt[1]-20)))
    pygame.display.flip()

    angle1 = (angle_of_vector(*vec1) + 1/3) % 360
    vec1 = radius * math.cos(angle1*math.pi/180), radius * -math.sin(angle1*math.pi/180)
    angle2 = (angle_of_vector(*vec2) + 1) % 360
    vec2 = radius * math.cos(angle2*math.pi/180), radius * -math.sin(angle2*math.pi/180)

pygame.quit()
exit()