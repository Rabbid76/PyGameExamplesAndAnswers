# Bouncing Ball doesn't come back pygame
# https://stackoverflow.com/questions/55001320/bouncing-ball-doesnt-come-back-pygame/55002157#55002157
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Collide with frame, window border and restrict to rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((400, 600))

try:
    ball = pygame.image.load("icon/Ball64.png")
except:
    ball = pygame.Surface((64, 64), pygame.SRCALPHA)
    pygame.draw.circle(ball, (255, 255, 0), (32, 32), 32)
balldiameter = ball.get_width()

(x, y) = (180, 200)
t = 1 # time variable
a = 2 # acceleration constant
tol = 40 # tolerance
i = 0 # just some iterator
direction = 1
start = False

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            start = True

    if start:
        y += (a * (t ^ 2)) * direction
        t += direction

        if abs(y - window.get_height()) < tol:
            y = window.get_height()-balldiameter/2
            t -= 1
            direction *= -1
        elif t == 0:
            direction *= -1
    
    window.fill((64, 64, 64))
    window.blit(ball, (round(x), round(y)))
    pygame.display.flip()

pygame.quit()
exit()