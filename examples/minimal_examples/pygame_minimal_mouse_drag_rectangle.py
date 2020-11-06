# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# Dragging object along x-axis in pygame
# https://stackoverflow.com/questions/61781533/dragging-object-along-x-axis-in-pygame/61781683#61781683)
#
# How to drag an object around the screen in pygame?
# https://stackoverflow.com/questions/64241742/how-to-drag-an-object-around-the-screen-in-pygame/64249660#64249660
#
# GitHub - Mouse - Mouse Drag
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_aygnd_mosuse_events.md

import pygame

class DragOperator:
    def __init__(self, rect):
        self.rect = rect
        self.dragging = False
        self.rel_pos = (0, 0)
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = self.rect.collidepoint(event.pos)
                self.rel_pos = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y
            if event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            if event.type == pygame.MOUSEMOTION and self.dragging:
                self.rect.topleft = event.pos[0] - self.rel_pos[0], event.pos[1] - self.rel_pos[1]

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

rectangle = pygame.Rect(0, 0, 40, 40)
rectangle.center = window.get_rect().center
drag_rectangle = DragOperator(rectangle)

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    drag_rectangle.update(event_list)
    rectangle_color = (0, 255, 0) if drag_rectangle.dragging else (255, 0, 0)

    window.fill(0)
    pygame.draw.rect(window, rectangle_color, rectangle)
    pygame.display.flip()

pygame.quit()
exit()