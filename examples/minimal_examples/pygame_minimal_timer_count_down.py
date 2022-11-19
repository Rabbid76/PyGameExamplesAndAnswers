# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# Countdown timer in Pygame
# https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame/63551239#63551239 
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Time - Counter based on timer event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame
import math

pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
counter = 100
text = font.render(str(counter), True, (0, 128, 0))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event:
            counter -= 1
            text = font.render(str(counter), True, (0, 128, 0))
            if counter == 0:
                pygame.time.set_timer(timer_event, 0)                

    window.fill((255, 255, 255))
    text_rect = text.get_rect(center = window.get_rect().center)
    window.blit(text, text_rect)
    
    arc_rect = window.get_rect().inflate(-10, -10)
    percentage = counter/100
    end_angle = 2 * math.pi * percentage
    pygame.draw.arc(window, (255, 0, 0), arc_rect, 0, end_angle, 10)
    
    pygame.display.flip()

pygame.quit()
exit()