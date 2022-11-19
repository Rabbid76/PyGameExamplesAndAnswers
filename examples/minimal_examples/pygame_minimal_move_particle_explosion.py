# Projectile motion and gravity in pygame only sometimes working
# https://stackoverflow.com/questions/55822116/projectile-motion-and-gravity-in-pygame-only-sometimes-working/55836374#55836374
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Particles
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame
import random
import math

class ProjectileSprite(pygame.sprite.Sprite):
    GRAVITY = -9.8  

    def new(surf, image):
        speed = random.randrange(10, 50)
        angle = math.radians(random.randrange(-45, 45))
        start = surf.get_width() // 2, window.get_height() - image.get_height() // 2
        return ProjectileSprite(*start, image, speed, angle)

    def __init__(self, x, y, bitmap, velocity, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image       = bitmap
        self.rect        = bitmap.get_rect()
        self.start_x     = x
        self.start_y     = y
        self.rect.center = self.start_x, self.start_y
        self.start_time  =  pygame.time.get_ticks()   
        self.velocity    = velocity
        self.angle       = angle 

    def reset(self, current_time):
        self.start_time = current_time
        self.velocity = random.randrange(10, 50)
        self.angle = math.radians(random.randrange(-45, 45))

    def update(self, current_time, bottom):
        time_change = (current_time - self.start_time) / 150.0
        if self.velocity > 0 and time_change > 0:
            half_gravity_time_squared = self.GRAVITY * time_change * time_change / 2.0
            displacement_x = self.velocity * math.sin(self.angle) * time_change 
            displacement_y = self.velocity * math.cos(self.angle) * time_change + half_gravity_time_squared
            self.rect.center = round(self.start_x + displacement_x), round(self.start_y - displacement_y)

            if self.rect.y >= bottom - self.rect.height:
                self.rect.y = bottom - self.rect.height
                self.velocity = 0
                #self.kill()

pygame.init()
window  = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

particle_image = pygame.Surface((10, 10), pygame.SRCALPHA)
pygame.draw.circle(particle_image, (255, 0, 0), (5, 5), 5)

all_sprites = pygame.sprite.Group()
for i in range(20):
    all_sprites.add(ProjectileSprite.new(window, particle_image))

done  = False
while not done:
    clock.tick_busy_loop(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_PLUS:
                all_sprites.add(ProjectileSprite.new(window, particle_image))

            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                for s in all_sprites:
                    s.reset(current_time)

    window.fill((64, 64, 64))
    all_sprites.update(current_time, window.get_height())
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()