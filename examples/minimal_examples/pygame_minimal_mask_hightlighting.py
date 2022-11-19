# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# How to add a white surface with the shape of my original image in pygame?
# https://stackoverflow.com/questions/67884084/how-to-add-a-white-surface-with-the-shape-of-my-original-image-in-pygame/67889758#67889758
#
# GitHub - Mask - Selection and highlighting
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mask.md
#
# https://replit.com/@Rabbid76/PyGame-HighlightObject

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

class TestObject:
    def __init__(self, center, filename):
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center = center)
        self.selected = False

def create_white_surf(surf, alpha):
    mask = pygame.mask.from_surface(surf)
    white_surface = mask.to_surface()
    white_surface.set_colorkey((0, 0, 0))
    white_surface.set_alpha(alpha)
    return white_surface

obj_list = [
    TestObject((90, 90), 'icon/Apple64.png'), 
    TestObject((210, 90), 'icon/Plums64.png'),
    TestObject((90, 210), 'icon/Cherries64.png'), 
    TestObject((210, 210), 'icon/Pear64.png')]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    for obj in obj_list:
        obj.selected = obj.rect.collidepoint(pygame.mouse.get_pos())      

    window.fill((127, 127, 128))

    for obj in obj_list:
        window.blit(obj.image, obj.rect)
        if obj.selected:
            white_surf = create_white_surf(obj.image, 64)
            window.blit(white_surf, obj.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()