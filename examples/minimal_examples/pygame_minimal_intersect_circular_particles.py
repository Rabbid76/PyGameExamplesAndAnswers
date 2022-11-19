# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Random systematic movement in pygame
# https://stackoverflow.com/questions/65468240/random-systematic-movement-in-pygame/65468502#65468502 
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import random
import pygame

class Particle(pygame.sprite.Sprite):
    def __init__(self, hue, pos, radius, dir, vel):
        super().__init__()
        self.pos = pygame.math.Vector2(pos)
        self.dir = pygame.math.Vector2(dir)
        self.vel = vel
        self.radius = radius
        self.rect = pygame.Rect(round(self.pos.x - radius), round(self.pos.y - radius), radius*2, radius*2)
        self.image = pygame.Surface((radius*2, radius*2))
        self.changeColor(hue)

    def changeColor(self, hue):
        self.hue = hue
        color = pygame.Color(0)
        color.hsla = (self.hue, 100, 50, 100)
        self.image.set_colorkey((0, 0, 0))
        self.image.fill(0)
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)

    def move(self):
        self.pos += self.dir * self.vel

    def update(self, border_rect):

        if self.pos.x - self.radius < border_rect.left:
            self.pos.x = border_rect.left + self.radius
            self.dir.x = abs(self.dir.x)
        elif self.pos.x + self.radius > border_rect.right:
            self.pos.x = border_rect.right - self.radius
            self.dir.x = -abs(self.dir.x)
        if self.pos.y - self.radius < border_rect.top:
            self.pos.y = border_rect.top + self.radius
            self.dir.y = abs(self.dir.y)
        elif self.pos.y + self.radius > border_rect.bottom:
            self.pos.y = border_rect.bottom - self.radius
            self.dir.y = -abs(self.dir.y) 

        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
rect_area = window.get_rect().inflate(-40, -40)

all_particles = pygame.sprite.Group()
radius, velocity = 5, 1
pos_rect = rect_area.inflate(-radius * 2, -radius * 2)

run = True
while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(all_particles.sprites()) < 100:
        hue = random.randrange(360)
        x = random.randrange(pos_rect.left, pos_rect.right)
        y = random.randrange(pos_rect.top, pos_rect.bottom)
        dir = pygame.math.Vector2(1, 0).rotate(random.randrange(360))
        particle = Particle(hue, (x, y), radius, dir, velocity)
        if not pygame.sprite.spritecollide(particle, all_particles, False, collided = pygame.sprite.collide_circle):
            all_particles.add(particle)

    for particle in all_particles:
        particle.move()

    particle_list = all_particles.sprites()
    for i, particle_1 in enumerate(particle_list):
        for particle_2 in particle_list[i:]:
            distance_vec = particle_1.pos - particle_2.pos
            if 0 < distance_vec.length_squared() < (particle_1.radius + particle_2.radius) ** 2:
                particle_1.dir.reflect_ip(distance_vec)
                particle_2.dir.reflect_ip(distance_vec)
                if abs(particle_1.hue - particle_2.hue) <= 180:
                    hue = (particle_1.hue + particle_2.hue) // 2
                else:
                    hue = (particle_1.hue + particle_2.hue + 360) // 2 % 360
                particle_1.changeColor(hue)
                particle_2.changeColor(hue)
                break

    all_particles.update(rect_area)

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect_area, 3)
    all_particles.draw(window)
    pygame.display.flip()

pygame.quit()
exit()