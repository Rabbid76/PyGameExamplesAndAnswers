# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Pygame: Image chasing the mouse cursor from certain length
# https://stackoverflow.com/questions/55168892/pygame-image-chasing-the-mouse-cursor-from-certain-length/55169273#55169273
#
# GitHub - Move towards target - Follow target or mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_move_towards_target.md
#
# https://replit.com/@Rabbid76/PyGame-FollowMouse

import pygame

step_size = 3

def FollowMe(pops, fpos):
    target_vector       = pygame.math.Vector2(*pops)
    follower_vector     = pygame.math.Vector2(*fpos)
    new_follower_vector = pygame.math.Vector2(*fpos)

    distance = follower_vector.distance_to(target_vector)
    if distance > 0:
        direction_vector    = (target_vector - follower_vector) / distance
        step_distance       = min(distance, step_size)
        new_follower_vector = follower_vector + direction_vector * step_distance

    return (new_follower_vector.x, new_follower_vector.y) 

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

follower = (100, 100)
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player   = pygame.mouse.get_pos()
    follower = FollowMe(player, follower)

    window.fill(0)  
    pygame.draw.circle(window, (0, 0, 255), player, 10)
    pygame.draw.circle(window, (255, 0, 0), (round(follower[0]), round(follower[1])), 10)
    pygame.display.flip()

pygame.quit()
exit()