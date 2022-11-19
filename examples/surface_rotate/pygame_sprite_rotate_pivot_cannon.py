# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How do I rotate an image around its center using PyGame?
# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
#
# How can you rotate an image around an off center pivot in Pygame
# https://stackoverflow.com/questions/59909942/how-can-you-rotate-an-image-around-an-off-center-pivot-in-pygame/59909946#59909946
#
# How to set the pivot point (center of rotation) for pygame.transform.rotate()?
# https://stackoverflow.com/questions/15098900/how-to-set-the-pivot-point-center-of-rotation-for-pygame-transform-rotate/69312319#69312319
#
# How do I make image rotate with mouse python
# https://stackoverflow.com/questions/65573379/how-do-i-make-image-rotate-with-mouse-python/65575874#65575874
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_rotate.md
#
# GitHub - Sprite, Group and Sprite mask - Drag Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-RotateSpriteAroundOffCenterPivotCannon

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class SpriteRotate(pygame.sprite.Sprite):

    def __init__(self, imageName, origin, pivot):
        super().__init__() 
        self.image = pygame.image.load(imageName)
        self.original_image = self.image
        self.rect = self.image.get_rect(topleft = (origin[0]-pivot[0], origin[1]-pivot[1]))
        self.origin = origin
        self.pivot = pivot
        self.angle = 0

    def update(self):
        image_rect = self.original_image.get_rect(topleft = (self.origin[0] - self.pivot[0], self.origin[1]-self.pivot[1]))
        offset_center_to_pivot = pygame.math.Vector2(self.origin) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-self.angle)
        rotated_image_center = (self.origin[0] - rotated_offset.x, self.origin[1] - rotated_offset.y)
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center = rotated_image_center)
  
pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cannon = SpriteRotate('icon/cannon.png', (200, 200), (33.5, 120))
cannon_mount = SpriteRotate('icon/cannon_mount.png', (200, 200), (43, 16))
all_sprites = pygame.sprite.Group([cannon, cannon_mount])
angle_range = [-90, 0]
angle_step = -1

frame = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    all_sprites.update()
    screen.fill((64, 128, 255))
    pygame.draw.rect(screen, (127, 127, 127), (0, 250, 400, 150))
    all_sprites.draw(screen)
    pygame.display.flip()
    frame += 1
    cannon.angle += angle_step
    if not angle_range[0] < cannon.angle < angle_range[1]:
        angle_step *= -1
    
pygame.quit()
exit()

