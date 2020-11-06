# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Why is alpha blending not working properly?
# https://stackoverflow.com/questions/54342525/why-is-alpha-blending-not-working-properly-pygame/54348618#54348618
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Transparency
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md

import pygame
import pygame.font
pygame.init()

screen = pygame.display.set_mode((640, 400))

def BlendSurface(image, pos, alpha):
    #blendImage = image.convert_alpha()
    #blendImage.fill((255,255,255, min(1.0,alpha)*255), None, pygame.BLEND_RGBA_MULT)
    #screen.blit(blendImage, pos)
    alphaVal = int(max(0, min(254, alpha*254)))
    image.set_alpha(alphaVal)
    screen.blit(image, pos)

clock = pygame.time.Clock()

font = pygame.font.SysFont('Times New Roman', 100)
text = font.render('blend text', False, (255, 255, 0))

i = 0
run = False
while not run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    i = i + 1 if i <= 200 else 0

    screen.fill((0, 0, 255))
    BlendSurface(text, (100, 100), i/200) 
    pygame.display.flip()
    
pygame.quit()
exit()