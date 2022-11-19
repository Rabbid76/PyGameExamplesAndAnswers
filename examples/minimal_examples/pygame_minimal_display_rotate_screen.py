# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# Rotate pygame screen
# https://stackoverflow.com/questions/69394255/rotate-pygame-screen/69394709#69394709
#
# GitHub - Display, display position, resize, coordinate system and scroll - PyGameExamplesAndAnswers - Coordinate system
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
font = pygame.font.SysFont(None, 100)
clock = pygame.time.Clock()
text = font.render("Display", True, (255, 255, 0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.fill(0)
    window.blit(text, text.get_rect(center = window.get_rect().center))
    window.blit(pygame.transform.rotate(window, 90), (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()