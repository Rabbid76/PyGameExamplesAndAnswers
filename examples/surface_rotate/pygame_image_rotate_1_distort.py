# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# How do I rotate an image around its center using PyGame?
# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
#
# How to rotate an image around its center while its scale is getting larger(in Pygame)
# https://stackoverflow.com/questions/54462645/how-to-rotate-an-image-around-its-center-while-its-scale-is-getting-largerin-py/54713639#54713639
#
# GitHub - PyGameExamplesAndAnswers - Rotate surface - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))
pygame.init()

screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
try:
    image = pygame.image.load('icon/AirPlaneFront1-128.png')
except:
    text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
    image = pygame.Surface((text.get_width()+1, text.get_height()+1))
    pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
    image.blit(text, (1, 1))

angle = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            angle = 1

    pos = (screen.get_width()/2, screen.get_height()/2)
    pos = (0, 0)
    image = pygame.transform.rotate(image, angle)

    screen.fill(0)
    screen.blit(image, pos)
    pygame.draw.rect (screen,(255, 0, 0), (*pos, *image.get_size()),2)
    pygame.display.flip()
    
pygame.quit()
exit()