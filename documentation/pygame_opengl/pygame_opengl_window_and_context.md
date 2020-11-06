[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# PyGame window and OpenGL context

Related Stack Overflow questions:

- [OpenGL error 1282 when trying scale a mesh in pyopengl](https://stackoverflow.com/questions/64076734/opengl-error-1281-when-trying-scale-a-mesh-in-pyopengl)
- [Python OpenGL not working properly when trying to color 3D objects](https://stackoverflow.com/questions/64081660/python-opengl-not-working-properly-when-trying-to-color-3d-objects/64086720?noredirect=1#comment113375140_64086720)  
- [glDrawArrays only updates when i exit](https://stackoverflow.com/questions/49957653/gldrawarrays-only-updates-when-i-exit/49957866#49957866)
- [OpenGL render view without a visible window in python](https://stackoverflow.com/questions/51627603/opengl-render-view-without-a-visible-window-in-python/51672538#51672538)
- [Is there a way to display a pygame window over OpenGL?](https://stackoverflow.com/questions/61547251/is-there-a-way-to-display-a-pygame-window-over-opengl/61547556#61547556)

A current and valid [OpenGL Context](https://www.khronos.org/opengl/wiki/OpenGL_Context)  for any OpenGL statement. You need to set the `pygame.OPENGL` flag when creating the display _Surface_:

```py
window = pg.display.set_mode((sw,sh), pygame.DOUBLEBUF | pygame.OPENGL)
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
