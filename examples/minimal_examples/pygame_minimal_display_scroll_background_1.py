# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# Making the background move sideways in pygame
# https://stackoverflow.com/questions/55050166/making-the-background-move-sideways-in-pygame/55068602#55068602
#
# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Scroll background
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 100, *window.get_size(), (64, 64, 64), (127, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)
pos_x, speed = 0, 10

run = False
while not run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    keys = pygame.key.get_pressed()
    pos_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed

    bg_w = background.get_width()
    x_rel = pos_x % bg_w
    x_part2 = x_rel - bg_w if x_rel > 0 else x_rel + bg_w
    
    window.blit(background, (x_rel, 0))
    window.blit(background, (x_part2, 0))
    pygame.display.flip()

pygame.quit()
exit()