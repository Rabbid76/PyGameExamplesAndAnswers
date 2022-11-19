# Hypotrochoid
# https://en.wikipedia.org/wiki/Hypotrochoid
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame, math

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

center = window.get_rect().center
a, b, h = 100, 60, 100
points = []
for i in range(360*3):
    t = math.radians(i)
    x = (a-b)*math.cos(t) + h*math.cos((a-b)/b*t) + center[0]
    y = (a-b)*math.sin(t) - h*math.sin((a-b)/b*t) + center[1]
    points.append((x, y))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0) 
    pygame.draw.aalines(window, "white", True, points)
    pygame.display.flip()

pygame.image.save(window, "c:/temp/Hypotrochoid.png")
pygame.quit()
exit()
