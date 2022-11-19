# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# Pygame make sprite walk in given rotation
# https://stackoverflow.com/questions/66402816/pygame-make-sprite-walk-in-given-rotation/66403030#66403030
#
# GitHub - Move towards target - Follow target or mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_move_towards_target.md

import pygame, math

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

sprite = pygame.sprite.Sprite()
sprite.image = img_star = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(sprite.image, (255, 255, 0), (10, 10), 10)
sprite.rect = sprite.image.get_rect(center = window.get_rect().center)
group = pygame.sprite.Group(sprite)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dx = mouse_x - sprite.rect.centerx
            dy = mouse_y - sprite.rect.centery
            #dist = math.sqrt(dx*dx + dy*dy)
            dist = math.hypot(dx, dy)
            steps = 10
            if dist > 0:
                sprite.rect.x += steps * dx / dist
                sprite.rect.y += steps * dy / dist

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()