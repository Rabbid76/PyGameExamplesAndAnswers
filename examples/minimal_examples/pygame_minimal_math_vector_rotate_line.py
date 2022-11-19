# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Python center axis rotation segment
# https://stackoverflow.com/questions/64446045/python-pygame-center-axis-rotation-segment-line/64446683#64446683
#
# GitHub - PyGameExamplesAndAnswers - Vector - Reflection
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_math_vector_and_reflection.md
#
# https://replit.com/@Rabbid76/PyGame-VectorRotateLine

import pygame
pygame.init()

window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

line_vector = pygame.math.Vector2(1, 0)
radius, angle = 100, 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    center_x, center_y = window.get_rect().center    
    rot_vector = line_vector.rotate(angle) * radius
    angle -= 1
    start = round(center_x + rot_vector.x), round(center_y + rot_vector.y)
    end = round(center_x - rot_vector.x), round(center_y - rot_vector.y)
    
    window.fill(0)
    pygame.draw.line(window, (255, 255, 255), start, end, 3)
    pygame.display.flip()

pygame.quit()
exit()