# pygame.Rect object
# https://www.pygame.org/docs/ref/rect.html#pygame.Rect
#
# Maximising Collidable area for a hexagonal "Button" in pygame
# https://stackoverflow.com/questions/76399452/maximising-collidable-area-for-a-hexagonal-button-in-pygame/76399557#76399557
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Point and hexagon
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame, math

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()


len = 100
sin_len = math.sin(math.radians(60)) * len
cos_len = math.cos(math.radians(60)) * len
pts = [
    (len, 0), (len-cos_len, sin_len), (cos_len-len, sin_len),
    (-len, 0), (cos_len-len, -sin_len), (len-cos_len, -sin_len)]
pts = [(x + 200, y + 200) for x, y in pts]

tile_heihgt = sin_len * 2
tile_width = len * 2
tiel_rect = pygame.Rect(0, 0, tile_width, tile_heihgt)
tiel_rect.center = (200, 200)

def collideHexagon(bounding_rect, position):
    px, py = position
    if bounding_rect.collidepoint((px, py)):
        dx = min(px - bounding_rect.left, bounding_rect.right - px)
        dy = abs(py - bounding_rect.centery)
        if dy < dx * math.tan(math.radians(60)):
            return True
    return False

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    color = "white"
    if collideHexagon(tiel_rect, pygame.mouse.get_pos()):
        color = "red"
 
    window.fill(0)
    pygame.draw.polygon(window, color, pts)         
    pygame.display.flip() 

pygame.quit()
exit()
