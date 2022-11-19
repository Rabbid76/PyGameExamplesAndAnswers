# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Water ripple effect Python and Pygame, from coding train video
# https://stackoverflow.com/questions/60336688/wter-ripple-effect-python-and-pygame-from-coding-train-video/60337269#60337269
#
# from coding train video
# https://www.youtube.com/watch?v=BZUdGqeOD0w
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Effects
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame   
pygame.init()

window = pygame.display.set_mode((300, 200))

size = window.get_size()
dampening = 0.999
current = [[0]*size[1] for col in range(size[0])]
previous = [[0]*size[1] for col in range(size[0])]

image = pygame.Surface(size)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
        
    if any(pygame.mouse.get_pressed()):
        mouse_pos = pygame.mouse.get_pos()
        previous[mouse_pos[0]][mouse_pos[1]] = 500

    pixelArray = pygame.PixelArray(image)
    for i in range(1,size[0]-1):
        for j in range(1,size[1]-1):
            current[i][j] = (
                previous[i-1][j] + 
                previous[i+1][j] +
                previous[i][j-1] + 
                previous[i][j+1]) / 2 - current[i][j]
            current[i][j] *= dampening
            val = 255-min(255, max(0, round(current[i][j])))
            pixelArray[i, j] = (val, val, val)
    pixelArray.close()

    previous, current = current, previous

    window.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()     