# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Time - Counter based on timer event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md
#
# https://replit.com/@Rabbid76/PyGame-TimerCallback

import pygame

class Timer:
    def __init__(self, timer_id, timer_interval, callback_function):
        self.timer_id = timer_id
        self.timer_interval = timer_interval
        self.callback_function = callback_function
        pygame.time.set_timer(self.timer_id, self.timer_interval)

    def validate(self, event_list):
        if self.timer_id in [event.type for event in event_list]:
            self.callback_function()

class CounterText(pygame.sprite.Sprite):
    def __init__(self, pos, font):
        super().__init__()
        self.counter = 0
        self.pos = pos
        self.font = font
        self.updateImage()
    
    def updateImage(self):
        self.image = self.font .render(str(self.counter), True, (255, 255, 255))
        self.rect = self.image.get_rect(center = self.pos)

    def increment(self, value):
        self.counter += value
        self.updateImage()

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
font150 = pygame.font.SysFont(None, 150)

counter_sprite = CounterText(window.get_rect().center, font150)
all_sprites = pygame.sprite.Group(counter_sprite)
timer = Timer(pygame.USEREVENT, 1000, lambda : counter_sprite.increment(1))

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
    timer.validate(event_list)

    window.fill(0)   
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()