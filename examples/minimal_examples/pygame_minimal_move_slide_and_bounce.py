# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Collision detection / physics for simple game
# https://stackoverflow.com/questions/59656983/collision-detection-physics-for-simple-game/59658289#59658289
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Slide
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import pygame
import math

pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

centerX, centerY = window.get_rect().center
stageR =  min(window.get_size()) // 2 - 20
xR = stageR // 10
x1, y1 = centerX - stageR * 8 // 10, centerY
x1_dir, y1_dir = 0, 0
x2, y2 = centerX + stageR * 8 // 10, centerY
x2_dir, y2_dir = 0, 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    x1_dir += (keys[pygame.K_d] - keys[pygame.K_a]) * 0.1
    if keys[pygame.K_d] == keys[pygame.K_a]:
        x1_dir *= 0.98
    y1_dir += (keys[pygame.K_s] - keys[pygame.K_w]) * 0.1
    if keys[pygame.K_s] == keys[pygame.K_w]:
        y1_dir *= 0.98
    x2_dir += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 0.1
    if keys[pygame.K_RIGHT] == keys[pygame.K_LEFT]:
        x2_dir *= 0.98
    y2_dir += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 0.1
    if keys[pygame.K_DOWN] == keys[pygame.K_UP]:
        y2_dir *= 0.98

    v12 = pygame.math.Vector2(x1-x2, y1-y2)
    distance = v12.length()
    hit_dist = 2*xR
    if distance <= hit_dist:
        # vector beteween center points
        nv = v12.normalize()
        # movement direction and combined relative movement
        d1 = pygame.math.Vector2(x1_dir, y1_dir)
        d2 = pygame.math.Vector2(x2_dir, y2_dir)
        dd = d1 - d2
        # normalized movement and normal distances
        if dd.length() > 0:
            ddn = dd.normalize()
            dir_dist  = ddn.dot(v12)
            norm_dist = pygame.math.Vector2(-ddn[0], ddn[1]).dot(v12)
            # minimum distance along the line of relative movement
            min_dist = math.sqrt(hit_dist*hit_dist - norm_dist*norm_dist)
            if dir_dist < min_dist:
                # update postions of the players so that the distance is 2*xR
                d1l, d2l = d1.length(), d2.length()
                d1n = d1/d1l if d1l > 0 else d1
                d2n = d2/d2l if d2l > 0 else d2
                x1 -= d1n.x * d1l / (d1l+d2l)
                y1 -= d1n.y * d1l / (d1l+d2l)
                x2 -= d2n.x * d2l / (d1l+d2l)
                y2 -= d2n.y * d2l / (d1l+d2l)
                # recalculate vector beteween center points
                v12 = pygame.math.Vector2(x1-x2, y1-y2)
                nv = v12.normalize()

            # reflect movement vectors
            rd1 = d1.reflect(nv)
            rd2 = d2.reflect(nv)
            len1, len2 = rd1.length(), rd2.length()
            if len1 > 0:
                rd1 = rd1 * len2 / len1
                x1_dir, y1_dir = rd1.x, rd1.y
            else:
                x1_dir, y1_dir = -x2_dir, -y2_dir
            if len2 > 0:
                rd2 = rd2 * len1 / len2
                x2_dir, y2_dir = rd2.x, rd2.y
            else:
                x2_dir, y2_dir = -x1_dir, -y1_dir
        
        print ("HIT")

    x1 += x1_dir
    y1 += y1_dir
    x2 += x2_dir
    y2 += y2_dir

    window.fill(0)
    pygame.draw.circle(window, (127, 191, 255), (centerX,centerY), stageR)
    pygame.draw.circle(window, (192, 0, 0), (round(x1), round(y1)), xR)
    pygame.draw.circle(window, (0, 127, 0), (round(x2),round(y2)), xR)
    pygame.display.flip()

pygame.quit()
exit()