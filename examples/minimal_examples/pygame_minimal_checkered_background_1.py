# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# How To Create A Checkered Background Using Pygame Surfarrays?
# https://stackoverflow.com/questions/73277963/how-to-create-a-checkered-background-using-pygame-surfarrays/73278096#73278096  
#
# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Checkered background
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()