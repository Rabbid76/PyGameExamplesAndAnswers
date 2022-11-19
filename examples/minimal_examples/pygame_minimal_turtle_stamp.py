# Is there a .stamp() method in pygame like in turtle?
# https://stackoverflow.com/questions/66485793/is-there-a-stamp-method-in-pygame-like-in-turtle/66504640#66504640
#
# GitHub - PyGameExamplesAndAnswers - Turtle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_turtle.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

turtle = pygame.Surface((48, 40), pygame.SRCALPHA)
for p in [(5, 5), (27, 5), (5, 35), (27, 35)]:
    pygame.draw.circle(turtle, "brown", p, 5)
pygame.draw.circle(turtle, "green", (40, 20), 8)
pygame.draw.circle(turtle, "darkgreen", (16, 20), 16)
turtle_rect = turtle.get_rect(center = (60, 60))

stamps = []

def stamp(pos, surf):
    stamps.append((pos, surf))

def draw_stamps(target_surf):
    for pos, surf in stamps:
         target_surf.blit(surf, pos)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
        if event.type == pygame.MOUSEBUTTONDOWN:
            stamp(turtle_rect.topleft, turtle)

    keys = pygame.key.get_pressed()
    turtle_rect.x += (keys[pygame.K_d] - keys[pygame.K_a]) * 5
    turtle_rect.y += (keys[pygame.K_s] - keys[pygame.K_w]) * 5 
    turtle_rect.clamp_ip(window.get_rect())              

    window.fill((255, 255, 255))
    draw_stamps(window)
    window.blit(turtle, turtle_rect)
    pygame.display.flip()

pygame.quit()
exit()