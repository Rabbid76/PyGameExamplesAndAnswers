[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# [How to group, then rotate and translate grouped objects in python opengl](https://stackoverflow.com/questions/50303616/how-to-group-then-rotate-and-translate-grouped-objects-in-python-opengl)

A rubik's cube can be organized by an 3 dimensional array of *3x3x3* cubes. It seems to be easy to rotate a slice of the cube, but note if on slice is rotated the positions of the  cube change and have to be reorganized. Not only the position changes, also the orientation of the (rotated) single cubes changes.

First of all remove the PyGame and OpenGL initialization form the constructor of the class `Cube`. That is the wrong place for this. In the following will generate 27 objects of type Cube.

Each cube has to know where it is initially located (`self.init_i`) and where it is current located after some rotations (`self.current_i`). This information is encoded in a list with 3 elements, one for each axis. The values are indices of cube in the *NxNxN* rubik's cube in range *[0, N[*.  
The orientation of a single cube is encoded in 3 dimensional [Rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix) (`self.rot`). The rotation matrix has to be initialized by the [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix).

<!-- language: py -->

    class Cube():
        def __init__(self, id, N, scale):
            self.N = N
            self.scale = scale
            self.init_i = [*id]
            self.current_i = [*id]
            self.rot = [[1 if i==j else 0 for i in range(3)] for j in range(3)]

Create a list of the 27 cubes

<!-- language: py -->

    cr = range(3)
    self.cubes = [Cube((x, y, z), 3, scale) for x in cr for y in cr for z in cr]

If a slice of the rubik's cube is rotated, then it has to be checked which of the single cubes is affected. This can be done by checking if the slice matches the entry of the rotation axis of the current position.  

<!-- language: py -->

    def isAffected(self, axis, slice, dir):
        return self.current_i[axis] == slice

To rotate a cube, the position and the orientation has to be rotated by 90° around an `axis`. A 3 dimension rotation matrix consists of 3 direction vectors. A d dimensional vector can be rotated by swapping the coordinates of the vector and inverting the x coordinate of the result for a right rotation and inverting the y coordinate of the result for a left rotation:

<!-- language: lang-none -->

    rotate right: (x, y) -> (-y, x)
    rotate left:  (x, y) -> (y, -x)

Since all the vectors of the rotation matrix are in an axis aligned plane this algorithm can be used to change the orientation and the position of the cube. `axis` the rotation axis *(x=0, y=1, z=2)* and `dir` is the rotation direction (*1* is right and *-1* left)
To rotate the axis vector, 2 components of the vector have to be swapped and one of them inverted. 

e.g rotate left around the Y-axis:

<!-- language: lang-none -->

    (x, y, z) -> (z, y, -x)

When the position is rotated, then the indices have to be swapped. Inverting an index means to map the index `i` to the index `N-1-i`:

e.g rotate left around the Y-axis:

<!-- language: lang-none -->

    (ix, iy, iz) -> (iz, iy, N-1-ix)

Rotation of a single cube:

<!-- language: py -->

    i, j = (axis+1) % 3, (axis+2) % 3
    for k in range(3):
        self.rot[k][i], self.rot[k][j] = -self.rot[k][j]*dir, self.rot[k][i]*dir

    self.current_i[i], self.current_i[j] = (
        self.current_i[j] if dir < 0 else self.N - 1 - self.current_i[j],
        self.current_i[i] if dir > 0 else self.N - 1 - self.current_i[i] )

When the cube has to be drawn, then the current position of the cube (`self.current_i`) and the orientation `self.rot` can be used to set up 4x4 transformation matrix:

<!-- language: py -->

    def transformMat(self):
        scaleA = [[s*self.scale for s in a] for a in self.rot]  
        scaleT = [(p-(self.N-1)/2)*2.1*self.scale for p in self.current_i] 
        return [
            *scaleA[0], 0,
            *scaleA[1], 0,
            *scaleA[2], 0,
            *scaleT,    1]

With [`glPushMatrix`](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glPushMatrix.xml) respectively [`glPushMatrix`](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glPushMatrix.xml). By [`glMultMatrix`](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glMultMatrix.xml) a matrix can be multiplied to the current matrix.  
The following function draws a single cube. The parameters `angle`, `axis`, `slice`, `dir` and it can even apply an animation to the cube, by setting `animate=True` and setting parameters `angle`, `axis`, `slice`, `dir`:

<!-- language: py -->

    def draw(self, col, surf, vert, animate, angle, axis, slice, dir):

        glPushMatrix()
        if animate and self.isAffected(axis, slice, dir):
            glRotatef( angle*dir, *[1 if i==axis else 0 for i in range(3)] )
        glMultMatrixf( self.transformMat() )

        glBegin(GL_QUADS)
        for i in range(len(surf)):
            glColor3fv(colors[i])
            for j in surf[i]:
                glVertex3fv(vertices[j])
        glEnd()

        glPopMatrix()

To draw the cubes, it is sufficient to call the method `draw` in a loop:

<!-- language: py -->

    for cube in self.cubes:
        cube.draw(colors, surfaces, vertices, animate, animate_ang, *action)

The implementation of the class `Cube` works for any *NxNxN* Rubik's cube. 

See the example program for a *3x3x3* cube. The slices of the cube are rotated to the right by the keys **1** to **9** and to the left by the keys **F1** to **F9**:

[![][1]][1]

    import pygame
    import random
    from pygame.locals import *

    from OpenGL.GL import *
    from OpenGL.GLU import *

    vertices = (
        ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1), (-1, -1, -1),
        ( 1, -1,  1), ( 1,  1,  1), (-1, -1,  1), (-1,  1,  1)
    )
    edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
    surfaces = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))
    colors = ((1, 0, 0), (0, 1, 0), (1, 0.5, 0), (1, 1, 0), (1, 1, 1), (0, 0, 1))

    class Cube():
        def __init__(self, id, N, scale):
            self.N = N
            self.scale = scale
            self.init_i = [*id]
            self.current_i = [*id]
            self.rot = [[1 if i==j else 0 for i in range(3)] for j in range(3)]

        def isAffected(self, axis, slice, dir):
            return self.current_i[axis] == slice

        def update(self, axis, slice, dir):

            if not self.isAffected(axis, slice, dir):
                return

            i, j = (axis+1) % 3, (axis+2) % 3
            for k in range(3):
                self.rot[k][i], self.rot[k][j] = -self.rot[k][j]*dir, self.rot[k][i]*dir

            self.current_i[i], self.current_i[j] = (
                self.current_i[j] if dir < 0 else self.N - 1 - self.current_i[j],
                self.current_i[i] if dir > 0 else self.N - 1 - self.current_i[i] )

        def transformMat(self):
            scaleA = [[s*self.scale for s in a] for a in self.rot]  
            scaleT = [(p-(self.N-1)/2)*2.1*self.scale for p in self.current_i] 
            return [*scaleA[0], 0, *scaleA[1], 0, *scaleA[2], 0, *scaleT, 1]

        def draw(self, col, surf, vert, animate, angle, axis, slice, dir):

            glPushMatrix()
            if animate and self.isAffected(axis, slice, dir):
                glRotatef( angle*dir, *[1 if i==axis else 0 for i in range(3)] )
            glMultMatrixf( self.transformMat() )

            glBegin(GL_QUADS)
            for i in range(len(surf)):
                glColor3fv(colors[i])
                for j in surf[i]:
                    glVertex3fv(vertices[j])
            glEnd()

            glPopMatrix()

    class EntireCube():
        def __init__(self, N, scale):
            self.N = N
            cr = range(self.N)
            self.cubes = [Cube((x, y, z), self.N, scale) for x in cr for y in cr for z in cr]

        def mainloop(self):

            rot_cube_map  = { K_UP: (-1, 0), K_DOWN: (1, 0), K_LEFT: (0, -1), K_RIGHT: (0, 1)}
            rot_slice_map = {
                K_1: (0, 0, 1), K_2: (0, 1, 1), K_3: (0, 2, 1), K_4: (1, 0, 1), K_5: (1, 1, 1),
                K_6: (1, 2, 1), K_7: (2, 0, 1), K_8: (2, 1, 1), K_9: (2, 2, 1),
                K_F1: (0, 0, -1), K_F2: (0, 1, -1), K_F3: (0, 2, -1), K_F4: (1, 0, -1), K_F5: (1, 1, -1),
                K_F6: (1, 2, -1), K_F7: (2, 0, -1), K_F8: (2, 1, -1), K_F9: (2, 2, -1),
            }  

            ang_x, ang_y, rot_cube = 0, 0, (0, 0)
            animate, animate_ang, animate_speed = False, 0, 5
            action = (0, 0, 0)
            while True:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == KEYDOWN:
                        if event.key in rot_cube_map:
                            rot_cube = rot_cube_map[event.key]
                        if not animate and event.key in rot_slice_map:
                            animate, action = True, rot_slice_map[event.key]
                    if event.type == KEYUP:
                        if event.key in rot_cube_map:
                            rot_cube = (0, 0)

                ang_x += rot_cube[0]*2
                ang_y += rot_cube[1]*2

                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
                glTranslatef(0, 0, -40)
                glRotatef(ang_y, 0, 1, 0)
                glRotatef(ang_x, 1, 0, 0)

                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

                if animate:
                    if animate_ang >= 90:
                        for cube in self.cubes:
                            cube.update(*action)
                        animate, animate_ang = False, 0

                for cube in self.cubes:
                    cube.draw(colors, surfaces, vertices, animate, animate_ang, *action)
                if animate:
                    animate_ang += animate_speed

                pygame.display.flip()
                pygame.time.wait(10)

    def main():

        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        glEnable(GL_DEPTH_TEST) 

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        NewEntireCube = EntireCube(3, 1.5) 
        NewEntireCube.mainloop()

    if __name__ == '__main__':
        main()
        pygame.quit()
        quit()

  [1]: https://i.stack.imgur.com/ZriyZ.gif