[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

For the computation of a reflection vector see [Vector - Reflection](pygame_vector_and_reflection.md).

# Collision and Intersection

## Collide with frame, window border and restrict to rectangle

Related Stack Overflow questions:

- [How to make ball bounce off wall with Pygame?](https://stackoverflow.com/questions/59802794/how-to-make-ball-bounce-off-wall-with-pygame/59803018#59803018)  
  ![How to make ball bounce off wall with Pygame?](https://i.stack.imgur.com/DKzqg.gif)
- [Window border in pygame](https://stackoverflow.com/questions/64205777/window-border-in-pygame/64206877#64206877)
- [I made a border in this pong game, but the paddles can cross it. How do I stop that?](https://stackoverflow.com/questions/63607681/i-made-a-border-in-this-pong-game-but-the-paddles-can-cross-it-how-do-i-stop-t/63609229#63609229)

:scroll: **[Minimal example - Restrict object to frame](../../examples/minimal_examples/pygame_minimal_intersect_frame_clamp.py)**

:scroll: **[Minimal example - Let a ball bounce off floor](../../examples/minimal_examples/pygame_minimal_intersect_circle_floor.py)**

PyGame has a feature that does exactly what you want it to do. Use [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) objects and [`pygame.Rect.clamp()`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.clamp) respectively [`pygame.Rect.clamp_ip()`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.clamp_ip):

> Returns a new rectangle that is moved to be completely inside the argument Rect. 

With this function, an object can be kept completely in the window. Get the window rectangle with [`get_rect`](pygame.Surface.get_rect)and clamp the object in the window:

```py
while run:
    # [...]

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y += -paddle_speed

    # [...]

    winRect = win.get_rect()
    paddle1.rect.clamp_ip(winRect)
    paddle2.rect.clamp_ip(winRect)
    paddle3.rect.clamp_ip(winRect)
    paddle4.rect.clamp_ip(winRect)

    # [...]
```

## Point and Rectangle - Click in rectangle

Related Stack Overflow questions:

- [How to detect when a rectangular object, image or sprite is clicked](https://stackoverflow.com/questions/58917346/how-to-detect-when-a-sprite-is-clicked/58935218#58935218)
- [How do I detect if the mouse is hovering over a button? PyGame button class is not displaying the text or changing colour on hover](https://stackoverflow.com/questions/63831057/pygame-button-class-is-not-displaying-the-text-or-changing-colour-on-hover/63831641#63831641)

:scroll: **[Minimal example - Mouse collide with rectangle](../../examples/minimal_examples/pygame_minimal_rectangle_collidepoint.py)**

## Point and Grid - Click in grid

Related Stack Overflow questions:

- [How would I keep track of the users clicks on the chessboard?](https://stackoverflow.com/questions/63584252/how-would-i-keep-track-of-the-users-clicks-on-the-chessboard/63584453#63584453)

## Point in triangle

Related Stack Overflow questions:

- [Only some points inside of triangle are considered 'inside' the triangle](https://stackoverflow.com/questions/59289954/only-some-points-inside-of-triangle-are-considered-inside-the-triangle/59290098#59290098)  
  ![Only some points inside of triangle are considered 'inside' the triangle](https://i.stack.imgur.com/2q2G9.gif)

:scroll: **[Minimal example - Is point in triangle](../../examples/minimal_examples/pygame_minimal_intersect_point_triangle.py)**

## Point and Circle - Click in circle

Related Stack Overflow questions:

- [How do I determine if my mouse is over randomly spawning objects](https://stackoverflow.com/questions/62129176/how-do-i-determine-if-my-mouse-is-over-randomly-spawning-objects/62129302#62129302)

## Rectangle and rectangle

Related Stack Overflow questions:

- **[How to detect collisions between two rectangular objects or images in pygame](https://stackoverflow.com/questions/63561028/how-to-detect-collision-between-two-images-in-pygame/63561152#63561152)**
- [Pygame: colliding rectangles with other rectangles in the same list](https://stackoverflow.com/questions/54793858/pygame-colliding-rectangles-with-other-rectangles-in-the-same-list/54794440#54794440)
- [Does pygame.colliderect() work the same way in both of these situations?](https://stackoverflow.com/questions/60936579/does-pygame-colliderect-work-the-same-way-in-both-of-these-situations/60936704#60936704)
- [Animation glitch in Pygame](https://stackoverflow.com/questions/56912016/animation-glitch-in-pygame/56914481#56914481)  
  ![Animation glitch in Pygame](https://i.stack.imgur.com/iTfNl.gif)

  :scroll: **[Minimal example - Compute PI by collision of rectangles](../../examples/minimal_examples/pygame_minimal_intersect_rectangle_compute_pi.py)**

- [Collision detection against player and blocks in the map](https://stackoverflow.com/questions/59957214/collision-detection-against-player-and-blocks-in-the-map/59957520#59957520)
- [PyGame collision system working only every other time](https://stackoverflow.com/questions/64334715/pygame-collision-system-working-only-every-other-time/64334754#64334754)

I recommend to use a [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint) object and either [`.collidepoint()`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint) or [`colliderect()`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect) to find a collision between a rectangle and an object.

```py
rect1 = pygame.Rect(x1, y1, w1, h1)
rect2 = pygame.Rect(x2, y2, w2, h2)
if rect1.colliderect(rect2):
    # [...]
```

```py
rect = pygame.Rect(x1, y1, w1, h1)
if rect1.collidepoint((x2, y2)):
    # [...]
```

The method `colliderect` evaluates, if a `pygame.Rect` object intersects, with a rectangle. `hbox1` and `hbox2` are rectangle objects, then the result of `hbox1.colliderect(hbox2)` is equal to the result of `hbox2.colliderect(hbox1)`. The operation is [Commutative](https://en.wikipedia.org/wiki/Commutative_property).  
But note, that the argument to `colliderect` does not need to be a `pygame.Rect` object. The argument is allowed to be a tuple, with 4 components (x, y, width, height), too.

If the rectangles (`x1`, `y1`, `w1`, `h1`) and (`x2`, `y2`, `w2`, `h2`) are intersection can be evaluated by:

```py
intersect = x1 < x2+w2 and x2 < x1+w1 and y1 < y2+h2 and y2 < y1+h1
```

It's easy to see that the two rectangles can be swapped and the result will be the same.

## Rectangle and list of rectangles

Related Stack Overflow questions:

- [rect collision with list of rects](https://stackoverflow.com/questions/61007064/rect-collision-with-list-of-rects/61007391#61007391)
- [Use collidelist in class](https://stackoverflow.com/questions/63705475/use-collidelist-in-class/63705792#63705792)

Use [`pygame.Rect.collidelist`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidelist) to test whether a rectangle collides with one of a list of rectangles.

[`collidelist`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidelist):

> Test whether the rectangle collides with any in a sequence of rectangles. The index of the first collision found is returned. If no collisions are found an index of -1 is returned.

```py
if player_rect.colliderect(tile_rects) >= 0:
    # [...]
```

[`pygame.Rect.collidelist`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidelist) and [`pygame.Rect.collidelistall`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidelistall) can be used for the collision test between a rectangle and a list of rectangles.

:scroll: **[Minimal example - Mouse collide with list of rectangles](../../examples/minimal_examples/pygame_minimal_rectangle_collidelist.py)**

[`pygame.Rect.collidedict`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidedict) and [`pygame.Rect.collidedictall`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidedictall) can be used for the collision collision test between a rectangle and a dictionary of rectangles.

Use [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) and [`colliderect()`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect) to detect the collision between the bounding rectangles of 2 images ([`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) objects). The bounding rectangle of a Surface can be get by [`get_rect()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect), where the location has to be set by an keyword argument

```py
rect = surface.get_rect(topleft = (x, y))
```

Note, a collision of a `Sprite` object and a [`Group`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) or event 2 `Group`s can be found by [`pygame.sprite.spritecollide()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollide) respectively [`pygame.sprite.groupcollide()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.groupcollide).

## Rectangle and circle

Related Stack Overflow questions:

- [How do I avoid an glitchy collision between circle and rectangle in PyGame?](https://stackoverflow.com/questions/58139771/pygame-pong-collision-glithcy/58145450#58145450)  
  ![How do I avoid an glitchy collision between circle and rectangle in PyGame?](https://i.stack.imgur.com/ekmV6.gif)
  ![How do I avoid an glitchy collision between circle and rectangle in PyGame?](https://i.stack.imgur.com/30mEF.gif)

  :scroll: **[Minimal example - Avoid glitchy collision between circle and rectangle](../../examples/minimal_examples/pygame_minimal_intersect_circle_rectangle_1.py)**

- [Issue finding side of collision for Circle-Rectangle collision](https://stackoverflow.com/questions/61718259/issue-finding-side-of-collision-for-circle-rectangle-collision/61719115#61719115)  
  ![Issue finding side of collision for Circle-Rectangle collision](https://i.stack.imgur.com/J1lc1.gif)

  :scroll: **[Minimal example - Find the intersection side between the circle and the rectangle](../../examples/minimal_examples/pygame_minimal_intersect_circle_rectangle_2.py)**

- [Detect collision between textbox and circle in pygame](https://stackoverflow.com/questions/58305721/detect-collision-between-textbox-and-circle-in-pygame/58306368#58306368)

  :scroll: **[Minimal example - Find the intersection of a small rectangle with the outline of a large circle](../../examples/minimal_examples/pygame_minimal_intersect_circle_rectangle_3.py)**

- [How can I know if a circle and a rect is touched in Pygame?](https://stackoverflow.com/questions/54840710/how-can-i-know-if-a-circle-and-a-rect-is-touched-in-pygame/54841116#54841116)

  :scroll: **[Minimal example - Find the intersection of a rectangle and a circle](../../examples/minimal_examples/pygame_minimal_intersect_circle_rectangle_4.py)**

How to avoid a glitchy collision between circle and rectangle:

There are 2 strategies to a void that.

1. Move the ball in the way, that it is touching the player but not intersecting the player once a collision is detected. e.g.:

    ```py
    dx = ballposx - player.rect.centerx
    dy = ballposy - player.rect.centery

    if abs(dx) > abs(dy):
        ballposx = player.rect.left-ballrad if dx < 0 else player.rect.right+ballrad
    else:
        ballposy = player.rect.top-ballrad if dy < 0 else player.rect.bottom+ballrad
    ```

2. Reflect the movement of the ball only if its movement vector points in a direction "against" the ball. e.g.:

    ```py
    if abs(dx) > abs(dy):
        if (dx < 0 and v[0] > 0) or (dx > 0 and v[0] < 0):
            v.reflect_ip(pygame.math.Vector2(1, 0))
    else:
        if (dy < 0 and v[1] > 0) or (dy > 0 and v[1] < 0):
            v.reflect_ip(pygame.math.Vector2(0, 1))
    ```

:scroll: **[Minimal example - Avoid glitchy collision between circle and rectangle](../../examples/minimal_examples/pygame_minimal_intersection_circle_rectangle_1.py)**

### Pong

Related Stack Overflow questions:

- **[Sometimes the ball doesn't bounce off the paddle in pong game](https://stackoverflow.com/questions/62864205/sometimes-the-ball-doesnt-bounce-off-the-paddle-in-pong-game)**  
  ![Sometimes the ball doesn't bounce off the paddle in pong game](https://i.imgur.com/tF3EwGX.gif)

### Not axis aligned (rotated) rectangle and circle

Related Stack Overflow questions:

- [pygame, detecting collision of a rotating rectangle](https://stackoverflow.com/questions/59553156/pygame-detecting-collision-of-a-rotating-rectangle/59553589#59553589)  
  ![pygame, detecting collision of a rotating rectangle](https://i.stack.imgur.com/pUeof.gif)
- [Pygame: How do I set boundaries for a rotating square?](https://stackoverflow.com/questions/61092553/pygame-how-do-i-set-boundaries-for-a-rotating-square/61094073#61094073)  
  ![Pygame: How do I set boundaries for a rotating square?](https://i.stack.imgur.com/hA2jp.gif)

## Line and line

Related Stack Overflow questions:

- [Problem with calculating line intersections](https://stackoverflow.com/questions/56312503/problem-with-calculating-line-intersections/56312654#56312654)  
  ![Problem with calculating line intersections](https://i.stack.imgur.com/l2NS9.png)

  :scroll: **[Minimal example - Intersect lines 1](../../examples/minimal_examples/pygame_minimal_interdect_line_line_1.py)**

- [Problem with finding the closest intersection](https://stackoverflow.com/questions/56316263/problem-with-finding-the-closest-intersection/56316370#56316370)  
  ![Problem with finding the closest intersection](https://i.stack.imgur.com/nLoJr.png)

  :scroll: **[Minimal example - Intersect lines 2](../../examples/minimal_examples/pygame_minimal_interdect_line_line_2.py)**

- [fiding every point of intersection of multiple lines using pygame in python for creation of game board](https://stackoverflow.com/questions/63521847/fiding-every-point-of-intersection-of-multiple-lines-using-pygame-in-python-for/63523520#63523520)  
  ![fiding every point of intersection of multiple lines using pygame in python for creation of game board](https://i.stack.imgur.com/6Do1b.png)
- [Line-to-line intersect with pygame's inverted y-axis](https://stackoverflow.com/questions/56048621/line-to-line-intersect-with-pygames-inverted-y-axis/56062849#56062849)

- [Make cursor unable to move through sprite pygame](https://stackoverflow.com/questions/54509869/make-cursor-unable-to-move-through-sprite-pygame/54511823#54511823)  
  ![Make cursor unable to move through sprite pygame](https://i.stack.imgur.com/QAJAL.gif)
  
  :scroll: **[Minimal example - Block mouse cursor by obstacle](../../examples/minimal_examples/pygame_minimal_mouse_cursor_block_by_obstacle.py)**

To find the intersection points of 2 rays or line segments in two-dimensional space, I use vector arithmetic and the following algorithm:

![Problem with calculating line intersections](https://i.stack.imgur.com/5Fzz0.png)

```lang-none
P     ... point on the 1. line
R     ... direction of the 1. line

Q     ... point on the 2. line
S     ... direction of the 2. line

alpha ... angle between Q-P and R
beta  ... angle between R and S

gamma  =  180° - alpha - beta

h  =  | Q - P | * sin(alpha)
u  =  h / sin(beta)

t  = | Q - P | * sin(gamma) / sin(beta)

t  =  dot(Q-P, (S.y, -S.x)) / dot(R, (S.y, -S.x))  =  determinant(mat2(Q-P, S)) / determinant(mat2(R, S))
u  =  dot(Q-P, (R.y, -R.x)) / dot(R, (S.y, -S.x))  =  determinant(mat2(Q-P, R)) / determinant(mat2(R, S))

X  =  P + R * t  =  Q + S * u
```

See also [Line–line intersection](https://en.wikipedia.org/wiki/Determinant)

If `t == 1`, then `X = P + R`. This can be used to assess whether the intersection is on a line segment.  
If a line is defined through the 2 points `L1` and `L2`, it can be defined that `P = L1` and `R = L2-L1`. Therefore the point of intersection (`X`) lies on the line segment from `L1` to `L2` if `0 <= t <= 1`.  
The same relation applies to `u` and `S`.

The following function implements the above algorithm using [`pygame.math.Vector2`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2) objects of the [`pygame.math`](https://www.pygame.org/docs/ref/math.html) module:

```py
def intersect_line_line_vec2(startObs, endObs, origin, endpoint):
    P = pygame.Vector2(startObs)
    R = (endObs - P)
    Q = pygame.Vector2(origin)
    S = (endpoint - Q)
    d = R.dot((S.y, -S.x))
    if d == 0:
        return None
    t = (Q-P).dot((S.y, -S.x)) / d 
    u = (Q-P).dot((R.y, -R.x)) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        X  =  P + R * t
        return (X.x, X.y)
    return None
```

The same algorithm without the use of the [`pygame.math`](https://www.pygame.org/docs/ref/math.html) module, less readable but more or less the same:

```py
def intersect_line_line(P0, P1, Q0, Q1):  
    d = (P1[0]-P0[0]) * (Q1[1]-Q0[1]) + (P1[1]-P0[1]) * (Q0[0]-Q1[0]) 
    if d == 0:
        return None
    t = ((Q0[0]-P0[0]) * (Q1[1]-Q0[1]) + (Q0[1]-P0[1]) * (Q0[0]-Q1[0])) / d
    u = ((Q0[0]-P0[0]) * (P1[1]-P0[1]) + (Q0[1]-P0[1]) * (P0[0]-P1[0])) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        return P1[0] * t + P0[0] * (1-t), P1[1] * t + P0[1] * (1-t)
    return None
```

## Rectangle and polygon

Related Stack Overflow questions:

- [Detecting collisions between polygons and rectangles in Pygame](https://stackoverflow.com/questions/64095396/detecting-collisions-between-polygons-and-rectangles-in-pygame/64106246#64106246)  
  ![Detecting collisions between polygons and rectangles in Pygame](../../screenshot/pygame_minimal_intersect_rectangle_polygon.gif)

  :scroll: **[Minimal example - Find the intersection of a rectangle and a polygon](../../examples/minimal_examples/pygame_minimal_intersect_circle_ellipse.py)**

## Circle and polygon

Related Stack Overflow questions:

- [How to make ball bounce off triangle in pygame?](https://stackoverflow.com/questions/54256104/how-to-make-ball-bounce-off-triangle-in-pygame)  
  ![How to make ball bounce off triangle in pygame?](https://i.stack.imgur.com/dAf8O.gif)

  :scroll: **[Minimal example - Let a ball bounce off a triangle](../../examples/minimal_examples/pygame_minimal_intersect_circle_triangle.py)**

## Circle and circle

Related Stack Overflow questions:

- [Pygame how to let balls collide](https://stackoverflow.com/questions/63145493/pygame-how-to-let-balls-collide)  
  ![Pygame how to let balls collide](https://i.stack.imgur.com/pNzMb.gif)

  :scroll: **[Minimal example - Make circles bounce off each other](../../examples/minimal_examples/pygame_minimal_intersect_circle_circle_1.py)**

- [pygame Get the balls to bounce off each other](https://stackoverflow.com/questions/63586822/pygame-get-the-balls-to-bounce-off-each-other)  
  ![pygame Get the balls to bounce off each other](https://i.stack.imgur.com/dlD4v.gif)

  :scroll: **[Minimal example - Make balls bounce off each other](../../examples/minimal_examples/pygame_minimal_intersect_circle_circle_2.py)**

- [Collision detection / physics for simple game](https://stackoverflow.com/questions/59656983/collision-detection-physics-for-simple-game/59658289#59658289)  
  ![Collision detection / physics for simple game](https://i.stack.imgur.com/bqVOa.gif)
- [Pygame: How to make two objects stop moving once they collide](https://stackoverflow.com/questions/62054942/pygame-how-to-make-two-objects-stop-moving-once-they-collide/62068800#62068800)

## Circle and ellipse

Related Stack Overflow questions:

- [Collision detection between an ellipse and a circle](https://stackoverflow.com/questions/64107897/collision-detection-between-an-ellipse-and-a-circle/64108816#64108816)  
  ![Collision detection between an ellipse and a circle](https://i.stack.imgur.com/ITAxv.gif)

  :scroll: **[Minimal example - Find the intersection of a circle and a rectangle](../../examples/minimal_examples/pygame_minimal_intersect_circle_ellipse.py)**

```py
from math import pi, sin, cos, atan2, radians, copysign, sqrt
```

```py
class Ellipse:
    # [...]

    def pointFromAngle(self, a):
        c = cos(a)
        s = sin(a)
        ta = s / c  ## tan(a)
        tt = ta * self.rx / self.ry  ## tan(t)
        d = 1. / sqrt(1. + tt * tt)
        x = self.centre[0] + copysign(self.rx * d, c)
        y = self.centre[1] - copysign(self.ry * tt * d, s)
        return x, y
```
