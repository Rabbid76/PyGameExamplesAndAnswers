# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# I want to make the character run faster if I press the key twice in a row in a game [closed]
# https://stackoverflow.com/questions/64311651/i-want-to-make-the-character-run-faster-if-i-press-the-key-twice-in-a-row-in-a-g/64311802#64311802
#
# GitHub - PyGameExamplesAndAnswers - Keys and keyboard events - Keys
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_keys_and_keyboard_event.md 

import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center

vel = 0
key_time = 0
fast_key_time = 500 # 0.5 seconds

run = True
while run:
    current_time = pygame.time.get_ticks()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if vel == -5 and current_time < key_time + fast_key_time:
                    vel = -10
                else:
                    vel = -5
                key_time = current_time
            if event.key == pygame.K_RIGHT:
                if vel == 5 and current_time < key_time + fast_key_time:
                    vel = 10
                else:
                    vel = 5
                key_time = current_time

    rect.x += vel
        
    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.flip()

pygame.quit()
exit()