# pygame.Rect object
# https://www.pygame.org/docs/ref/rect.html#pygame.Rect
#
# How do I detect collision in pygame?
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame/65064907#65064907
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Overview
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-collidepoint

import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))
rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(100, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    point = pygame.mouse.get_pos()
    collide = rect.collidepoint(point)
    color = (255, 0, 0) if collide else (255, 255, 255)
    
    window.fill(0)
    pygame.draw.rect(window, color, rect)
    pygame.display.flip()

pygame.quit()
exit()
