# Adding rects in list for displaying in 7-segment digits in pygame
# https://stackoverflow.com/questions/66533451/adding-rects-in-list-for-displaying-in-7-segment-digits-in-pygame/66533802#66533802  
#
# GitHub - PyGameExamplesAndAnswers - Miscellaneous - Collection
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_miscellaneous.md
#
# https://replit.com/@Rabbid76/PyGame-7SegementDisplay

import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

binaries = ([1,1,1,1,1,1,0],[1,1,0,0,0,0,0],[1,0,1,1,0,1,1],[1,1,1,0,0,1,1],
[1,1,0,0,1,0,1],[0,1,1,0,1,1,1],[0,1,1,1,1,0,1],[1,1,0,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1])
positions = ([60,10,10,50],[60,70,10,50],[10,120,50,10],[0,70,10,50],[0,10,10,50],[10,0,50,10],[10,60,50,10])

def draw_digit(surf, color, pos, i):
    for j, on in enumerate(binaries[i]):
        if on:
            pygame.draw.rect(surf, color, pygame.Rect(positions[j]).move(pos))

run = True
count = 0  
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(0)
    draw_digit(screen, "green", (65, 85), count // 10)
    draw_digit(screen, "green", (165, 85), count % 10)
    count += 1
    if count >= 100:
        count = 0
    pygame.display.update()