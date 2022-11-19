# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Create trails of paticles for the bullets
# https://stackoverflow.com/questions/72643317/create-trails-of-paticles-for-the-bullets/72644068#72644068
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Particles
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

import pygame, random

pygame.init()
window = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("icon/Rocket64.png")
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect(center = (x, y))
        self.particles = []

    def move(self):
        for particle in self.particles:
            particle[0][0] -= 2
            particle[0][1] += particle[1]
        particle = [list(self.rect.midleft), random.uniform(-2, 2), pygame.Color(255, random.randrange(255), 0)]
        self.particles.append(particle)
        if len(self.particles) > 30:
            self.particles.pop(0)
        self.rect.centerx += 3

    def draw(self, screen):
        for i, particle in enumerate(self.particles):
            pygame.draw.circle(screen, particle[2], particle[0], (i//3+2))
        screen.blit(self.image, self.rect)
        

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (32, 32, 32), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles] 

bullet = Bullet(0, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
    bullet.move()
    if bullet.rect.left >= 400:
        bullet.rect.right = 0

    window.blit(background, (0, 0))
    bullet.draw(window)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()