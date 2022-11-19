# Pygame Curve Movement Problem How To Fix?
# https://stackoverflow.com/questions/67766962/pygame-curve-movement-problem-how-to-fix/67777164#67777164
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Gravity
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame
pygame.init()

class Object:
    def __init__(self, x, y, height, width, color):
        self.pos = pygame.math.Vector2(x, y)
        self.color = color
        self.rect = pygame.Rect(x, y, height, width)
        self.speed = pygame.math.Vector2(-10.0, 0)
        self.gravity = 1
        self.friction = 0.99
    
    def draw(self):
        self.rect.center = (self.pos.x, self.pos.y)
        pygame.draw.circle(window, self.color, (self.pos.x, self.pos.y), self.rect.width//2)
    
    def update(self, target_pos):
        dir_vec = pygame.math.Vector2(target_pos) - self.rect.center
        v_len_sq = dir_vec.length_squared()
        if v_len_sq > 0:
            dir_vec.scale_to_length(self.gravity)
            self.speed = (self.speed + dir_vec) * self.friction
            self.pos += self.speed

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("test map")
clock = pygame.time.Clock()
meteor = Object(250, 400, 20, 20, (255, 255, 255))
target = Object(250, 200, 20, 20, (205, 0, 0))
move = True

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                move = False
                meteor = Object(250, 400, 20, 20, (255, 255, 255))
            else:
                move = True

    if (meteor.pos - target.pos).length() < 10:
        move = False
    if move:
        meteor.update(target.rect.center)

    window.fill((0,0,0))
    meteor.draw()
    target.draw()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()