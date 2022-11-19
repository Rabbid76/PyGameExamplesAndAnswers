# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Is it possible to implement gradual movement of an object to given coordinates in Pygame?
# https://stackoverflow.com/questions/60356812/is-it-possible-to-implement-gradual-movement-of-an-object-to-given-coordinates-i/60356995#60356995
#
# How to make a circle move diagonally from corner to corner in pygame
# https://stackoverflow.com/questions/65814020/how-to-make-a-circle-move-diagonally-from-corner-to-corner-in-pygame/65814431#65814431
# 
# How to move the object in squared path repeatedly?
# https://stackoverflow.com/questions/71340195/how-to-move-the-object-in-squared-path-repeatedly/71340468#71340468
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate - Move in grid
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

corner_points = [(100, 100), (300, 300), (300, 100), (100, 300)]
pos = corner_points[0]
speed = 2

def move(pos, speed, points):
    circle_dir = pygame.math.Vector2(points[0]) - pos
    if circle_dir.length() <= speed:
        pos = points[0]
        points.append(points[0])
        points.pop(0)
    else:
        circle_dir.scale_to_length(speed)
        new_pos = pygame.math.Vector2(pos) + circle_dir
        pos = (new_pos.x, new_pos.y) 
    return pos

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos = move(pos, speed, corner_points)
           
    window.fill(0)
    pygame.draw.lines(window, "gray", True, corner_points) 
    pygame.draw.circle(window, "red", pos, 20)
    pygame.display.update()
    clock.tick(100)

pygame.quit()
exit()