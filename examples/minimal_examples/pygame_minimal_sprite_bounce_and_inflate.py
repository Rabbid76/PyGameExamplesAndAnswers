# I can't get the object to bounce off the walls normally due to its resizing in pygam
# https://stackoverflow.com/questions/77770306/i-cant-get-the-object-to-bounce-off-the-walls-normally-due-to-its-resizing-in-p/77770428#77770428
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Collide with frame, window border and restrict to rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
import random

class Ball(pygame.sprite.Sprite):

    def __init__(self, startpos, velocity, startdir):
        super().__init__()
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        self.original_image = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, (0, 255, 0), (50, 50), 50)
        self.radius = 5
        self.image = pygame.transform.scale(self.original_image, (self.radius * 2, self.radius * 2))
        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))

    def reflect(self, NV, border_rect):
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))
        self.radius = min(50, self.radius + 1)
        self.image = pygame.transform.scale(self.original_image, (self.radius * 2, self.radius * 2))
        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))
        self.rect.clamp_ip(border_rect)
        self.pos = self.rect.center

    def update(self, border_rect):
        self.pos += self.dir * self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)
        if self.rect.left < border_rect.left:
            self.reflect((1, 0), border_rect)
        if self.rect.right > border_rect.right:
            self.reflect((-1, 0), border_rect)
        if self.rect.top < border_rect.top:
            self.reflect((0, 1), border_rect)
        if self.rect.bottom > border_rect.bottom:
            self.reflect((0, -1), border_rect)
   
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

all_groups = pygame.sprite.Group()
start, velocity, direction = (250, 250), 5, (random.random(), random.random())
ball = Ball(start, velocity, direction)
all_groups.add(ball)

border_rect = pygame.Rect(100, 100, 300, 300)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_groups.update(border_rect)

    window.fill('black')
    pygame.draw.rect(window, (255, 0, 0), border_rect, 1)
    all_groups.draw(window)
    pygame.display.flip()