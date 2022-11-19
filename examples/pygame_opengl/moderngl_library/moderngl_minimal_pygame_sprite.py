# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Render pygame sprites with pyopengl
# https://stackoverflow.com/questions/54543587/render-pygame-sprites-with-pyopengl/65653236#65653236
#
# GitHub - PyGame and ModernGL library
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/moderngl_library/pygame_moderngl_library.md

import os
import pygame
import moderngl
import ctypes

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resource'))

vertex_shader_sprite = """
#version 330
in vec2 in_position;
in vec2 in_uv;
out vec2 v_uv;
void main()
{
    v_uv = in_uv;
    gl_Position = vec4(in_position, 0.0, 1.0);
}
"""

fragment_shader_sprite = """
#version 330
out vec4 fragColor;
uniform sampler2D u_texture;
in vec2 v_uv;
void main() 
{
    fragColor = texture(u_texture, v_uv);
}
"""

class ModernGLGroup(pygame.sprite.Group):

    gl_context = None
    gl_program = None
    gl_buffer = None
    gl_vao = None
    gl_textures = {}

    def __init__(self, sprites = None):
        if sprites == None:
            super().__init__() 
        else:
            super().__init__(sprites) 

    def get_program():
        if ModernGLGroup.gl_program == None:
            ModernGLGroup.gl_program = ModernGLGroup.gl_context.program(
                vertex_shader = vertex_shader_sprite,
                fragment_shader = fragment_shader_sprite)
        return ModernGLGroup.gl_program
    
    def get_buffer():
        if ModernGLGroup.gl_buffer == None:
            ModernGLGroup.gl_buffer = ModernGLGroup.gl_context.buffer(None, reserve=6*4*4)
        return ModernGLGroup.gl_buffer

    def get_vao():
        if ModernGLGroup.gl_vao == None:
            ModernGLGroup.gl_vao = ModernGLGroup.gl_context.vertex_array(
                ModernGLGroup.get_program(), [(ModernGLGroup.get_buffer(), "2f4 2f4", "in_position", "in_uv")])
        return ModernGLGroup.gl_vao

    def get_texture(image):
        if not image in ModernGLGroup.gl_textures:
            rgba_image = image.convert_alpha()
            texture = ModernGLGroup.gl_context.texture(rgba_image.get_size(), 4, rgba_image.get_buffer())
            texture.swizzle = 'BGRA'
            ModernGLGroup.gl_textures[image] = texture
        return ModernGLGroup.gl_textures[image]

    def convert_vertex(pt, surface):
        return pt[0] / surface.get_width() * 2 - 1, 1 - pt[1] / surface.get_height() * 2 

    def render(sprite, surface):
        corners = [
            ModernGLGroup.convert_vertex(sprite.rect.bottomleft, surface),
            ModernGLGroup.convert_vertex(sprite.rect.bottomright, surface),
            ModernGLGroup.convert_vertex(sprite.rect.topright, surface),
            ModernGLGroup.convert_vertex(sprite.rect.topleft, surface)] 
        vertices_quad_2d = (ctypes.c_float * (6*4))(
            *corners[0], 0.0, 1.0, 
            *corners[1], 1.0, 1.0, 
            *corners[2], 1.0, 0.0,
            *corners[0], 0.0, 1.0, 
            *corners[2], 1.0, 0.0, 
            *corners[3], 0.0, 0.0)
        
        ModernGLGroup.get_buffer().write(vertices_quad_2d)
        ModernGLGroup.get_texture(sprite.image).use(0)
        ModernGLGroup.get_vao().render()    

    def draw(self, surface):
        for sprite in self:
            ModernGLGroup.render(sprite, surface)

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        try:
            self.image = pygame.image.load('icon/AirPlaneFront1-256.png').convert_alpha()
        except:
            self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (255, 255, 0), (50, 50), 50)
        self.rect = self.image.get_rect(center = (x, y))
       
    def update(self, surface):
        keys = pygame.key.get_pressed()
        vel = 5
        if keys[pygame.K_LEFT]:
            self.rect.left = max(0, self.rect.left-vel)
        if keys[pygame.K_RIGHT]:
            self.rect.right = min(surface.get_width(), self.rect.right+vel)
        if keys[pygame.K_UP]:
            self.rect.top = max(0, self.rect.top-vel)
        if keys[pygame.K_DOWN]:
            self.rect.bottom = min(surface.get_height(), self.rect.bottom+vel)

pygame.init()
window = pygame.display.set_mode((500, 500), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

gl_context = moderngl.create_context()
gl_context.enable(moderngl.BLEND)
ModernGLGroup.gl_context = gl_context

sprite_object = SpriteObject(*window.get_rect().center)
group = ModernGLGroup(sprite_object)

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    group.update(window)

    gl_context.clear(0.2, 0.2, 0.2)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()
