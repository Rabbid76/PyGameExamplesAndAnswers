# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Pygame how to let balls collide
# https://stackoverflow.com/questions/63145493/pygame-how-to-let-balls-collide/63187016#63187016
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-CirclesBounceOff

import pygame

pygame.init()

width, height = 400, 400
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

x1, y1, r1, mx1, my1 = 200, 200, 50, 2, 0.5
x2, y2, r2, mx2, my2 = 300, 200, 50, -1, -1.5

def move(c, v, r, m):
    c += v
    if c < r: c, v = r, -v
    if c > m-r: c, v = m-r, -v   
    return c, v

hit_count = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x1, mx1 = move(x1, mx1, r1, width)
    y1, my1 = move(y1, my1, r1, height)
    x2, mx2 = move(x2, mx2, r2, width)
    y2, my2 = move(y2, my2, r2, height)

    v1 = pygame.math.Vector2(x1, y1)
    v2 = pygame.math.Vector2(x2, y2)
    if v1.distance_to(v2) < r1 + r2 - 2:
        hit_count += 1
        print("hit:", hit_count)

        nv = v2 - v1
        m1 = pygame.math.Vector2(mx1, my1).reflect(nv)
        m2 = pygame.math.Vector2(mx2, my2).reflect(nv)
        mx1, my1 = m1.x, m1.y
        mx2, my2 = m2.x, m2.y

    window.fill((127, 127, 127))
    pygame.draw.circle(window, (255, 0, 0), (round(x1), round(y1)), r1, 4)
    pygame.draw.circle(window, (0, 0, 255), (round(x2), round(y2)), r2, 4)
    pygame.display.flip()

pygame.quit()
exit()