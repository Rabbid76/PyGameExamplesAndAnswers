# Problem with recognising where a ray in raycaster intersects a wall along the horizontal axis
# https://stackoverflow.com/questions/73776052/problem-with-recognising-where-a-ray-in-raycaster-intersects-a-wall-along-the-ho/73777906#73777906
#
# GitHub - PyGameExamplesAndAnswers - Raycasting
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_raycasting.md

import pygame
import math

pygame.init()

tile_size, map_size = 50, 8
board = [
    '########',
    '#   #  #',
    '#   # ##',
    '#  ##  #',
    '#      #',
    '###  ###',
    '#      #',
    '########']

def cast_rays(sx, sy, angle):
    rx = math.cos(angle)
    ry = math.sin(angle)
    map_x = sx // tile_size
    map_y = sy // tile_size

    t_max_x = sx/tile_size - map_x
    if rx > 0:
        t_max_x = 1 - t_max_x
    t_max_y = sy/tile_size - map_y
    if ry > 0:
        t_max_y = 1 - t_max_y

    while True:
        if ry == 0 or t_max_x < t_max_y * abs(rx / ry):
            side = 'x'
            map_x += 1 if rx > 0 else -1
            t_max_x += 1
            if map_x < 0 or map_x >= map_size:
                break
        else:
            side = 'y'
            map_y += 1 if ry > 0 else -1
            t_max_y += 1
            if map_x < 0 or map_y >= map_size:
                break
        if board[int(map_y)][int(map_x)] == "#":
            break

    if side == 'x':
        x = (map_x + (1 if rx < 0 else 0)) * tile_size
        y = player_y + (x - player_x) * ry / rx
    else:
        y = (map_y + (1 if ry < 0 else 0)) * tile_size
        x = player_x + (y - player_y) * rx / ry
    return (x, y), math.hypot(x - sx, y - sy)    


window = pygame.display.set_mode((tile_size*map_size, tile_size*map_size))
clock = pygame.time.Clock()

board_surf = pygame.Surface((tile_size*map_size, tile_size*map_size))
for row in range(8):
    for col in range(8):
        color = (192, 192, 192) if board[row][col] == '#' else (96, 96, 96)
        pygame.draw.rect(board_surf, color, (col * tile_size, row * tile_size, tile_size - 2, tile_size - 2))

player_x, player_y = round(tile_size * 4.5) + 0.5, round(tile_size * 4.5) + 0.5
player_angle = 0
max_speed = 3

run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    
    keys = pygame.key.get_pressed()
    hit_pos_front, dist_front = cast_rays(player_x, player_y, player_angle)
    hit_pos_back, dist_back = cast_rays(player_x, player_y, player_angle + math.pi)
    player_angle += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 0.1
    speed = ((0 if dist_front <= max_speed else keys[pygame.K_UP]) - (0 if dist_back <= max_speed else keys[pygame.K_DOWN])) * max_speed
    player_x += math.cos(player_angle) * speed
    player_y += math.sin(player_angle) * speed
    hit_pos, dist = cast_rays(player_x, player_y, player_angle)

    window.blit(board_surf, (0, 0))
    pygame.draw.line(window, (0, 255, 0), (player_x, player_y), hit_pos)
    pygame.draw.circle(window, (255, 0, 0), (player_x, player_y), 8)
    pygame.display.flip()

pygame.quit()
exit()