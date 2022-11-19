# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# pygame Get the balls to bounce off each other
# https://stackoverflow.com/questions/63586822/pygame-get-the-balls-to-bounce-off-each-other/63587147#63587147
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-BallsBounceOff

import os
import random
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

size = 64
try:
    ballImage = pygame.transform.smoothscale(pygame.image.load("icon/Ball64.png"), (size, size))
except:
    ballImage = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.circle(ballImage, (255, 255, 0), (size//2, size//2), size//2)

class Ball(pygame.sprite.Sprite):
    def __init__(self, startpos, velocity, startdir):
        super().__init__()
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        self.image = ballImage
        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))

    def reflect(self, NV):
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))

    def update(self):
        self.pos += self.dir * 10
        self.rect.center = round(self.pos.x), round(self.pos.y)

        if self.rect.left <= 0:
            self.reflect((1, 0))
            self.rect.left = 0
        if self.rect.right >= window.get_width():
            self.reflect((-1, 0))
            self.rect.right = window.get_width()
        if self.rect.top <= 0:
            self.reflect((0, 1))
            self.rect.top = 0
        if self.rect.bottom >= window.get_height():
            self.reflect((0, -1))
            self.rect.bottom = window.get_height()

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

all_balls = pygame.sprite.Group()

start, velocity, direction = (100, 100), 10, (random.random(), random.random())
ball_1 = Ball(start, velocity, direction)

start, velocity, direction = (300, 300), 10, (random.random(), random.random())
ball_2 = Ball(start, velocity, direction)

all_balls.add(ball_1, ball_2)

def reflectBalls(ball_1, ball_2):
    v1 = pygame.math.Vector2(ball_1.rect.center)
    v2 = pygame.math.Vector2(ball_2.rect.center)
    r1 = ball_1.rect.width // 2
    r2 = ball_2.rect.width // 2
    d = v1.distance_to(v2)
    if d < r1 + r2 - 2:
        dnext = (v1 + ball_1.dir).distance_to(v2 + ball_2.dir)
        nv = v2 - v1
        if dnext < d and nv.length() > 0:
            ball_1.reflect(nv)
            ball_2.reflect(nv)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_balls.update()

    ball_list = all_balls.sprites()
    for i, b1 in enumerate(ball_list):
        for b2 in ball_list[i+1:]:
            reflectBalls(b1, b2)

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), window.get_rect(), 1)
    all_balls.draw(window)
    pygame.display.flip()

pygame.quit()
exit()