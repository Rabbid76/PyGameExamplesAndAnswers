# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# How to turn the sprite in pygame while moving with the keys
# https://stackoverflow.com/questions/64792467/how-to-turn-the-sprite-in-pygame-while-moving-with-the-keys/64792568#64792568
#
# Image rotation while moving
# https://stackoverflow.com/questions/57226587/image-rotation-while-moving/57227063#57227063
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 
#
# https://replit.com/@Rabbid76/PyGame-CarMovement

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

car = pygame.image.load('icon/CarRed64.png')
position = pygame.math.Vector2(window.get_rect().center)
direction = pygame.math.Vector2(5, 0)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        position += direction
    if keys[pygame.K_s]:
        position -= direction
    if keys[pygame.K_a]:
        direction.rotate_ip(-1)
    if keys[pygame.K_d]:
        direction.rotate_ip(1)

    window.fill(0)
    angle = direction.angle_to((1, 0))
    rotated_car = pygame.transform.rotate(car, angle)
    window.blit(rotated_car, rotated_car.get_rect(center = (round(position.x), round(position.y))))
    pygame.display.flip()

pygame.quit()
exit()