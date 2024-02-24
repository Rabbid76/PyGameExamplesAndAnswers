# Rendering Images At a Different Framerate Than The Game Window
# https://stackoverflow.com/questions/75712024/rendering-images-at-a-different-framerate-than-the-game-window/75712065#75712065
#
# GitHub - Time, timer event and clock
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

explosion = []
for i in range(10):
    e = pygame.Surface((100, 100), pygame.SRCALPHA)
    pygame.draw.circle(e, (200 - i * 10, 200 - i * 20, 0), (50, 50), i*5)
    explosion.append(e)	

clock = pygame.time.Clock() 
animate_frames = 10
animations = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            animations.append([event.pos, 0])

    window.fill('#000000')
    for animation in animations[:]:
        animation[1] += 1
        frame_index = animation[1] // animate_frames
        if frame_index < len(explosion):
            frame = explosion[frame_index]
            framerect = frame.get_rect(center=animation[0])
            window.blit(frame, framerect)
        else:
            animations.remove(animation)
        
    pygame.display.update()
    clock.tick(100)

pygame.quit()
exit()
