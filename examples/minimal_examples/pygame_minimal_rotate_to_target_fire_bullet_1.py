# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Why aren't any bullets appearing on screen? - pygame
# https://stackoverflow.com/questions/59126785/why-arent-any-bullets-appearing-on-screen-pygame/59126918#59126918 
#
# GitHub - PyGameExamplesAndAnswers - Move towards target - Move towards target Shoot a bullet in a certain direction - Rotate player and shoot bullet towards faced direction
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_move_towards_target.md

import os
import math
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def blit_point_to_mouse(target_surf, char_surf, x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    vector_x, vector_y = mouse_x - x, mouse_y - y
    angle = (180 / math.pi) * -math.atan2(vector_y, vector_x) - 90
    rotated_surface = pygame.transform.rotate(char_surf, round(angle))
    rotated_surface_location = rotated_surface.get_rect(center = (x, y))
    target_surf.blit(rotated_surface, rotated_surface_location)

def spawn_bullet(list_of_bullets, x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    vector_x, vector_y = mouse_x - x, mouse_y - y
    distance = math.hypot(vector_x, vector_y)
    if distance == 0:
        return
    speed = 5
    move_vec = (speed * vector_x / distance, speed * vector_y / distance)
    list_of_bullets.append([x, y, move_vec])

pygame.init()
window = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

rocket = pygame.image.load('icon/Rocket64.png')
rocket_rect = rocket.get_rect(center = window.get_rect().center)
velocity = 6
list_of_bullets = []
bullet = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(bullet, (64, 64, 64), (10, 10), 10)
pygame.draw.circle(bullet, (96, 96, 96), (10, 10), 9)
pygame.draw.circle(bullet, (128, 128, 128), (9, 9), 7)
pygame.draw.circle(bullet, (160, 160, 160), (8, 8), 5)
pygame.draw.circle(bullet, (192, 192, 192), (7, 7), 3)
pygame.draw.circle(bullet, (224, 224, 224), (6, 6), 1)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            spawn_bullet(list_of_bullets, *rocket_rect.center)

    for bullet_pos in list_of_bullets:
        bullet_pos[0] += bullet_pos[2][0]
        bullet_pos[1] += bullet_pos[2][1]
        if not (0 <= bullet_pos[0] < window.get_width() and 0 < bullet_pos[1] < window.get_height()):
            del list_of_bullets[list_of_bullets.index(bullet_pos)]
            continue

    keys = pygame.key.get_pressed()
    rocket_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * velocity
    rocket_rect.y += (keys[pygame.K_UP] - keys[pygame.K_DOWN]) * velocity
    rocket_rect.clamp_ip(window.get_rect())
    
    window.fill(0)
    for bullet_pos in list_of_bullets:
        window.blit(bullet, bullet.get_rect(center = (round(bullet_pos[0]),round(bullet_pos[1]))))
    blit_point_to_mouse(window, rocket, *rocket_rect.center)
    pygame.display.flip()

pygame.quit()
exit()