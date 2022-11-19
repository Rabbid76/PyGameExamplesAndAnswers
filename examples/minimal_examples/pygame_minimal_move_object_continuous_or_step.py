# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# I have a function that detects if i press a key in pygame, but it only detects one key?
# https://stackoverflow.com/questions/73953058/i-have-a-function-that-detects-if-i-press-a-key-in-pygame-but-it-only-detects-o/73953116#73953116
#
# GitHub - PyGameExamplesAndAnswers - Keys and keyboard events - Keys
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_keys_and_keyboard_event.md 

import pygame

key_count = {}
def key_pressed(keys, key, one_click):
    pressed = keys[key]
    key_count[key] = (key_count.get(key, 0) + 1) if pressed else 0
    return key_count[key] == 1 if one_click else pressed

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

rect = pygame.Rect(190, 190, 20, 20)
single_step = False

run = True
while run:
    clock.tick(100)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            single_step = not single_step

    keys = pygame.key.get_pressed()
    speed = 20 if single_step else 2
    rect.x += (key_pressed(keys, pygame.K_d, single_step) - key_pressed(keys, pygame.K_a, single_step)) * speed
    rect.y += (key_pressed(keys, pygame.K_s, single_step) - key_pressed(keys, pygame.K_w, single_step)) * speed
    rect.x %= 400
    rect.y %= 400
    
    window.fill(0)
    pygame.draw.rect(window, "red", rect)
    pygame.display.flip()

pygame.quit()
exit()
