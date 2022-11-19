# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# How do I gently change the direction of movement when moving forward?
# https://stackoverflow.com/questions/70541096/how-do-i-gently-change-the-direction-of-movement-when-moving-forward/70541236#70541236
#
# How to turn the sprite in pygame while moving with the keys
# https://stackoverflow.com/questions/64792467/how-to-turn-the-sprite-in-pygame-while-moving-with-the-keys/64792568#64792568
#
# Image rotation while moving
# https://stackoverflow.com/questions/57226587/image-rotation-while-moving/57227063#57227063
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import pygame
import math
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class MyCar(pygame.sprite.Sprite):       
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self) 
        self.image = image   
        self.rect = self.image.get_rect(center = (x, y)) 
        self.speed = 5                     
        self.driving_angle = 0  
        self.steering_angle = 0      
       
    def update(self, border_rect):  
        keys = pygame.key.get_pressed()
        move = keys[pygame.K_UP] - keys[pygame.K_DOWN]
        stear = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]       
        self.steering_angle = max(-2.5, min(2.5, self.steering_angle - stear * 0.2))  
        self.rect.y -= round(math.cos(math.radians(self.driving_angle)) * move * self.speed)
        self.rect.x -= round(math.sin(math.radians(self.driving_angle)) * move * self.speed)
        self.driving_angle += (self.steering_angle * move) % 360 
        self.rect.x = self.rect.x % border_rect.width
        self.rect.y = self.rect.y % border_rect.height
 
def blitRotateCenter(surf, image, left, top, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (left, top)).center)
    surf.blit(rotated_image, new_rect)
    return new_rect

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

car_image = pygame.image.load('icon/CarRed64.png').convert_alpha()
car_image = pygame.transform.rotate(car_image, 90) 
car_sprite = MyCar(250, 400, car_image)

run = True
while run:
    clock.tick(100)      
    events = pygame.event.get()
    for event in events:                     
        if event.type == pygame.QUIT:
            run = False
                   
    car_sprite.update(window.get_rect()) 

    window.fill((0, 0, 0)) 
    car_sprite.rect = blitRotateCenter(window, car_sprite.image, *car_sprite.rect.center, car_sprite.driving_angle) 
    pygame.display.flip()

pygame.quit()
exit() 