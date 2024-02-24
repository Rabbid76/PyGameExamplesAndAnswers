
# Sometimes the ball doesn't bounce off the paddle in pong game
# https://stackoverflow.com/questions/62864205/sometimes-the-ball-doesnt-bounce-off-the-paddle-in-pong-game

import pygame

pygame.init()
window = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

radius = 10
move_x, move_y = 3, 3
#ball = pygame.Rect(window.get_width()//2-radius, window.get_height()//2-radius, radius*2, radius)
ball = pygame.Rect(window.get_width()//2+125, 20, radius*2, radius)
paddleHeight = 80
paddleLeft = pygame.Rect(20, (window.get_height()-paddleHeight)//2, 10, paddleHeight)
paddleRight = pygame.Rect(window.get_width()-30, (window.get_height()-paddleHeight)//2, 10, paddleHeight)

start = False

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: start = True

    keys = pygame.key.get_pressed()
    paddleLeft.y += (keys[pygame.K_s] - keys[pygame.K_w]) * 5
    paddleRight.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    paddleLeft.clamp_ip(window.get_rect())
    paddleRight.clamp_ip(window.get_rect())

    if start:
        ball.x += move_x
        ball.y += move_y
    if ball.left <= 0 or ball.right >= window.get_width(): move_x *= -1
    if ball.top <= 0 or ball.bottom >= window.get_height(): move_y *= -1

    if ball.colliderect(paddleLeft):
        move_x *= -1
        ball.left = paddleLeft.right
    if ball.colliderect(paddleRight):
        move_x *= -1
        ball.right = paddleRight.left 

    window.fill('black')
    pygame.draw.rect(window, (255, 255, 255), paddleLeft)
    pygame.draw.rect(window, (255, 255, 255), paddleRight)
    pygame.draw.circle(window, (255, 255, 255), ball.center, radius)
    pygame.display.flip()

pygame.quit()
exit()
