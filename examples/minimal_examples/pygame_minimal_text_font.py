# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# How to display some text in pygame?
# https://stackoverflow.com/questions/58695609/how-to-display-some-text-in-pygame/58695757#58695757
#
# How to scale the font size in pygame based on display resolution?
# https://stackoverflow.com/questions/56855775/how-to-scale-the-font-size-in-pygame-based-on-display-resolution/56857032#56857032
#
# I need to add text to my rectangles, how would I do this?
# https://stackoverflow.com/questions/55511081/i-need-to-add-text-to-my-rectangles-how-would-i-do-this/55521100#55521100
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Text
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md

import pygame
import pygame.font

pygame.init()
font = pygame.font.SysFont(None, 50)
text = font.render('Hello World', True, (255, 0, 0))

window = pygame.display.set_mode((300, 100))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(text, text.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()