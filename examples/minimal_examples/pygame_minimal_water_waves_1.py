# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How can I connect two points with a series of circles?
# https://stackoverflow.com/questions/73838853/how-can-i-connect-two-points-with-a-series-of-circles/73839646#73839646
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Bezier
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

from random import randint
import pygame

class Node:
    def __init__(self, x, y, force, k, v):
        self.x = x
        self.y = y
        self.y0 = y
        self.force = force
        self.k = k
        self.v = v
        self.direction = 1

    def oscillate(self):
        self.y += self.v * self.direction
        if self.y0 - self.force / self.k > self.y or self.y0 + self.force / self.k < self.y:
            self.direction *= -1

    def draw(self, surf):
        pygame.draw.circle(surf, "black", (self.x, self.y), 3)

window = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

width, height = window.get_size()  
no_of_nodes = 25  
dx = width / no_of_nodes
nodes = [Node(i*dx, height//2, randint(15, 30), 1, 0.5) for i in range(no_of_nodes+1)]

def ptOnCurve(b, t):
    q = b.copy()
    for k in range(1, len(b)):
        for i in range(len(b) - k):
            q[i] = (1-t) * q[i][0] + t * q[i+1][0], (1-t) * q[i][1] + t * q[i+1][1]
    return round(q[0][0]), round(q[0][1])

def bezier(b, samples):
    return [ptOnCurve(b, i/samples) for i in range(samples+1)]

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for molecule in nodes:
        molecule.oscillate()

    ts = []
    for i in range(len(nodes)):
        pa = nodes[max(0, i-1)]
        pb = nodes[min(len(nodes)-1, i+1)]
        ts.append((pb.y-pa.y) / (pb.x-pa.x))

    pts = [(width, height), (0, height)]
    for i in range(len(nodes)-1):
        p0 = nodes[i].x, nodes[i].y
        p3 = nodes[i+1].x, nodes[i+1].y
        p1 = p0[0] + 10, p0[1] + 10 * ts[i]
        p2 = p3[0] - 10, p3[1] - 10 * ts[i+1]
        pts += bezier([p0, p1, p2, p3], 4)

    window.fill("white")
    pygame.draw.polygon(window, 'aqua', pts)
    for molecule in nodes:
        molecule.draw(window)
    pygame.display.flip()

pygame.quit()
exit()