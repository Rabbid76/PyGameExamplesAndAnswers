# How to correctly update the grid in falling sand simulation?
# https://stackoverflow.com/questions/71257560/how-to-correctly-update-the-grid-in-falling-sand-simulation/71257698#71257698
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Gravity
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame, random

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

fire_ball_event = pygame.USEREVENT
pygame.time.set_timer(fire_ball_event, 200)

fireball = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(fireball, "yellow", (10, 10), 10)
pygame.draw.circle(fireball, "orange", (10, 13), 7)
pygame.draw.circle(fireball, "red", (10, 16), 4)
fireballs = []

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == fire_ball_event:
            x = random.randrange(10, window.get_width()-10)
            fireballs.append(pygame.Rect(x, -20, 20, 20))

    for fireballrect in fireballs[:]:
        fireballrect.y += 1
        if fireballrect.top > window.get_height():
            fireballs.remove(fireballrect)

    window.fill(0)
    for fireballrect in fireballs:
        window.blit(fireball, fireballrect)
    pygame.display.flip()

pygame.quit()
exit()