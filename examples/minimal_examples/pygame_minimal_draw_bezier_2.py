# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How Can I Make a Thicker Bezier in Pygame?
# https://stackoverflow.com/questions/71365567/how-can-i-make-a-thicker-bezier-in-pygame/71365892#71365892
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Bezier
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame
import pygame.gfxdraw

def ptOnCurve(b, t):
    q = b.copy()
    for k in range(1, len(b)):
        for i in range(len(b) - k):
            q[i] = (1-t) * q[i][0] + t * q[i+1][0], (1-t) * q[i][1] + t * q[i+1][1]
    return round(q[0][0]), round(q[0][1])

def bezier(surf, b, samples, color, thickness):
    pts = [ptOnCurve(b, i/samples) for i in range(samples+1)]
    pygame.draw.lines(surf, color, False, pts, thickness)

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    x, y = pygame.mouse.get_pos()
    b_points = [(100, 100), (150, 100), (250, y), (x, y)]

    window.fill('black')
    bezier(window, b_points, 10, (128, 0, 0), 10)
    pygame.draw.lines(window, (128, 128, 128), False, b_points, 1)
    pygame.gfxdraw.bezier(window, b_points, 6, (255, 255, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()