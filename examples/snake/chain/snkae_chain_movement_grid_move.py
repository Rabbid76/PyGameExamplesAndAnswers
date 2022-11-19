# How do I get the snake to grow and chain the movement of the snake's body?
# https://stackoverflow.com/questions/62010434/how-do-i-get-the-snake-to-grow-and-chain-the-movement-of-the-snakes-body

import pygame
import random

pygame.init()
COLUMNS, ROWS, SIZE = 10, 10, 20
screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE))
clock  = pygame.time.Clock()
font = pygame.font.SysFont(None, 18)

background = pygame.Surface((COLUMNS*SIZE, ROWS*SIZE))
background.fill((255, 255, 255))
for i in range(2, COLUMNS-1):
    pygame.draw.line(background, (128, 128, 128), (i*SIZE-1, SIZE), (i*SIZE-1, (ROWS-1)*SIZE), 2)
for i in range(2, ROWS-1):
    pygame.draw.line(background, (128, 128, 128), (SIZE, i*SIZE-1), ((COLUMNS-1)*SIZE, i*SIZE-1), 2)
for i in range(COLUMNS-2):
    label = font.render(str(i), True, (0, 0, 0), (255, 255, 255))
    background.blit(label, (i*SIZE + 26, 5))
    background.blit(label, (6, i*SIZE + 25))

length = 1
body = [(3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]

run = True
while run:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for i in reversed(range(len(body))):
        pos = body[i]
        color = (255, 128, 0) if i== 0 else (128, 128, 128) if i == len(body)-1 else (0, 128, 0)
        pygame.draw.rect(screen, color, ((pos[0]+1)*SIZE, (pos[1]+1)*SIZE, SIZE, SIZE), 6)

    pn = ((body[0][0]+1)*SIZE + SIZE//2), ((body[0][1]+1)*SIZE + SIZE//2)
    ph = ((body[1][0]+1)*SIZE + SIZE//2), ((body[1][1]+1)*SIZE + SIZE//2)
    pt = ((body[-1][0]+1)*SIZE + SIZE//2), ((body[-1][1]+1)*SIZE + SIZE//2)

    pygame.draw.line(screen, (255, 0, 0), (pt[0]-SIZE, pt[1]-SIZE), (pt[0]+SIZE, pt[1]+SIZE), 3)
    pygame.draw.line(screen, (255, 0, 0), (pt[0]-SIZE, pt[1]+SIZE), (pt[0]+SIZE, pt[1]-SIZE), 3)

    pygame.draw.circle(screen, (255, 0, 0), ph, 5)
    pygame.draw.line(screen, (255, 0, 0), pn, ph, 3)
    pygame.draw.polygon(screen, (255, 0, 0), [(pn[0]-5, pn[1]+3), (pn[0]+5, pn[1]+3), (pn[0], pn[1]-7)])

    pygame.display.flip()