# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Sprite follow another flexible way within certain distance limits
# https://stackoverflow.com/questions/60064644/sprite-follow-another-flexible-way-within-certain-distance-limits

# How to make smooth movement in pygame
# https://stackoverflow.com/questions/64087982/how-to-make-smooth-movement-in-pygame/64088747?noredirect=1 
#
# GitHub - Move towards target - Follow target or mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_move_towards_target.md

import pygame

LERP_FACTOR      = 0.05
minimum_distance = 25
maximum_distance = 100

def FollowMe(pops, fpos):
    target_vector       = pygame.math.Vector2(*pops)
    follower_vector     = pygame.math.Vector2(*fpos)
    new_follower_vector = pygame.math.Vector2(*fpos)

    distance = follower_vector.distance_to(target_vector)
    if distance > minimum_distance:
        direction_vector    = (target_vector - follower_vector) / distance
        min_step            = max(0, distance - maximum_distance)
        max_step            = distance - minimum_distance
        step_distance       = min_step + (max_step - min_step) * LERP_FACTOR
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