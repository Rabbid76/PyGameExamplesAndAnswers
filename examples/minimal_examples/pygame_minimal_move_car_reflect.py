# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# The car moves and changes direction when it hits the window edge
# https://stackoverflow.com/questions/65001510/the-car-moves-and-changes-direction-when-it-hits-the-window-edge/65010442#65010442
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 
#
# https://replit.com/@Rabbid76/PyGame-CarMovementReflect

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

player_image = pygame.image.load('icon/CarRed64.png').convert_alpha()
player_pos = pygame.math.Vector2(player_image.get_width() // 2, window.get_height() // 2)
player_move = pygame.math.Vector2(0, 0)
speed = 3

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            dx = event.pos[0] - player_pos.x
            dy = event.pos[1] - player_pos.y
            if dx != 0 or dY != 0:
                player_move = pygame.math.Vector2(dx, dy)
                player_move.scale_to_length(speed)

    player_pos += player_move
    player_rect = player_image.get_rect(center = (round(player_pos.x), round(player_pos.y)))
    if player_rect.left < 0:
       player_rect.left = 0 
       player_pos.x = player_rect.centerx
       player_move.x = abs(player_move.x)
    if player_rect.right > window.get_width():
       player_rect.right = window.get_width()
       player_pos.x = player_rect.centerx
       player_move.x = -abs(player_move.x)
    if player_rect.top < 0:
       player_rect.top = 0 
       player_pos.y = player_rect.centery
       player_move.y = abs(player_move.y)
    if player_rect.bottom > window.get_height():
       player_rect.bottom = window.get_height()
       player_pos.y = player_rect.centery
       player_move.y = -abs(player_move.y)

    angle = player_move.angle_to((1, 0))
    rotated_player = pygame.transform.rotate(player_image, angle)
    rotated_rect = rotated_player.get_rect(center = player_rect.center)
    
    window.fill((247, 247,247))
    window.blit(rotated_player, rotated_rect)    
    pygame.display.flip()

pygame.quit()
exit()