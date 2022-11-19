# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# How can I test if a point is in an ellipse?
# https://stackoverflow.com/questions/59971407/how-can-i-test-if-a-point-is-in-an-ellipse/65601453#65601453
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Point and Ellipse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame

pygame.init()

width, height = 400, 400
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

ellipse_rect = pygame.Rect(0, 0, 200, 100)
ellipse_rect.center = window.get_rect().center

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    a = ellipse_rect.width // 2
    b = ellipse_rect.height // 2
    scale_y = a / b
    cpt_x, cpt_y = ellipse_rect.center
    test_x, test_y = pygame.mouse.get_pos()
    dx = test_x - cpt_x
    dy = (test_y - cpt_y) * scale_y
    collide = dx*dx + dy*dy <= a*a  
            
    window.fill(0)
    
    color = (127, 0, 0) if collide else (0, 127, 0)
    pygame.draw.ellipse(window, color, ellipse_rect)
    if collide:
        pygame.draw.ellipse(window, (255, 255, 255), ellipse_rect, 3)

    pygame.display.flip()

pygame.quit()
exit()