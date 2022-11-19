# How would I clamp the player sprite to a certain polygon boundary
# https://stackoverflow.com/questions/73991746/how-would-i-clamp-the-player-sprite-to-a-certain-polygon-boundary/74085878#74085878
#
# GitHub - PyGameExamplesAndAnswers - Mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mask.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))
import pygame, math

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

cage_mask_image = pygame.Surface((200, 300), pygame.SRCALPHA)
pygame.draw.circle(cage_mask_image, "white", (100, 100), 100)
pygame.draw.rect(cage_mask_image, "white", (0, 100, 200, 200))
cage_mask = pygame.mask.from_surface(cage_mask_image)
cage_rect = cage_mask_image.get_rect(center = (200, 200))

bird_image = pygame.image.load('icon/Bird64.png').convert_alpha()
bird_mask = pygame.mask.from_surface(bird_image)
bird_mask_count = bird_mask.count()
bird_rect = bird_image.get_rect(center = (200, 200))
speed = 5

cage_color = (64, 64, 64)
cage_image = pygame.Surface((200, 300), pygame.SRCALPHA)
pygame.draw.arc(cage_image, cage_color, (0, 0, 200, 200), 0, math.pi, 5)
pygame.draw.rect(cage_image, cage_color, (0, 100, 200, 200), 5)
pygame.draw.line(cage_image, cage_color, (100, 0), (100, 300), 5)
for x in [33, 66, 134, 167]:
    pygame.draw.line(cage_image, cage_color, (x, 100), (x, 300), 5)
for x in [33, 66]:
    pygame.draw.arc(cage_image, cage_color, (x, 0, 200-x*2, 200), 0, math.pi, 5)
   

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    keys = pygame.key.get_pressed()
    new_bird_rect = bird_rect.copy()
    new_bird_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    new_bird_rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
    offset_x = new_bird_rect.x - cage_rect.x
    offset_y = new_bird_rect.y - cage_rect.y
    overlap_count = cage_mask.overlap_area(bird_mask, (offset_x, offset_y))
    if overlap_count == bird_mask_count:
        bird_rect = new_bird_rect

    window.fill("lightblue")
    window.blit(bird_image, bird_rect)
    window.blit(cage_image, cage_rect)
    pygame.display.flip()

pygame.quit()
exit()