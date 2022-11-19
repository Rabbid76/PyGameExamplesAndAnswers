# use a color lookup table with pygame
# https://stackoverflow.com/questions/63748651/use-a-color-lookup-table-with-pygame/64198152#64198152
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Lookup table
# https://stackoverflow.com/questions/63748651/use-a-color-lookup-table-with-pygame/64198152#64198152

import pygame
import numpy as np
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

lut = np.arange(10) * 10
img = np.random.randint(0,9,size=(3,3))
img2 = lut[img]

LUT = np.empty([256,3],np.uint8)
for gg in range(0,256):
    LUT[gg,:] = [gg,gg,gg]

def applyLUT(surf, LUT):
    buffer = pygame.surfarray.pixels3d(surf)
    I = (255*np.random.rand(*surf.get_size())).astype(int)

    lutBuffer = (LUT[buffer[:,:,0],:] + LUT[buffer[:,:,1],:] + LUT[buffer[:,:,2],:]) / 3
    buffer[:,:,:] = lutBuffer

pygame.init()
window = pygame.display.set_mode((600, 480))
clock = pygame.time.Clock()
image = pygame.image.load('image/parrot1.png').convert()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    scaled_image = pygame.transform.scale(image, window.get_size())
    applyLUT(scaled_image, LUT)

    window.fill(0)
    window.blit(scaled_image, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()
