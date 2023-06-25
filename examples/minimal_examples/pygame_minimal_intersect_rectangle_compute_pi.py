# pygame.Rect object
# https://www.pygame.org/docs/ref/rect.html
#
# Animation glitch when simulating the collision of two blocks for the calculation of PI
# https://stackoverflow.com/questions/56912016/animation-glitch-in-pygame
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Rectangle and rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame

# this function is calculating the new velocity of the block after collision,
# based on law of conservation of momentum and kinetic energy
def exchange_vel(v1, m1, v2, m2):
    return ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2

#power = int(input('enter: '))  # mass ratio
power = 4 # try 3 or 5

s1, s2 = 100, 50  # block sides
x1, y1 = 1000, 250  # bigger block coords
x2, y2 = 500, y1 + s1 - s2  # smaller block coords
z = 0

v1 = -0.5  # initial velocity of block 1
v2 = 0  # initial velocity of block 2
m1, m2 = 100 ** (power - 1), 1  # mass of blocks
no_of_collisions = 0  # counting number of collisions

pygame.init()
window = pygame.display.set_mode((1200, 500))
font = pygame.font.SysFont(None, 50)
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x1 += v1  # changing block coordinates according to velocity

    # changing velocity after collision
    if not x2 + s2 < x1 or x1 + s1 < x2:
        v1, v2 = exchange_vel(v1, m1, v2, m2), exchange_vel(v2, m2, v1, m1)
        no_of_collisions += 1

    # When the block hits the left wall, the speed is reversed
    x2 += v2
    if x2 <= 0:
        v2 *= -1
        no_of_collisions += 1

    t1 = x1 if x1 >= s2 else s2 
    t2 = x2 if x1 >= s2 else z % 2
    z += 1

    window.fill((127, 127, 127))
    window.blit(font.render('collisions ' + str(no_of_collisions), True, (0, 0, 0)), (10, 10))
    pygame.draw.rect(window, (0, 0, 255), (t2, y2, s2, s2))
    pygame.draw.rect(window, (192, 0, 0), (t1, y1, s1, s1))
    pygame.display.flip()

pygame.quit()