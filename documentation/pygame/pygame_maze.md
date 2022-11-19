[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Maze

- [Hide and Seek/Maze game in pygame not working](https://stackoverflow.com/questions/63853997/hide-and-seek-maze-game-in-pygame-not-working/63854295#63854295)  
  ![scene](https://i.stack.imgur.com/2QYir.gif)

- [Pygame Maze Game not creating levels correctly](https://stackoverflow.com/questions/59436266/pygame-maze-game-not-creating-levels-correctly/59436430#59436430)

- [How do I move elements of a matrix in python?](https://stackoverflow.com/questions/65174955/how-do-i-move-elements-of-a-matrix-in-python/65178270#65178270)  
  ![How do I move elements of a matrix in python?](https://i.stack.imgur.com/QgD5t.gif)

- [How do I randomly move objects in a maze using pygame?](https://stackoverflow.com/questions/65189546/how-do-i-randomly-move-objects-in-a-maze-using-pygame/65190004#65190004)  
  ![How do I randomly move objects in a maze using pygame?](https://i.stack.imgur.com/C7gft.gif)

- [How I make my python code delete the pills from my pac man game?](https://stackoverflow.com/questions/65201227/how-i-make-my-python-code-delete-the-pills-from-my-pac-man-game/65204858#65204858)  
  ![How I make my python code delete the pills from my pac man game?](https://i.stack.imgur.com/aO99q.gif)

## Maze collision detection

Related Stack Overflow questions:

- [Collision for Pygame Game Map](https://stackoverflow.com/questions/65887274/collision-for-pygame-game-map/65888081#65888081)  

- [Adding collision to maze walls](https://stackoverflow.com/questions/55833941/adding-collision-to-maze-walls/55837809#55837809)  
  ![Adding collision to maze walls](https://i.stack.imgur.com/EUDwK.gif)

  :scroll: **[Minimal example - Maze generator](../../examples/minimal_examples/pygame_minimal_maze_1.py)**

- [How to implement barriers to stop the player moving through walls](https://stackoverflow.com/questions/65124664/how-to-implement-barriers-to-stop-the-player-moving-through-walls/65130719#65130719)  
  ![How to implement barriers to stop the player moving through walls](https://i.stack.imgur.com/WKJ5K.gif)

  :scroll: **[Minimal example - Maze generator 2](../../examples/minimal_examples/pygame_minimal_maze_2.py)**

- [Creating collisions between a Sprite and a list (that aren't sprites) in a Maze](https://stackoverflow.com/questions/68665022/creating-collisions-between-a-sprite-and-a-list-that-arent-sprites-in-a-maze/68668529#68668529)  
  ![Creating collisions between a Sprite and a list (that aren't sprites) in a Maze](https://i.stack.imgur.com/5aYT2.gif)  

- [How do I prevent the player from moving through the walls in a maze in pygame?](https://stackoverflow.com/questions/68691507/how-do-i-prevent-the-player-from-moving-through-the-walls-in-a-maze-in-pygame/68691536#68691536)

I have a maze organized in a grid. Each cell of the grid stores the information about the walls to its right and bottom neighboring cell. The player is an object of a certain size whose bounding box is known. I want to move the player smoothly through the maze with the walls preventing them from going through.

![move player in maze](https://i.stack.imgur.com/2JBsh.png)

```py
class Maze:
    def __init__(self, rows = 9, columns = 9):
        self.size = (columns, rows)
        self.walls = [[[True, True] for _ in range(self.size[1])] for __ in range(self.size[0])]
        visited = [[False for _ in range(self.size[1])] for __ in range(self.size[0])]
        i, j = (self.size[0]+1) // 2, (self.size[1]+1) // 2
        visited[i][j] = True
        stack = [(i, j)]
        while stack:
            current = stack.pop()
            i, j = current
            nl = [n for n in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] 
                  if 0 <= n[0] < self.size[0] and 0 <= n[1] < self.size[1] and not visited[n[0]][n[1]]]
            if nl:
                stack.insert(0, current)
                next = random.choice(nl)
                self.walls[min(next[0], current[0])][min(next[1], current[1])][abs(next[1]-current[1])] = False
                visited[next[0]][next[1]] = True
                stack.insert(0, next)
```

There are several solutions to this problem. Implement simple logic that tests if there is a wall in the player's path when the player moves. Discard the movement when a collision with a wall is detected.

Add methods to the `Maze` class that check for a wall between a cell and its neighboring cell:

```py
class Maze:
    # [...]

    def wall_left(self, i, j):
        return i < 1 or self.walls[i-1][j][0]
    def wall_right(self, i, j):
        return i >= self.size[0] or self.walls[i][j][0]
    def wall_top(self, i, j):
        return j < 1 or self.walls[i][j-1][1]
    def wall_bottom(self, i, j):
        return j >= self.size[0] or self.walls[i][j][1]
```

Calculate the rows and columns of the corner points of the player's bounding box.

```py
i0 = (player_rect.left - maze_pos[0]) // cell_size 
i1 = (player_rect.right - maze_pos[0]) // cell_size
j0 = (player_rect.top - maze_pos[1]) // cell_size  
j1 = (player_rect.bottom - maze_pos[1]) // cell_size  
```

As the player moves, test to see if the player is entering a new cell. Use the new methods in the `Maze` class to test whether there is a wall in the player's path. Skip the movement if the path is blocked by a wall:

```py
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    new_rect = player_rect.move(-3, 0)
    ni = (new_rect.left - maze_pos[0]) // cell_size
    if i0 == ni or not (maze.wall_left(i0, j0) or maze.wall_left(i0, j1) or (j0 != j1 and maze.wall_bottom(ni, j0))):
        player_rect = new_rect
if keys[pygame.K_RIGHT]:
    new_rect = player_rect.move(3, 0)
    ni = (new_rect.right - maze_pos[0]) // cell_size
    if i1 == ni or not (maze.wall_right(i1, j0) or maze.wall_right(i1, j1) or (j0 != j1 and maze.wall_bottom(ni, j0))):
        player_rect = new_rect
keys = pygame.key.get_pressed()
if keys[pygame.K_UP]:
    new_rect = player_rect.move(0, -3)
    nj = (new_rect.top - maze_pos[1]) // cell_size
    if j0 == nj or not (maze.wall_top(i0, j0) or maze.wall_top(i1, j0) or (i0 != i1 and maze.wall_right(i0, nj))):
        player_rect = new_rect
if keys[pygame.K_DOWN]:
    new_rect = player_rect.move(0, 3)
    nj = (new_rect.bottom - maze_pos[1]) // cell_size
    if j1 == nj or not (maze.wall_bottom(i0, j1) or maze.wall_bottom(i1, j1) or (i0 != i1 and maze.wall_right(i0, nj))):
        player_rect = new_rect
```

![maze move - collision logic](https://i.stack.imgur.com/LG0Xm.gif)

:scroll: **[Minimal example - Maze collision detection with logic](../../examples/minimal_examples/pygame_minimal_maze_collide_1.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-Maze-CollisionLogic](https://replit.com/@Rabbid76/PyGame-Maze-CollisionLogic#main.py)**

Another solution is to use mask collision. Draw the maze of a transparent [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html):

```py
cell_size = 40
maze = Maze()
maze_surf = pygame.Surface((maze.size[0]*cell_size, maze.size[1]*cell_size), pygame.SRCALPHA)
draw_maze(maze_surf, maze, 0, 0, cell_size, (196, 196, 196), 3)
```

Crate a [`pygame.Mask`](https://www.pygame.org/docs/ref/mask.html) from the _Surface_ with  [`pygame.mask.from_surface`](https://www.pygame.org/docs/ref/mask.html#pygame.mask.from_surface):

```py
maze_mask = pygame.mask.from_surface(maze_surf)
```

Create a mask form the player:

```py
player_rect = pygame.Rect(190, 190, 20, 20)
player_surf = pygame.Surface(player_rect.size, pygame.SRCALPHA)
pygame.draw.circle(player_surf, (255, 255, 0), (player_rect.width//2, player_rect.height//2), player_rect.width//2)
player_mask = pygame.mask.from_surface(player_surf)
```

Calculate the new position of the player:

```py
keys = pygame.key.get_pressed()
new_rect = player_rect.move(
    (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 3,  
    (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 3)
```

Use [`pygame.mask.Mask.overlap`](https://www.pygame.org/docs/ref/mask.html#pygame.mask.Mask.overlap) to see if the masks are intersects (see [Pygame collision with masks](https://stackoverflow.com/questions/57455811/pygame-collision-with-masks/57499484#57499484)). Skip the movement when the mask of the maze intersects the player's mask:

```py
offset = (new_rect.x - maze_pos[0]), (new_rect.y - maze_pos[1])
if not maze_mask.overlap(player_mask, offset):
    player_rect = new_rect
```

![maze move - mask collision](https://i.stack.imgur.com/PeY8C.gif)][1]

:scroll: **[Minimal example - Maze collision detection with mask](../../examples/minimal_examples/pygame_minimal_maze_collide_2.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-Maze-MaskCollision](https://replit.com/@Rabbid76/PyGame-Maze-MaskCollision#main.py)**