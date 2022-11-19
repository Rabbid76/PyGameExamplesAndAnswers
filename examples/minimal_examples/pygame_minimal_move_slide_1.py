
# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# How to fix character constantly accelerating in both directions after deceleration Pygame?
# https://stackoverflow.com/questions/59832445/how-to-fix-character-constantly-accelerating-in-both-directions-after-decelerati/59846286#59846286  
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Slide
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import pygame

pygame.init()

window = pygame.display.set_mode((500, 140))
clock = pygame.time.Clock()

border = pygame.Rect(0, 0, window.get_width()-40, 100)
border.center = window.get_rect().center
player_xy = list(window.get_rect().center)
radius = 10
PLAYER_ACCEL, PLAYER_FRICT = 0.5, 0.02
veloc = 0

run = True
while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    accel = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_ACCEL
    
    # change velocity by acceleration and reduce dependent on friction
    veloc = (veloc + accel) * (1 - PLAYER_FRICT)

    # change position of player by velocity
    player_xy[0] += veloc

    if player_xy[0] < border.left + radius:
        player_xy[0] = border.left + radius
        veloc = 0
    if player_xy[0] > border.right - radius:
        player_xy[0] = border.right - radius
        veloc = 0

    window.fill(0) 
    pygame.draw.rect(window, (255, 0, 0), border, 1)
    pygame.draw.circle(window, (0, 255, 0), (round(player_xy[0]), round(player_xy[1])), radius)
    pygame.display.flip()

pygame.quit()
exit()