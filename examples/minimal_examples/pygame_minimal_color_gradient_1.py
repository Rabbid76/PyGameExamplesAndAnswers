# How would I make a heatmap in pygame on a grid
# https://stackoverflow.com/questions/55617119/how-would-i-make-a-heatmap-in-pygame-on-a-grid/55618024#55618024
# 
# GitHub - PyGameExamplesAndAnswers - Color
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_color.md

import pygame
pygame.init()

window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(20, 20)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    rect.clamp_ip(window.get_rect().inflate(-10, -10))

    fx = rect.centerx / window.get_width()
    fy = rect.centery / window.get_height()
    color = (63 + 128 * fx, 63 + 128 * fy, 63 + 128 * (1-fx) * (1-fy), 255)

    grid_size = 10
    grid_width = window.get_width() / grid_size
    grid_height = window.get_height() / grid_size
    grid_margin = 0
    distance_from_left = 0
    distance_from_top = 0

    pos_center = rect.center
    grid = []
    for y in range(grid_size):
        row = []
        for x in range(grid_size):

            gx = x * (grid_width + grid_margin) + distance_from_left
            gy = y * (grid_height + grid_margin) + distance_from_top
            distance = pygame.math.Vector2(rect.center).distance_to((gx + grid_width/2, gy + grid_height/2))
            maxLen = grid_size * (grid_height + grid_margin)

            f = max(0, 1 - distance / maxLen)
            color = (127 * f, 191 * f, 63 + 192 * f)

            row.append([gx, gy, color])
        grid.append(row)

    window.fill(0)
    for row in grid:
        for x, y, colour in row:
            pygame.draw.rect(window, colour, (x, y, grid_width, grid_height))

    pygame.draw.rect(window, (255, 0, 0), window.get_rect(), 8)
    pygame.draw.line(window, (255, 0, 0), rect.topleft, rect.bottomright, 3)
    pygame.draw.line(window, (255, 0, 0), rect.bottomleft, rect.topright, 3)
    pygame.display.flip()

pygame.quit()
exit()