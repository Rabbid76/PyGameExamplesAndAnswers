# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Detecting collisions between polygons and rectangles in Pygame
# https://stackoverflow.com/questions/64095396/detecting-collisions-between-polygons-and-rectangles-in-pygame/64106246#64106246
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Rectangle and polygon
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-CollisionPolygonRectangle

import pygame

def collideLineLine(P0, P1, Q0, Q1):
    d = (P1[0]-P0[0]) * (Q1[1]-Q0[1]) + (P1[1]-P0[1]) * (Q0[0]-Q1[0]) 
    if d == 0:
        return None
    t = ((Q0[0]-P0[0]) * (Q1[1]-Q0[1]) + (Q0[1]-P0[1]) * (Q0[0]-Q1[0])) / d
    u = ((Q0[0]-P0[0]) * (P1[1]-P0[1]) + (Q0[1]-P0[1]) * (P0[0]-P1[0])) / d
    return 0 <= t <= 1 and 0 <= u <= 1

def colideRectLine(rect, p1, p2):
    return (collideLineLine(p1, p2, rect.topleft, rect.bottomleft) or
            collideLineLine(p1, p2, rect.bottomleft, rect.bottomright) or
            collideLineLine(p1, p2, rect.bottomright, rect.topright) or
            collideLineLine(p1, p2, rect.topright, rect.topleft))

def collideRectPolygon(rect, polygon):
    for i in range(len(polygon)-1):
        if colideRectLine(rect, polygon[i], polygon[i+1]):
            return True
    return False

class Player:
    def __init__(self, x, y, color, size = 20, speed = 5):
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x, y, size, size).move(-size//2, -size//2)
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

def create_polygon(x, y, d):
    return [
        (x - d//2, y - d), (x + d//2, y - d),
        (x + d, y - d//2), (x + d, y + d//2),
        (x + d//2, y + d), (x - d//2, y + d),
        (x - d, y + d//2), (x - d, y - d//2),
        (x - d//2, y - d)]

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

player = Player(*window.get_rect().center, (255, 255, 0))
polygon = create_polygon(*window.get_rect().center, min(window.get_size()) // 3)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    new_rect = player.rect.copy()
    new_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player.speed
    new_rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player.speed
    if not collideRectPolygon(new_rect, polygon):
        player.rect = new_rect.copy()   

    window.fill(0)
    pygame.draw.polygon(window, (255, 0, 0), polygon, 1)
    player.draw()
    pygame.display.flip()

pygame.quit()
exit()