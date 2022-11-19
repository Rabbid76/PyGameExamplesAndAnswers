# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Why it doesn't spin in a circle? And how to fix it?
# https://stackoverflow.com/questions/62883103/why-it-doesnt-spin-in-a-circle-and-how-to-fix-it/62883770#62883770
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import os
import math
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

image = pygame.transform.flip(pygame.image.load('icon/Rocket64.png').convert_alpha(), False, True)
angle = 0
pos_list = []
x, y = screen.get_width() // 2 + 100, screen.get_height() // 2
vel, angle_step = 5, 3

start = False
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    x -= math.sin(math.radians(angle)) * vel
    y += math.cos(math.radians(angle)) * vel 
    if angle + angle_step >= 360:
        pos_list.clear()
        angle = 0
    else:
        angle += angle_step

    if (x, y) not in pos_list:
        pos_list.append((x, y))
    rot_image = pygame.transform.rotate(image, -angle)

    screen.fill((122,122,122))
    if len(pos_list) > 1:
        pygame.draw.lines(screen, (0, 0, 0), False, pos_list)
    screen.blit(rot_image, rot_image.get_rect(center = (round(x), round(y))))
    pygame.display.flip()

pygame.quit()
exit()