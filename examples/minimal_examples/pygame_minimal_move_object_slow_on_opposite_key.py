# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# Python only running while loop once
# https://stackoverflow.com/questions/59706667/python-only-running-while-loop-once/59706711#59706711
#
# How to get if a key is pressed pygame
# https://stackoverflow.com/questions/59830738/how-to-get-if-a-key-is-pressed-pygame/59831073#59831073
#
# Changing movement speed when multiple keys are pressed
# https://stackoverflow.com/questions/64321190/changing-movement-speed-when-multiple-keys-are-pressed/64321597#64321597
#
# GitHub - PyGameExamplesAndAnswers - Keys and keyboard events - Keys
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_keys_and_keyboard_event.md 

import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center
vel = 5

last_direction_key = None
run = True
while run:
    clock.tick(60)
    
    pressed=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
                last_direction_key = event.key
     
   
    if pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]:
        if last_direction_key == pygame.K_LEFT:
            rect.x += 3
        else:
            rect.x -= 3
    elif pressed[pygame.K_LEFT]:
        rect.x -= 6
    elif pressed[pygame.K_RIGHT]:
        rect.x += 6
        
    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()

    window.fill('black')
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.flip()

pygame.quit()
exit()