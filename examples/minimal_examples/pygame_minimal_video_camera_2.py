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
import pygame.camera

pygame.init()
pygame.camera.init()

camera_list = pygame.camera.list_cameras()
camera = pygame.camera.Camera(camera_list[0])

window = pygame.display.set_mode(camera.get_size())
clock = pygame.time.Clock()
camera.start()

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    camera_frame = camera.get_image()

    window.fill(0)
    window.blit(camera_frame, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()