# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# How to create a text input box with pygame?
# https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame/64613666#64613666
#
# How to make a string's content appears on screen as we type on keyboard?
# https://stackoverflow.com/questions/60455692/how-to-make-a-strings-content-appears-on-screen-as-we-type-on-keyboard/60456556#60456556
#
# GitHub - PyGameExamplesAndAnswers - Text and font
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
#
# https://replit.com/@Rabbid76/PyGame-TextInput#main.py

import pygame
pygame.init()
window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 100)
text = ""
input_active = True

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode

        window.fill(0)
        text_surf = font.render(text, True, (255, 0, 0))
        window.blit(text_surf, text_surf.get_rect(center = window.get_rect().center))
        pygame.display.flip()

pygame.quit()
exit()