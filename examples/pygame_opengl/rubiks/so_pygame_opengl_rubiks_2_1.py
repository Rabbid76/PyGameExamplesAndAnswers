# OpenGL Rubik's Cube colors not displaying correctly when turning
# https://stackoverflow.com/questions/56729403/opengl-rubiks-cube-colors-not-displaying-correctly-when-turning

import pygame
from pygame.locals import *

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *

class Piece:
  
    def __init__(self, x, y, z, position):
        self.x = x
        self.y = y
        self.z = z
        self.len = 0.5
        self.v = [(-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1), (-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1)]
        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6),
                      (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
        self.surfaces = [(0, 1, 2, 3), (5, 4, 7, 6), (4, 0, 3, 7), (1, 5, 6, 2),
                         (4, 5, 1, 0), (3, 2, 6, 7)]
        self.colors = [ 
            (0, 0, 1),     # blue
            (0, 1, 0),     # green
            (1, 0.5, 0.1), # orange
            (1, 0, 0),     # red
            (1, 1, 0),     # yellow
            (1, 1, 1)]     # white
        self.matrix = position

    def lr(self, dir):
        color_ind = []
        if dir == -1:
            color_ind = [4, 5, 2, 3, 1, 0]
        else:
            color_ind = [5, 4, 2, 3, 0, 1]
        new_colors = []
        for i in color_ind:
            new_colors.append(self.colors[i])
        self.colors = new_colors

    def ud(self, dir):
        color_ind = []
        if dir == -1:
            color_ind = [2, 3, 1, 0, 4, 5]
        else:
            color_ind = [3, 2, 0, 1, 4, 5]
        new_colors = []
        for i in color_ind:
            new_colors.append(self.colors[i])
        self.colors = new_colors

    def update(self, x, y, z):
        self.matrix = np.matrix([[x, 0, 0], [0, y, 0], [0, 0, z]])
        print(self.matrix)
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        glEnable(GL_DEPTH_TEST)

        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)

        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glScalef(self.len, self.len, self.len)

        glLineWidth(5)
        glColor3fv((0, 0, 0))
        glBegin(GL_LINES)
        for e in self.edges:
            glVertex3fv(self.v[e[0]])
            glVertex3fv(self.v[e[1]])
        glEnd()

        glBegin(GL_QUADS)
        for i in range(len(self.surfaces)):
            glColor3fv(self.colors[i])
            for j in self.surfaces[i]:
                glVertex3fv(self.v[j])
        glEnd()

        glPopMatrix()


dim = 3
cube = []

for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            matrix = np.matrix([[x, 0, 0], [0, y, 0], [0, 0, z]])
            cube.append(Piece(x, y, z, matrix))

def turn_x(layer, direction):
    trans_matrix = np.matrix([[0, 1*direction], [-1*direction, 0]])
    for i in range(len(cube)):
        block = cube[i]
        if block.x == layer:
            new_point = trans_matrix * np.matrix([[block.y], [block.z]])
            block.update(block.x, new_point.item(0), new_point.item(1))
            #block.update(block.x, block.z*direction, -block.y*direction)
            block.lr(direction)


def turn_y(layer, direction):
    trans_matrix = np.matrix([[0, 1*direction], [-1*direction, 0]])
    for i in range(len(cube)):
        block = cube[i]
        if block.y == layer:
            new_point = trans_matrix * np.matrix([[block.x], [block.z]])
            block.update(new_point.item(0), block.y, new_point.item(1))
            #block.update(block.z*direction, block.y, -block.x*direction)
            block.ud(direction)

def main():
    pygame.init()
    display = (400, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50)

    angle_x = 0
    angle_y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    turn_x(1, 1)
                if event.key == pygame.K_4:
                    turn_x(1, -1)
                if event.key == pygame.K_5:
                    turn_y(1, 1)
                if event.key == pygame.K_6:
                    turn_y(1, -1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            angle_y += 5
        if keys[pygame.K_DOWN]:
            angle_y -= 5
        if keys[pygame.K_RIGHT]:
            angle_x += 5
        if keys[pygame.K_LEFT]:
            angle_x -= 5

        glClearColor(0.6, 0.6, 0.6, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10)
        glRotatef(45, 1, 1, 0)

        glRotatef(angle_y, -1, 0, 0)
        glRotatef(angle_x, 0, 1, 0)

        for c in cube:
            c.draw()
        pygame.display.flip()
        pygame.time.wait(10)

main()