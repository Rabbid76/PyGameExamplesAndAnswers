# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# No more than one button works at a time in pygame, how to fix this?
# https://stackoverflow.com/questions/69593109/no-more-than-one-button-works-at-a-time-in-pygame-how-to-fix-this/69593913#69593913
#
# How to use Pygame touch events in a mobile game?
# https://stackoverflow.com/questions/69593109/how-to-use-pygame-touch-events-in-a-mobile-game/69593913#69593913
#
# GitHub - Mouse - Mouse and mouse event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

buttons = [
    pygame.Rect(25, 25, 100, 100),
    pygame.Rect(175, 25, 100, 100),
    pygame.Rect(25, 175, 100, 100),
    pygame.Rect(175, 175, 100, 100)]
colors = [(64, 0, 0), (64, 64, 0), (0, 64, 0), (0, 0, 64)]
colorsH = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]

fingers = {}
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.FINGERDOWN:
            x = event.x * window.get_height()
            y = event.y * window.get_width()
            fingers[event.finger_id] = x, y
        if event.type == pygame.FINGERUP:
            fingers.pop(event.finger_id, None)

    highlight = [any(r.collidepoint(p) for _, p in fingers.items()) for _, r in enumerate(buttons)]

    window.fill(0)
    for rect, color, colorH, h in zip(buttons, colors, colorsH, highlight):
        c = colorH if h else color
        pygame.draw.rect(window, c, rect)
    pygame.display.flip()

pygame.quit()
exit()