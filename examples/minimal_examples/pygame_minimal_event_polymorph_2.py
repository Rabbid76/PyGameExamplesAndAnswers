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

class EventHandler:
    targets = {}
    def register(type):
        def decorator(fn):
            EventHandler.targets.setdefault(type, []).append(fn)  
        return decorator
    def notify(event):
        fnl =  EventHandler.targets[event.type] if event.type in EventHandler.targets else []  
        for fn in fnl: 
          fn(event)

@EventHandler.register(pygame.QUIT)
def onExit(event):
    pygame.quit()
    exit()

@EventHandler.register(pygame.KEYDOWN)
def keydownPrint(event):
    print("Key pressed: " + pygame.key.name(event.key))

@EventHandler.register(pygame.KEYDOWN)
def keydownAction(event):
    global count
    count += 1

count = 0
font50 = pygame.font.SysFont(None, 50)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        EventHandler.notify(event)

    text_surface = font50.render(str(count), True, (255, 255, 255))
    window.fill('black')
    window.blit(text_surface, text_surface.get_rect(center = window.get_rect().center))
    pygame.display.flip()