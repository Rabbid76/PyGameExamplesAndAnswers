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

def angle_of_vector(x, y):
    #return math.degrees(math.atan2(-y, x))            # 1: with math.atan
    return pygame.math.Vector2(x, y).angle_to((1, 0))  # 2: with pygame.math.Vector2.angle_to
    
def angle_of_line(x1, y1, x2, y2):
    #return math.degrees(math.atan2(-y1-y2, x2-x1))    # 1: math.atan
    return angle_of_vector(x2-x1, y2-y1)               # 2: pygame.math.Vector2.angle_to
    
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

angle = 0
radius = 150
vec = (radius, 0)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    cpt = window.get_rect().center
    pt = cpt[0] + vec[0], cpt[1] + vec[1]
    angle = angle_of_vector(*vec)

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), cpt, radius, 1)
    pygame.draw.line(window, (0, 255, 0), cpt, (cpt[0] + radius, cpt[1]), 3)
    pygame.draw.line(window, (255, 0, 0), cpt, pt, 3)
    text_surf = font.render(str(round(angle/5)*5) + "°", True, (255, 0, 0))
    text_surf.set_alpha(127)
    window.blit(text_surf, text_surf.get_rect(bottomleft = (cpt[0]+20, cpt[1]-20)))
    pygame.display.flip()

    angle = (angle + 1) % 360
    vec = radius * math.cos(angle*math.pi/180), radius * -math.sin(angle*math.pi/180)

pygame.quit()
exit()