# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# Make a Single Word Within a String Bold
# https://stackoverflow.com/questions/72409725/make-a-single-word-within-a-string-bold/72409816#72409816
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Bold
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
#
# https://replit.com/@Rabbid76/PyGame-Text

import pygame
import pygame.freetype

pygame.init()
window = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

ft_font = pygame.freetype.SysFont('Courier', 50)
text1, rect1 = ft_font.render("Some ",
    fgcolor = (255, 255, 255), style = pygame.freetype.STYLE_DEFAULT)
text2, rect2 = ft_font.render("Text", 
    fgcolor = (255, 255, 255), style = pygame.freetype.STYLE_STRONG)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window_center = window.get_rect().center

    window.fill(0)
    window.blit(text1, (50, 75))
    window.blit(text2, (50 + rect1.width, 75))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
