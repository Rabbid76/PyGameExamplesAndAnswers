# How to fade from one colour to another in pygame?
# https://stackoverflow.com/questions/51973441/how-to-fade-from-one-colour-to-another-in-pygame/68702388#68702388
# 
# GitHub - PyGameExamplesAndAnswers - Color
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_color.md

import pygame, math

def lerp_color(colors, value):
    fract, index = math.modf(value)
    color1 = pygame.Color(colors[int(index) % len(colors)])
    color2 = pygame.Color(colors[int(index + 1) % len(colors)])
    return color1.lerp(color2, fract)

pygame.init()
window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            start_time = pygame.time.get_ticks()

    colors = ["green", "blue", "purple", "pink", "red", "orange", "yellow"]
    value = (pygame.time.get_ticks() - start_time) / 1000
    current_color = lerp_color(colors, value)

    window.fill((255, 255, 255))
    pygame.draw.circle(window, current_color, window.get_rect().center, 100)
    pygame.display.flip()

pygame.quit()
exit()