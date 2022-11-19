# pygame.Rect object
# https://www.pygame.org/docs/ref/rect.html#pygame.Rect
#
# How do I detect collision in pygame?
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame/65064907#65064907
#
# How do you program collision in classes?
# https://stackoverflow.com/questions/69331228/how-do-you-program-collision-in-classes/69332148#69332148
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Overview
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-spritecollide

import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))

class RectSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        super().__init__() 
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = pygame.Rect(x, y, w, h)

player = RectSprite((255, 0, 0), 0, 0, 50, 50)
obstacle1 = RectSprite((128, 128, 128), 50, 150, 50, 50)
obstacle2 = RectSprite((128, 128, 128), 150, 50, 50, 50)
all_group = pygame.sprite.Group([obstacle1, obstacle2, player])
obstacle_group = pygame.sprite.Group([obstacle1, obstacle2])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.rect.center = pygame.mouse.get_pos()
    collide = pygame.sprite.spritecollide(player, obstacle_group, False)
    
    window.fill(0)
    all_group.draw(window)
    for s in collide:
        pygame.draw.rect(window, (255, 255, 255), s.rect, 5, 1)
    pygame.display.flip()

pygame.quit()
exit()
