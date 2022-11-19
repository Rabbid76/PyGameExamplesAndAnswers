# Setting up an invisible boundary for my sprite
# https://stackoverflow.com/questions/69180916/setting-up-an-invisible-boundary-for-my-sprite/69181366#69181366  
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Collide with frame, window border and restrict to rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame

pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 40, 40)
rect.center = window.get_rect().center
speed = 10

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    

    keys = pygame.key.get_pressed()
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed  
    rect.clamp_ip(pygame.display.get_surface().get_rect())    

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()