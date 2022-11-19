# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# Two keypresses processed in each frame (pygame snake game)
# https://stackoverflow.com/questions/74249252/two-keypresses-processed-in-each-frame-pygame-snake-game/74326162#74326162
#
# GitHub - Keys and keyboard events
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_keys_and_keyboard_event.md 

import pygame
pygame.init()

COLUMNS, ROWS, TIESIZE = 20, 20, 20
window = pygame.display.set_mode((COLUMNS*TIESIZE, ROWS*TIESIZE))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

snake_x, snake_y = 9, 9
key_map = {pygame.K_a: 'L', pygame.K_d: 'R', pygame.K_w: 'U', pygame.K_s: 'D'}
direction_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
direction_queue = []
direction = 'R'

run = True
while run:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN:
            if event.key in key_map:
               direction_queue.append(key_map[event.key])

    text_surf = font.render(str(direction_queue), True, 'black')
    if direction_queue:
        direction = direction_queue[0]
        direction_queue.pop(0)
    snake_x = (snake_x + direction_map[direction][0]) % COLUMNS
    snake_y = (snake_y + direction_map[direction][1]) % ROWS

    window.fill("white")
    for c in range (1, COLUMNS):
        pygame.draw.line(window, "gray", (c*TIESIZE, 0), (c*TIESIZE, window.get_height()))
    for r in range (1, ROWS):
        pygame.draw.line(window, "gray", (0, r*TIESIZE), (window.get_width(), r*TIESIZE))
    rect = pygame.Rect(snake_x*TIESIZE, snake_y*TIESIZE, TIESIZE, TIESIZE)
    pygame.draw.rect(window, "red", rect)
    window.blit(text_surf, (10, 340))
    pygame.display.flip()
    
pygame.quit()
exit()