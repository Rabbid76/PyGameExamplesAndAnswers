# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# PyGame collision with masks
# https://stackoverflow.com/questions/57455811/pygame-collision-with-masks/57499484#57499484
#
# Collision between masks in PyGame
# https://stackoverflow.com/questions/55817422/collision-between-masks-in-pygame/55818093#55818093
#
# GitHub - Sprite, Group and Sprite mask - Sprite mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SurfaceMaskIntersect

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

moving_object = pygame.image.load('icon/AirPlaneFront1-128.png').convert_alpha()
obstacle = pygame.image.load('icon/Rocket64.png').convert_alpha()
moving_object_mask = pygame.mask.from_surface(moving_object)
obstacle_mask = pygame.mask.from_surface(obstacle)
obstacle_rect = obstacle.get_rect(center = window.get_rect().center)
red = 1

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    moving_object_rect = moving_object.get_rect(center = pygame.mouse.get_pos())
    #moving_object_rect = moving_object.get_rect(center = (window.get_width() // 2, window.get_height() // 2 + round(math.sin(pygame.time.get_ticks()/1000) * 90)))

    offset = (obstacle_rect.x - moving_object_rect.x), (obstacle_rect.y - moving_object_rect.y)
    background_color = (0, 0, 0)
    if moving_object_mask.overlap(obstacle_mask, offset):
        red = min(255, red+4)
        background_color = (red, 0, 0)
    else: 
        red = 1

    window.fill(background_color)
    window.blit(moving_object, moving_object_rect)
    window.blit(obstacle, obstacle_rect)
    pygame.display.flip()