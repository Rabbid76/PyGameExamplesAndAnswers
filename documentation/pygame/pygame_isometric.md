[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Scepticism is the first step towards truth."  
Denis Diderot, Pensées philosophiques

---

# Isometric

Related Stack Overflow quest

- [Draw a staggered isometric map with python](https://stackoverflow.com/questions/66568267/draw-a-staggered-isometric-map-with-python/66569330#66569330)  
- **[Get isometric tile mouse selection in Pygame](https://stackoverflow.com/questions/71336864/get-isometric-tile-mouse-selection-python/73996398#73996398)**

  📁 **[Minimal example - isometric grid](../../examples/minimal_examples/pygame_minimal_isometric_map.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) replit.com/@Rabbid76/Pygame-IsometircMap](https://replit.com/@Rabbid76/Pygame-IsometircMap#main.py)**

Define the corner points of the map:

```py
map_outline = [
    pygame.math.Vector2(left_x, left_y), 
    pygame.math.Vector2(top_x, top_y),
    pygame.math.Vector2(right_x, right_y,
    pygame.math.Vector2(bottom_x, bottom_y)
]
```

With this information you can calculate the x and y axis of the map:

```py
origin = map_outline[0]
x_axis = (map_outline[1] - map_outline[0]) / columns
y_axis = (map_outline[3] - map_outline[0]) / rows
```

![Get isometric tile mouse selection in Pygame](https://i.stack.imgur.com/76T75.png)

You can use the x-axis and the y-axis to calculate a point in the map as a function of the row and column:

```py
def transform(p, mat2x2):
    x = p[0] * mat2x2[0][0] + p[1] * mat2x2[1][0]
    y = p[0] * mat2x2[0][1] + p[1] * mat2x2[1][1]
    return pygame.math.Vector2(x, y)

p_position = transform((column + 0.5, row + 0.5), (x_axis, y_axis)) + origin
```

![Get isometric tile mouse selection in Pygame](https://i.stack.imgur.com/ME2Xc.gif)

If you want to get the row and column depending on the mouse cursor, you need to do the opposite. You need to calculate the [inverse 2x2 matrix](https://en.wikipedia.org/wiki/Invertible_matrix) from the x and y axis. Using the inverse matrix, you can calculate the row and column as a function of a point on the map:

```py
def inverseMat2x2(m):
    a, b, c, d = m[0].x, m[0].y, m[1].x, m[1].y
    det = 1 / (a*d - b*c)
    return [(d*det, -b*det), (-c*det, a*det)]

m_pos = pygame.mouse.get_pos()
m_grid_pos = transform(pygame.math.Vector2(m_pos) - origin, point_to_grid)
m_col, m_row = int(m_grid_pos[0]), int(m_grid_pos[1])
```

![Get isometric tile mouse selection in Pygame](https://i.stack.imgur.com/AE7IS.gif)

## Isometric cube

Related Stack Overflow quest

- [How to create a rhomboid in pygame](https://stackoverflow.com/questions/73651474/how-to-create-a-rhomboid-in-pygame/73652102#73652102)  
  ![How to create a rhomboid in pygame](https://i.stack.imgur.com/TRKlB.gif)  

  📁 **[Minimal example - isometric cube](../../examples/minimal_examples/pygame_minimal_isometric_cube.py)**
