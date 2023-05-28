# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Remove border from opencv generated ellipse in pygame
# https://stackoverflow.com/questions/75720083/remove-border-from-opencv-generated-ellipse-in-pygame/75724348#75724348
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw arc
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame
import cv2
import numpy as np

pygame.init()
window = pygame.display.set_mode((400, 400))

def drawAACircle(surf, color, center, radius, width, angle):
    circle_image = np.zeros((radius*2, radius*2, 4), dtype = np.uint8)
    circle_image = cv2.ellipse(circle_image, (radius, radius), (radius-width, radius-width), (angle*-.5)-90 , 0, angle, (*color, 255), width, lineType=cv2.LINE_AA)  
    circle_surf = pygame.image.frombuffer(circle_image.tobytes(), circle_image.shape[1::-1], "RGBA")
    pos = (center[0]-radius, center[1]-radius)
    
    surf.blit(circle_surf, pos, special_flags=pygame.BLEND_PREMULTIPLIED)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill('black')
    #window.fill('white')
    drawAACircle(window, (255, 255, 255), window.get_rect().center, 150, 20, 360)
    pygame.display.flip()

pygame.quit()
quit()