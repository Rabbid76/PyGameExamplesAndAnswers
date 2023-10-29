[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"I'm a programmer. I like programming. And the best way I've found to have a positive impact on code is to write it."  
Robert C. Martin, Clean Architecture

---

# Move towards target

## Shoot a bullet in a certain direction - Rotate player and shoot bullet towards faced direction

Related Stack Overflow questions:

- [How to move a sprite according to an angle in Pygame](https://stackoverflow.com/questions/46697502/how-to-move-a-sprite-according-to-an-angle-in-pygame/68698440#68698440)  
  ![How to move a sprite according to an angle in Pygame](https://i.stack.imgur.com/HBVPx.gif)

- [How can you rotate the sprite and shoot the bullets towards the mouse position?](https://stackoverflow.com/questions/59126785/how-can-you-rotate-the-sprite-and-shoot-the-bullets-towards-the-mouse-position/59126918#59126918)  
  ![How can you rotate the sprite and shoot the bullets towards the mouse position?](https://i.stack.imgur.com/zGoZr.gif)

  :scroll: **[Minimal example - Rotate player and shoot bullet towards faced direction 1](../../examples/minimal_examples/pygame_minimal_rotate_to_target_fire_bullet_1.py)**

- [calculating direction of the player to shoot PyGmae](https://stackoverflow.com/questions/60464828/calculating-direction-of-the-player-to-shoot-pygame/60465212#60465212)  
  ![calculating direction of the player to shoot PyGmae](https://i.stack.imgur.com/3F8Mt.gif)

  :scroll: **[Minimal example - Rotate player and shoot bullet towards faced direction 2](../../examples/minimal_examples/pygame_minimal_rotate_to_target_fire_bullet_2.py)**

- [How do you point the barrel towards mouse in pygame?](https://stackoverflow.com/questions/70283340/how-do-you-point-the-barrel-towards-mouse-in-pygame/70318324#70318324)
  ![How do you point the barrel towards mouse in pygame?](https://i.stack.imgur.com/dmBVe.gif)

- [Moving forward after angle change. Pygame](https://stackoverflow.com/questions/61106297/moving-forward-after-angle-change-pygame/61106823#61106823)  
  ![Moving forward after angle change. Pygame](https://i.stack.imgur.com/A7RFW.gif)

- [Firing particles from a player at a constant speed with cos() and sin() in python pygame](https://stackoverflow.com/questions/64993388/firing-particles-from-a-player-at-a-constant-speed-with-cos-and-sin-in-pytho/64994334#64994334)

## Shoot bullets towards target or mouse

Related Stack Overflow questions:

- **[Shooting a bullet in pygame in the direction of mouse](https://stackoverflow.com/questions/59977052/shooting-a-bullet-in-pygame-in-the-direction-of-mouse/59980344#59980344)**  
  ![Shooting a bullet in pygame in the direction of mouse](https://i.stack.imgur.com/oyzor.gif)

  :scroll: **[Minimal example - shoot bullet towards mouse](../../examples/minimal_examples/pygame_minimal_move_to_target_fire_bullet_1.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-FireBulletInDirectionOfMouse](https://replit.com/@Rabbid76/PyGame-FireBulletInDirectionOfMouse#main.py)**

- [How to shoot a projectile in the way the player is looking in a TDS](https://stackoverflow.com/questions/68970922/how-to-shoot-a-projectile-in-the-way-the-player-is-looking-in-a-tds/68971138#68971138)  
  ![How to shoot a projectile in the way the player is looking in a TDS](https://i.stack.imgur.com/04Uou.gif)

- [How Can I Make An Arrow Image Move Rotated Direction?](https://stackoverflow.com/questions/65589860/how-can-i-make-an-arrow-image-move-rotated-direction/65592518#65592518)

- [How to make my rectangle rotate with a rotating sprite](https://stackoverflow.com/questions/65622705/how-to-make-my-rectangle-rotate-with-a-rotating-sprite/65640631#65640631)  
  ![How to make my rectangle rotate with a rotating sprite](https://i.stack.imgur.com/ocqjL.gif)

[`pygame.transform.rotate`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate) does not transform the object itself, but creates a new rotated surface and returns it.

If you want to fire a bullet in a certain direction, the direction is defined the moment the bullet is fired, but it does not change continuously.  
When the bullet is fired, set the starting position of the bullet and calculate the direction vector to the mouse position:

```py
self.pos = (x, y)
mx, my = pygame.mouse.get_pos()
self.dir = (mx - x, my - y)
```

The direction vector should not depend on the distance to the mouse, but it has to be a [Unit vector](https://en.wikipedia.org/wiki/Unit_vector).
Normalize the vector by dividing by the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)

```py
length = math.hypot(*self.dir)
if length == 0.0:
    self.dir = (0, -1)
else:
    self.dir = (self.dir[0]/length, self.dir[1]/length)
```

Compute the angle of the vector and rotate the bullet. In general, the angle of a vector can be computed by `atan2(y, x)`. The y-axis needs to be reversed (`atan2(-y, x)`) as the y-axis generally points up, but in the PyGame coordinate system the y-axis points down (see [How to know the angle between two vectors?](https://stackoverflow.com/questions/42258637/how-to-know-the-angle-between-two-vectors/64563327#64563327)):

```py
angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

self.bullet = pygame.Surface((7, 2)).convert_alpha()
self.bullet.fill((255, 255, 255))
self.bullet = pygame.transform.rotate(self.bullet, angle)
```

To update the position of the bullet, it is sufficient to scale the direction (by a velocity) and add it to the position of the bullet:

```py
self.pos = (self.pos[0]+self.dir[0]*self.speed,
            self.pos[1]+self.dir[1]*self.speed)
```

To draw the rotated bullet in the correct position, take the bounding rectangle of the rotated bullet and set the center point with `self.pos` (see [How do I rotate an image around its center using PyGame?](https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144)):

```py
bullet_rect = self.bullet.get_rect(center = self.pos)
surf.blit(self.bullet, bullet_rect)  
```

## Follow target or mouse

### Enemy follow

Related Stack Overflow questions:

- [Pygame make sprite walk in given rotation](https://stackoverflow.com/questions/66402816/pygame-make-sprite-walk-in-given-rotation/66403030#66403030)  
  ![Pygame make sprite walk in given rotation](https://i.stack.imgur.com/SyPzP.gif)

  :scroll: **[Minimal example - Move to mouse](../../examples/minimal_examples/pygame_minimal_move_follow_4.py)**

- [pygame 2 dimensional movement of an enemy towards the player, how to calculate x and y velocity?](https://stackoverflow.com/questions/66404707/pygame-2-dimensional-movement-of-an-enemy-towards-the-player-how-to-calculate-x/66406985#66406985)  
  ![pygame 2 dimensional movement of an enemy towards the player, how to calculate x and y velocity?](https://i.stack.imgur.com/PNKiu.gif)

  :scroll: **[Minimal example - Follow moving target](../../examples/minimal_examples/pygame_minimal_move_follow_5.py)**

- [Pygame: Image chasing the mouse cursor from certain length](https://stackoverflow.com/questions/55168892/pygame-image-chasing-the-mouse-cursor-from-certain-length/55169273#55169273)

  :scroll: **[Minimal example - Follow target](../../examples/minimal_examples/pygame_minimal_move_follow_1.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-FollowMouse](https://replit.com/@Rabbid76/PyGame-FollowMouse#main.py)**

- [How to make an enemy follow the player in pygame?](https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame/73511789#73511789)  
- **[How to make smooth movement in pygame](https://stackoverflow.com/questions/64087982/how-to-make-smooth-movement-in-pygame/64088747#64088747)**  
  [Sprite follow another flexible way within certain distance limits](https://stackoverflow.com/questions/60064644/sprite-follow-another-flexible-way-within-certain-distance-limits/60082313#60082313)  
  ![How to make smooth movement in pygame](https://i.stack.imgur.com/9HL3b.gif)

  :scroll: **[Minimal example - Follow target smoothly](../../examples/minimal_examples/pygame_minimal_move_follow_smoothly.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-FollowMouseSmoothly](https://replit.com/@Rabbid76/PyGame-FollowMouseSmoothly#main.py)**

- **[how to make particles follow my mouse in pygame](https://stackoverflow.com/questions/63412401/how-to-make-particles-follow-my-mouse-in-pygame/63412536#63412536)**
- [How can i make a block follow another block in pygame](https://stackoverflow.com/questions/59799575/how-can-i-make-a-block-follow-another-block-in-pygame/59799746#59799746)

- [Track Mouse Movement while confined](https://stackoverflow.com/questions/64491342/track-mouse-movement-while-confined/65378782#65378782)  
  ![Track Mouse Movement while confined](https://i.stack.imgur.com/uaesh.gif)

- [Teach enemy that the way thru screen border is shorter than going all over the screen](https://stackoverflow.com/questions/69674788/teach-enemy-that-the-way-thru-screen-border-is-shorter-than-going-all-over-the-s)  
  ![Teach enemy that the way thru screen border is shorter than going all over the screen](https://i.stack.imgur.com/czBUc.gif)

- [How to make the ball rotate in pygame, python?](https://stackoverflow.com/questions/74214342/how-to-make-the-ball-rotate-in-pygame-python/74218983#74218983)  
  ![How to make the ball rotate in pygame, python?](https://i.stack.imgur.com/CcQQ8.gif)

For a more sophisticated solution, you've to compute the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) form the point to the target. Use [`pygame.math.Vector2`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2) for the computation.

Compute the distance from between the follower and the sprite and the unit direction vector from (`follower_x`, `follower_y`) to (`mainsprite_x`, `mainsprite_y`). The [Unit Vector](https://en.wikipedia.org/wiki/Unit_vector) can be computed by dividing the direction vector by the distance or by normalizing ([`normalize()`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.normalize)) the direction vector:

```py
target_vector = Vector2(mainsprite_x, mainsprite_y)
follower_vector = Vector2(follower_x, follower_y)

distance = follower_vector.distance_to(target_vector)
direction_vector = target_vector - follower_vector
if distance > 0:
    direction_vector /= distance
```

Now you can define an exact `step_distance` and move to follower int direction of the sprite:

```py
if distance > 0:
    new_follower_vector = follower_vector + direction_vector * step_distance.
```

Define a `maximum_distance` and a `minimum_distance`. The minimum step distance is:

```py
min_step = max(0, distance - maximum_distance)
```

The maximum  step distance is

```py
max_step = distance - minimum_distance
```

Put it all together:

```py
minimum_distance    = 0
maximum_distance    = 10000
target_vector       = Vector2(mainsprite_x, mainsprite_y)
follower_vector     = Vector2(follower_x, follower_y)
new_follower_vector = Vector2(follower_x, follower_y)

distance = follower_vector.distance_to(target_vector)
if distance > minimum_distance:
    direction_vector    = (target_vector - follower_vector) / distance
    min_step            = max(0, distance - maximum_distance)
    max_step            = distance - minimum_distance
    step_distance       = min_step + (max_step - min_step) * LERP_FACTOR
    new_follower_vector = follower_vector + direction_vector * step_distance
```

:scroll: **[Minimal example - Follow target smoothly](../../examples/minimal_examples/pygame_minimal_move_follow_smoothly.py)**

![How to make smooth movement in pygame](https://i.stack.imgur.com/9HL3b.gif)

:scroll: **[Minimal example - Ball follow ball](../../examples/minimal_examples/pygame_minimal_move_follow_2.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-FollowBall](https://replit.com/@Rabbid76/PyGame-FollowBall#main.py)**

![Minimal example - Ball follow ball](../../screenshot/pygame_minimal_move_follow_2.gif)

:scroll: **[Minimal example - Object follow target](../../examples/minimal_examples/pygame_minimal_move_follow_3.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-FollowInGrid](https://replit.com/@Rabbid76/PyGame-FollowInGrid#main.py)**

![Minimal example - Object follow target](../../screenshot/pygame_minimal_move_follow_3.gif)
