# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# How do I make the image repeat - for example 10x in a row - in Pygame
# https://stackoverflow.com/questions/69884697/how-do-i-make-the-image-repeat-for-example-10x-in-a-row-in-pygame/69884946#69884946
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Triggered by a time interval
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

# https://replit.com/@Rabbid76/PyGame-Sprite

import os
import random
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__() 
        self.image = image.copy()
        size = image.get_size()
        x = random.randrange(size[0]//2, window.get_width()-size[0]//2)
        y = random.randrange(size[1]//2, window.get_height()-size[1]//2)
        self.rect = self.image.get_rect(center = (x, y))
        self.alpha = 255
    
    def update(self):
        if self.alpha >= 0:
            self.image.set_alpha(self.alpha)
        else:
            self.kill()
        self.alpha -= 1
        
object_surf = pygame.image.load('icon/Bird64.png').convert_alpha()
all_sprites = pygame.sprite.Group()
time_interval = 200 # 200 milliseconds == 0.2 seconds
next_object_time = 0 

start = False
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            start = True
            next_object_time = pygame.time.get_ticks()

    current_time = pygame.time.get_ticks()
    if start and current_time > next_object_time:
        next_object_time += time_interval
        all_sprites.add(Player(object_surf))

    all_sprites.update()

    window.fill(0)
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()