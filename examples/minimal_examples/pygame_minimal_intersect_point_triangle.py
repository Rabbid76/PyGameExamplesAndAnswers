# Only some points inside of triangle are considered 'inside' the triangle
# https://stackoverflow.com/questions/59289954/only-some-points-inside-of-triangle-are-considered-inside-the-triangle
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Point in triangle 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
from math import sqrt

pygame.init()
DISPLAY = pygame.display.set_mode((300, 300))

def drawTriangle(pointA, pointB, pointC, color):
    pygame.draw.polygon(DISPLAY, color, [pointA, pointB, pointC], 5)

def getLine(pointA, pointB):
    return sqrt((pointB[0] - pointA[0])**2 + (pointB[1]-pointA[1])**2)

def getArea(pointA, pointB, pointC):

    AB = getLine(pointA, pointB)
    BC = getLine(pointB, pointC)
    CA = getLine(pointC, pointA)

    s = (AB + BC + CA) / 2

    return sqrt(s*(s-AB) * (s-BC) * (s-CA))

def getArea2(pointA, pointB, pointC): 
    x1, y1 = pointA
    x2, y2 = pointB
    x3, y3 = pointC
    return abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0)

A = [100, 100]
B = [200, 100]
C = [150, 200]
Color = (255, 255, 255)

while(True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    mpx, mpy = pygame.mouse.get_pos()
    posArray = [mpx, mpy]

    drawTriangle(A, B, C, Color)

    Area = getArea(A, B, C)

    trigA = getArea(A, B, posArray)
    trigB = getArea(posArray, B, C)
    trigC = getArea(A, posArray, C)

    if abs(trigA + trigB + trigC - Area) < 0.001:
        Color = (0, 255, 0)
    else:
        Color = (255, 255, 255)

    pygame.display.update()

pygame.quit()
exit()