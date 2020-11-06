[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)
---

# Snake


Related Stack Overflow questions:

- [How do I chain the movement of a snake's body?](https://stackoverflow.com/questions/62010434/how-do-i-chain-the-movement-of-a-snakes-body/62010435#62010435)  
  ![1](https://i.stack.imgur.com/z9D7B.png)![2](https://i.stack.imgur.com/ZpKnj.gif)  
  ![3](https://i.stack.imgur.com/o1sqa.png)![4](https://i.stack.imgur.com/Q6zUm.gif)

In general you have to distinguish between 2 different types of _snake_. In the first case, the snake moves in a grid and every time when the snake moves, it strides ahead one field in the grid. In the other type, the snakes position is not in a raster and not snapped on the fields of the grid, the position is free and the snake slides smoothly through the fields.  
In former each element of the body is snapped to the fields of the grid, as the head is. The other is more trick, because the position of a body element depends on the size of the element and the dynamic, previous positions of the snakes head.

First the _snake_, which is snapped to a grid.

The elements of the snake can be stored in a list of tuples.  Each tuple contains the column and row of the snakes element in the grid. The changes to the items in the list directly follow the movement of the snake. If the snake moves, a the new position is add to the head of the list and the tail of the list is removed.  

For instance we have a snake with the following elements:

```py
body = [(3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]
```

When the snakes head moves form `(3, 3)` to (`3, 2`), then the new head position is add to the head of the list (`body.insert(0, (3, 2)`):

```py
body = [(3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]
```

Finally the tail of the ist is removed (`del body[-1]`):

```py
body = [(3, 2), (3, 3), (3, 4), (4, 4), (5, 4)]
```

![1](https://i.stack.imgur.com/z9D7B.png)

:scroll: **[Minimal example](../../examples/minimal_examples/pygame_minimal_snake_move_grid.py)**

<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-SnakeMoveInGrid](https://repl.it/@Rabbid76/PyGame-SnakeMoveInGrid#main.py)</kbd>

![2](https://i.stack.imgur.com/ZpKnj.gif)

Now the _snake_ with completely free positioning.

We have to track all the positions which the snake's head has visited in a list. We have to place the elements of the snakes body on the positions in the list like the pearls of a chain.

![3](https://i.stack.imgur.com/o1sqa.png)

The key is, to compute the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between the last element of the body in the chain and the following positions on the track.
When an new point with a distance that is large enough is found, then an new pearl (element) is add to the chain (body).

```py
dx, dy = body[-1][0]-pos[0], body[-1][1]-pos[1]
if math.sqrt(dx*dx + dy*dy) >= distance:
    body.append(pos)
```

The following function has 3 arguments. `track` is the list of the head positions. `no_pearls` is then number of elements of the shakes body and `distance` is the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between the elements. The function creates and returns a list of the snakes body positions.

```py
def create_body(track, no_pearls, distance):
    body = [(track[0])]
    track_i = 1
    for i in range(1, no_pearls):
        while track_i < len(track):
            pos = track[track_i]
            track_i += 1
            dx, dy = body[-1][0]-pos[0], body[-1][1]-pos[1]
            if math.sqrt(dx*dx + dy*dy) >= distance:
                body.append(pos)
                break
    while len(body) < no_pearls:
        body.append(track[-1])
    del track[track_i:]
    return body
```

:scroll: **[Minimal example](../../examples/minimal_examples/pygame_minimal_snake_move_free.py)**

<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-SnakeMoveFree](https://repl.it/@Rabbid76/PyGame-SnakeMoveFree#main.py)</kbd>

![4](https://i.stack.imgur.com/Q6zUm.gif)