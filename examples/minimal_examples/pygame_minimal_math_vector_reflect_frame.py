# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Use vector2 in pygame. Collide with the window frame and restrict the ball to the rectangular area
# https://stackoverflow.com/questions/60213103/use-vector2-in-pygame/60214064#60214064 
#
# GitHub - PyGameExamplesAndAnswers - Vector - Reflection
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_math_vector_and_reflection.md
#
# https://replit.com/@Rabbid76/PyGame-BallBounceOffFrame#main.py

import os
import pygame
import random
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class Ball(pygame.sprite.Sprite):

    def __init__(self, startpos, velocity, startdir):
        super().__init__()
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        self.image = pygame.image.load('icon/ball64.png').convert_alpha()
        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))

    def reflect(self, NV):
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))

    def update(self):
        self.pos += self.dir * self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)

    
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

all_groups = pygame.sprite.Group()
start, velocity, direction = window.get_rect().center, 5, (random.random(), random.random())
ball = Ball(start, velocity, direction)
all_groups.add(ball)
frame_rect = pygame.Rect(100, 100, 300, 300)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            ball.dir = pygame.math.Vector2(random.random(), random.random()).normalize()
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.dir = pygame.math.Vector2(event.pos[0] - ball.rect.centerx, event.pos[1] - ball.rect.centery).normalize()

    all_groups.update()

    if ball.rect.left <= frame_rect.left:
        ball.reflect((1, 0))
    if ball.rect.right >= frame_rect.right:
        ball.reflect((-1, 0))
    if ball.rect.top <= frame_rect.top:
        ball.reflect((0, 1))
    if ball.rect.bottom >= frame_rect.bottom:
        ball.reflect((0, -1))
    ball.rect.clamp_ip(frame_rect)

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), frame_rect, 1)
    all_groups.draw(window)
    pygame.display.flip()

pygame.quit()
exit()