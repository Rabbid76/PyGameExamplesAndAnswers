# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Why is alpha blending not working properly?
# https://stackoverflow.com/questions/54342525/why-is-alpha-blending-not-working-properly-pygame/54348618#54348618
#
# GitHub - PyGameExamplesAndAnswers - vBlending and transparency - Blending
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md

import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600), 0, 32)

def transparentSurface(size):
    surface = pygame.Surface(screen.get_size()).convert_alpha()
    surface.fill((0, 0, 0, 0))
    return surface

alpha, increase = 0, 1
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(pygame.Color(247, 25, 0,255))
    
    alpha_surface1 = transparentSurface(screen.get_size())
    pygame.draw.rect(alpha_surface1, (247, 137, 0, 255), (120, 120, 480, 480))

    alpha_surface2 =  transparentSurface(screen.get_size())
    pygame.draw.rect(alpha_surface2, (220, 247, 0, alpha), (240, 240, 360, 360))

    alpha_surface3 =  transparentSurface(screen.get_size())
    pygame.draw.rect(alpha_surface3, (0, 247, 4), (360, 360, 240, 240) )

    alpha_surface4 =  transparentSurface(screen.get_size())
    pygame.draw.rect(alpha_surface4, (0, 78, 247, alpha), (480, 480, 120, 120) )
    
    screen.blit(alpha_surface1, (0,0))
    screen.blit(alpha_surface2, (0,0))
    screen.blit(alpha_surface3, (0,0))
    screen.blit(alpha_surface4, (0,0))

    pygame.display.flip()
    
    alpha += increase
    if alpha < 0 or alpha > 255:
        increase *= -1
        alpha = max(0, min(255, alpha))

pygame.quit()
exit()