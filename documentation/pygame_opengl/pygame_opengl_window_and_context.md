[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# PyGame window and OpenGL context

Related Stack Overflow questions:

- [OpenGL error 1282 when trying scale a mesh in pyopengl](https://stackoverflow.com/questions/64076734/opengl-error-1281-when-trying-scale-a-mesh-in-pyopengl)
- [Python OpenGL not working properly when trying to color 3D objects](https://stackoverflow.com/questions/64081660/python-opengl-not-working-properly-when-trying-to-color-3d-objects/64086720?noredirect=1#comment113375140_64086720)  
- [glDrawArrays only updates when i exit](https://stackoverflow.com/questions/49957653/gldrawarrays-only-updates-when-i-exit/49957866#49957866)
- [OpenGL render view without a visible window in python](https://stackoverflow.com/questions/51627603/opengl-render-view-without-a-visible-window-in-python/51672538#51672538)
- [Is there a way to display a pygame window over OpenGL?](https://stackoverflow.com/questions/61547251/is-there-a-way-to-display-a-pygame-window-over-opengl/61547556#61547556)
- [How to blit a png image as an image overlay in PyOpenGL?](https://stackoverflow.com/questions/56767373/how-to-blit-a-png-image-as-an-image-overlay-in-pyopengl/56768773#56768773)  

A current and valid [OpenGL Context](https://www.khronos.org/opengl/wiki/OpenGL_Context) are required for any OpenGL statement. You need to set the `pygame.OPENGL` flag when creating the display _Surface_:

```py
window = pg.display.set_mode((sw, sh), pygame.DOUBLEBUF | pygame.OPENGL)
```

If you want to use the [Depth Test](https://www.khronos.org/opengl/wiki/Depth_Test)t, you need to ensure that the default frame buffer has a depth buffer. Set the depth buffer size attribute (`GL_DEPTH_SIZE`) with [`pygame.display.gl_set_attribute`](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode) (Try a size of 24, if that doesn't work then switch to 16):

```py
pygame.display.gl_set_attribute(GL_DEPTH_SIZE, 24) # <--- set depth buffer size

pygame.display.set_mode((width, height), pygame.DOUBLEBUF| pygame.OPENGL)

glEnable(GL_DEPTH_TEST) # <--- enable depth test
```

If the display mode is `pygame.OPENGL`, [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip) performs a GL buffer swap.

You need to enable double buffering by setting the `pygame.DOUBLEBUF` display mode flag (see [`pygame.display.set_mode()`](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)):

```py
screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
```

If you do not want to use double buffering, you must force the execution of GL commands manually with [`glFlush()`](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glFlush.xml):

```py
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # [...]

    glFlush() # force the execution of GL commands
```

It is not possible to create an [OpenGL Context](https://www.khronos.org/opengl/wiki/OpenGL_Context) with an version above 1.0 without any window.  
See the answer to the question [Creating OpenGL context without window](https://stackoverflow.com/questions/12482166/creating-opengl-context-without-window).

However, it is possible to use a completely hidden window for "offscreen" rendering.
Unfortunately it is not possible with [Pygame](https://www.pygame.org/news)  to create an initially hidden window.
It is only possible to hide a window after it has been created by calling [`pygame.display.iconify()`](https://www.pygame.org/docs/ref/display.html#pygame.display.iconify).  
See also [Hiding pygame display](https://stackoverflow.com/questions/10466590/hiding-pygame-display).

However, it is possible to create an initially hidden window with the [GLFW](http://www.glfw.org/) library by setting the  [window hint](http://www.glfw.org/docs/latest/window_guide.html#window_hints) `VISIBLE` to `False`.

## Save rendering (Screenshot)

Related Stack Overflow questions:

- [How to save pygame scene as jpeg?](https://stackoverflow.com/questions/66209365/how-to-save-pygame-scene-as-jpeg/66209486#66209486)  
- [Screenshots in OpenGL using python](https://stackoverflow.com/questions/71661677/screenshots-in-opengl-using-python/71663843#)
- [How can I draw a list to the screen in pygame?](https://stackoverflow.com/questions/72265793/how-can-i-draw-a-list-to-the-screen-in-pygame/72268437#72268437)

You can save a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object, object as the _Surface_ associated with the screen with [`pygame.image.save()`](https://www.pygame.org/docs/ref/image.html#pygame.image.save):

> This will save your Surface as either a BMP, TGA, PNG, or JPEG image.

```py
screen = pygame.display.set_mode((w, h))

# [...]

pygame.image.save(screen , "screenshot.jpg")
```

---

However, this doesn't work for `pygame.OPENGL` Surfaces. You must read the framebuffer with [`glReadPixels`](http://pyopengl.sourceforge.net/documentation/manual-3.0/glReadPixels.html) before the display is updated (before `pygame.display.flip()` or `pygame.display.update()`). Use [`pygame.image.fromstring()`](https://www.pygame.org/docs/ref/image.html#pygame.image.fromstring) to create new _Surfaces_ from the buffer. Finally, save the _Surface_ to a file:

```py
screen = pygame.display.set_mode((w, h), pygame.DOUBLEBUF | pygame.OPENGL)

# [...]

size = screen.get_size()
buffer = glReadPixels(0, 0, *size, GL_RGBA, GL_UNSIGNED_BYTE)
pygame.display.flip()

screen_surf = pygame.image.fromstring(buffer, size, "RGBA")
pygame.image.save(screen_surf, "screenshot.jpg")
```

If the data is in a texture (e.g. stored in a compute shader) you can read it with [`glGetTexImage`](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexImage.xhtml):

```py
image_buffer = glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA, GL_UNSIGNED_BYTE)
image_surf = pygame.image.fromstring(image_buffer, (width, height), "RGBA")
```

:scroll: **[OpenGL immediate mode - screenshot, glReadPixels](../../examples/pygame_opengl/immediate_mode/pygame_opengl_screenshot_glReadPixels.py)**  
:scroll: **[OpenGL immediate mode - store color buffer, glGetTexImage](../../examples/pygame_opengl/immediate_mode/pygame_opengl_store_colorbuffer_glGetTexImage.py)**  

## Mixed drawing

Related Stack Overflow questions:

- [How can I draw using pygame, while also drawing with pyopengl?](https://stackoverflow.com/questions/66552579/how-can-i-draw-using-pygame-while-also-drawing-with-pyopengl/66552664#66552664)

You can't do that directly.

However you can draw on a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object with the [`pygame.draw`](https://www.pygame.org/docs/ref/draw.html) module or [`pygame.Surface.blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit). Use [`pygame.PixelArray`](https://www.pygame.org/docs/ref/pixelarray.html) to access the pixels on the surface directly. Use the pixels to generate an OpenGL [Texture](https://www.khronos.org/opengl/wiki/Texture) object. This texture can be used in OpenGL. 

In the other direction you can render into a OpenGL [Renderbuffer](https://www.khronos.org/opengl/wiki/Renderbuffer_Object) or  [Texture](https://www.khronos.org/opengl/wiki/Texture) object (see [Framebuffers](https://learnopengl.com/Advanced-OpenGL/Framebuffers)). Load the texture onto the GPU with [`glReadPixels`](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glReadPixels.xhtml) or [`glGetTexImage`](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexImage.xhtml) and create a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) with [`pygame.image.frombuffer`](https://www.pygame.org/docs/ref/image.html#pygame.image.frombuffer).

- [pygame + opengl = display text](https://stackoverflow.com/questions/67608968/pygame-opengl-display-text/67639147#67639147)  
  ![pygame + opengl = display text](https://i.stack.imgur.com/fEc07.gif)  