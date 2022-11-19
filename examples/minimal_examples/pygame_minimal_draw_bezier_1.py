# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Trying to make a Bezier Curve on PyGame library
# https://stackoverflow.com/questions/69804595/trying-to-make-a-bezier-curve-on-pygame-library/69816648#69816648
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Bezier
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock() 

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    p0,  p1, p2 = (250, 200), pygame.mouse.get_pos(), (250, 300)

    window.fill(0)
    for p in [p0, p1, p2]:
        pygame.draw.circle(window, (255, 255, 255), p, 5)
    for i in range(101):
        t = i / 100
        px = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
        py = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2       
        pygame.draw.rect(window, (255, 255, 0), (px, py, 1, 1))

    pygame.display.update()

pygame.quit()
exit()