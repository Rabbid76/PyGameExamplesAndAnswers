# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# How to make a circular countdown timer in Pygame?
# https://stackoverflow.com/questions/67168804/how-to-make-a-circular-countdown-timer-in-pygame/67168896#67168896
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Time - Counter based on timer event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame
import cv2
import numpy
import math

pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
counter = 100
text = font.render(str(counter), True, (0, 128, 0))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

def drawArc(surf, color, center, radius, width, end_angle):
    arc_rect = pygame.Rect(0, 0, radius*2, radius*2)
    arc_rect.center = center
    pygame.draw.arc(surf, color, arc_rect, 0, end_angle, width)

def drawArcCv2(surf, color, center, radius, width, end_angle):
    circle_image = numpy.zeros((radius*2+4, radius*2+4, 4), dtype = numpy.uint8)
    circle_image = cv2.ellipse(circle_image, (radius+2, radius+2),
        (radius-width//2, radius-width//2), 0, 0, end_angle, (*color, 255), width, lineType=cv2.LINE_AA) 
    circle_surface = pygame.image.frombuffer(circle_image.flatten(), (radius*2+4, radius*2+4), 'RGBA')
    surf.blit(circle_surface, circle_surface.get_rect(center = center))

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
    #drawArc(window, (255, 0, 0), (100, 100), 90, 10, 2*math.pi*counter/100)
    drawArcCv2(window, (255, 0, 0), (100, 100), 90, 10, 360*counter/100)
    pygame.display.flip()

pygame.quit()
exit()