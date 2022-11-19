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
        direction = 'r' if x >= player_x else 'l'
    else:
        y = (map_y + (1 if ry < 0 else 0)) * tile_size
        x = player_x + (y - player_y) * rx / ry
        direction = 'd' if y >= player_y else 'u'
    return (x, y), math.hypot(x - sx, y - sy), direction   

def cast_fov(sx, sy, angle, fov, no_ofrays):
    max_d = math.tan(math.radians(fov/2))
    step = max_d * 2 / no_ofrays
    rays = []
    for i in range(no_ofrays):
        d = -max_d + (i + 0.5) * step
        ray_angle = math.atan2(d, 1)
        pos, dist, direction = cast_rays(sx, sy, angle + ray_angle)
        rays.append((pos, dist, dist * math.cos(ray_angle), direction))
    return rays

area_width = tile_size * map_size
window = pygame.display.set_mode((area_width*2, area_width))
clock = pygame.time.Clock()

board_surf = pygame.Surface((area_width, area_width))
for row in range(8):
    for col in range(8):
        color = (192, 192, 192) if board[row][col] == '#' else (96, 96, 96)
        pygame.draw.rect(board_surf, color, (col * tile_size, row * tile_size, tile_size - 2, tile_size - 2))

player_x, player_y = round(tile_size * 4.5) + 0.5, round(tile_size * 4.5) + 0.5
player_angle = 0
max_speed = 3
colors = {'r' : (196, 128, 64), 'l' : (128, 128, 64), 'd' : (128, 196, 64), 'u' : (64, 196, 64)}

run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    
    keys = pygame.key.get_pressed()
    hit_pos_front, dist_front, side_front = cast_rays(player_x, player_y, player_angle)
    hit_pos_back, dist_back, side_back = cast_rays(player_x, player_y, player_angle + math.pi)
    player_angle += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 0.1
    speed = ((0 if dist_front <= max_speed else keys[pygame.K_UP]) - (0 if dist_back <= max_speed else keys[pygame.K_DOWN])) * max_speed
    player_x += math.cos(player_angle) * speed
    player_y += math.sin(player_angle) * speed
    rays = cast_fov(player_x, player_y, player_angle, 60, 40)

    window.blit(board_surf, (0, 0))
    for ray in rays:
        pygame.draw.line(window, (0, 255, 0), (player_x, player_y), ray[0])
    pygame.draw.line(window, (255, 0, 0), (player_x, player_y), hit_pos_front)
    pygame.draw.circle(window, (255, 0, 0), (player_x, player_y), 8)

    pygame.draw.rect(window, (128, 128, 255), (400, 0, 400, 200))
    pygame.draw.rect(window, (128, 128, 128), (400, 200, 400, 200))
    for i, ray in enumerate(rays):
        height = round(10000 / ray[2])
        width = area_width // len(rays)
        color = pygame.Color((0, 0, 0)).lerp(colors[ray[3]], min(height/256, 1))
        rect = pygame.Rect(area_width + i*width, area_width//2-height//2, width, height)
        pygame.draw.rect(window, color, rect)
    pygame.display.flip()

pygame.quit()
exit()