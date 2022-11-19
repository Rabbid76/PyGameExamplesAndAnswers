# How to load and play a video in pygame
# https://stackoverflow.com/questions/21356439/how-to-load-and-play-a-video-in-pygame/69054207#69054207
# 
# How to play video in Pygame currently?
# https://stackoverflow.com/questions/62870381/how-to-play-video-in-pygame-currently
# 
# GitHub - PyGameExamplesAndAnswers - Camera and Video
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_camera_and_video.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

import pygame
import moviepy.editor

pygame.init()
video = moviepy.editor.VideoFileClip("video/sample-mp4-file.mp4")
#video = moviepy.editor.VideoFileClip(r"C:\data\Google Drive\video\20200806_101707.mp4")
#video = moviepy.editor.VideoFileClip(r"C:\data\Video\Zeichentrick\Rabbids\Rabbids.Invasion.S01E01.Omelet.Party.-.Rabbid.Mollusk.-.Rabbid.Are.You.There.WEBRip.x264.AAC.mp4")

video.preview()

pygame.quit()