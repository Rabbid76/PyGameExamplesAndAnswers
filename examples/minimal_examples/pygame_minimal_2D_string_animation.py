# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Simple physics string
# https://stackoverflow.com/questions/41862541/simple-physics-string/67749043#67749043
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Particles
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame

pygame.init()
window = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

class Node():
    def __init__(self, position, mass, initial_velocity):
        self.position = pygame.math.Vector2(position)
        self.mass = mass
        self.velocity = pygame.math.Vector2(initial_velocity)

class String():
    def __init__(self, nodes, gravity = .981, spring_constant = 10):
        self.nodes = nodes[:]
        self.gravity = gravity
        self.spring_constant = spring_constant
        self.set_distance = 1

    def calculateForces(self):
        for i in range(1, len(self.nodes), 1):
            n1, n0 = self.nodes[i], self.nodes[i - 1]
            distance = n1.position.distance_to(n0.position)
            force = -self.spring_constant * (distance - self.set_distance) / n1.mass
            n_dist_v = (n1.position - n0.position) / distance * force
            n1.velocity = 0.71 * n1.velocity + n_dist_v + pygame.math.Vector2(0, self.gravity)
        for i in range(1, len(self.nodes), 1):
            self.nodes[i].position += self.nodes[i].velocity

    def draw(self, surf):
        pygame.draw.aalines(surf, [0, 0, 0], False, [node.position for node in self.nodes])

def createString():
    return String([Node([150 + i * 10, 100], 120, [0, 1]) for i in range(25)])
string = String([Node([150 + i * 10, 100], 120, [0, 1]) for i in range(25)])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            string = createString()

    string.calculateForces()
    window.fill([255, 255, 255])
    string.draw(window)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()