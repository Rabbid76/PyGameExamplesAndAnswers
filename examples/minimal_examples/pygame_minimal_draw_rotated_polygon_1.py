# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# how to make rotate polygon on key in pygame?
# https://stackoverflow.com/questions/75116101/how-to-make-rotate-polygon-on-key-in-pygame/75116556#75116556 
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame

def rotate_points_around_pivot(points, pivot, angle):
    pp = pygame.math.Vector2(pivot)
    rotated_points = [
        (pygame.math.Vector2(x, y) - pp).rotate(angle) + pp for x, y in points]
    return rotated_points

def draw_rotated_polygon(surface, color, points, angle, pivot=None):
    if pivot == None:
        lx, ly = zip(*points)
        min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
        bounding_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        pivot = bounding_rect.center
    rotated_points = rotate_points_around_pivot(points, pivot, angle)
    pygame.draw.polygon(surface, color, rotated_points)

pygame.init()
window = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()
pivot = (125, 125)
size = 90
points = [(0, -1), (-0.8660, 0.5), (0.8660, 0.5)]
points = [(pivot[0] + x * size, pivot[1] + y * size) for x, y in points]
angle = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #key = pygame.key.get_pressed()
    #if key[pygame.K_r]:
    angle += 1

    window.fill("black")
    #pygame.draw.circle(window, "yellow", (125, 125), size, 1)
    draw_rotated_polygon(window, "white", points, angle, pivot)
    pygame.display.flip()

pygame.quit()
exit()