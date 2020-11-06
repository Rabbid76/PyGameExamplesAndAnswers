# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# How to make ball bounce off triangle in pygame?
# https://stackoverflow.com/questions/54256104/how-to-make-ball-bounce-off-triangle-in-pygame
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and polygon
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((500, 300))

try:
    ball = pygame.image.load("icon/Ball64.png")
except:
    ball = pygame.Surface((64, 64), pygame.SRCALPHA)
    pygame.draw.circle(ball, (255, 255, 0), (32, 32), 32)
ballvec = pygame.math.Vector2(1.5, 1.5)
ballpos = pygame.math.Vector2(150, 250)
balldiameter = ball.get_width()

def reflect_circle_on_line(lp0, lp1, pt, dir, radius):
    l_dir = (lp1 - lp0).normalize()                 # direction vector of the line
    nv = pygame.math.Vector2(-l_dir[1], l_dir[0])   # normal vector to the line
    d = (lp0-pt).dot(nv)                            # distance to line
    ptX = pt + nv * d                               # intersection point on endless line
    if (abs(d) > radius or dir.dot(ptX-pt) <= 0 or  # test if the ball hits the line   
        (ptX-lp0).dot(l_dir) < 0 or (ptX-lp1).dot(l_dir) > 0):
        return dir 
    r_dir = dir.reflect(nv)                         # reflect the direction vector on the line (like a billiard ball)                       
    return r_dir
      
triangle1 = [(250, 220), (400, 300), (100, 300)]
triangle2 = [(250, 80), (400, 0), (100, 0)]
screen_rect = [(0, 0), (0, window.get_height()), window.get_size(), (window.get_width(), 0)]

line_list = []
for p0, p1 in zip(triangle1, triangle1[1:] + triangle1[:1]):
    line_list.append((pygame.math.Vector2(p0), pygame.math.Vector2(p1)))
for p0, p1 in zip(triangle2, triangle2[1:] + triangle2[:1]):
    line_list.append((pygame.math.Vector2(p0), pygame.math.Vector2(p1)))
for p0, p1 in zip(screen_rect, screen_rect[1:] + screen_rect[:1]):
    line_list.append((pygame.math.Vector2(p0), pygame.math.Vector2(p1)))

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for line in line_list:
        ballvec = reflect_circle_on_line(*line, ballpos, ballvec, balldiameter/2)
    ballpos = ballpos + ballvec
    
    window.fill((64, 64, 64))
    pygame.draw.polygon(window, (255, 0, 0), triangle1, 0)
    pygame.draw.polygon(window, (0, 0, 255), triangle2, 0)
    window.blit(ball, (round(ballpos[0]-balldiameter/2), round(ballpos[1]-balldiameter/2)))
    pygame.display.flip()

pygame.quit()
exit()