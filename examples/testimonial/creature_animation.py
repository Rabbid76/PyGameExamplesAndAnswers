# https://replit.com/@Rabbid76
# https://replit.com/@Rabbid76/Pygame-CreatureAnimation#main.py

import pygame
import math

def create_smiley():
    local_surf = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.circle(local_surf, "white", (25, 25), 25)
    pygame.draw.circle(local_surf, "black", (25, 25), 25, 2)
    pygame.draw.circle(local_surf, "black", (15, 18), 5)
    pygame.draw.circle(local_surf, "black", (35, 18), 5)
    pygame.draw.lines(local_surf, "black", False, [(15, 32), (20, 38), (30, 38), (35, 32)], 3) 
    return local_surf

def create_ghost():
    local_surf = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.circle(local_surf, "white", (25, 25), 24)
    pygame.draw.circle(local_surf, "black", (25, 25), 24, 2)
    pygame.draw.rect(local_surf, (0, 0, 0, 0), (0, 25, 50, 25))
    for x in range(7, 44, 12):
        pygame.draw.circle(local_surf, "white", (x, 38), 6)
        pygame.draw.circle(local_surf, "black", (x, 38), 6, 2)
    pygame.draw.rect(local_surf, "black", (1, 25, 48, 11), 2)    
    pygame.draw.rect(local_surf, "white", (3, 25, 44, 12))
    pygame.draw.circle(local_surf, "black", (15, 18), 5)
    pygame.draw.circle(local_surf, "black", (35, 18), 5)
    return local_surf

class Creature(pygame.sprite.Sprite):
    def __init__(self, image, animation, color_animation):
        super().__init__() 
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect()
        self.animation = animation
        self.color_animation = color_animation
    def update(self):
        if self.animation:
            self.animation.update_rect(self.rect)
        if self.color_animation:
            self.image = self.color_animation.update_image(self.original_image)

class HypotrochoidAnimation:
    def __init__(self, start, center):
        self.frame = start
        self.center = center
    def update_rect(self, rect):
        t = math.radians(self.frame)
        a, b, h = 100, 60, 100
        x = self.center[0] + (a-b)*math.cos(t) + h*math.cos((a-b)/b*t)
        y = self.center[1] + (a-b)*math.sin(t) - h*math.sin((a-b)/b*t)
        self.frame = (self.frame + 4) % (360 * 3)
        rect.center = round(x), round(y)

class HueColorAnimation:
    def __init__(self, start):
        self.frame = start
    def update_image(self, image):
        color = pygame.Color(0)
        color.hsla = (self.frame, 100, 50, 100)
        self.frame = (self.frame + 1) % 360
        colouredImage = pygame.Surface(image.get_size())
        colouredImage.fill(color)
        finalImage = image.copy()
        finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
        return finalImage

pygame.init()

displ_surf = pygame.display.set_mode((400, 400))
displ_surf.fill((64, 64, 64))
clock = pygame.time.Clock()

background_surf = pygame.Surface(displ_surf.get_size())
background_surf.fill((64, 64, 64))
background_surf.set_alpha(10)

center = displ_surf.get_rect().center
creatures = pygame.sprite.Group([
    Creature(create_smiley(), HypotrochoidAnimation(0, center), HueColorAnimation(0)),
    Creature(create_smiley(), HypotrochoidAnimation(360*3/4, center), HueColorAnimation(120)),
    Creature(create_smiley(), HypotrochoidAnimation(360*3/4*2, center), HueColorAnimation(240)),
    Creature(create_ghost(), HypotrochoidAnimation(360*3/4*3, center), 0)
])
frame = 0

run = True
while run:
    clock.tick(50)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pygame.image.save(displ_surf, 'creature_animation.png')

    creatures.update()

    displ_surf.blit(background_surf, (0, 0))
    creatures.draw(displ_surf)  
    pygame.display.flip()

pygame.quit()
exit()
