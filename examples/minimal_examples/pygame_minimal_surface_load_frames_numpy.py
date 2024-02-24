# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Pygame and Numpy Animations
# https://stackoverflow.com/questions/54415196/pygame-and-numpy-animations
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load Pillow image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import pygame
import numpy as np
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

radius = 100
frames = 20
data = np.zeros(shape = (radius*2, radius*2, 4, frames), dtype = "uint8")
for x in range(data.shape[0]): 
    for y in range(data.shape[1]):
        px, py = x - data.shape[0]/2, y - data.shape[1]/2
        for i in range(frames):
            maxY2 = (radius*radius - px*px) * pow(abs(i-frames/2) / frames, 2)
            if px*px + py* py < radius*radius:
                if py * py < maxY2:
                    data[y, x, (0, 3), i] = 255, 255
                    if (px*px + py*py)*4 > radius*radius:
                        data[y, x, (1, 2), i] = 255, 255
                else:
                    data[y, x, (2, 3), i] = 255, 255 
                   

#surf_list = [pygame.image.frombuffer(data[:,:,[2, 1, 0, 3], i].flatten(), (data.shape[1::-1]), 'RGBA') for i in range(data.shape[3])]
#surf_list = [pygame.image.frombuffer(d[:,:,[2, 1, 0, 3]].flatten(), (data.shape[1::-1]), 'RGBA') for d in np.moveaxis(data, 3, 0)]
#surf_list = [pygame.image.frombuffer(d[:,:,[2, 1, 0, 3]].flatten(), (data.shape[1::-1]), 'RGBA') for d in np.rollaxis(data, 3)]
surf_list = [pygame.image.frombuffer(d[:,:,[2, 1, 0, 3]].flatten(), (data.shape[1::-1]), 'RGBA') for d in data.transpose(3, 0, 1, 2)]

"""
surf_list = []
for d in data.transpose(3, 0, 1, 2):
    bytes = d[:,:,[2, 1, 0, 3]].flatten()
    size = data.shape[1::-1]
    format = 'RGBA'
    surface = pygame.image.frombuffer(bytes, size, format)
    surf_list.append(surface)
"""

count = 0
run = False
while not run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    window.fill('black')
    window.blit(surf_list[count], surf_list[0].get_rect(center = window.get_rect().center))
    pygame.display.flip()
    count = (count + 1) %  len(surf_list)

pygame.quit()
exit()