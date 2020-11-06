# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Setting a pygame surface to have rounded corners
# https://stackoverflow.com/questions/63700231/setting-a-pygame-surface-to-have-rounded-corners/63701005#63701005
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame

class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.Surface((100, 100))
        self.original_image.fill((255, 0, 0))
        self.image = self.original_image
        self.rect = self.image.get_rect()

    def set_rounded(self, roundness):
        size = self.original_image.get_size()
        self.rect_image = pygame.Surface(size, pygame.SRCALPHA)
        
        pygame.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius=roundness)

        #pg.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius=roundness)

        r, c = roundness, (255, 255, 255)
        pygame.draw.rect(self.rect_image, c, (r, 0, size[0]-2*r, size[1]))
        pygame.draw.rect(self.rect_image, c, (0, r, size[1], size[1]-2*r))
        for cpt in [(r, r), (size[0]-r, r), (r, size[1]-r), (size[0]-r, size[1]-r)]:  
            pygame.draw.circle(self.rect_image, c, cpt, r)

        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN) 

pygame.init()
window = pygame.display.set_mode((200, 200))

rect_object = Rectangle()
rect_object.set_rounded(30)
rect_object.rect.center = window.get_rect().center
group = pygame.sprite.Group(rect_object)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((32, 32, 32))
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()