# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# moving with a normalized vector in pygame inconsistent?
# https://stackoverflow.com/questions/68486375/moving-with-a-normalized-vector-in-pygame-inconsistent/68486486#68486486
#
# GitHub - PyGameExamplesAndAnswers - Rectangle - Floating point coordinates
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_rectangle.md 

import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, positions):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill('red')
        self.positions = [pygame.math.Vector2(p) for p in positions]
        self.pos = pygame.math.Vector2(positions[0])
        self.rect = self.image.get_rect(center = positions[0])
        self.speed = 5
        self.direction = 1
        self.current = 0

    def update(self):
        prev_pt = self.positions[self.current]
        next_pt = self.positions[(self.current + self.direction) % len(self.positions)]
        direction = (next_pt - prev_pt).normalize()
        if (next_pt - self.pos).length_squared() < self.speed * self.speed:
            self.pos = pygame.math.Vector2(next_pt)
            self.current = (self.current + self.direction) % len(self.positions)
            if self.current == 0 or self.current == len(self.positions) - 1:
                self.direction *= -1
        else:
            self.pos += direction * self.speed 
        self.rect.center = (round(self.pos.x), round(self.pos.y))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

positions = [(50, 50), (150, 350), (200, 200), (350, 250), (300, 50)]
object_group = pygame.sprite.GroupSingle(Object(positions))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    object_group.update()

    window.fill(0)
    pygame.draw.lines(window, 'grey', False, positions, 4)
    for p in positions:
        pygame.draw.circle(window, 'white', p, 8)
    object_group.draw(window)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()