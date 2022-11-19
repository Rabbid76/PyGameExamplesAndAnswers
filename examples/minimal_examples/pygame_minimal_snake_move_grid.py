# How do I chain the movement of a snake's body?
# https://stackoverflow.com/questions/62010434/how-do-i-chain-the-movement-of-a-snakes-body/62010435#62010435
# 
# GitHub - PyGameExamplesAndAnswers - Snake
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_snake.md
#
# https://replit.com/@Rabbid76/PyGame-SnakeMoveInGrid

import pygame
import random

pygame.init()
COLUMNS, ROWS, SIZE = 10, 10, 20
screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE))
clock  = pygame.time.Clock()

background = pygame.Surface((COLUMNS*SIZE, ROWS*SIZE))
background.fill((255, 255, 255))
for i in range(1, COLUMNS):
    pygame.draw.line(background, (128, 128, 128), (i*SIZE-1, 0), (i*SIZE-1, ROWS*SIZE), 2)
for i in range(1, ROWS):
    pygame.draw.line(background, (128, 128, 128), (0, i*SIZE-1), (COLUMNS*SIZE, i*SIZE-1), 2)

def random_pos(body):
    while True:
        pos = random.randrange(COLUMNS), random.randrange(ROWS)
        if pos not in body:
            break
    return pos

length = 1
body = [(COLUMNS//2, ROWS//2)]
dir = (1, 0)
food = random_pos(body)

run = True
while run:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: dir = (-1, 0)
            elif event.key == pygame.K_RIGHT: dir = (1, 0)
            elif event.key == pygame.K_UP: dir = (0, -1)
            elif event.key == pygame.K_DOWN: dir = (0, 1)

    body.insert(0, body[0][:])
    body[0] = (body[0][0] + dir[0]) % COLUMNS, (body[0][1] + dir[1]) % ROWS
    if body[0] == food:
        food = random_pos(body)
        length += 1
    while len(body) > length:
        del body[-1]

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (255, 0, 255), (food[0]*SIZE, food[1]*SIZE, SIZE, SIZE))
    for i, pos in enumerate(body):
        color = (255, 0, 0) if i==0 else (0, 192, 0) if (i%2)==0 else (255, 128, 0)
        pygame.draw.rect(screen, color, (pos[0]*SIZE, pos[1]*SIZE, SIZE, SIZE))
    pygame.display.flip()

pygame.quit()
exit()