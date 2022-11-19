# pygame.freetype module
# https://www.pygame.org/docs/ref/freetype.html
#
# How to scale the font size in pygame based on display resolution?
# https://stackoverflow.com/questions/56855775/how-to-scale-the-font-size-in-pygame-based-on-display-resolution/56857032#56857032
#
# I need to add text to my rectangles, how would I do this?
# https://stackoverflow.com/questions/55511081/i-need-to-add-text-to-my-rectangles-how-would-i-do-this/55521100#55521100
#
# Pygame smooth fonts
# https://stackoverflow.com/questions/20088670/pygame-smooth-fonts/65406337#65406337
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Text
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
#
# https://replit.com/@Rabbid76/PyGame-FreeTypeText

import pygame
import pygame.freetype

pygame.init()
window = pygame.display.set_mode((500, 150))
clock = pygame.time.Clock()

ft_font = pygame.freetype.SysFont('Times New Roman', 80)

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))
    text_rect = ft_font.get_rect('Hello World')
    text_rect.center = window.get_rect().center
    ft_font.render_to(window, text_rect.topleft, 'Hello World', (255, 0, 0))
    pygame.display.flip()

pygame.quit()
exit()