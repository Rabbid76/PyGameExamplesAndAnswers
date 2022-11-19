
# How do I get the snake to grow and chain the movement of the snake's body?
# https://stackoverflow.com/questions/62010434/how-do-i-get-the-snake-to-grow-and-chain-the-movement-of-the-snakes-body

import pygame
import random
import math

pygame.init()
COLUMNS, ROWS, SIZE = 10, 10, 20
WIDTH, HEIGHT = COLUMNS*SIZE, ROWS*SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock  = pygame.time.Clock()

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((255, 255, 255))
for i in range(1, COLUMNS):
    pygame.draw.line(background, (128, 128, 128), (i*SIZE-1, 0), (i*SIZE-1, ROWS*SIZE), 2)
for i in range(1, ROWS):
    pygame.draw.line(background, (128, 128, 128), (0, i*SIZE-1), (COLUMNS*SIZE, i*SIZE-1), 2)

def create_body(track, no_pearls, distance):
    body = [(track[0])]
    track_i = 1
    for i in range(1, no_pearls):
        while track_i < len(track):
            pos = track[track_i]
            track_i += 1
            dx, dy = body[-1][0]-pos[0], body[-1][1]-pos[1]
            if math.sqrt(dx*dx + dy*dy) >= distance:
                body.append(pos)
                break
    while len(body) < no_pearls:
        body.append(track[-1])
    del track[track_i+50:]
    return body

length = 6
track = [(WIDTH//2, HEIGHT//2)]
dir = (1, 0)
move = True


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: dir = (-1, 0)
            elif event.key == pygame.K_RIGHT: dir = (1, 0)
            elif event.key == pygame.K_UP: dir = (0, -1)
            elif event.key == pygame.K_DOWN: dir = (0, 1)
            elif event.key == pygame.K_SPACE: move = not move

    if move:
        track.insert(0, track[0][:])    
        track[0] = (track[0][0] + dir[0]) % WIDTH, (track[0][1] + dir[1]) % HEIGHT

    body = create_body(track, length, 20)
        
    screen.blit(background, (0, 0))
    pygame.draw.lines(screen, (0, 0, 255), False, track, 3)
    cross = 3
    for i, pos in enumerate(body):
        color = (255, 128, 0) if i== 0 else (0, 128, 0)
        pygame.draw.circle(screen, color, pos, SIZE//2, 3)
        pygame.draw.line(screen, (255, 0, 0), (pos[0]-cross, pos[1]-cross), (pos[0]+cross, pos[1]+cross), 3)
        pygame.draw.line(screen, (255, 0, 0), (pos[0]-cross, pos[1]+cross), (pos[0]+cross, pos[1]-cross), 3)
    pygame.display.flip()