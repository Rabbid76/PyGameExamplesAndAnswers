# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# I define a movement method for a character, but I don't know how to itmake it pause for a moment between each move
# https://stackoverflow.com/questions/71546585/i-define-a-movement-method-for-a-character-but-i-dont-know-how-to-itmake-it-pa/71546649#71546649
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()
rect = pygame.Rect(0, 80, 40, 40)

time_interval = 500 # 500 milliseconds == 0.1 seconds
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_interval) 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        if event.type == timer_event:

            rect.x += 40
            if rect.x >= 400:
                rect.x = 0

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()