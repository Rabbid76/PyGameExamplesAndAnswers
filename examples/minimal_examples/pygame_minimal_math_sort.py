# I want to make a visualized bubble sort in pygame, the sort works but the visualization doesn't
# https://stackoverflow.com/questions/58039583/i-want-to-make-a-visualized-bubble-sort-in-pygame-the-sort-works-but-the-visual/58039872#58039872
#
# GitHub - PyGameExamplesAndAnswers - Math and Vector - Sort
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_math_vector_and_reflection.md

import pygame
import random

pygame.init()

window = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

max_number = window.get_width() // 10
numbers_to_order = list(range(1, max_number+1))
random.shuffle(numbers_to_order)

# start control variables
i, j = 0, 0

run = True
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    bar_width = window.get_width() // len(numbers_to_order)
    scale_height = window.get_height() // len(numbers_to_order)
    for k, n in enumerate(numbers_to_order):
        rect = (k * bar_width, window.get_height() - n * scale_height, bar_width, n * scale_height)
        color = pygame.Color(255, 255, 255)
        color.hsla = (int(360 * n / max_number), 100, 50, 100)
        pygame.draw.rect(window, color, rect)
    pygame.display.flip()
    
    # sort (1 step)
    try:
        if numbers_to_order[j] > numbers_to_order[j+1]:
            x = numbers_to_order[j]
            numbers_to_order[j] = numbers_to_order[j+1]
            numbers_to_order[j+1] = x
    except(IndexError):
        pass

    # increment control variables
    if j < len(numbers_to_order)-1:
        j += 1
    elif i < len(numbers_to_order)-1:
        i += 1
        j = 0

pygame.quit()
exit()