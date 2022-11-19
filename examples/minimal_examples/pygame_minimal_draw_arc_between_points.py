# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Creating an arc between two points pygame
# https://stackoverflow.com/questions/58954526/creating-an-arc-between-two-points-pygame/58959662#58959662
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw arc
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import math
import pygame

def distance(A, B):
    return math.hypot(B[0] - A[0], B[1] - A[1])

def angle(A, B, aspectRatio):
    return math.atan2(A[1] - B[1], (B[0] - A[0]) / aspectRatio)

pygame.init()
window = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    center, lenA, lenB = (window.get_width() // 2, window.get_height() // 2 - 100), 500, 350
    pts = [(center[0]-175, center[1]+125), (center[0]+150, center[1]+140)]
    ptsC = [(255, 0, 0), (0, 0, 255)]
    
    distances = [distance(center, p) for p in pts]
    angles = [angle(center, p, lenA / lenB) for p in pts]
    
    window.fill((255, 255, 255))
    for p in pts:
        pygame.draw.line(window, (0, 196, 0), center, p, 1)
    pygame.draw.arc(window, (0, 0, 0), (center[0] - lenA // 2, center[1] - lenB // 2, lenA, lenB), *angles)
    for p, c in zip(pts, ptsC):
        pygame.draw.line(window, c, [p[0], p[1]-20], [p[0], p[1]+20], 1)
        pygame.draw.line(window, c, [p[0]-20, p[1]], [p[0]+20, p[1]], 1)
    pygame.display.flip()

pygame.quit()
exit()