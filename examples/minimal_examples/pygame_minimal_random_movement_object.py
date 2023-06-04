# Population Simulation in Python
# https://stackoverflow.com/questions/75501098/population-simulation-in-python/75501705#75501705
#
# GitHub - PyGameExamplesAndAnswers - Random movement distribution
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
import random

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

class Shape(): 
    def __init__(self, x, y): 
        self.color = 'white'
        self.move_length = 0
        self.direction = [0, 0]
        self.radius = 25
        self.rect = pygame.Rect(0, 0, self.radius*2, self.radius*2) 
        self.rect.center = (x, y)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def move(self, screen):
        if self.move_length == 0:
            self.move_length = random.randrange(10, 100)
            self.direction = [[0, -1], [0, 1], [-1, 0], [1, 0]][random.randrange(0, 4)]
        self.move_length -= 1
        
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]
        if self.rect.x - self.radius <= 0:
            self.direction[0] *= -1
            self.rect.x = self.radius
        if self.rect.x + self.radius > screen.get_width():
            self.direction[0] *= -1
            self.rect.x = screen.get_width() - self.radius
        if self.rect.y - self.radius <= 0:
            self.direction[1] *= -1
            self.rect.y = self.radius
        if self.rect.y + self.radius > screen.get_height():
            self.direction[1] *= -1
            self.rect.y = screen.get_height() - self.radius
 
sheep = Shape(200, 200)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    sheep.move(window)

    window.fill(0)
    sheep.draw(window)
    pygame.display.flip()

pygame.quit()
exit()