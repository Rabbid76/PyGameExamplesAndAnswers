# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Texture arrays in OpenGL
# https://stackoverflow.com/questions/64122446/texture-arrays-in-opengl/64124199#64124199
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL 4 - Mesh
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/moderngl_library/pygame_opengl_4.md

import os, math, ctypes
import glm
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.arrays import *
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resource'))

image_path = "icon"
image_names = ["Pear64.png", "Apple64.png", "Watermelon64.png", "Plums64.png", "Banana64.png", "Cherries64.png"]

glsl_vert = """
#version 450 core

layout (location = 0) in vec3 a_pos;
layout (location = 1) in vec3 a_nv;
layout (location = 2) in vec3 a_uv;

out vec3 v_pos;
out vec3 v_nv;
out vec3 v_uv;

uniform mat4 u_proj;
uniform mat4 u_view;
uniform mat4 u_model;

void main()
{
    mat4 model_view = u_view * u_model;
    mat3 normal     = transpose(inverse(mat3(model_view)));

    vec4 view_pos   = model_view * vec4(a_pos.xyz, 1.0);

    v_pos       = view_pos.xyz;
    v_nv        = normal * a_nv;  
    v_uv        = a_uv;  
    gl_Position = u_proj * view_pos;
}
"""

glsl_frag = """
#version 450 core

out vec4 frag_color;
in  vec3 v_pos;
in  vec3 v_nv;
in  vec3 v_uv;

layout (binding = 0) uniform sampler2DArray u_texture;

const vec3 sideColor[6] = vec3[6](
    vec3(1.0, 0.0, 0.0),
    vec3(0.0, 1.0, 0.0),
    vec3(0.0, 0.0, 1.0),
    vec3(1.0, 1.0, 0.0),
    vec3(1.0, 0.0, 1.0),
    vec3(0.0, 1.0, 1.0)
);

void main()
{
    vec3  N            = normalize(v_nv);
    vec3  V            = -normalize(v_pos);
    float ka           = 0.1;
    float kd           = max(0.0, dot(N, V)) * 0.9;
    vec4  textureColor = texture(u_texture, v_uv.xyz);
    vec3  color        = mix(sideColor[int(v_uv.z + 0.5)].rgb, textureColor.rgb, textureColor.a);
    frag_color         = vec4(color.rgb * (ka + kd), 1.0);
}
"""

pygame.init()

image_planes = [
    (GLubyte * 4)(255, 0, 0, 255), (GLubyte * 4)(0, 255, 0, 255), (GLubyte * 4)(0, 0, 255, 255),
    (GLubyte * 4)(255, 255, 0, 255), (GLubyte * 4)(0, 255, 255, 255), (GLubyte * 4)(255, 0, 255, 255)]
image_size = (1, 1)

for i, filename in enumerate(image_names):
    try:
        image = pygame.image.load(os.path.join(image_path, filename))
        image_size = image.get_size()
        image_planes[i] = pygame.image.tostring(image, 'RGBA')
    except:
        pass

class MyWindow:

    def __init__(self, w, h):
        self.__caption = 'OpenGL Window'
        self.__vp_size = [w, h]

        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)  
        self.__screen = pygame.display.set_mode(self.__vp_size, pygame.DOUBLEBUF| pygame.OPENGL)
        
        self.__program = compileProgram( 
            compileShader(glsl_vert, GL_VERTEX_SHADER),
            compileShader(glsl_frag, GL_FRAGMENT_SHADER),
        )
        self.___attrib = { a : glGetAttribLocation (self.__program, a) for a in ['a_pos', 'a_nv', 'a_uv'] }
        print(self.___attrib)
        self.___uniform = { u : glGetUniformLocation (self.__program, u) for u in ['u_model', 'u_view', 'u_proj'] }
        print(self.___uniform)

        v = [[-1,-1,1], [1,-1,1], [1,1,1], [-1,1,1], [-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]]
        n = [[0,0,1], [1,0,0], [0,0,-1], [-1,0,0], [0,1,0], [0,-1,0]]
        e = [[0,1,2,3], [1,5,6,2], [5,4,7,6], [4,0,3,7], [3,2,6,7], [1,0,4,5]]
        t = [[0, 0], [1, 0], [1, 1], [0, 1]]
        index_array = [si*4+[0, 1, 2, 0, 2, 3][vi] for si in range(6) for vi in range(6)]
        attr_array = []
        for si in range(len(e)):
            for i, vi in enumerate(e[si]):
                attr_array += [*v[vi], *n[si], *t[i], si]

        self.__no_vert = len(attr_array) // 10
        self.__no_indices = len(index_array)
        vertex_attributes = (ctypes.c_float * len(attr_array))(*attr_array)
        indices = (ctypes.c_uint32 * self.__no_indices)(*index_array)

        self.__vao = glGenVertexArrays(1)
        self.__vbo, self.__ibo = glGenBuffers(2)

        glBindVertexArray(self.__vao)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__ibo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, self.__vbo)
        glBufferData(GL_ARRAY_BUFFER, vertex_attributes, GL_STATIC_DRAW)

        float_size = ctypes.sizeof(ctypes.c_float)   
        glVertexAttribPointer(self.___attrib['a_pos'], 3, GL_FLOAT, False, 9*float_size, None)
        glVertexAttribPointer(self.___attrib['a_nv'], 3, GL_FLOAT, False, 9*float_size, ctypes.c_void_p(3*float_size))
        glVertexAttribPointer(self.___attrib['a_uv'], 3, GL_FLOAT, False, 9*float_size, ctypes.c_void_p(6*float_size))
        glEnableVertexAttribArray(self.___attrib['a_pos'])
        glEnableVertexAttribArray(self.___attrib['a_nv'])
        glEnableVertexAttribArray(self.___attrib['a_uv'])

        glEnable(GL_DEPTH_TEST)
        glUseProgram(self.__program)

        glActiveTexture(GL_TEXTURE0)
        sizeX, sizeY = image_size
        self.tex_obj = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D_ARRAY, self.tex_obj)
        glTexImage3D(GL_TEXTURE_2D_ARRAY, 0, GL_RGBA, sizeX, sizeY, 6, 0, GL_RGBA, GL_UNSIGNED_BYTE, None)
        for i in range(6):
            glTexSubImage3D(GL_TEXTURE_2D_ARRAY, 0, 0, 0, i, sizeX, sizeY, 1, GL_RGBA, GL_UNSIGNED_BYTE, image_planes[i])
        glTexParameterf(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    def run(self):
        self.__starttime = 0
        self.__starttime = self.elapsed_ms()
        
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.__mainloop()
            pygame.display.flip()

        pygame.quit()
        exit()

    def elapsed_ms(self):
      return pygame.time.get_ticks() - self.__starttime

    def __mainloop(self):

        proj, view, model  = glm.mat4(1), glm.mat4(1), glm.mat4(1)
        aspect = self.__vp_size[0]/self.__vp_size[1]
        proj = glm.perspective(glm.radians(90.0), aspect, 0.1, 10.0)
        view = glm.lookAt(glm.vec3(0,-3,0), glm.vec3(0, 0, 0), glm.vec3(0,0,1))
        angle1 = self.elapsed_ms() * math.pi * 2 / 5000.0
        angle2 = self.elapsed_ms() * math.pi * 2 / 7333.0
        model = glm.rotate(model, angle1, glm.vec3(1, 0, 0))
        model = glm.rotate(model, angle2, glm.vec3(0, 1, 0))

        glUniformMatrix4fv(self.___uniform['u_proj'], 1, GL_FALSE, glm.value_ptr(proj) )
        glUniformMatrix4fv(self.___uniform['u_view'], 1, GL_FALSE, glm.value_ptr(view) )
        glUniformMatrix4fv(self.___uniform['u_model'], 1, GL_FALSE, glm.value_ptr(model) )

        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glDrawElements(GL_TRIANGLES, self.__no_indices, GL_UNSIGNED_INT, None)

window = MyWindow(800, 600)
window.run()