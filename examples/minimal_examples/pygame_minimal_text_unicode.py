# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# Displaying unicode symbols using pygame
# https://stackoverflow.com/questions/63398332/displaying-unicode-symbols-using-pygame/63398488#63398488
#
# GitHub - PyGameExamplesAndAnswers - Text and font
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((500, 500))

seguisy80 = pygame.font.SysFont("segoeuisymbol", 80)
queenblack = "♔"
queenblack = '\u2654'
queenblacktext = seguisy80.render(queenblack, True, BLACK)

run = True
while run:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(WHITE)
    window.blit(queenblacktext, (100, 100))
    pygame.display.flip()

pygame.quit()
exit()