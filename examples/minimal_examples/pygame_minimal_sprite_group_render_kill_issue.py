# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Why is self.kill() not removing the object from the group?
# https://stackoverflow.com/questions/73378230/why-is-self-kill-not-removing-the-object-from-the-group?noredirect=1#comment129587586_73378230
#
# GitHub - Sprite, Group and Sprite mask - Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import pygame

elementGroup = pygame.sprite.Group()
entityGroup = pygame.sprite.Group()

class Element(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        elementGroup.add(self)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        entityGroup.add(self)

class Bullet(Element, Entity):
    def __init__(self):
        Entity.__init__(self)
        Element.__init__(self)

bullet = Bullet()

print(len(elementGroup), len(entityGroup))
bullet.kill()
print(len(elementGroup), len(entityGroup))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill('black')
    pygame.display.flip()

pygame.quit()
exit()