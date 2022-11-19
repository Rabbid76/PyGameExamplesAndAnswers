# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# Python 3.8 pygame timer?
# https://stackoverflow.com/questions/59944795/python-3-8-pygame-timer/59944869#59944869  
#
# pygame tetris fever_mode adding timer
# https://stackoverflow.com/questions/69590294/pygame-tetris-fever-mode-adding-timer/69590304?noredirect=1#comment123004378_69590304
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Time - Counter based on timer event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame
pygame.init()
window = pygame.display.set_mode((200, 200))

pygame.time.set_timer(pygame.USEREVENT, 500)
blink = True

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.USEREVENT:
            blink = not blink
    
    window.fill(0)
    if blink:
        pygame.draw.circle(window, (255, 0, 0), (100, 100), 80)
    pygame.display.flip()

pygame.quit()
exit()