# How do I chain the movement of a snake's body?
# https://stackoverflow.com/questions/62010434/how-do-i-chain-the-movement-of-a-snakes-body/62010435#62010435
# 
# GitHub - PyGameExamplesAndAnswers - Snake
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_snake.md
#
# https://replit.com/@Rabbid76/PyGame-SnakeMoveFree

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

def hit(pos_a, pos_b, distance):
    dx, dy = pos_a[0]-pos_b[0], pos_a[1]-pos_b[1]
    return math.sqrt(dx*dx + dy*dy) < distance

def random_pos(body):
    pos = None
    while True:
        pos = random.randint(SIZE//2, WIDTH-SIZE//2), random.randint(SIZE//2, HEIGHT-SIZE//2)
        if not any([hit(pos, bpos, 20) for bpos in body]):
            break
    return pos

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
    del track[track_i:]
    return body

length = 1
track = [(WIDTH//2, HEIGHT//2)]
dir = (1, 0)
food = random_pos(track)

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

    track.insert(0, track[0][:])
    track[0] = (track[0][0] + dir[0]) % WIDTH, (track[0][1] + dir[1]) % HEIGHT

    body = create_body(track, length, 20)

    if hit(body[0], food, 20):
        food = random_pos(body)
        length += 1

    screen.blit(background, (0, 0))
    pygame.draw.circle(screen, (255, 0, 255), food, SIZE//2)
    for i, pos in enumerate(body):
        color = (255, 0, 0) if i==0 else (0, 192, 0) if (i%2)==0 else (255, 128, 0)
        pygame.draw.circle(screen, color, pos, SIZE//2)
    pygame.display.flip()

pygame.quit()
exit()