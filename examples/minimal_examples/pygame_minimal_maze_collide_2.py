# How do I prevent the player from moving through the walls in a maze in pygame?
# https://stackoverflow.com/questions/68691507/how-do-i-prevent-the-player-from-moving-through-the-walls-in-a-maze-in-pygame/68691508#68691508
#
# GitHub - PyGameExamplesAndAnswers - Maze
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_maze.md
#
# https://replit.com/@Rabbid76/PyGame-Maze-MaskCollision

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

maze_pos = 20, 20
cell_size = 40
maze = Maze()
maze_surf = pygame.Surface((maze.size[0]*cell_size, maze.size[1]*cell_size), pygame.SRCALPHA)
draw_maze(maze_surf, maze, 0, 0, cell_size, (196, 196, 196), 3)
maze_mask = pygame.mask.from_surface(maze_surf)

player_rect = pygame.Rect(190, 190, 20, 20)
player_surf = pygame.Surface(player_rect.size, pygame.SRCALPHA)
pygame.draw.circle(player_surf, (255, 255, 0), (player_rect.width//2, player_rect.height//2), player_rect.width//2)
player_mask = pygame.mask.from_surface(player_surf)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    new_rect = player_rect.move(
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 3,  
        (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 3)

    offset = (new_rect.x - maze_pos[0]), (new_rect.y - maze_pos[1])
    if not maze_mask.overlap(player_mask, offset):
        player_rect = new_rect

    window.fill(0)
    window.blit(maze_surf, maze_pos)
    window.blit(player_surf, player_rect)
    pygame.display.flip()

pygame.quit()
exit()
