# Sometimes the ball doesn't bounce off the paddle in pong game
# https://stackoverflow.com/questions/62864205/sometimes-the-ball-doesnt-bounce-off-the-paddle-in-pong-game

import pygame

pygame.init()
width, height = 400, 600
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

start_pos = (180, 160)
pos_list = []
step = 20
pos_list.append((start_pos[0]-step*2, start_pos[1]-step*2))
pos_list.append((start_pos[0]-step, start_pos[1]-step))
pos_list.append((start_pos[0], start_pos[1]))
pos_list.append((start_pos[0]+step, start_pos[1]+step))
pos_list.append((160, pos_list[-1][1]))
for i in range(3):
    lx, ly = pos_list[-1]
    pos_list.append((lx-step, ly+step))

current_i = 0
run = True
while run:
    clock.tick(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False


    window.fill((255, 255, 255))

    for pos in pos_list:
        pygame.draw.circle(window, (196, 196, 196), pos, 40, 1)

    pygame.draw.rect(window, (0, 0, 0), (200, 200, 40, 160), 3)

    pygame.draw.circle(window, (0, 0, 0), pos_list[current_i], 40, 3)
    if current_i > 0:
        pygame.draw.lines(window, (0, 196, 0), False, pos_list[:min(3, current_i+1)], 3)
    if current_i > 2:
        pygame.draw.lines(window, (228, 0, 0), False, pos_list[2:min(4, current_i+1)], 3)
    if current_i > 3:
        pygame.draw.lines(window, (0, 196, 0), False, pos_list[3:current_i+1], 3)
    current_i += 1
    if current_i >= len(pos_list):
        current_i = 0

    pygame.display.flip()