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

pygame.init()
window = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

courer_regular = pygame.font.match_font("Courier", bold = False)
courer_bold = pygame.font.match_font("Courier", bold = True)

font = pygame.font.Font(courer_regular, 50)
font_b = pygame.font.Font(courer_bold, 50)
text1 = font.render("Some ", True, (255, 255, 255))
text2 = font_b.render("Text", True, (255, 255, 255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.fill(0)
    window.blit(text1, (50, 75))
    window.blit(text2, (50 + text1.get_width(), 75))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
