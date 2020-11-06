[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Vector

## Euclidean distance an length

Related Stack Overflow questions:

- [Trying to Make Slime Bombs and clear screen with spacebar](https://stackoverflow.com/questions/60515767/trying-to-make-slime-bombs-and-clear-screen-with-spacebar/60515933#60515933)
- [Im currently making a game with pygame and I need an explanation on some vector code](https://stackoverflow.com/questions/61670940/im-currently-making-a-game-with-pygame-and-i-need-an-explanation-on-some-vector/61674234#61674234)
- [PyGame, make the tank gun follow your cursor, also good collision implementation practices](https://stackoverflow.com/questions/62455073/pygame-make-the-tank-gun-follow-your-cursor-also-good-collision-implementation/62455339#62455339)

## Angle between vectors

Related Stack Overflow questions:

- [How to know the angle between two points?](https://stackoverflow.com/questions/42258637/how-to-know-the-angle-between-two-points)

In general, the angle of a vector _(x, y)_ can be calculated by `math.atan2(y, x)`. The vector can be defined by 2 points _(x1, y1)_ and _(x2, y2)_ on a line. Therefore the angle of the line is `math.atan2(y2-y1, x2-x1)`.
Be aware that the y-axis needs to be reversed (`-y` respectively `y1-y2`) because the y-axis is generally pointing up but in the PyGame coordinate system the y-axis is pointing down. The unit of the angle in the Python `math` module is [Radian](https://en.wikipedia.org/wiki/Radian), but the unit of the angle in PyGame functions like [`pygame.transform.rotate()`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate) is [Degree](https://en.wikipedia.org/wiki/Degree). Hence the angle has to be converted from Radians to Degrees by `math.degrees`:

```py
import math

def angle_of_vector(x, y):
    return math.degrees(math.atan2(-y, x))

def angle_of_line(x1, y1, x2, y2):
    return math.degrees(math.atan2(-y1-y2, x2-x1))
```

This can be simplified by using the [`angle_to`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.angle_to) method of the `pygame.math.Vector2` object. This method computes the angle between 2 vectors in the PyGame coordinate system in degrees. Therefore it is not necessary to reverse the y-axis and convert from radians to degrees. Just calculate the angle between the vector and _(1, 0)_:

```py
def angle_of_vector(x, y):
    return pygame.math.Vector2(x, y).angle_to((1, 0))

def angle_of_line(x1, y1, x2, y2):
    return angle_of_vector(x2-x1, y2-y1)
```

:scroll: **[Minimal example - Calculate angle of vector animation](../../examples/minimal_examples/pygame_minimal_vector_angle_of_vector.py)**

![How to know the angle between two points?](https://i.stack.imgur.com/Sb5p3.gif)

[`angle_to`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.angle_to) can be used to calculate the angle between 2 vectors or lines:

```py
def angle_between_vectors(x1, y1, x2, y2):
    return pygame.math.Vector2(x1, y1).angle_to((x2, y2))
```

:scroll: **[Minimal example - Calculate angle between vector animation](../../examples/minimal_examples/pygame_minimal_vector_angle_between_vectors.py)**

![How to know the angle between two points?](https://i.stack.imgur.com/fW3WH.gif)

## Dot product

Related Stack Overflow questions:

- [Pygame how to find the nearest sprite in an array and lock onto it?](https://stackoverflow.com/questions/55579764/pygame-how-to-find-the-nearest-sprite-in-an-array-and-lock-onto-it/55580166#55580166)
- [converting the difference in vectors to between 0 and 1](https://stackoverflow.com/questions/64017147/converting-the-difference-in-vectors-to-between-0-and-1/64017259#64017259)  
- [Pygame - Find which side hit during collision between two rectangles](https://stackoverflow.com/questions/55711053/pygame-find-which-side-hit-during-collision-between-two-rectangles/55711895#55711895)
- [How to plot circles every 20 pixels between two randomly generated points in Pygame?](https://stackoverflow.com/questions/56245338/how-to-plot-circles-every-20-pixels-between-two-randomly-generated-points-in-pyg/56245525#56245525)
- [How do I make an object spawned from the edge of the map follow a diagonal line towards the middle?](https://stackoverflow.com/questions/59726059/how-do-i-make-an-object-spawned-from-the-edge-of-the-map-follow-a-diagonal-line/59728884#59728884)
- [How to get the angle between two vectors in pygame?](https://stackoverflow.com/questions/62871041/how-to-get-the-angle-between-two-vectors-in-pygame/62871200#62871200)

I recommend to use [`pygame.math.Vector2`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2) and the function [`.distance_to()`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.distance_to) to calculate the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) distance between 2 points.  

```py
def chase(self):
    pos = pygame.math.Vector2(self.x, self.y)
    enemy = min([e for e in enemies], key=lambda e: pos.distance_to(pygame.math.Vector2(e.x, e.y)))
```

Explanation:

`lambda e: pos.distance_to(pygame.math.Vector2(e.x, e.y))` calcaultes the distance of the argument `e` to the `pygame.math.Vector2` object `pos`.  
[`min`](https://docs.python.org/3/library/functions.html#min) finds the minimum element in an [*iterable*](https://docs.python.org/3/glossary.html#term-iterable). The "minimum" value is given by the function which is set to the `key` argument.  

`pos` is initialized by the position of the `Missile`. For each element of `enemies` the distance to `pos` is calculated and the enemy which is closest to `pos` is returned by `min`.  

Of course this can be further simplified by manually calculating the squared euclidean distance:

```py
def chase(self):
    enemy = min([e for e in enemies], key=lambda e: pow(e.x-self.x, 2) + pow(e.y-self.y, 2))
```

The [Dot product](https://en.wikipedia.org/wiki/Dot_product) of 2 vectors is equal the *cosine* of the angle between the 2 vectors multiplied by the magnitude (length) of both vectors.

```lang-none
dot( A, B ) == | A | * | B | * cos( angle_A_B )
```

This follows, that the *dot* product of 2 unit vectors is equal the *cosine* of the angle between the 2 vectors, because the length of a [unit vector](https://en.wikipedia.org/wiki/Unit_vector) is 1.

```lang-none
uA = normalize( A )
uB = normalize( B )
cos( angle_A_B ) == dot( uA, uB )
```

[![A dot B](https://i.stack.imgur.com/HUIrX.png)](https://i.stack.imgur.com/HUIrX.png)

If 2 normalized vectors point in the same direction, then the dot product is 1, if the point in the opposite direction, the dot product is -1 and if the vectors are perpendicular then the dot product is 0.

In pygame the dot product can be computed by [`math.Vector2.dot()`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.dot). If `A` and `B` are [`pygame.math.Vector2`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2) objects:

```py
uA = A.normalize()
uB = B.normalize()
AdotB = uA.dot(uB)
```

## Reflection

Related Stack Overflow questions:

- [Angle Reflexion for bouncing ball in a circle](https://stackoverflow.com/questions/54543170/angle-reflexion-for-bouncing-ball-in-a-circle/54543878#54543878)
- [How do I determine a direction vector for a point on a circle to be away from a circle?](https://stackoverflow.com/questions/57678408/how-do-i-determine-a-direction-vector-for-a-point-on-a-circle-to-be-away-from-a/57678750#57678750)
- [Use vector2 in pygame. Collide with the window frame and restrict the ball to the rectangular area](https://stackoverflow.com/questions/60213103/use-vector2-in-pygame/60214064#60214064)  
  ![Use vector2 in pygame](https://i.stack.imgur.com/jbmJ1.gif)

  :scroll: **[Minimal example - Bball bounce off the frame](../../examples/minimal_examples/pygame_minimal_vector_reflect_frame.py)**

  <kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-BallBounceOffFrame](https://repl.it/@Rabbid76/PyGame-BallBounceOffFrame#main.py)</kbd>

Calculate the [reflection](https://en.wikipedia.org/wiki/Reflection_(mathematics)) vector to the incident vector on the circular surface.  
In the following formula `N` is the normal vector of the circle, `I` is the incident vector (the current direction vector of the bouncing ball) and `R` is the reflection vector (outgoing direction vector of the bouncing ball):

```lang-none
R = I - 2.0 * dot(N, I) * N.
```

Use the [`pygame.math.Vector2`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.normalize).

To calculate the normal vector, you' ve to know the "hit" point (`dvx`, `dvy`) and the center point of the circle (`cptx`, `cpty`): 

```py
circN = (pygame.math.Vector2(cptx - px, cpty - py)).normalize()
``` 

Calculate the reflection:

```py
vecR = vecI - 2 * circN.dot(vecI) * circN
```

The new angle can be calculated by [`math.atan2(y, x)`](https://docs.python.org/3/library/math.html):

```py
self.angle  = math.atan2(vecR[1], vecR[0])
```

## Rotate

Related Stack Overflow questions:

- [Python pygame - center axis rotation segment line](https://stackoverflow.com/questions/64446045/python-pygame-center-axis-rotation-segment-line/64446683#64446683)
  ![Python pygame - center axis rotation segment line](https://i.stack.imgur.com/C6EWg.gif)