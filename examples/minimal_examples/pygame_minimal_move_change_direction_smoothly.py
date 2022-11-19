# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# How to change my ball direction by clicking keys in pygame?
# https://stackoverflow.com/questions/65358328/how-to-change-my-ball-direction-by-clicking-keys-in-pygame/65358558#65358558  
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate - Move in grid
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import pygame
import random

pygame.init()
window = pygame.display.set_mode((300, 300))
background = pygame.Surface(window.get_size(), pygame.SRCALPHA)
background.fill((0, 0, 0, 1))
clock = pygame.time.Clock()

x = random.randint(100, 200)
y = random.randint(100, 200)
direction = pygame.math.Vector2(1, 0).rotate(random.randint(0, 360))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction.rotate_ip(-1)
    if keys[pygame.K_RIGHT]:
        direction.rotate_ip(1)

    x = (direction.x + x) % window.get_width()
    y = (direction.y + y) % window.get_height()
    #x = max(0, min(direction.x + x, win.get_width()))
    #y = max(0, min(direction.y + y, win.get_height()))
    
    window.blit(background, (0, 0))
    pygame.draw.circle(window, (255,0,0), (round(x), round(y)), 6)
    pygame.display.update()

pygame.quit()