# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# Pygame- rotate sprite and follow path simultaneously
# https://stackoverflow.com/questions/56297756/pygame-rotate-sprite-and-follow-path-simultaneously/56298370#56298370
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Throw
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

ball = pygame.sprite.Sprite()
ball.orig_image = pygame.image.load('icon/Ball64.png')
ball.image = ball.orig_image
start_pos = ball.image.get_width() // 2 + 20, ball.image.get_height() // 2 + 20
ball.rect = ball.image.get_rect(center = start_pos)

group = pygame.sprite.GroupSingle(ball)

i = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if i < 65:
        ball.image = pygame.transform.rotate(ball.orig_image, i*20)
        x, y = start_pos[0] + i*5, start_pos[1] + ((i-20)*(i-20) + 1) / 5
        ball.rect = ball.image.get_rect(center = (x, y))
    
    group.draw(window)
    pygame.display.flip()

    i += 1
    if i >= 120:
        i = 0
        window.fill(0)

pygame.quit()
exit()