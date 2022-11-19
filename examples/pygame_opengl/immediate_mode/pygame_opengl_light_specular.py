# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# How to make specular lighting on python to implement the Phong lighting?
# https://stackoverflow.com/questions/67544996/how-to-make-specular-lighting-on-python-to-implement-the-phong-lighting/67545182#67545182
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Light
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *

vertex_shader = """
varying vec3 vN;
varying vec3 v;
varying vec4 color;
void main(void)  
{     
   v = vec3(gl_ModelViewMatrix * gl_Vertex);       
   vN = normalize(gl_NormalMatrix * gl_Normal);
   color = gl_Color;
   gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;  
}
"""

fragment_shader = """
varying vec3 vN;
varying vec3 v; 
varying vec4 color;
#define MAX_LIGHTS 1 
void main (void) 
{ 
   vec3 N = normalize(vN);
   vec4 finalColor = vec4(0.0, 0.0, 0.0, 0.0);
   
   for (int i=0;i<MAX_LIGHTS;i++)
   {
      vec3 L = normalize(gl_LightSource[i].position.xyz - v); 
      vec3 E = normalize(-v); // we are in Eye Coordinates, so EyePos is (0,0,0) 
      vec3 R = normalize(-reflect(L,N)); 
   
      vec4 Iamb = gl_LightSource[i].ambient; 
      vec4 Idiff = gl_LightSource[i].diffuse * max(dot(N,L), 0.0);
      Idiff = clamp(Idiff, 0.0, 1.0); 
      vec4 Ispec = gl_LightSource[i].specular * pow(max(dot(R,E),0.0),0.3*gl_FrontMaterial.shininess);
      Ispec = clamp(Ispec, 0.0, 1.0); 
   
      finalColor += Iamb + Idiff + Ispec;
   }
   gl_FragColor = color * finalColor; 
}
"""

verticies = (
    (0, - 0, 1.15894198417663574),
    (0.63384598493576048, -0.63384598493576048, 0.63384598493576048),
    (0.81949597597122192, 0, 0.81949597597122192),
    (1.15894198417663574, 0, -0),
    (0.81949597597122192, 0.81949597597122192, -0),
    (0.81949597597122192, 0, -0.81949597597122192),
    (0.63384598493576048, 0.63384598493576048, 0.63384598493576048),
    (0.81949597597122192, -0.81949597597122192, 0),
    (-0, 0.81949597597122192, 0.81949597597122192),
    (-0.81949597597122192, 0, 0.81949597597122192),
    (0.63384598493576048, 0.63384598493576048, -0.63384598493576048),
    (0, 0, -1.15894198417663574),
    (0, -0.81949597597122192, -0.81949597597122192),
    (-0.81949597597122192, 0, -0.81949597597122192),
    (0, 0.81949597597122192, -0.81949597597122192),
    (0.63384598493576048, -0.63384598493576048, -0.63384598493576048),
    (-0, 1.15894198417663574, 0),
    (-0.81949597597122192, 0.81949597597122192, 0),
    (-1.15894198417663574, 0, 0),
    (-0.63384598493576048, 0.63384598493576048, 0.63384598493576048),
    (0, -1.15894198417663574, 0),
    (-0.81949597597122192, -0.81949597597122192, 0),
    (0, -0.81949597597122192, 0.81949597597122192),
    (-0.63384598493576048, -0.63384598493576048, 0.63384598493576048),
    (-0.63384598493576048, 0.63384598493576048, -0.63384598493576048),
    (-0.63384598493576048, -0.63384598493576048, -0.63384598493576048),
)

surfaces = (
    (20, 21, 25, 12), (21, 25, 13, 18), (17, 24, 14, 16), (18, 13, 24, 17),
    (16, 14, 10, 4), (3, 5, 15, 7), (0, 2, 6, 8), (0, 2, 1, 22),
    (0, 22, 23, 9), (0, 9, 19, 8), (13, 11, 12, 25), (11, 13, 24, 14),
    (11, 14, 10, 5), (11, 5, 15, 12), (3, 5, 10, 4), (17, 18, 9, 19),
    (17, 19, 8, 16), (16, 8, 6, 4), (3, 2, 6, 4), (3, 2, 1, 7),
    (7, 1, 22, 20), (20, 21, 23, 22), (9, 23, 21, 18), (15, 7, 20, 12),
)

normals = [
    (-0.35740624923526854, -0.8628558767968414, -0.3574080425574267),
    (-0.8628548655932644, -0.3574083665235253, -0.3574083665235253),
    (-0.3574083665235253, 0.8628548655932644, -0.3574083665235253),
    (-0.8628558767968414, 0.3574080425574267, -0.35740624923526854),
    (0.3574080425574267, 0.8628558767968414, -0.35740624923526854),
    (0.8628558767968414, -0.3574080425574267, -0.35740624923526854),
    (0.35740624923526854, 0.3574080425574267, 0.8628558767968414),
    (0.35740624923526854, -0.3574080425574267, 0.8628558767968414),
    (-0.3574080425574267, -0.35740624923526854, 0.8628558767968414),
    (-0.35740624923526854, 0.3574080425574267, 0.8628558767968414),
    (-0.35740647831364963, -0.35740647831364963, -0.8628564298415289),
    (-0.35740624923526854, 0.3574080425574267, -0.8628558767968414),
    (0.3574080425574267, 0.35740624923526854, -0.8628558767968414),
    (0.35740624923526854, -0.3574080425574267, -0.8628558767968414),
    (0.8628558767968414, 0.3574080425574267, -0.35740624923526854),
    (-0.8628564298415289, 0.35740647831364963, 0.35740647831364963),
    (-0.3574083665235253, 0.8628548655932644, 0.3574083665235253),
    (0.3574080425574267, 0.8628558767968414, 0.35740624923526854),
    (0.8628558767968414, 0.3574080425574267, 0.35740624923526854),
    (0.8628558767968414, -0.3574080425574267, 0.35740624923526854),
    (0.3574083665235253, -0.8628548655932644, 0.3574083665235253),
    (-0.35740624923526854, -0.8628558767968414, 0.3574080425574267),
    (-0.8628548655932644, -0.3574083665235253, 0.3574083665235253),
    (0.35740624923526854, -0.8628558767968414, -0.3574080425574267)
]

colors = (
    (1,1,1), (0,1,0), (0,0,1), (0,1,0), (0,0,1),
    (1,0,1), (0,1,0), (1,0,1), (0,1,0), (0,0,1),
)

edges = (
    (16, 17), (17, 18), (18, 21), (20, 21), (3, 4), (4, 16), (7, 3), (20, 7),
    (0, 2), (0, 9), (0, 22), (0, 8), (11, 13), (11, 12), (11, 14), (2, 3),
    (8, 16), (9, 18), (22, 20), (2, 1), (1, 22), (1, 7), (5, 11), (5, 15),
    (15, 12), (15, 7), (5, 3), (12, 20), (16, 14), (22, 23), (23, 9), (23, 21),
    (13, 24), (14, 24), (17, 24), (13, 25), (12, 25), (25, 21), (13, 18), (8, 6),
    (2, 6), (6, 4), (10, 4), (14, 10), (5, 10), (17, 19), (19, 9), (19, 8),
)

def shape(program):
    glEnable(GL_POLYGON_OFFSET_FILL)
    glPolygonOffset(1.0, 1.0)
    glEnable(GL_LIGHTING)  

    glUseProgram(program)
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(surfaces):
        glColor3fv(colors[i_surface % len(colors)])
        glNormal3fv(normals[i_surface])
        for vertex in surface:
            glVertex3fv(verticies[vertex])
    glEnd()

    glDisable(GL_LIGHTING)
    glDisable(GL_POLYGON_OFFSET_FILL)

    glUseProgram(0)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    window = pygame.display.set_mode((400, 300), pygame.DOUBLEBUF | pygame.OPENGL)
    w, h = window.get_size()
    clock = pygame.time.Clock()

    program = compileProgram( 
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, w/h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)

    glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0.4))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0, 0.5, 0.1, 0))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    #glColorMaterial(GL_FRONT_AND_BACK, GL_SPECULAR)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1,1,1,0))
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128)
    glEnable(GL_DEPTH_TEST)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glRotatef(5, 0, 1, 0)
        elif keys[pygame.K_RIGHT]:
            glRotatef(-5, 0, 1, 0)
        elif keys[pygame.K_UP]:
            glRotatef(5, 1, 0, 0)
        elif keys[pygame.K_DOWN]:
            glRotatef(-5, 1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        shape(program)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
    exit()
