# How to open camera with pygame in Windows?
# https://stackoverflow.com/questions/29673348/how-to-open-camera-with-pygame-in-windows
#
# blit opencv camera capture with pygame throws TypeError: argument 1 must be pygame.Surface, not cv2.VideoCapture
# https://stackoverflow.com/questions/74077114/blit-opencv-camera-capture-with-pygame-throws-typeerror-argument-1-must-be-pyga/74077144#74077144
# 
# python pygame.camera.init() NO vidcapture
# https://stackoverflow.com/questions/16266244/python-pygame-camera-init-no-vidcapture/69053911#69053911
# 
# GitHub - PyGameExamplesAndAnswers - Camera and Video
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_camera_and_video.md

import pygame
import cv2

capture = cv2.VideoCapture(0)
success, camera_image = capture.read()

window = pygame.display.set_mode(camera_image.shape[1::-1])
clock = pygame.time.Clock()

run = success
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    success, camera_image = capture.read()
    if success:
        camera_surf = pygame.image.frombuffer(camera_image.tobytes(), camera_image.shape[1::-1], "BGR")
    else:
        run = False
    window.blit(camera_surf, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()