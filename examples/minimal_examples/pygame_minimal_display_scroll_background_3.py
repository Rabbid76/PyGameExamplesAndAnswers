# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# How to move the player across a one background image?
# https://stackoverflow.com/questions/67736156/how-to-move-the-player-across-a-one-background-image?noredirect=1#comment119731761_67736156
#
# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Scroll background
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 0), (10, 10), 10)
        self.rect = self.image.get_rect(center = (x, y))
        self.x, self.y = self.rect.topleft

    def update(self, time_passed, window_size, map_size):
        key = pygame.key.get_pressed()
        self.x += (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * 500 * time_passed
        self.y += (key[pygame.K_DOWN] - key[pygame.K_UP]) * 500 * time_passed
        self.x = max(0, min(map_size[0]-20, self.x))
        self.y = max(0, min(map_size[1]-20, self.y))
        center = window_size[0] // 2, window_size[0] // 2
        pos = [round(self.x), round(self.y)]
        for i in range(2):
            if center[i] < pos[i] <= map_size[i]-center[i]:
                pos[i] = center[i]
            elif pos[i] > map_size[i] - center[i]: 
                pos[i] = window_size[i] - map_size[i] + pos[i]
        self.rect.topleft = pos
   
class Map(pygame.sprite.Sprite):
    def __init__(self, size, reference_object):
        super().__init__() 
        self.reference_object = reference_object
        self.image = pygame.Surface(size)
        ts, w, h, c1, c2 = 50, *size, (128, 128, 128), (64, 64, 64)
        tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
        [pygame.draw.rect(self.image, color, rect) for rect, color in tiles]
        self.rect = self.image.get_rect()

    def update(self, _, window_size, map_size):  
        self.rect.x = -max(0, min(map_size[0] - window_size[0], self.reference_object.x - 200))
        self.rect.y = -max(0, min(map_size[1] - window_size[1], self.reference_object.y - 200))
  
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

player = Player(200, 200)
map = Map((window.get_width() * 2, window.get_height() * 2), player)
all_sprites = pygame.sprite.Group([map, player])

run = True
while run:
    time_passed = clock.tick(100) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update(time_passed, window.get_size(), map.image.get_size())
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
quit()