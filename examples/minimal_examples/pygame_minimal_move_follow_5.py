# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# pygame 2 dimensional movement of an enemy towards the player, how to calculate x and y velocity?
# https://stackoverflow.com/questions/66404707/pygame-2-dimensional-movement-of-an-enemy-towards-the-player-how-to-calculate-x/66406985#66406985
#
# GitHub - Move towards target - Follow target or mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_move_towards_target.md

import pygame, math

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
player_x, player_y, player_vel = 100, 100, 5
enemy_x, enemy_y, enemy_vel = 300, 300, 3

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          
        
    keys = pygame.key.get_pressed()
    player_x = max(10, min(390, player_x + player_vel * (keys[pygame.K_d] - keys[pygame.K_a])))
    player_y = max(10, min(390, player_y + player_vel * (keys[pygame.K_s] - keys[pygame.K_w])))

    dx = player_x - enemy_x
    dy = player_y - enemy_y
    dist = math.hypot(dx, dy)
    if dist > 0:
        enemy_x += min(enemy_vel, dist) * dx / dist
        enemy_y += min(enemy_vel, dist) * dy / dist

    window.fill(0)
    pygame.draw.circle(window, (0, 128, 255), (player_x, player_y), 10)
    pygame.draw.circle(window, (255, 32, 32), (enemy_x, enemy_y), 10)
    pygame.display.flip()

pygame.quit()
exit()