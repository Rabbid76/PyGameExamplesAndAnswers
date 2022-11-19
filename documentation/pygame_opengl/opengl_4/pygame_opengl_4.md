[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# PyGame and OpenGL 4

## Vertex buffer and vertex attributes

Related Stack Overflow questions:

- [Can't get glVertexAttribPointer to render colour from shaders](https://stackoverflow.com/questions/59898858/cant-get-glvertexattribpointer-to-render-colour-from-shaders/59899044#59899044)  

If a named buffer object is bound, then the 5th parameter of [`glVertexAttribPointer`](http://pyopengl.sourceforge.net/documentation/manual-3.0/glVertexAttribPointer.html) is treated as a byte offset into the buffer object's data store. However, the type of the parameter is still a pointer (`c_void_p`).  

Hence the offset must be cast with [`c_void_p`](https://docs.python.org/3/library/ctypes.html). If the offset is 0, the 5th parameter can either be `None` or `c_void_p(0)`:

```py
loc_col = glGetAttribLocation(shader_program, "color")
glVertexAttribPointer(loc_col, 3, GL_FLOAT, False, 6*4, ctypes.c_void_p(3*4))
```

## Mesh

Related Stack Overflow questions:

- [Pygame OpenGL 3D Cube Lag](https://stackoverflow.com/questions/50312760/pygame-opengl-3d-cube-lag/50314047#50314047)  
  ![PyGame OpenGL 3D Cube Lag](https://i.stack.imgur.com/Go9Ym.gif)

  :scroll: **[OpenGL immediate mode - Draw a cube with outline](../../../examples/pygame_opengl/opengl_4/pygame_opengl_mesh_cube_outline.py)**

  :scroll: **[OpenGL immediate mode - Draw a cube with indces and outline](../../../examples/pygame_opengl/opengl_4/pygame_opengl_mesh_cube_indices_outline.py)**

## Clipping and Stencil

Related Stack Overflow questions:

- [How to use stencil buffer to achieve hierarchical clipping](https://stackoverflow.com/questions/56636337/how-to-use-stencil-buffer-to-achieve-hierarchical-clipping/56637285#5663728)  

## Matrix and vertex transformation

Related Stack Overflow questions:

- [How to perform OpenGL rotation in more than 1 axis using shaders, pygame, and pyopengl](https://stackoverflow.com/questions/58075996/how-to-perform-opengl-rotation-in-more-than-1-axis-using-shaders-pygame-and-py/58076894#58076894)

Pyrr's [`Matrix44`](https://pyrr.readthedocs.io/en/latest/api_matrix.html#module-pyrr.matrix44) behaves like and is implemented using [`numpy.array`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html).

For [Numpy](https://numpy.org) arrays the `*` operator means element-wise multiplication, while the `@` operator means matrix multiplication.
See [`array`](https://numpy.org/devdocs/user/numpy-for-matlab-users.html).

The expression

>```py
>rot = rot_x * rot_y
>```

performs a component-wise multiplication of the elements of the matrix.

The correct operator for the matrix multiplication is:

```py
rot = rot_x @ rot_y
```

## Shader

Related Stack Overflow questions:

- [In python, how do you implement vertex and fragment shaders (programmable pipeline) in a openGL first person shooter view?](https://stackoverflow.com/questions/59896103/vertex-fragment-shaders-for-a-opengl-firsrt-person-shooter-view/59898241#59898241)  

### Texture

Related Stack Overflow questions:

- [Texture arrays in OpenGL](https://stackoverflow.com/questions/64122446/texture-arrays-in-opengl/64124199#64124199)  
  ![Texture arrays in OpenGL](https://i.stack.imgur.com/zlH2Z.gif)

  :scroll: **[OpenGL immediate mode - Cube and texture array](../../../examples/pygame_opengl/opengl_4/pygame_opengl_mesh_cube_texture_array.py)**

- [Use Texture Arrays To Texture A Sphere In OpenGL](https://stackoverflow.com/questions/64209236/use-texture-arrays-to-texture-a-sphere-in-opengl?noredirect=1#comment113552166_64209236)

It is like wrapping a checkered paper around the sphere. The 3D vertex coordinates form the sphere. The checkered paper is the 2D texture, with the 2D texture coordinates arranged in a grid. Each texture coordinate has to be associated to a point on the sphere (a vertex coordinate).
