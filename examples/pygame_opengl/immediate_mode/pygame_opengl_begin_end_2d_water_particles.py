# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Converting pygame 2d water ripple to pyOpenGL
# https://stackoverflow.com/questions/63732713/converting-pygame-2d-water-ripple-to-pyopengl/63744177#63744177
#
# pygame pyopengl texture a changing polygon with many sides
# https://stackoverflow.com/questions/63745181/pygame-pyopengl-texture-a-changing-polygon-with-many-sides/63746178#63746178
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL import *
from OpenGL.GL import *

def draw_polygon(surf_rect, polygon_points):
    #glBegin(GL_LINE_STRIP)
    glBegin(GL_TRIANGLE_STRIP)
    for pt in polygon_points:
        glVertex2f(*pt)
        glVertex2f(pt[0], surf_rect.height)
    glEnd()
    
class WaterParticle():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.target_y = y
        self.velocity = 0
        self.k = 0.04  
        self.d = 0.08
    def update(self):
        x = self.y - self.target_y
        a = -(self.k * x + self.d * self.velocity)
        #self.p[1] += -0.1 if x > 0 else 0.1 if x < 0 else 0
        self.y += self.velocity
        self.velocity += a

class Water():
    def __init__(self, x_start, x_end, y_start, segment_length, passes, spread):
        n = abs(x_end - x_start + segment_length - 1) // segment_length + 1
        self.particles = [WaterParticle(i * segment_length + x_start, y_start) for i in range(n)]
        self.passes = passes
        self.spread = spread

    def update(self):
        for particle in self.particles:
            particle.update() 

        left_deltas = [0] * len(self.particles)
        right_deltas = [0] * len(self.particles)
        for _ in range(self.passes):  
            for i in range(len(self.particles)):
                if i > 0:  
                    left_deltas[i] = self.spread * (self.particles[i].y - self.particles[i - 1].y)
                    self.particles[i - 1].velocity += left_deltas[i]
                if i < len(self.particles)-1:
                    right_deltas[i] = self.spread * (self.particles[i].y - self.particles[i + 1].y)
                    self.particles[i + 1].velocity += right_deltas[i]
            for i in range(len(self.particles)):
                if i > 0:
                    self.particles[i-1].y += left_deltas[i]
                if i < len(self.particles) - 1:
                    self.particles[i+1].y += right_deltas[i]
 
    def splash(self, index, speed):
        if index > 0 and index < len(self.particles):
            self.particles[index].velocity += speed
                
    def draw(self, surf_rect):
        polygon_points = []
        for spring in range(len(self.particles)):
            polygon_points.append((self.particles[spring].x, self.particles[spring].y))
        glColor3f(0, 0, 1)
        draw_polygon(surf_rect, polygon_points)
        
pygame.init()
window = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, *window.get_size(), 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glClearColor(1, 1, 1, 1)

water_line_y = window.get_height() // 2
water = Water(0, window.get_width(), window.get_height() // 2, 3, 8, 0.025)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            velocity = water_line_y - event.pos[1]
            if velocity > 0:
                index = int(len(water.particles) * event.pos[0] / window.get_width())
                water.splash(index, velocity)
    
    water.update()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    water.draw(window.get_rect())
    pygame.display.flip()
    clock.tick(50)