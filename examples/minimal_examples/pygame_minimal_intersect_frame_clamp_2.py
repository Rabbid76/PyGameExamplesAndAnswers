# Window border in pygame
# https://stackoverflow.com/questions/64205777/window-border-in-pygame/64206877#64206877
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Collide with frame, window border and restrict to rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

circleX, circleY, radius = window.get_width() // 2, window.get_height() // 2, 50
vel = 10

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circleX -= vel
    if keys[pygame.K_RIGHT]:
        circleX += vel
    if keys[pygame.K_UP]:
        circleY-= vel
    if keys[pygame.K_DOWN]:
        circleY += vel

    clampRect = window.get_rect().inflate(-radius*2, -radius*2)
    circleX = max(clampRect.left, min(clampRect.right, circleX))
    circleY = max(clampRect.top, min(clampRect.bottom, circleY))

    window.fill(0)
    pygame.draw.circle(window, (255, 0, 0), (circleX, circleY), radius)
    pygame.display.flip()

pygame.quit()
exit()