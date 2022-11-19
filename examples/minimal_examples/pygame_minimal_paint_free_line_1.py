# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Line drawing in pygame
# https://stackoverflow.com/questions/66491982/line-drawing-in-pygame/66492121#66492121
#
# GitHub - PyGameExamplesAndAnswers - Paint
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_paint.md
#
# https://replit.com/@Rabbid76/PyGame-PaintFreeThickLine

import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

lines = []
draw = False

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False      
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = not draw
            if draw:
               lines.append([event.pos])
        if event.type == pygame.MOUSEMOTION and draw:
            lines[-1].append(event.pos)


    window.fill((255, 255, 255))
    for points in lines:
        if len(points) > 1:
            pygame.draw.lines(window, (0, 0, 0), False, points, 50)
            for p in points:
                pygame.draw.circle(window, (0, 0, 0), p, 25)
    pygame.display.flip()

pygame.quit()
exit()