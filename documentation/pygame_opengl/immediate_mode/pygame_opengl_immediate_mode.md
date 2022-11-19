[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# PyGame and OpenGL immediate mode (Legacy OpenGL)

Related Stack Overflow questions:

- [What does “immediate mode” mean in OpenGL?](https://stackoverflow.com/questions/6733934/what-does-immediate-mode-mean-in-opengl)

> One example of "immediate mode" is using `glBegin` and `glEnd` with `glVertex` in between them. Another example of "immediate mode" is to use `glDrawArrays` with a client vertex array (i.e. not a vertex buffer object). [...]

## Primitive and Mesh

Related Stack Overflow questions:

- [GL_LINES not showing up on top of cube?](https://stackoverflow.com/questions/56624147/gl-lines-not-showing-up-on-top-of-cube/56624975#56624975)  
  ![scene](https://i.stack.imgur.com/Go9Ym.gif)

  :scroll: **[OpenGL immediate mode - Draw a cube with a glBegin/glEnd sequnce and an outline](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_cube_outline.py)**  
  :scroll: **[OpenGL immediate mode - Draw a cube with a glBegin/glEnd sequnce and an outline (polygon mode)](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_cube_outline_2.py)**  

- [Drawing points on a surface of a sphere](https://stackoverflow.com/questions/50307431/drawing-points-on-a-surface-of-a-sphere/50307674#50307674)  
 ![scene](https://i.stack.imgur.com/PXKRd.png)

 :scroll: **[OpenGL immediate mode - Draw points around a spherical shape](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_sphere_points.py)**

- [Converting pygame 2d water ripple to pyOpenGL](https://stackoverflow.com/questions/63732713/converting-pygame-2d-water-ripple-to-pyopengl/63744177#63744177)  
  ![scene](https://i.stack.imgur.com/sf0o4.gif)

- [pygame pyopengl texture a changing polygon with many sides](https://stackoverflow.com/questions/63745181/pygame-pyopengl-texture-a-changing-polygon-with-many-sides/63746178#63746178)  
  ![scene](https://i.stack.imgur.com/RUDto.gif)

:scroll: **[OpenGL immediate mode - 2D water particles](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_cube_texture.py)**

- [X Error of failed request: BadValue (integer parameter out of range for operation), PyOpenGL](https://stackoverflow.com/questions/48350671/x-error-of-failed-request-badvalue-integer-parameter-out-of-range-for-operatio/48353815#48353815)  
  ![cube outline](https://i.stack.imgur.com/plgw5.png)

  :scroll: **[OpenGL immediate mode - Draw a simple triangle](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_triangle.py)**

  :scroll: **[OpenGL immediate mode - Draw simple triangles with polygon depth offset](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_triangle_polygonoffset.py)**

- [How do I add an image as texture of my 3D cube in pyopengl](https://stackoverflow.com/questions/67367424/how-do-i-add-an-image-as-texture-of-my-3d-cube-in-pyopengl/67367851#67367851)  
  ![How do I add an image as texture of my 3D cube in pyopengl](https://i.stack.imgur.com/kGBr8.gif)

  :scroll: **[OpenGL immediate mode - Draw a cube with texture](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_cube_texture.py)**
  :scroll: **[OpenGL immediate mode - Draw a cube with texture](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_light_texture.py)**

Examples:

:scroll: **[OpenGL immediate mode - Draw GLU object](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_glu_objects.py)**
### Fixed attribute

Related Stack Overflow questions:

- [PyGame OpenGL 3D Cube Lag](https://stackoverflow.com/questions/50312760/pygame-opengl-3d-cube-lag/50314047#50314047)  
  ![PyGame OpenGL 3D Cube Lag](https://i.stack.imgur.com/Go9Ym.gif)

  :scroll: **[OpenGL immediate mode - Draw a cube with outline using fixed function attributes](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_fixed_attribute_cube.py)**

  :scroll: **[OpenGL immediate mode - Draw a cube with outline using fixed function attributes (VAO)](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_fixed_attribute_cube_vao.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-opengl-cube-wireframe](https://replit.com/@Rabbid76/pygame-opengl-cube-wireframe#main.py)**

## Draw lines and polygons

- [Draw variable number of lines - PyOpenGL](https://stackoverflow.com/questions/64079973/draw-variable-number-of-lines-pyopengl/64080275#64080275)  
  ![scene](https://i.stack.imgur.com/AuX7d.gif)

  :scroll: **[OpenGL immediate mode - Draw contours](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_draw_contour.py)**

## Wavefront .obj file

The [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file) file format is a simple data-format that represents 3D geometry.

- [PyOpenGL how do I import an obj file?](https://stackoverflow.com/questions/59923419/pyopengl-how-do-i-import-an-obj-file/59926122#59926122)  
- [Is there a way to change the location and size of an imported .obj file in Pygame?](https://stackoverflow.com/questions/59609837/is-there-a-way-to-change-the-location-and-size-of-an-imported-obj-file-in-pygam/59610853#59610853)  
  ![scene](https://i.stack.imgur.com/Jvb2x.png)

  :scroll: **[OpenGL immediate mode - Import obj (wavefront)](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_obj.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/pygame-opengl-wavefront-obj](https://replit.com/@Rabbid76/pygame-opengl-wavefront-obj#main.py)**

## Fixed function attributes

[Rendering Image in Pygame Using PyOpenGL](https://stackoverflow.com/questions/56122387/rendering-image-in-pygame-using-pyopengl)

[is there a way to render points faster OpenGL](https://stackoverflow.com/questions/56787061/is-there-a-way-to-render-points-faster-opengl/56794726#56794726)  

## Scale, Rotate, Translate

- [PyOpenGl Pygame window freezes when run](https://stackoverflow.com/questions/54683378/pyopengl-pygame-window-freezes-when-run/54696233#54696233)  
- [Drawing a cube with Pygame and OpenGL in Python environment](https://stackoverflow.com/questions/66623528/drawing-a-cube-with-pygame-and-opengl-in-python-environment/66623589#66623589)  
  ![PyOpenGl Pygame window freezes when run](https://i.stack.imgur.com/jUWiH.gif)  

  :scroll: **[OpenGL immediate mode - Draw a wireframe cube](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_cube_wireframe.py)**

- [How to rotate a cube using mouse in pyopengl](https://stackoverflow.com/questions/59823131/how-to-rotate-a-cube-using-mouse-in-pyopengl/59823600#59823600)  
  ![How to rotate a cube using mouse in pyopengl](https://i.stack.imgur.com/zwhCC.gif)

  :scroll: **[OpenGL immediate mode - rotate ](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_matrix_cube_rotate_1.py)**

- [how to drag camera with the mouse like in blender](https://stackoverflow.com/questions/70398671/how-to-drag-camera-with-the-mouse-like-in-blender/70398950#70398950)  
  ![how to drag camera with the mouse like in blender](https://i.stack.imgur.com/dzCLn.gif)  

  :scroll: **[OpenGL immediate mode - rotate around local](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_matrix_cube_rotate_2.py)**

- [Move around cube using WASD in Pygame?](https://stackoverflow.com/questions/64881896/move-around-cube-using-wasd-in-pygame/64882112#64882112)  
  ![Move around cube using WASD in Pygame?](https://i.stack.imgur.com/MSI1c.gif)

  :scroll: **[OpenGL immediate mode - translate object](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_matrix_cube_translate.py)**

- [OpenGL python and pygame translation after rotation not working for mouselook and movement](https://stackoverflow.com/questions/60244843/opengl-python-and-pygame-translation-after-rotation-not-working-for-mouselook-an/60248986#60248986)  
  ![scene](https://i.stack.imgur.com/cCV23.gif)

  :scroll: **[OpenGL immediate mode - translate and rotate](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_matrix_cube_translate_and_rotate.py)**

- [Moving only one cube out of 2 in Python with PyOpenGL](https://stackoverflow.com/questions/60901079/moving-only-one-cube-out-of-2-in-python-with-pyopengl)  
- [PyOpenGL: move two objects separately?](https://stackoverflow.com/questions/61679379/pyopengl-move-two-objects-separately/61682813#61682813)

  :scroll: **[OpenGL immediate mode - move objects individually](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_matrix_move_objects_individually_1.py)**

- [Python OpenGL not working properly when trying to color 3D objects](https://stackoverflow.com/questions/64081660/python-open-gl-not-working-properly-when-trying-to-color-3d-objects/64086720#64086720)

- [Align individual objects in pyOpenGL to create a bigger aggregated object](https://stackoverflow.com/questions/58590491/align-individual-objects-in-pyopengl-to-create-a-bigger-aggregated-object/58594997#58594997)  
  ![Align individual objects in pyOpenGL to create a bigger aggregated object](https://i.stack.imgur.com/vMqWn.gif)  

Examples:

[individual object transformation](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_cube_individual_transformation.py)

## Projection

### Orthographic projection

### Perspective projection

[confusion about glPerspective and GL_POLYGON](https://stackoverflow.com/questions/62009985/confusion-about-glperspective-and-gl-polygon/62010145#62010145)  

[Strange “X” on PyOpenGL + PyGame](https://stackoverflow.com/questions/63024240/strange-x-on-pyopengl-pygame)  

## Camera

### First person

- [Stackoverflow question: how to modify the view of the camera with pygame and openGL](https://stackoverflow.com/questions/47169618/how-to-modify-the-view-of-the-camera-with-pygame-and-opengl/47173089#47173089)
  ![Stackoverflow question: how to modify the view of the camera with pygame and openGL](https://i.stack.imgur.com/jtVF8.png)  

  :scroll: **[OpenGL immediate mode - first person 1](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_matrix_firstperson_1.py)**  
  :scroll: **[OpenGL immediate mode - first person 2](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_matrix_firstperson_2.py)**

- [How create a camera on PyOpenGL that can do “perspective rotations” on mouse movements?](https://stackoverflow.com/questions/56609044/how-create-a-camera-on-pyopengl-that-can-do-perspective-rotations-on-mouse-mov/56609894#56609894)  
  ![scene](https://i.stack.imgur.com/0cb9x.gif)

  :scroll: **[OpenGL immediate mode - first person 3](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_matrix_firstperson_3.py)**

- [How to rotate a certain object (Quad) in PyOpenGL?](https://stackoverflow.com/questions/56646279/how-to-rotate-a-certain-object-quad-in-pyopengl/56646504?noredirect=1#comment99864711_56646504)  
  [How to test if a 2d point in pygame screen is part of a 3d object in PyOpenGL?](https://stackoverflow.com/questions/56681932/how-to-test-if-a-2d-point-in-pygame-screen-is-part-of-a-3d-object-in-pyopengl/56700807?noredirect=1#comment99965769_56700807)  
  [How to do knock-backs in PyOpenGL with object facing?](https://stackoverflow.com/questions/56714854/how-to-do-knock-backs-in-pyopengl-with-object-facing)  
  ![scene](https://i.stack.imgur.com/k0K8i.gif)

- [how to get vertical rotation in 3D space with OpenGL?](https://stackoverflow.com/questions/55638222/how-to-get-vertical-rotation-in-3d-space-with-opengl/55639392#55639392)  
  ![scene](https://i.stack.imgur.com/BgUZK.gif)

- [how to modify the view of the camera with pygame and openGL](https://stackoverflow.com/questions/47169618/how-to-modify-the-view-of-the-camera-with-pygame-and-opengl)

- [Cannot draw to the same position using gluSphere()?](https://stackoverflow.com/questions/56832809/cannot-draw-to-the-same-position-using-glusphere)  

- [Python OpenGL does not render every Triangle in a Quadrilateral](https://stackoverflow.com/questions/57598269/python-opengl-does-not-render-every-triangle-in-a-quadrilateral/57598464#57598464)  

- [Problems with creating a UI and glRotatef()](https://stackoverflow.com/questions/57981147/pygame-and-legacy-pyopengl-problems-with-creating-a-ui-and-glrotatef)  

- [Using gluLookAt() causes the objects to spin](https://stackoverflow.com/questions/54316746/using-glulookat-causes-the-objects-to-spin/54371129#54371129)  

## Light

[Basic OpenGL Lighting](https://www.sjbaker.org/steve/omniv/opengl_lighting.html)  
[Per Fragment Lighting](https://www.opengl.org/sdk/docs/tutorials/ClockworkCoders/lighting.php) 

- [How to correctly add a light to make object get a better view with pygame and pyopengl](https://stackoverflow.com/questions/56514791/how-to-correctly-add-a-light-to-make-object-get-a-better-view-with-pygame-and-py)  
  ![scene](https://i.stack.imgur.com/svZ9q.gif)

  :scroll: **[OpenGL immediate mode - light model](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_light.py)**  
  :scroll: **[OpenGL immediate mode - light model, depth range issue](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_light_depth_range_issue.py)**  

- [How to make specular lighting on python to implement the Phong lighting?](https://stackoverflow.com/questions/67544996/how-to-make-specular-lighting-on-python-to-implement-the-phong-lighting/67545182#67545182)  
  ![scene](https://i.stack.imgur.com/x4yEs.gif)

  :scroll: **[OpenGL immediate mode - Phong shading light model](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_light_specular.py)**  

## Mouse position and Unproject

[How to find PyGame Window Coordinates of an OpenGL Vertice?](https://stackoverflow.com/questions/46801701/how-to-find-pygame-window-coordinates-of-an-opengl-vertice)  

[How to test if a 2d point in pygame screen is part of a 3d object in PyOpenGL?](https://stackoverflow.com/questions/56681932/how-to-test-if-a-2d-point-in-pygame-screen-is-part-of-a-3d-object-in-pyopengl/56700807#56700807)

### Hit detection

- [How to find PyGame Window Coordinates of an OpenGL Vertice?](https://stackoverflow.com/questions/46801701/how-to-find-pygame-window-coordinates-of-an-opengl-vertice/46815050#46815050)

  :scroll: **[OpenGL immediate mode - hit detection 1](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_hit_detection_1.py)**  
  :scroll: **[OpenGL immediate mode - hit detection 2](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_hit_detection_2.py)**  

## Text

- [pygame + opengl = display text](https://stackoverflow.com/questions/67608968/pygame-opengl-display-text/67639147#67639147)  
  ![pygame + opengl = display text](https://i.stack.imgur.com/fEc07.gif)  

  :scroll: **[OpenGL immediate mode - Text](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_pixel_text.py)**  
  :scroll: **[OpenGL immediate mode - Text with transparent background](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_pixel_text_transparent.py)**  

  **[![](https://i.stack.imgur.com/5jD0C.png) replit.com/@Rabbid76/pygame-opengl-text#main.py](https://replit.com/@Rabbid76/pygame-opengl-text#main.py)**

Compare [`glWindowPos`](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glWindowPos.xml) and [`glRasterPos`](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glRasterPos.xml). While the coordinates of `glRasterPos` are transformed by the current modelview and projection matrices, `glWindowPos` directly updates the x and y coordinates of the current raster position.

## Texture

- [PyOpenGL texture isn't displaying correctly](https://stackoverflow.com/questions/68468091/pyopengl-texture-isnt-displaying-correctly/68489022#68489022)  
- [My pygame/pyopengl code seems to apply a texture to every surface](https://stackoverflow.com/questions/68902541/my-pygame-pyopengl-code-seems-to-apply-a-texture-to-every-surface/68902623#68902623)  
  ![texture](https://i.stack.imgur.com/Ev2Aj.png)

  :scroll: **[Texture - glDrawPixels](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_glDrawPixels.py)**  
  :scroll: **[Texture - Surface to texture](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_surface_to_texture.py)**
  :scroll: **[OpenGL immediate mode - Draw a quad with texture](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_quad_texture.py)**

## Shader

- [Vertex/fragment shaders for a OpenGL firsrt-person shooter view?](https://stackoverflow.com/questions/59896103/vertex-fragment-shaders-for-a-opengl-firsrt-person-shooter-view/59898241#59898241)

:scroll: **[OpenGL immediate mode - immediat mode shader 1](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_begin_end_shader_1.py)**  

If you use a shader program, then the matrix transformations have to be done in the vertex shader.
The [Legacy OpenGL](https://www.khronos.org/opengl/wiki/Legacy_OpenGL) matrix stack is deprecated. If you use a shader program and the legacy matrices, then you have
to step back to a [OpenGL Shading Language 1.20](https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.1.20.pdf) (`#version 120`) shader.  
In this version the  built in uniforms like `gl_ModelViewProjectionMatrix` can be used. See [Lighthouse3d.com - Hello World in GLSL](https://www.lighthouse3d.com/tutorials/glsl-12-tutorial/hello-world-in-glsl/).

e.g.:

```glsl
# version 120
attribute vec3 a_position;
attribute vec3 a_color;

varying vec3 v_color;

void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * vec4(a_position, 1.0);
    v_color = a_color;
}
```

## Video and Camera

- [Draw a background video behind a 3D model in OpenGL](https://stackoverflow.com/questions/68533162/draw-a-background-video-behind-a-3d-model-in-opengl/68533213#68533213)  
  ![Draw a background video behind a 3D model in OpenGL](https://i.stack.imgur.com/w2vqd.gif)

  :scroll: **[OpenGL immediate mode - Draw a quad with texture](../../../examples/pygame_opengl/immediate_mode/pygame_opengl_camera_background.py)**
