# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# How to display an image after a time interval?
# https://stackoverflow.com/questions/45609076/how-to-display-an-image-after-a-time-interval/63761611#63761611
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Time - Until a certain time
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md
#
# https://replit.com/@Rabbid76/PyGame-TimerAfterACertainTime

import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

#image = pygame.image.load('pic.png')
image = pygame.Surface((100, 100))
image.fill((255, 255, 255))
image_time = 0

run = True
while run:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            image_time = current_time + 1000 # 1000 milliseconds == 3 seconds

    screen.fill(0)

    if image_time > 0 and current_time >= image_time:
        screen.blit(image, image.get_rect(center = screen.get_rect().center))
    else:
        pygame.draw.rect(screen, (255, 255, 255), image.get_rect(center = screen.get_rect().center), 1)

    pygame.display.flip()

pygame.quit()
exit()