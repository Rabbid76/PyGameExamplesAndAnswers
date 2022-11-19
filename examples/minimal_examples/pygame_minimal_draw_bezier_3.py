# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# [How to make sprite move to point along a curve in pygame
# https://stackoverflow.com/questions/74070512/how-to-make-sprite-move-to-point-along-a-curve-in-pygame/74070714#74070714
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Bezier
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock() 

def bezier(p0, p1, p2, t):
    px = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
    py = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2   
    return px, py

dx = 0
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pts = [(100, 100), (100, 400), (400, 400)]

    window.fill(0)
    for p in pts:
        pygame.draw.circle(window, (255, 255, 255), p, 5)
    for i in range(101):
        x, y = bezier(*pts, i / 100)
        pygame.draw.rect(window, (255, 255, 0), (x, y, 1, 1))

    p = bezier(*pts, dx / 100)
    dx = (dx + 1) % 101
    pygame.draw.circle(window, (255, 0, 0), p, 5)
    pygame.display.update()

pygame.quit()
exit()