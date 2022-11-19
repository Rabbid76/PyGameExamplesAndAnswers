# “Floating Blobs” experiment in pygame
# https://stackoverflow.com/questions/56817337/floating-blobs-experiment-in-pygame
#
# GitHub - PyGameExamplesAndAnswers - Random movement distribution
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
import random
import math

class Blob(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__() 
        self.color = color
        self.radius = radius
        self.create_image(x, y, color)
    
    def create_image(self, x, y, color):
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = (x, y))
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)

    def update(self, surface):
        for blob in blobs:
            if blob != self and pygame.sprite.collide_circle(self, blob):
                if self.radius > blob.radius:
                    a1 = self.radius * self.radius * math.pi / 4
                    a2 = blob.radius * blob.radius * math.pi / 4
                    self.radius = math.ceil(math.hypot(self.radius, blob.radius))
                    self.color = self.color.lerp(blob.color, a2 / (a1 + a2))
                    self.create_image(*self.rect.center, self.color)
                    blob.kill()

        speed = round(self.radius / 2)
        move = random.choice([(-speed, 0), (speed, 0), (0, -speed), (0, speed)])
        self.rect.move_ip(move)
        self.rect.clamp_ip(surface.get_rect())
                

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

blobs = pygame.sprite.Group()
for n in range(25):
    radius = random.randint(2, 8)
    x = random.randint(radius, window.get_width() - radius)
    y = random.randint(radius, window.get_height() - radius)
    color = pygame.Color(0)
    color.hsla = (random.randrange(360), 100, 50, 100)
    blobs.add(Blob(x, y, radius, color))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(blobs) > 1:
        blobs.update(window)

    window.fill((255, 255, 255))
    blobs.draw(window)
    pygame.display.flip()

pygame.quit()
exit()