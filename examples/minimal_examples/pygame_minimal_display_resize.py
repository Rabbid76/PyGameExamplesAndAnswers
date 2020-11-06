# pygame.display module
# https://www.pygame.org/docs/ref/display.html

# python pygame the background image changes with the screen size
# https://stackoverflow.com/questions/59694909/python-pygame-the-background-image-changes-with-the-screen-size/59694983#59694983

# Switching to Pygame Fullscreen Mode working only one time
# https://stackoverflow.com/questions/62412357/switching-to-pygame-fullscreen-mode-working-only-one-time/62413119#62413119

# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Resize and resize event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
width, height = 500, 500
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
clock = pygame.time.Clock()

screen_width, screen_height = 1920, 1080

img = "image/parrot1.png"
bk_orig = pygame.image.load(img).convert()
bk = pygame.transform.smoothscale(bk_orig, (width, height))

fullscreen = False

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.VIDEORESIZE:
            width, height = event.size
            type = pygame.FULLSCREEN if fullscreen else pygame.RESIZABLE
            window = pygame.display.set_mode(event.size, type)
            bk = pygame.transform.smoothscale(bk_orig, (width, height))

        elif event.type == pygame.KEYDOWN:
            if not fullscreen and event.key == pygame.K_f:
                fullscreen = True
                pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, size = (screen_width, screen_height)))
            if fullscreen and event.key == pygame.K_ESCAPE:
                fullscreen = False
                pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, size = (500, 500)))

    window.blit(bk, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()