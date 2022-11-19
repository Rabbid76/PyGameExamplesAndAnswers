# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Surface alpha lost when converting pygame to cv2 to pygame
# https://stackoverflow.com/questions/69888520/surface-alpha-lost-when-converting-pygame-to-cv2-to-pygame/69888915#69888915
# 
# Dark borders in cv2.blur
# https://stackoverflow.com/questions/69977901/dark-borders-in-cv2-blur/69981313#69981313)   
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Particles
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame, cv2 
import numpy as np

def Bloom1(canvas: pygame.Surface):
    size = canvas.get_size()
    newCanvas = pygame.Surface(size, pygame.SRCALPHA)
    newCanvas.set_colorkey((0,0,0))
    canvas_rgb = pygame.surfarray.array3d(canvas)
    canvas_alpha = pygame.surfarray.array_alpha(canvas).reshape((*canvas_rgb.shape[0:2], 1))
    canvas_rgba = np.concatenate((canvas_rgb, canvas_alpha), 2)
    #cv2.GaussianBlur(canvas_rgba, ksize=(9, 9), sigmaX=10, sigmaY=10, dst=canvas_rgba)
    cv2.blur(canvas_rgba, ksize=(15, 15), dst=canvas_rgba)
    newCanvas.blit(pygame.image.frombuffer(canvas_rgba.transpose((1, 0, 2)).copy(order='C'), size, 'RGBA'), (0,0))
    return newCanvas

def Bloom2(canvas: pygame.Surface):
    size = canvas.get_size()
    canvas_color = pygame.surfarray.array2d(canvas)
    canvas_rgba = canvas_color.view(dtype=np.uint8).reshape((*canvas_color.shape, 4))
    newCanvas = pygame.Surface(size, pygame.SRCALPHA)
    #cv2.GaussianBlur(canvas_rgba, ksize=(9, 9), sigmaX=10, sigmaY=10, dst=canvas_rgba)
    cv2.blur(canvas_rgba, ksize=(15, 15), dst=canvas_rgba)
    pygame.surfarray.blit_array(newCanvas, canvas_color)
    return newCanvas

def BloomNoPremultipliedAlpha(canvas: pygame.Surface):
    size = canvas.get_size()
    canvas_color = pygame.surfarray.array2d(canvas)
    canvas_rgba = canvas_color.view(dtype=np.uint8).reshape((*canvas_color.shape, 4))
    newCanvas = pygame.Surface(size, pygame.SRCALPHA)
    #cv2.GaussianBlur(canvas_rgba, ksize=(9, 9), sigmaX=10, sigmaY=10, dst=canvas_rgba)
    cv2.blur(canvas_rgba, ksize=(15, 15), dst=canvas_rgba)
    canvas_rgba[:,:,0:3] = canvas_rgba[:,:,0:3] * 255.0 / canvas_rgba[:,:,[3,3,3]]
    pygame.surfarray.blit_array(newCanvas, canvas_color)
    return newCanvas

pygame.init()
window = pygame.display.set_mode((800, 300))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 100, *window.get_size(), (160, 160, 160), (96, 96, 96)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

font = pygame.font.SysFont(None, 90)
text = font.render("Bloom", True, 0)
surface = pygame.Surface((250, 250))
surface.fill(0)
pygame.draw.circle(surface, (255, 255, 255), surface.get_rect().center, 100)
surface.blit(text, text.get_rect(center = surface.get_rect().center))
surface.set_colorkey(0)
surface = surface.convert_alpha()

surface1 = Bloom1(surface)
surface2 = Bloom2(surface)
surface3 = BloomNoPremultipliedAlpha(surface)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.blit(background, (0, 0))
    window.blit(surface1, surface1.get_rect(center = (150, 150)), special_flags = pygame.BLEND_PREMULTIPLIED)
    window.blit(surface2, surface2.get_rect(center = (400, 150)), special_flags = pygame.BLEND_PREMULTIPLIED)
    window.blit(surface3, surface1.get_rect(center = (650, 150)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
