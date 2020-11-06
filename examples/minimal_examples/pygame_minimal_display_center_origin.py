# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# How do I change the Pygame coordinate system so that the center of the window is (0,0)?
# https://stackoverflow.com/questions/61514113/how-do-i-change-the-pygame-coordinate-system-so-that-the-center-of-the-window-is/61516769#61516769
#
# GitHub - Display, display position, resize, coordinate system and scroll - PyGameExamplesAndAnswers - Coordinate system
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

def center_origin_func(surf, p):
    return (p[0] + surf.get_width() // 2, p[1] + surf.get_height() // 2)

center_origin = lambda p: (p[0] + screen.get_width() // 2, p[1] + screen.get_height() // 2)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    screen.fill(0)

    pygame.draw.circle(screen, (255, 0, 0), center_origin_func(screen, (0, 0)), 100)
    pygame.draw.circle(screen, (0, 255, 0), center_origin((0, 0)), 50)

    pygame.display.flip()

pygame.quit()
exit()