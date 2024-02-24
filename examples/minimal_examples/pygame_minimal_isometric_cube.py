# Get isometric tile mouse selection in Pygame
# https://stackoverflow.com/questions/71336864/get-isometric-tile-mouse-selection-python/73996398#73996398
# 
# How to create a rhomboid in pygame
# https://stackoverflow.com/questions/73651474/how-to-create-a-rhomboid-in-pygame/73652102#73652102
#
# GitHub - PyGameExamplesAndAnswers - Isometric cube
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_isometric.md

import pygame, math

def drawCube(surf, center, size, angle):
    v = pygame.math.Vector2(1, 0)
    v.rotate_ip(angle + 45)
    lx = round(v.x * size * math.sqrt(2) / 2)
    ly = round(v.y * size * math.sqrt(2) / 2)
    x, y = center
    s = size/2
    f1 = [(x+lx, y-s+ly//2), (x-ly, y-s+lx//2), (x-lx, y-s-ly//2), (x+ly, y-s-lx//2)]
    pts = [(lx, ly//2), (-ly, lx//2), (-lx, -ly//2), (ly, -lx//2)]
    faces = []
    for i in range(4):
        p0, p1 = pts[i], pts[(i+1) % 4]
        f = [(p0[0]+x, p0[1]+y-s), (p1[0]+x, p1[1]+y-s), (p1[0]+x, p1[1]+y+s), (p0[0]+x, p0[1]+y+s)]
        faces.append(f)
    colors = ["red", "yellow", "green", "blue"]
    for face, color in zip(faces, colors):
        if (face[0][1] + face[1][1]) / 2 > y-s:
            pygame.draw.polygon(surf, color, face, 3)
    pygame.draw.polygon(surf, "white", f1, 3)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

angle = 0
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window_center = window.get_rect().center

    window.fill('black')
    drawCube(window, window_center, 150, angle)
    pygame.display.flip()

    angle += 1

pygame.quit()
exit()