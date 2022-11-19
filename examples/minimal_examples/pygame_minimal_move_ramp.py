# pygame.Rect object
# https://www.pygame.org/docs/ref/rect.html
#
# when the rectangle descends the ramp, the rectangle shakes
# https://stackoverflow.com/questions/70521047/when-the-rectangle-descends-the-ramp-the-rectangle-shakes/70521216#70521216
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Rectangle and diagonal slope (ramp)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame

pygame.init()

window = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

class Ramp(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, color, [(0, 0), (0, h), (w, h)])
        self.rect = self.image.get_rect(topleft = (x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft= (x, y))
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, 0)
        self.on_ground = True
                              
    def update(self, border, jump):
        self.previouse_rect = self.rect.copy()
        keys = pygame.key.get_pressed()
        self.direction.x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
        if jump and self.on_ground:
            self.direction.y = -20
            self.on_ground = False
        self.direction.y += 0.9
        self.pos += self.direction
        self.rect.topleft = round(self.pos.x), round(self.pos.y)
        width, height = border.size
        if self.rect.left <= 0:
            self.rect.left = 0
            self.pos.x = self.rect.left
        if self.rect.right >= width:
            self.rect.right = width
            self.pos.x = self.rect.x
        if self.rect.bottom >= height:
            self.rect.bottom = height
            self.direction.y = 0
            self.on_ground = True
            self.pos.y = self.rect.y
        
def ramp_collide(player, ramp):
    if player.rect.colliderect(ramp.rect):
        if player.previouse_rect.right-1 <= ramp.rect.left:
            player.rect.right = ramp.rect.left
            player.pos.x = player.rect.x
        else:
            ratio = ramp.rect.height / ramp.rect.width
            bottom = ramp.rect.bottom - (ramp.rect.right - max(player.rect.left, ramp.rect.left)) * ratio
            if player.on_ground or player.rect.bottom > bottom:
                player.rect.bottom = bottom
                player.pos.y = player.rect.y
                player.direction.y = 0
                player.on_ground = True

player = Player(480, 200, 'blue')
ramp = Ramp(150, 250, 300, 150, 'red')
all_sprites = pygame.sprite.Group(player, ramp)

run = True
while run:
    clock.tick(60)
    jump = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jump = True

    player.update(window.get_rect(), jump)
    ramp_collide(player, ramp)

    window.fill('lightgray')
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()

