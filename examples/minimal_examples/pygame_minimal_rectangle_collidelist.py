# pygame.Rect object
# https://www.pygame.org/docs/ref/rect.html
#
# Pygame: colliding rectangles with other rectangles in the same list
# https://stackoverflow.com/questions/54793858/pygame-colliding-rectangles-with-other-rectangles-in-the-same-list/54794440#54794440
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Rectangle and rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_rectangle.md

import pygame

pygame.init()

window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    w, h = window.get_size()
    rectangles = []
    for x in range(0, w - 29, 30):
        for y in range(0, h - 29, 30):
            rectangles.append(pygame.Rect(x + 15, y + 15, 20, 20))

    point = pygame.mouse.get_pos()

    window.fill(0)
    for r in rectangles:
        pygame.draw.rect(window, (255, 0, 0), r)
    collideindex = pygame.Rect(point, (1, 1)).collidelist(rectangles)
    if collideindex >= 0:
        pygame.draw.rect(window, (255, 255, 255), rectangles[collideindex].inflate(2, 2), 2)
    pygame.display.flip()

pygame.quit()
exit()