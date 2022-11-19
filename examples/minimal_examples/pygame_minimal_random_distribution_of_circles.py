# Random non overlapping circles(with circle number controlled) in python and pygame
# https://stackoverflow.com/questions/62079192/random-non-overlapping-circleswith-circle-number-controlled-in-python-and-pyga/62080074#62080074
#
# GitHub - PyGameExamplesAndAnswers - Random and random distribution - Random distribution
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_random_and_random_distribution.md

import random
import math
import pygame

def euclidean_distance(x1, y1, x2, y2):
    #return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return math.hypot((x1 - x2), (y1 - y2))

pygame.init()
window = pygame.display.set_mode((400, 400))
font50 = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

pygame.time.delay(10000)

run = True
circle_list = []
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    r = random.randint(10, 20)
    x = random.randint(10+r, window.get_width()- r-10)
    y = random.randint(10+r, window.get_height()-r-10)
    if not any((x2, y2, r2) for x2, y2, r2 in circle_list if euclidean_distance(x, y, x2, y2) < r + r2):
        circle_list.append((x, y, r))    

    window.fill((255, 255, 255))
    for x, y, r in circle_list:
        pygame.draw.circle(window, (0, 0, 0), (round(x), round(y)), int(r), 3)
    window.blit(font50.render(str(len(circle_list)), True, (255, 0, 0)), (10, 10))
    pygame.display.flip()
 
pygame.quit()
exit()