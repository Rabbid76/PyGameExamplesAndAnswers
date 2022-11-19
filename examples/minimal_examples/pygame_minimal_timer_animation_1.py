# Trouble with explosion animation Pygame
# https://stackoverflow.com/questions/70128800/trouble-with-explosion-animation-pygame/70129027#70129027
#
# GitHub - Motion and movement - Animation
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img_list = img_list
        self.frame_count = 0
        self.image = self.img_list[0]
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        self.frame_count += 1
        image_index = self.frame_count // 2
        if image_index < len(self.img_list):
            self.image = self.img_list[image_index]
        else:
            self.kill()

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

img_list = []
for i in range(0, 250, 10):
    img_list.append(pygame.Surface((80, 80), pygame.SRCALPHA))
    pygame.draw.circle(img_list[-1], (255, 255-i, 0), (40, 40), round(1 + 39 * (250-i) / 250))
explosion_group = pygame.sprite.Group()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            explosion = Explosion(event.pos[0], event.pos[1])
            explosion_group.add(explosion)
            
    explosion_group.update() 
            
    window.fill(0)
    explosion_group.draw(window)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()