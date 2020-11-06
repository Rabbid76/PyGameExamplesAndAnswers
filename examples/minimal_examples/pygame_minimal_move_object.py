# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# How to get keyboard input in pygame?
# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
#
# How can I make a sprite move when key is held down
# https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down
#
# How to get if a key is pressed pygame
# https://stackoverflow.com/questions/59830738/how-to-get-if-a-key-is-pressed-pygame/59831073#59831073

# GitHub - PyGameExamplesAndAnswers - Keys and keyboard events - Keys
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_keys_and_keyboard_event.md 

import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center
vel = 5

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    keys = pygame.key.get_pressed()
    
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
        
    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.flip()

pygame.quit()
exit()