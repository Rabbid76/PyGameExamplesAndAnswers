# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# Spawning multiple instances of the same object concurrently in python
# https://stackoverflow.com/questions/62112754/spawning-multiple-instances-of-the-same-object-concurrently-in-python/62112894#62112894
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Triggered by a time interval
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md
#
# https://replit.com/@Rabbid76/PyGame-TimerEventSpawn

import pygame, random
pygame.init()
window = pygame.display.set_mode((300, 300))

class Object:
    def __init__(self):
        self.radius = 50
        self.x = random.randrange(self.radius, window.get_width()-self.radius)
        self.y = random.randrange(self.radius, window.get_height()-self.radius)
        self.color = pygame.Color(0)
        self.color.hsla = (random.randrange(0, 360), 100, 50, 100)

object_list = []
time_interval = 200 # 200 milliseconds == 0.2 seconds
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_interval)

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event:
            object_list.append(Object())
    
    window.fill(0)
    for object in object_list[:]:
        pygame.draw.circle(window, object.color, (object.x, object.y), round(object.radius))
        object.radius -= 0.2
        if object.radius < 1:
            object_list.remove(object)
    pygame.display.flip()

pygame.quit()
exit()
