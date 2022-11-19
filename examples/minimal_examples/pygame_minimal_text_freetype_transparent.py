# pygame.freetype module
# https://www.pygame.org/docs/ref/freetype.html
#
# Python - Pygame - rendering translucent text
# https://stackoverflow.com/questions/20620109/how-to-render-transparent-text-with-alpha-channel-in-pygame/64552616#64552616
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Transparent text
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
#
# https://replit.com/@Rabbid76/PyGame-TransparentFreeTypeText#main.py

import pygame
import pygame.freetype

pygame.init()

window = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()
ft_font = pygame.freetype.SysFont('Times New Roman', 150)

text_surf2, text_rect2 = ft_font.render('test text', (255, 0, 0, 128))

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
    
    text_rect = ft_font.get_rect('test text')
    text_rect.center = (window.get_width() // 2, window.get_height() // 2 - 70)
    ft_font.render_to(window, text_rect.topleft, 'test text', (255, 0, 0, 128))
    
    text_rect2.center = (window.get_width() // 2, window.get_height() // 2 + 70)
    window.blit(text_surf2, text_rect2)
    
    pygame.display.flip()

pygame.quit()
exit()