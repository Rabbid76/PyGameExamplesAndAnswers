# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How to draw bubbles and turn them animated into circles
# https://stackoverflow.com/questions/73055748/how-to-draw-bubbles-and-turn-them-animated-into-circles/73128299#73128299
#
# GitHub - PyGameExamplesAndAnswers - Paint
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_paint.md

import pygame, random

class Bubble:
    def __init__(self, start):
        self.color = pygame.Color(0)
        self.color.hsla = (random.randrange(0, 360), 100, 50, 100)
        self.points = [list(start)]
        self.closed = False
        self.finished = False
    def add_point(self, point, close):
        self.points.append(list(point))
        self.closed = close
        if self.closed:
            x_, y_ = list(zip(*self.points))
            x0, y0, x1, y1 = min(x_), min(y_), max(x_), max(y_)
            rect = pygame.Rect(x0, y0, x1-x0, y1-y0)
            self.center = rect.center
            self.radius = max(*rect.size) // 2
    def animate(self):
        if self.closed and not self.finished:
            cpt = pygame.math.Vector2(self.center) + (0.5, 0.5)
            self.finished = True
            for i, p in enumerate(self.points):
                pt = pygame.math.Vector2(p)
                v = pt - cpt
                l = v.magnitude()
                if l + 0.5 < self.radius:
                    self.finished = False
                v.scale_to_length(min(self.radius, l+0.5))
                pt = cpt + v
                self.points[i] = [pt.x, pt.y]
                
    def draw(self, surf):
        if self.finished:
            pygame.draw.circle(surf, self.color, self.center, self.radius, 3)
        elif len(self.points) > 1:
            pygame.draw.lines(surf, self.color, self.closed, self.points, 3)

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
bubbles = []
pressed = False
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            bubbles.append(Bubble(event.pos))
            pressed = True

        elif event.type == pygame.MOUSEMOTION and pressed:
            bubbles[-1].add_point(event.pos, False)
            
        elif event.type == pygame.MOUSEBUTTONUP:
            bubbles[-1].add_point(event.pos, True)
            pressed = False

    for bubble in bubbles:
        bubble.animate()

    window.fill((32, 32, 64))
    for bubble in bubbles:
        bubble.draw(window)
    pygame.display.update()

pygame.quit()
exit()