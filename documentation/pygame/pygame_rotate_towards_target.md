[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."
Martin Fowler (1999)

---

# Rotate towards target or mouse

Related Stack Overflow questions:

- **[How to rotate an image(player) to the mouse direction?](https://stackoverflow.com/questions/58603835/how-to-rotate-an-imageplayer-to-the-mouse-direction/58604116#58604116)**  
  [How do I make my player rotate towards mouse position?](https://stackoverflow.com/questions/56627414/how-do-i-make-my-player-rotate-towards-mouse-position/56627834#56627834)  
  [Still Having Problems With Rotating Cannon's Properly Towards The Player PyGame](https://stackoverflow.com/questions/62520375/still-having-problems-with-rotating-cannons-properly-towards-the-player-pygame)  
  [How do I make image rotate with mouse python](https://stackoverflow.com/questions/65573379/how-do-i-make-image-rotate-with-mouse-python/65575874#65575874)  
  ![How to rotate an image(player) to the mouse direction?](https://i.stack.imgur.com/0E6u6.gif)
  ![How do I make my player rotate towards mouse position?](https://i.stack.imgur.com/eOdjl.gif)
  ![Still Having Problems With Rotating Cannon's Properly Towards The Player PyGame](https://i.stack.imgur.com/PGm4q.gif)
  ![How do I make image rotate with mouse python](https://i.stack.imgur.com/B1CrI.gif)

  :scroll: **[Minimal example - Rotate surface towards mouse](../../examples/minimal_examples/pygame_minimal_rotate_to_target_1.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-RotateWithMouse](https://replit.com/@Rabbid76/PyGame-RotateWithMouse#main.py)**
  
  - [PyGame move drawn rect(not image) in the same way as the player, including rotation](https://stackoverflow.com/questions/59549149/pygame-move-drawn-rectnot-image-in-the-same-way-as-the-player-including-rotat/59552025#59552025)  
  ![PyGame move drawn rect(not image) in the same way as the player, including rotation](https://i.stack.imgur.com/ItYvA.gif)

  :scroll: **[Minimal example - Rotate laser towards mouse](../../examples/minimal_examples/pygame_minimal_rotate_to_target_intersect_laser.py)**

- [How to rotate a triangle to a certain angle in PyGame?](https://stackoverflow.com/questions/58100335/how-to-rotate-a-triangle-to-a-certain-angle-in-pygame/58102259#58102259)  
  ![How to rotate a triangle to a certain angle in PyGame?](https://i.stack.imgur.com/wAXqi.gif)

  :scroll: **[Minimal example - Rotate triangle towards mouse](../../examples/minimal_examples/pygame_minimal_rotate_towards_mouse_triangle.py)**

- [player turns in wrong direction if angle is negative](https://stackoverflow.com/questions/61817913/player-turns-in-wrong-direction-if-angle-is-negative)  
  ![player turns in wrong direction if angle is negative](https://i.stack.imgur.com/xxADo.gif)

  :scroll: **[Minimal example - Slowly rotate triangle towards mouse](../../examples/minimal_examples/pygame_minimal_rotate_towards_mouse_triangle_slowly.py)**

You have to compute the angle of the vector from the player to the mouse. get the mouse position by [`pygame.mouse.get_pos()`](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pos) and the rectangle ([`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html)) around the player:

```py
mx, my = pygame.mouse.get_pos()
player_rect = Player_1.get_rect(topleft=(P_X,P_Y))
```

Calculate the vector from the player to the mouse  and compute the angle of vector by [`math.atan2`](https://docs.python.org/3/library/math.html). The y-axis needs to be reversed (`-dy`) as the y-axis is generally pointing up, but in the PyGame coordinate system the y-axis is pointing down.

```py
dx, dy = mx - player_rect.centerx, player_rect.centery - my
angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
```

In addition, a correction angle must be deducted (`- correction_angle`). The correction angle depends on the _Sprite_. If the _Sprite_

![left](../../resource/icon/arrow_right.png) is looking to the right, the correction angle is 0: `correction_angle = 0`  
![left](../../resource/icon/arrow_up.png) is looking up, the correction angle is 90: `correction_angle = 90`  
![left](../../resource/icon/arrow_left.png) is looking to the left, the correction angle is 180: `correction_angle = 180`  
![left](../../resource/icon/arrow_down.png) is looking down, the correction angle is 90: `correction_angle = 270`  

Rotate the player with [`pygame.transform.rotate()`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate) by the angle around its center:  
(See also [How do I rotate an image around its center using Pygame?](https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144))

```py
rot_image = pygame.transform.rotate(Player_1, angle)
rot_image_rect = rot_image.get_rect(center=player_rect.center)
```

![How do I make my player rotate towards mouse position?](https://i.stack.imgur.com/eOdjl.gif)

:scroll: **[Minimal example - Rotate surface towards mouse](../../examples/minimal_examples/pygame_minimal_rotate_to_target_1.py)**

In pygame 2 dimensional vector arithmetic is implemented in [`pygame.math.Vector2`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2).

Define a `Vector2` object for the mouse position and the center of the triangle. Calculate the angle of vector form the center point to the mouse position  ([`.angle_to()`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.angle_to)):

```py
vMouse  = pygame.math.Vector2(mouse_pos)
vCenter = pygame.math.Vector2(center)
angle   = pygame.math.Vector2().angle_to(vMouse - vCenter)
```

Define the 3 points of the triangle around the (0, 0) and rotate them by the angle ([`.rotate()`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.rotate))

```py
points = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
rotated_point = [pygame.math.Vector2(p).rotate(angle) for p in points]
```

To calculate the final points, the points have to b scaled and translated by the center  of the triangle:

```py
triangle_points = [(vCenter + p*scale) for p in rotated_point]
```

A version of the algorithm, without the use of [`pygame.math.Vector2`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2), looks as follows:

```py
def rotate_triangle(center, scale, mouse_pos):

    dx = mouse_pos[0] - center[0]
    dy = mouse_pos[1] - center[1]
    len = math.sqrt(dx*dx + dy*dy)
    len = math.hypot(dx, dy)
    if len > 0:
        dx, dy = (dx*scale/len, dy*scale/len) if len > 0 else (1, 0)

    pts = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
    pts = [(center[0] + p[0]*dx + p[1]*dy, center[1] + p[0]*dy - p[1]*dx) for p in pts]
    return pts
```

Note this version is probably faster. It needs a `math.sqrt` (or `math.hypot`) operation, in compare to `math.atan2` which is probably used by `.angle_to()` and `math.sin` respectively `math.cos` which is probably used by `.rotate()`, of the former algorithm.
The result coordinates are the same.

:scroll: **[Minimal example - Rotate triangle towards mouse](../../examples/minimal_examples/pygame_minimal_rotate_towards_mouse_triangle.py)**

![How to rotate a triangle to a certain angle in PyGame?](https://i.stack.imgur.com/wAXqi.gif)

:scroll: **[Minimal example - Slowly rotate triangle towards mouse](../../examples/minimal_examples/pygame_minimal_rotate_towards_mouse_triangle_slowly.py)**

![player turns in wrong direction if angle is negative](https://i.stack.imgur.com/xxADo.gif)
