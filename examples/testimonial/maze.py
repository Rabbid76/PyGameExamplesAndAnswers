import pygame, random

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

    def wall_left(self, i, j):
        return i < 1 or self.walls[i-1][j][0]
    def wall_right(self, i, j):
        return i >= self.size[0] or self.walls[i][j][0]
    def wall_top(self, i, j):
        return j < 1 or self.walls[i][j-1][1]
    def wall_bottom(self, i, j):
        return j >= self.size[0] or self.walls[i][j][1]

def draw_maze(surf, maze, x, y, l, color, width):
    lines = [((x, y), (x + l * len(maze.walls), y)), ((x, y), (x, y + l * len(maze.walls[0])))] 
    for i, row in enumerate(maze.walls):
        for j, cell in enumerate(row):
            if cell[0]: lines += [((x + i*l + l, y + j*l), (x + i*l + l, y + j*l + l))]
            if cell[1]: lines += [((x + i*l, y + j*l + l), (x + i*l + l, y + j*l + l))]
    for line in lines:
        pygame.draw.line(surf, color, *line, width)

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

maze = Maze()
player_rect = pygame.Rect(190, 190, 20, 20)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    maze_pos = 20, 20
    cell_size = 40
    i0 = (player_rect.left - maze_pos[0]) // cell_size 
    i1 = (player_rect.right - maze_pos[0]) // cell_size
    j0 = (player_rect.top - maze_pos[1]) // cell_size  
    j1 = (player_rect.bottom - maze_pos[1]) // cell_size  

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

    window.fill(0)
    draw_maze(window, maze, 20, 20, cell_size, (196, 196, 196), 3)
    pygame.draw.circle(window, (255, 255, 0), player_rect.center, player_rect.width//2)
    pygame.display.flip()

pygame.quit()
exit()