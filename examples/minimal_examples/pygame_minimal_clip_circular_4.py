# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How do I display a large black rectangle with a moveable transparent circle in pygame?
# https://stackoverflow.com/questions/57393670/how-do-i-display-a-large-black-rectangle-with-a-moveable-transparent-circle-in-p/57612836#57612836
#
# GitHub - PyGameExamplesAndAnswers - Clipping - Circular clipping region
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_clipping.md

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init() 
window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

class MySprite(pygame.sprite.Sprite):
    def __init__(self, imageName, x, y):
        super().__init__() 
        self.image = pygame.image.load(imageName)
        self.rect = self.image.get_rect(center = (x, y))

player = MySprite("icon/avatar64.png", *window.get_rect().center)
speed = 5
group = pygame.sprite.Group([player])

areaRadius = 100
circularArea = pygame.Surface((areaRadius*2, areaRadius*2), pygame.SRCALPHA)
circularArea.fill((0, 0, 0, 255))
pygame.draw.circle(circularArea, (0,0,0,0), (areaRadius, areaRadius), areaRadius)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                
    keys = pygame.key.get_pressed()
    player.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    player.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
    player.rect.clamp_ip(window.get_rect().inflate(-10, -10))

    window.set_clip(None)
    window.fill(0)

    clipRect = pygame.Rect(player.rect.center, (0, 0)).inflate((areaRadius*2, areaRadius*2))
    window.set_clip(clipRect)

    fx = player.rect.centerx / window.get_width()
    fy = player.rect.centery / window.get_height()
    window.fill((63 + 128 * fx, 63 + 128 * fy, 63 + 128 * (1-fx) * (1-fy), 255))
    pygame.draw.rect(window, (255, 0, 0), window.get_rect(), 5)

    group.draw(window)
    window.blit(circularArea, clipRect.topleft)  
    pygame.display.flip()

pygame.quit()
exit()