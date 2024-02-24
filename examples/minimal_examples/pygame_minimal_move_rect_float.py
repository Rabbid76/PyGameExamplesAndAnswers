# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# moving with a normalized vector in pygame inconsistent?
# https://stackoverflow.com/questions/68486375/moving-with-a-normalized-vector-in-pygame-inconsistent/68486486#68486486
#
# GitHub - PyGameExamplesAndAnswers - Rectangle - Floating point coordinates
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_rectangle.md 

import pygame

class RedObject(pygame.sprite.Sprite):
    def __init__(self, p, t):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "red", (10, 10), 10)
        self.rect = self.image.get_rect(center = p)
        self.move = (pygame.math.Vector2(t) - p).normalize()
    def update(self, window_rect):
        self.rect.centerx += self.move.x * 2
        self.rect.centery += self.move.y * 2
        if not window_rect.colliderect(self.rect):
            self.kill()

class GreenObject(pygame.sprite.Sprite):
    def __init__(self, p, t):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "green", (10, 10), 10)
        self.rect = self.image.get_rect(center = p)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.move = (pygame.math.Vector2(t) - p).normalize()
    def update(self, window_rect):
        self.pos += self.move * 2
        self.rect.center = round(self.pos.x), round(self.pos.y)
        if not window_rect.colliderect(self.rect):
            self.kill()

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

start_pos = (200, 200)
all_sprites = pygame.sprite.Group()

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.add(RedObject(start_pos, event.pos))
            all_sprites.add(GreenObject(start_pos, event.pos))

    all_sprites.update(window.get_rect())

    window.fill('black')
    all_sprites.draw(window)
    pygame.draw.circle(window, "white", start_pos, 10)
    pygame.draw.line(window, "white", start_pos, pygame.mouse.get_pos())
    pygame.display.flip()

pygame.quit()
exit()