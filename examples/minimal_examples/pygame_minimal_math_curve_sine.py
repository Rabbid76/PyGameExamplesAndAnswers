# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Sine
# https://en.wikipedia.org/wiki/Sine
#
# Gaps in a line while trying to draw them with a mouse problem
# https://stackoverflow.com/questions/56379888/gaps-in-a-line-while-trying-to-draw-them-with-a-mouse-problem/56380523#56380523
#
# GitHub - PyGameExamplesAndAnswers - Math and Vector - Curve - Lissajous curve
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_math_vector_and_reflection.md

import pygame
import math
import fractions

pygame.init()
window = pygame.display.set_mode((800, 600))
font20 = pygame.font.SysFont(None, 20)

def draw(rect, center, vector, radius, currentPoint, axisColor, lineColor, curveColor):
    circlePt = round(center[0] + vector[0] * radius), round(center[1] + vector[1] * radius)
    xa = window.get_width() // 3
    yb = window.get_height() // 2
    curPt = (currentPoint[0] + xa, currentPoint[1] + yb)
    
    pygame.draw.line(window, axisColor, (xa, rect.top), (xa, rect.bottom), 1)
    pygame.draw.line(window, axisColor, (rect.left, rect.centery), (rect.right, rect.centery), 1)
    
    pygame.draw.circle(window, lineColor, center, radius, 3)
    pygame.draw.line(window, lineColor, (rect.left, circlePt[1]), (rect.right, circlePt[1]), 1)
    pygame.draw.line(window, lineColor, (circlePt[0], center[1]), circlePt, 1)
    pygame.draw.line(window, lineColor, center, circlePt, 1)
    pygame.draw.line(window, lineColor, curPt, (curPt[0], center[1]), 1)

    threshold = 10
    for i in range(len(points)):
        dist_p = 0 if i==0 else points[i][0]-points[i-1][0]
        dist_s = 0 if i>len(points)-2 else points[i+1][0]-points[i][0]
        pt = (points[i][0] + xa, points[i][1] + yb)
        if dist_p > threshold and dist_s > threshold: 
           pygame.draw.circle(window, curveColor, pt, 6, 0)
        elif 0 < dist_p < threshold:
           pygame.draw.line(window, curveColor, (points[i-1][0] + xa, points[i-1][1] + yb), pt, 2)

lastQ, q, rotCount = 3, 0, -1
radius = 100
points = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                lastQ, q, rotCount = 3, 0, -1
                points = []

    mouse = pygame.mouse.get_pos()
    rect = window.get_rect().inflate(-80, -80)
    center = (rect.centerx // 3, rect.centery) 

    vector = (mouse[0]-center[0], mouse[1]-center[1])
    distance = math.hypot(vector[0], vector[1])
    normVector = vector
    if distance > 0: 
        normVector = vector[0] / distance, vector[1] / distance
        vector = normVector[0] * radius, normVector[1] * radius

    angle = math.degrees(math.atan2(-normVector[1], normVector[0]))
    if angle < 0:
        angle += 360
    
    q = angle // 90
    if q == 0 and lastQ == 3:    
        rotCount += 1
    elif q == 3 and lastQ == 0:
        rotCount -= 1
    lastQ = q

    angle = angle + 360 * rotCount
   
    sinC   = round(normVector[1] * radius)
    point = (round(angle * (5/9)*3), sinC)
    if not any([x for x in points if x==point[0]]):
        points.append(point)
        points = sorted(points, key = lambda p : p[0])

    text1 = font20.render(f"Angle: {angle: 0.3f}°", 2, (0, 0, 0))
    text2 = font20.render(f"Sine:  {vector[1]: 0.3f}", 2, (0, 0, 0))

    window.fill((255, 255, 255))
    window.blit(text1, (rect.left, rect.top+50))
    window.blit(text2, (rect.left, rect.top+80))
    draw(rect, center, normVector, radius, point, (0, 0, 0), (127, 127, 127), (255, 0, 0))
    pygame.display.flip()

pygame.quit()
exit()