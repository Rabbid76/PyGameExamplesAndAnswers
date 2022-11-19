# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# How to make the ball rotate in pygame, python?
# https://stackoverflow.com/questions/74214342/how-to-make-the-ball-rotate-in-pygame-python/74218983#74218983
#
# Pygame: Image chasing the mouse cursor from certain length
# https://stackoverflow.com/questions/55168892/pygame-image-chasing-the-mouse-cursor-from-certain-length
#
# GitHub - Move towards target - Follow target or mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_move_towards_target.md
#
# https://replit.com/@Rabbid76/PyGame-FollowInGrid

import pygame

pygame.init()

window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

w, h = window.get_size()
background_grid = pygame.Surface((w, h)) 
background_grid.fill((255, 255, 255))

grid_size = 20
rows, columns = w // grid_size, h // grid_size
for x in range(0, w, grid_size):
    pygame.draw.line(background_grid, (128, 128, 128), (x, 0), (x, h))
for y in range(0, h, grid_size):
    pygame.draw.line(background_grid, (128, 128, 128), (0, y), (w, y))    

object_pos = (rows // 2, columns // 2)
follower_pos = (0, 0)

count = 0
run = True
while run:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    object_pos = (
        (object_pos[0] + keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) % rows,
        (object_pos[1] + keys[pygame.K_DOWN] - keys[pygame.K_UP]) % columns)
    
    if count % 2 == 1:
        dx, dy = object_pos[0] - follower_pos[0], object_pos[1] - follower_pos[1]
        if abs(dx) >= abs(dy):
            follower_pos = (follower_pos[0] + (1 if dx > 0 else -1), follower_pos[1])
        else:
            follower_pos = (follower_pos[0], follower_pos[1] + (1 if dy > 0 else -1))
    count += 1

    window.blit(background_grid, (0, 0))
    pygame.draw.rect(window, (255, 0, 0), (follower_pos[0] * grid_size, follower_pos[1] * grid_size, grid_size, grid_size))
    pygame.draw.rect(window, (0, 32, 128), (object_pos[0] * grid_size, object_pos[1] * grid_size, grid_size, grid_size))
    pygame.display.flip()

pygame.quit()
exit()