
import pygame

pygame.init()
width, height = 600, 400
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

radius = 10
move_x, move_y = 3, 3
#ball = pygame.Rect(width//2-radius, height//2-radius, radius*2, radius)
ball = pygame.Rect(width//2+125, 20, radius*2, radius)
paddleHeight = 80
paddleLeft = pygame.Rect(20, (height-paddleHeight)//2, 10, paddleHeight)
paddleRight = pygame.Rect(width-30, (height-paddleHeight)//2, 10, paddleHeight)

start = False

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: start = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddleLeft.top > 0: paddleLeft.y -= 5
    if keys[pygame.K_s] and paddleLeft.bottom < height: paddleLeft.y += 5
    if keys[pygame.K_UP] and paddleRight.top > 0: paddleRight.y -= 5
    if keys[pygame.K_DOWN] and paddleRight.bottom < height: paddleRight.y += 5

    if start:
        ball.x += move_x
        ball.y += move_y
    if ball.left <= 0 or ball.right >= width: move_x *=-1
    if ball.top <= 0 or ball.bottom >= height: move_y *=-1

    if ball.colliderect(paddleLeft):
        move_x *=-1
    if ball.colliderect(paddleRight):
        move_x *=-1    

    window.fill(0)
    pygame.draw.rect(window, (255, 255, 255), paddleLeft)
    pygame.draw.rect(window, (255, 255, 255), paddleRight)
    pygame.draw.circle(window, (255, 255, 255), ball.center, radius)
    pygame.display.flip()
