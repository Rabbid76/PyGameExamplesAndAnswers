# Pymunk
# http://www.pymunk.org/en/latest/
#  
# Get the updated coordinates of a pymunk rotating kinetic body
# https://stackoverflow.com/questions/64521750/get-the-updated-coordinates-of-a-pymunk-rotating-kinetic-body/64521960#64521960
# 
# GitHub - PyGameExamplesAndAnswers - PyGame and PyMuk
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_and_pymuk.md


import pymunk
import pymunk.pygame_util
import pygame
import math

width_mass=50
height_mass=50
pygame.init()

window = pygame.display.set_mode((800, 600))
draw_options = pymunk.pygame_util.DrawOptions(window)
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, -65)

pts = [(-27, -238.5), (27,-238.5), (27,238.5), (-27,238.5)]
body_type = pymunk.Body(body_type = pymunk.Body.KINEMATIC)  
body_type.position = window.get_rect().center
space.add(body_type)
for i in range(4):
    segment = pymunk.Segment(body_type, pts[i], pts[(i+1)%4], 2)
    segment.elasticity = 0
    segment.friction=0
    space.add(segment)

body_type.angular_velocity=0.5

body = pymunk.Body(mass=1, moment=100)
body.position = body_type.position[0], body_type.position[1] + 136.5

mass = pymunk.Poly.create_box(body, (width_mass, height_mass))
mass.elasticity = 0
space.add(body, mass)

running = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    abs_pos = body_type.position
    rel_pos = (0, 238.5)
    rel_dist, rel_angle = math.hypot(*rel_pos), math.atan2(rel_pos[1], rel_pos[0])
    angle = rel_angle + body_type.angle
    pos = abs_pos[0] + rel_dist * math.cos(angle), abs_pos[1] + rel_dist * math.sin(angle)

    window.fill((224, 224, 224))
    space.debug_draw(draw_options)
    for body in space.bodies:
        pygame.draw.circle(window, (255, 0, 0), (body.position[0], window.get_height() - body.position[1]), 7)    
    pygame.draw.circle(window, (255, 255, 0), (pos[0], window.get_height() - pos[1]), 7)
    pygame.display.update()
    space.step(0.01)