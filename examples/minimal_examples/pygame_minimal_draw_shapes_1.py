# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Pygame Drawing a Rectangle
# https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle/64629716#64629716
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md
#
# https://replit.com/@Rabbid76/PyGame-Shapes

import pygame

pygame.init()

window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))

    pygame.draw.rect(window, (0, 0, 255), (20, 20, 160, 160))
    pygame.draw.circle(window, (255, 0, 0), (100, 100), 80)
    pygame.draw.polygon(window, (255, 255, 0), 
        [(100, 20), (100 + 0.8660 * 80, 140), (100 - 0.8660 * 80, 140)])

    pygame.display.flip()

pygame.quit()
exit()