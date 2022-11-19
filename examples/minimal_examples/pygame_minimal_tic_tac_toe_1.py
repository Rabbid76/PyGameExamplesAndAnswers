# Pygame Tic Tak Toe Logic? How Would I Do It
# https://stackoverflow.com/questions/64825967/pygame-tic-tak-toe-logic-how-would-i-do-it/64934964#64934964 
#
# GitHub - PyGameExamplesAndAnswers - Tic Tac Toe
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_tictactoe.md

import pygame

class Cell():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.over = False

    def draw(self, window, outline=None):
        pygame.draw.rect(window, self.color, self.rect)
        if outline:
            pygame.draw.rect(window, outline, self.rect.inflate(-4, -4), 3)

    def isOver(self, pos):
        return self.rect.collidepoint(pos)

class GamePiece:
    def __init__(self, image):
        self.pos = (0, 0)
        self.image = image
    def set_pos(self, pos):
        self.pos = pos
    def draw(self, window):
        window.blit(self.image, self.image.get_rect(center = self.pos))

def new_particle(turn):
    image = cursor1 if turn % 2 == 0 else cursor2
    return GamePiece(image)

def has_won(pg):
    pg = particle_grid
    for i in range(3):
        if pg[i][0] and pg[i][1] and pg[i][2]:
            if pg[i][0].image == pg[i][1].image == pg[i][2].image:
                return pg[i][0].image
    for j in range(3):
        if pg[0][j] and pg[1][j] and pg[2][j]:
            if pg[0][j].image == pg[1][j].image == pg[2][j].image:
                return pg[0][j].image
    if pg[0][0] and pg[1][1] and pg[2][2]:
        if pg[0][0].image == pg[1][1].image == pg[2][2].image:
            return pg[0][0].image
    if pg[0][2] and pg[1][1] and pg[2][0]:
        if pg[0][2].image == pg[1][1].image == pg[2][0].image:
            return pg[0][2].image
    return None

def grid_is_full(pg):
    return all(cell for row in pg for cell in row)
        
pygame.init()
window = pygame.display.set_mode((500, 540))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
font =  pygame.font.SysFont(None, 50)

size = (80, 80)
cursor1 = pygame.Surface(size, pygame.SRCALPHA)
pygame.draw.line(cursor1, (0, 127, 255), (5, 5), (size[0]-5, size[1]-5), 7)
pygame.draw.line(cursor1, (0, 127, 255), (size[0]-5, 5), (5, size[1]-5), 7)
cursor2 = pygame.Surface(size, pygame.SRCALPHA)
pygame.draw.circle(cursor2, (127, 0, 255), (size[0]//2, size[1]//2), size[0]//2-5, 7)

score1 = 0
score2 = 0

button_grid = [[Cell((0, 64, 0), 80+i*120, 90+j*120, 100, 100, '') for i in range(3)] for j in range(3)]
particle_grid = [[None for i in range(3)] for j in range(3)]
turn = 0
particle = new_particle(turn)
lock_time = 0      
locked = False

runninggame = True
while runninggame:
    clock.tick(60)

    current_time = pygame.time.get_ticks()
    if locked and current_time > lock_time:
        locked = False
        particle_grid = [[None for i in range(3)] for j in range(3)]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninggame = False

        if event.type == pygame.MOUSEBUTTONDOWN and not locked:
            for i in range(len(button_grid)):
                for j in range(len(button_grid[0])):
                    b = button_grid[i][j]
                    if b.isOver(event.pos) and particle_grid[i][j] == None:
                        particle.set_pos(b.rect.center)
                        particle_grid[i][j] = particle
                        turn += 1
                        particle = new_particle(turn)
        
            won = has_won(particle_grid)
            if won or grid_is_full(particle_grid):
                lock_time = current_time + 1000
                locked = True
                if won == cursor1:
                    score1 += 1
                elif won == cursor2:
                    score2 += 1

    particle.set_pos(pygame.mouse.get_pos())
    scoreText1 =  font.render("Player 1    Score: " + str(score1), True, (128, 0, 0))
    scoreText2 =  font.render("Player 2    Score: " + str(score2), True, (128, 0, 0))

    window.fill((32, 32, 32))
    for i in range(len(button_grid)):
        for j in range(len(button_grid[0])):
            b = button_grid[i][j]
            p = particle_grid[i][j]
            
            is_over = p == None and b.isOver(pygame.mouse.get_pos())
            b.draw(window, (255, 255, 255) if is_over else None)
            if p:
                p.draw(window)
    window.blit(scoreText1, (80, 30))
    window.blit(scoreText2, (80, 460))
    if not locked:
        particle.draw(window)
    pygame.display.update()

pygame.quit()
exit()
