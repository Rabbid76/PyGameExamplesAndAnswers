[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Redundant comments are just places to collect lies and misinformation."  
Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

# Snake

## Snake movement

Related Stack Overflow questions:

- **[How do I chain the movement of a snake's body?](https://stackoverflow.com/questions/62010434/how-do-i-chain-the-movement-of-a-snakes-body/62010435#62010435)**  
  ![1](https://i.stack.imgur.com/z9D7B.png)![2](https://i.stack.imgur.com/ZpKnj.gif)  
  ![3](https://i.stack.imgur.com/o1sqa.png)![4](https://i.stack.imgur.com/Q6zUm.gif)

- [Python Snake Game snake does not follow](https://stackoverflow.com/questions/71054349/python-snake-game-snake-does-not-follow/71055045#71055045)  
  ![Python Snake Game snake does not follow](https://i.stack.imgur.com/2WVYH.gif)  

- [Snake segments that “flow” rather than “snap” to the snake's head position](https://stackoverflow.com/questions/54273041/python-snake-segments-that-flow-rather-than-snap-to-the-snakes-head-positi/54276792#54276792)  
  ![Snake segments that “flow” rather than “snap” to the snake's head position](https://i.stack.imgur.com/m4kJK.gif)

- [pygame.Rect.move_ip() not updating rect attribute](https://stackoverflow.com/questions/55036397/pygame-rect-move-ip-not-updating-rect-attribute/55046457#55046457)  
  ![pygame.Rect.move_ip() not updating rect attribute](https://i.stack.imgur.com/bMMK1.gif)

- [Snake Length in a Pygame Snake Game](https://stackoverflow.com/questions/55187822/snake-length-in-a-pygame-snake-game/55188306#55188306)  
  ![Snake Length in a Pygame Snake Game](https://i.stack.imgur.com/KdtpV.gif)

- [Adding length to the snake in snake game](https://stackoverflow.com/questions/56079171/adding-length-to-the-snake-in-snake-game/56079666#56079666)  
  ![Adding length to the snake in snake game](https://i.stack.imgur.com/AGr5q.gif)

- [Making snake with pygame. Having trouble making the snake longer when it touches the cooki](https://stackoverflow.com/questions/56927685/making-snake-with-pygame-having-trouble-making-the-snake-longer-when-it-touches/56939007#56939007)  
  ![Making snake with pygame. Having trouble making the snake longer when it touches the cooki](https://i.stack.imgur.com/OO76R.gif)

- [Pygame Snake Randomly Colliding with Self](https://stackoverflow.com/questions/58595706/pygame-snake-randomly-colliding-with-self/58596035#58596035)

- [Snake bodies not appending to snake correctly](https://stackoverflow.com/questions/60925569/snake-bodies-not-appending-to-snake-correctly/60934394#60934394)  
  ![Snake bodies not appending to snake correctly](https://i.stack.imgur.com/vUDx7.gif)

- [how to solve bug on snake wall teleportation](https://stackoverflow.com/questions/64624092/how-to-solve-bug-on-snake-wall-teleportation/64624385#64624385)

- [Can anyone tell me how to increase the snake size in my code?](https://stackoverflow.com/questions/65465695/can-anyone-tell-me-how-to-increase-the-snake-size-in-my-code/65466064#65466064)  
  ![Can anyone tell me how to increase the snake size in my code?](https://i.stack.imgur.com/bSk2B.gif)

- [how to control snake with only two keys i.e left and right](https://stackoverflow.com/questions/61862293/how-to-control-snake-with-only-two-keys-i-e-left-and-right/61863664#61863664)

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

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-SnakeMoveInGrid](https://replit.com/@Rabbid76/PyGame-SnakeMoveInGrid#main.py)**

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

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-SnakeMoveFree](https://replit.com/@Rabbid76/PyGame-SnakeMoveFree#main.py)**

![4](https://i.stack.imgur.com/Q6zUm.gif)

## Change direction

Related Stack Overflow questions:

- [How to disbale certain key when another key is pressed in pygame](https://stackoverflow.com/questions/70591779/how-to-disbale-certain-key-when-another-key-is-pressed-in-pygame/70592433#70592433)
- [how to control snake with only two keys i.e left and right](https://stackoverflow.com/questions/61862293/how-to-control-snake-with-only-two-keys-i-e-left-and-right/61863664#61863664)

## Snake collision

Related Stack Overflow questions:

- [How to detect and end game when a pygame sprite runs into its tail (using screen.get_at)?](https://stackoverflow.com/questions/54331922/how-to-detect-and-end-game-when-a-pygame-sprite-runs-into-its-tail-using-screen/54332544#54332544)  
  ![How to detect and end game when a pygame sprite runs into its tail (using screen.get_at)?](https://i.stack.imgur.com/PS4sx.gif)

- [How to detect if a rectangle is in another rectangle if they are both moving?](https://stackoverflow.com/questions/54920547/how-to-detect-if-a-rectangle-is-in-another-rectangle-if-they-are-both-moving/54930341#54930341)

- [Pygame Automation snake refuses to crash wall?](https://stackoverflow.com/questions/60015363/pygame-automation-snake-refuses-to-crash-wall/60015444#60015444)

## Spawn food

Related Stack Overflow questions:

- [Pygame Snake - Apple spawning inside snake](https://stackoverflow.com/questions/54429340/pygame-snake-apple-spawning-inside-snake/54466752#54466752)

## Miscellaneous

Related Stack Overflow questions:

- [Pygame window remains blank (OSX)](https://stackoverflow.com/questions/54605669/pygame-window-remains-blank-osx?noredirect=1)
- [Python Snake Game Finalization Issues](https://stackoverflow.com/questions/55424698/python-snake-game-finalization-issues/55424989#55424989)
- [Trouble with game over screen for Python game with Pygame](https://stackoverflow.com/questions/55436131/trouble-with-game-over-screen-for-python-game-with-pygame/55439324#55439324)
- [replacing cubes with images in snake](https://stackoverflow.com/questions/56108527/replacing-cubes-with-images-in-snake/56117700#56117700)
- [Black window pygame](https://stackoverflow.com/questions/56491605/black-window-pygame/56491726#56491726)
- [Pygame snake velocity too high when the fps above 15](https://stackoverflow.com/questions/61034515/pygame-snake-velocity-too-high-when-the-fps-above-15/61034931#61034931)