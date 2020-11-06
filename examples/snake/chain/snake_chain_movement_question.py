# How do I chain the movement of a snake's body?
# https://stackoverflow.com/questions/62010434/how-do-i-chain-the-movement-of-a-snakes-body/62010435#62010435

import pygame
import random

pygame.init()
COLUMNS, ROWS, SIZE = 10, 10, 20
WIDTH, HEIGHT = COLUMNS, ROWS
screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE))
clock  = pygame.time.Clock()

def new_food(body):
    while True:
        pos = random.randrange(COLUMNS), random.randrange(ROWS)
        if pos not in body: 
            break     
    return pos

snake_x, snake_y = WIDTH//2, HEIGHT//2
body = []
move_x, move_y = (1, 0)
food_x, food_y = new_food(body)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: move_x, move_y = (-1, 0)
            elif event.key == pygame.K_RIGHT: move_x, move_y = (1, 0)
            elif event.key == pygame.K_UP: move_x, move_y = (0, -1)
            elif event.key == pygame.K_DOWN: move_x, move_y = (0, 1)
 
    snake_x = (snake_x + move_x) % WIDTH
    snake_y = (snake_y + move_y) % HEIGHT 
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = new_food(body)
        body.append((snake_x, snake_x))

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 255), (food_x*SIZE, food_y*SIZE, SIZE, SIZE))
    pygame.draw.rect(screen, (255, 0, 0), (snake_x*SIZE, snake_y*SIZE, SIZE, SIZE))
    for i, pos in enumerate(body):
        color = (0, 192, 0) if (i%2)!=0 else (255, 128, 0)
        pygame.draw.rect(screen, color, (pos[0]*SIZE, pos[1]*SIZE, SIZE, SIZE))
    pygame.display.flip()
    clock.tick(5)