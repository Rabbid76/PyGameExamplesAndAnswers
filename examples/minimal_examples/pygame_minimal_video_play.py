# How to be efficient with MoviePy
# https://stackoverflow.com/questions/21356439/how-to-load-and-play-a-video-in-pygame/69054207#69054207 
#
# How to load and play a video in pygame
# https://stackoverflow.com/questions/21356439/how-to-load-and-play-a-video-in-pygame/69054207#69054207
# 
# GitHub - PyGameExamplesAndAnswers - Camera and Video
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_camera_and_video.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

import pygame
import cv2

video = cv2.VideoCapture("video/sample-mp4-file.mp4")
#video = cv2.VideoCapture(r"C:\data\Google Drive\video\20200806_101707.mp4")
#video = cv2.VideoCapture(r"C:\data\Video\Zeichentrick\Rabbids\Rabbids.Invasion.S01E01.Omelet.Party.-.Rabbid.Mollusk.-.Rabbid.Are.You.There.WEBRip.x264.AAC.mp4")
success, video_image = video.read()
fps = video.get(cv2.CAP_PROP_FPS)

window = pygame.display.set_mode(video_image.shape[1::-1])
clock = pygame.time.Clock()

run = success
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    success, video_image = video.read()
    if success:
        video_surf = pygame.image.frombuffer(
            video_image.tobytes(), video_image.shape[1::-1], "BGR")
    else:
        run = False
    window.blit(video_surf, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()
