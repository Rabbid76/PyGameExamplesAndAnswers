# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# How do I avoid an glitchy collision between circle and rectangle in PyGame?
# https://stackoverflow.com/questions/58139771/how-do-i-avoid-an-glitchy-collision-between-circle-and-rectangle-in-pygame/58145450#58145450
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Rectangle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame

class Player(object):
    def __init__(self, x, y, w, h):
        self.rect = pygame.rect.Rect(x, y, w, h)
    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.left = max(20, self.rect.left - 1)
        if key[pygame.K_RIGHT]:
            self.rect.right = min(window.get_height() - 20, self.rect.right + 1)
        if key[pygame.K_UP]:
            self.rect.top = max(20, self.rect.top - 1)
        if key[pygame.K_DOWN]:
            self.rect.bottom = min(window.get_width() - 20, self.rect.bottom + 1)
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)

pygame.init()
window = pygame.display.set_mode((240, 240))
clock=pygame.time.Clock()

player = Player(20, 20, 50, 50)
v, vel = pygame.math.Vector2(1, 1), 0.5
ballPosX, ballPosY, ballRadius = 120, 120, 10

run = True
while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    player.handle_keys()  

    min_x, min_y, max_x, max_y = 20, 20, window.get_width()-20, window.get_height()-20
    ballPosX += v[0] * vel
    ballPosY += v[1] * vel
    if ballPosX - ballRadius < min_x:
        ballPosX = ballRadius + min_x
        v[0] = -v[0]
    if ballPosY - ballRadius < min_y:
        ballPosY = ballRadius + min_y
        v[1] = -v[1]
    if ballPosX + ballRadius > max_x:
        ballPosX = max_x - ballRadius
        v[0] = -v[0]
    if ballPosY + ballRadius > max_y:
        ballPosY = max_y - ballRadius
        v[1] = -v[1]

    ball = pygame.Rect((0,0), (ballRadius*2, ballRadius*2))
    ball.center = int(ballPosX),int(ballPosY)
    if player.rect.colliderect(ball):
        dx = ballPosX - player.rect.centerx
        dy = ballPosY - player.rect.centery
        if abs(dx) > abs(dy):
            if dx < 0:
                ballPosX = max(player.rect.left-ballRadius, ballRadius+min_x) 
                player.rect.left = int(ballPosX)+ballRadius
            else:
                ballPosX = min(player.rect.right+ballRadius, max_x-ballRadius)
                player.rect.right = int(ballPosX)-ballRadius
            if (dx < 0 and v[0] > 0) or (dx > 0 and v[0] < 0):
                v.reflect_ip(pygame.math.Vector2(1, 0))
        else:
            if dy < 0:
                ballPosY = max(player.rect.top-ballRadius, ballRadius+min_y) 
                player.rect.top = int(ballPosY)+ballRadius
            else:
                ballPosY = min(player.rect.bottom+ballRadius, max_y-ballRadius)
                player.rect.bottom = int(ballPosY)-ballRadius
            ballPosY = player.rect.top-ballRadius if dy < 0 else player.rect.bottom+ballRadius
            if (dy < 0 and v[1] > 0) or (dy > 0 and v[1] < 0):
                v.reflect_ip(pygame.math.Vector2(0, 1))


    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255,0,0), (18, 18, 203, 203), 2)
    player.draw(window)
    pygame.draw.circle(window, (0, 255, 0), (round(ballPosX), round(ballPosY)), ballRadius)
    pygame.display.update()

pygame.quit()
exit()