# HSV to RGB Color Conversion
# https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
# 
# GitHub - PyGameExamplesAndAnswers - Color
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_color.md

import pygame

pygame.init()

window = pygame.display.set_mode((450, 300))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    w, h = window.get_size()
    for i in range(6):
        color = pygame.Color(0)
        color.hsla = (i * 60, 100, 50, 100)
        pygame.draw.circle(window, color, 
            (w//6 + w//3 * (i%3), h//4 + h//2 * (i//3)), 
            round(min(window.get_width() * 0.16, window.get_height() * 0.2)))

    pygame.display.flip()

pygame.quit()
exit()