# pygame.freetype module
# https://www.pygame.org/docs/ref/freetype.html
#
# Pygame: Centering text system font text
# https://stackoverflow.com/questions/65278123/pygame-centering-text-system-font-text/65278233#65278233
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Align text and text size
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md

import pygame
import pygame.freetype

pygame.init()
window = pygame.display.set_mode((400, 200))

def drawTextCentered(surface, text, text_size, color):
    text_rect = font.get_rect(text, size = 50)
    text_rect.center = surface.get_rect().center 
    font.render_to(surface, text_rect, text, color, size = 50)  

font = pygame.freetype.SysFont("comicsansms", 0) 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    drawTextCentered(window, "Hello World", 50, (255, 0, 0))  
    pygame.display.flip()

pygame.quit()
exit()