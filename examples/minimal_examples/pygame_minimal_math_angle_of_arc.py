# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Calculate angles that are in degrees (clockwise) to radians (counter clockwise)
# https://stackoverflow.com/questions/58845411/calculate-angles-that-are-in-degrees-clockwise-to-radians-counter-clockwise/58845851#58845851
#
# GitHub - PyGameExamplesAndAnswers - Vector - Angle between vectors and angle of arc
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_math_vector_and_reflection.md

import pygame
import math

pygame.init()
window = pygame.display.set_mode((450, 250))
clock = pygame.time.Clock()

def clockwiseArc(surface, color, point, radius, startAngle, endAngle):
    rect = pygame.Rect(0, 0, radius*2, radius*2)
    rect.center = point

    endRad = math.radians(-startAngle)
    startRad = math.radians(-endAngle)

    pygame.draw.arc(surface, color, rect, startRad, endRad)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    pygame.draw.line(window, 0, (150, 60), (150, 180))
    pygame.draw.line(window, 0, (300, 60), (300, 180))
    pygame.draw.line(window, 0, (90, 120), (210, 120))
    pygame.draw.line(window, 0, (240, 120), (360, 120))
    clockwiseArc(window, (255, 0, 0), (150, 120), 50, 320, 140) 
    clockwiseArc(window, (255, 0, 0), (300, 120), 50, 90, 180)   
    pygame.display.flip()

pygame.quit()
exit()