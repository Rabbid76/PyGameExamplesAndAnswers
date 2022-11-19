# pygame.math.Vector3 object
# https://www.pygame.org/docs/ref/math.html
#
# How to rotate a square around x-axis in a 3D space
# https://stackoverflow.com/questions/63651594/how-to-rotate-a-square-around-x-axis-in-a-3d-space/63654537#63654537
#
# GitHub - PyGameExamplesAndAnswers - Draw 3D
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_3D.md

import pygame, math
pygame.init()

class Mat3:
    def new_rotate_x(theta):
        s = math.sin(theta)
        c = math.cos(theta)
        return Mat3([[1, 0, 0], [0, c,  s], [0, -s, c]])
    def __init__(self, m = None):
        self.matrix = m if m else [[int(i==j) for i in range(3)] for j in range(3)]
    def __getitem__(self, i):
        return self.matrix[i]

class Vec2:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __getitem__(self, i):
        return [self.x, self.y][i]

class Vec3:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def __add__(a, b):
        return Vec3(a.x+b.x, a.y+b.y, a.z+b.z)
    def __getitem__(self, i):
        return [self.x, self.y, self.z][i]
    def dot(self, v):
        return sum(a*b for a, b in zip(self, v))

def multMat3Vec3(m, v):
    return Vec3(*[v.dot(column) for column in m])

def project(v, w, h):
    z_i = 1 / (0.001 if v.z == 0 else v.z)
    x_p = (v.x*z_i + 1) * w/2
    y_p = (v.y*z_i + 1) * h/2
    return Vec2(x_p, y_p)

window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

s = 1
modelPoints = [Vec3(-s, -s, -s), Vec3(s, -s, -s), Vec3(s, s, -s), Vec3(-s, s, -s)]
transVec = Vec3(0, 0, -4)
theta = 0

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rot_mat = Mat3.new_rotate_x(theta)
    theta -= math.pi / 180

    points = [multMat3Vec3(rot_mat, pt) for pt in modelPoints]
    points = [pt + transVec for pt in points]
    points = [project(pt, window.get_width(), window.get_height()) for pt in points]
    points = [(round(pt.x), round(pt.y)) for pt in points]
    
    window.fill((255, 255, 255))
    pygame.draw.lines(window, (0, 0, 0), True, points)
    pygame.display.flip()
    
pygame.quit()
exit()