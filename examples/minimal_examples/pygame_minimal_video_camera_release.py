# hard lag when webcam is release
# https://stackoverflow.com/questions/74215542/hard-lag-when-webcam-is-release/74217826#74217826
# 
# GitHub - PyGameExamplesAndAnswers - Camera and Video
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_camera_and_video.md

import pygame
import cv2
import threading

camera = cv2.VideoCapture(0)
success, camera_image = camera.read()
recording = True
def camera_release():
    camera.release()
release_thread = threading.Thread(target=camera_release)

pygame.init()
window = pygame.display.set_mode(camera_image.shape[1::-1])
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
off_text = font.render("recording off", True, (255, 255, 0))

run = success
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            recording = False
            release_thread.start()
    
    if recording:
        success, camera_image = camera.read()
        if success:
            camera_surf = pygame.image.frombuffer(camera_image.tobytes(), camera_image.shape[1::-1], "BGR")
    window.blit(camera_surf, (0, 0))
    if not recording:
        window.blit(off_text, off_text.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()