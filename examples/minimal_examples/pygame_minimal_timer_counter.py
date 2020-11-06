# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# Python 3.8 pygame timer?
# https://stackoverflow.com/questions/59944795/python-3-8-pygame-timer/59944869#59944869  
#
# How to display dynamically in Pygame?
# https://stackoverflow.com/questions/56453574/how-to-display-dynamically-in-pygame/56454295#56454295
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Time - Counter based on timer event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame

pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)

counter = 0
text = font.render(str(counter), True, (0, 128, 0))

time_delay = 1000
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_delay)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event:
            counter += 1
            text = font.render(str(counter), True, (0, 128, 0))

    window.fill((255, 255, 255))
    text_rect = text.get_rect(center = window.get_rect().center)   
    window.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
exit()