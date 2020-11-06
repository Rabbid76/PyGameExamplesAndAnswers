# pygame.freetype module
# https://www.pygame.org/docs/ref/freetype.html
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
import pygame.freetype

pygame.init()
ft_font = pygame.freetype.SysFont('Times New Roman', 50)

window = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    text_rect = ft_font.get_rect('test text')
    text_rect.center = window.get_rect().center
    ft_font.render_to(window, text_rect.topleft, 'test text', (255, 0, 0))
    pygame.display.flip()

pygame.quit()
exit()