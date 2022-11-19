# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# How to scroll the background surface in PyGame?
# https://stackoverflow.com/questions/55319181/how-to-scroll-the-background-surface-in-pygame/55321731#55321731
#
# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Scroll background
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import pygame

def scrollX(target_surf, source_surf, offset_x):
    width, height = target_surf.get_size()
    target_surf.blit(source_surf, (offset_x, 0))
    if offset_x < 0:
        target_surf.blit(source_surf, (width + offset_x, 0), (0, 0, -offset_x, height))
    else:
        target_surf.blit(source_surf, (0, 0), (width - offset_x, 0, offset_x, height))

def scrollY(target_surf, source_surf, offset_y):
    width, height = source_surf.get_size()
    target_surf.blit(source_surf, (0, offset_y))
    if offset_y < 0:
        target_surf.blit(source_surf, (0, height + offset_y), (0, 0, width, -offset_y))
    else:
        target_surf.blit(source_surf, (0, 0), (0, height - offset_y, width, offset_y))

pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 100, *window.get_size(), (64, 64, 64), (127, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)
pos_x, pos_y, speed = 0, 0, 10

run = False
while not run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    keys = pygame.key.get_pressed()
    pos_x = (pos_x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed) % window.get_width()
    pos_y = (pos_y + (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed) % window.get_height()

    scrollX(window, background, pos_x)
    scrollY(window, window.copy(), pos_y)

    pygame.display.flip()

pygame.quit()
exit()
