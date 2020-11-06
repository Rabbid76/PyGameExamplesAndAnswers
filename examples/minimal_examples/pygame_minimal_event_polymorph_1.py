# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# Pygame: how to write event-loop polymorphically
# https://stackoverflow.com/questions/60406647/pygame-how-to-write-event-loop-polymorphically/60408967#60408967
#
# GitHub - Event and application loop - Event loop - Polymorphic event loop
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_event_and_application_loop.md

import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

class EventHandler():
    targets = {}
    @staticmethod
    def add(type, event):
        EventHandler.targets.setdefault(type, []).append(event)    
    @staticmethod
    def notify(event):  
        if event.type in EventHandler.targets:
            for target in EventHandler.targets[event.type]:
                target.determine_event(event)
    @staticmethod
    def determine_event(event): pass

class Exit(EventHandler):
    @staticmethod
    def determine_event(event):
        pygame.quit()
        exit()

class KeydownPrint(EventHandler):
    @staticmethod
    def determine_event(event):
        print("Key pressed: " + pygame.key.name(event.key))

class KeydownAction(EventHandler):
    @staticmethod
    def determine_event(event):
        global count
        count += 1

EventHandler.add(pygame.QUIT, Exit)
EventHandler.add(pygame.KEYDOWN, KeydownPrint)
EventHandler.add(pygame.KEYDOWN, KeydownAction)

count = 0
font50 = pygame.font.SysFont(None, 50)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        EventHandler.notify(event)

    text_surface = font50.render(str(count), True, (255, 255, 255))
    window.fill(0)
    window.blit(text_surface, text_surface.get_rect(center = window.get_rect().center))
    pygame.display.flip()