# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Im trying to make a fade in and out
# https://stackoverflow.com/questions/75001219/im-trying-to-make-a-fade-in-and-out/75003503#75003503 
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Fade in and out
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

font = pygame.font.SysFont(None, 100)
text = font.render("image", True, (255, 255, 0))
image = pygame.Surface(window.get_size(), pygame.SRCALPHA)
pygame.draw.ellipse(image, "red", window.get_rect().inflate(-20, -20))
image.blit(text, text.get_rect(center = window.get_rect().center))
image.set_alpha(0)

def blitFadeIn(target, image, pos, step=2):
    alpha = image.get_alpha()
    alpha = min(255, alpha + step)
    image.set_alpha(alpha)
    target.blit(image, pos)
    return alpha == 255

def blitFadeOut(target, image, pos, step=2):
    alpha = image.get_alpha()
    alpha = max(0, alpha - step)
    image.set_alpha(alpha)
    target.blit(image, pos)
    return alpha == 0

fade_in = False
fade_out = False
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if not fade_in and not fade_out:
                fade_in = True
                alpha = 0

    window.blit(background, (0, 0))
    if fade_in:
        done = blitFadeIn(window, image, (0, 0))
        if done:
            fade_in, fade_out = False, True
    if fade_out:
        done = blitFadeOut(window, image, (0, 0))
        if done:
            fade_out = False
    pygame.display.flip()

pygame.quit()
exit()