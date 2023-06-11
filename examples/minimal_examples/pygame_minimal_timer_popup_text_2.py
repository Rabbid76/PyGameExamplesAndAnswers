# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# How can i controll collision from sprites?
# https://stackoverflow.com/questions/71184756/how-can-i-controll-collision-from-sprites/73938856#73938856
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - For a period of time
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame, random

pygame.init()
window = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

bounds = pygame.Rect(20, 20, 360, 360)
hit_text_image = font.render("hit", True, "yellow")
text_pos_and_time = []
pop_up_seconds = 1

ball = pygame.sprite.Sprite()
ball.image = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(ball.image, "red", (20, 20), 20)
ball.rect = ball.image.get_rect(center = window.get_rect().center)
ball.pos = pygame.Vector2(ball.rect.center)
ball.dir = pygame.Vector2(random.uniform(0.5, 1), random.uniform(0.5, 1))
ball.dir.normalize_ip()
ball.speed = 0

obstacles = []
for pos in [(100, 200), (300, 100), (250, 300)]:
    obstacle = pygame.sprite.Sprite()
    obstacle.image = pygame.Surface((60, 60))
    obstacle.image.fill("darkgreen")
    obstacle.rect = obstacle.image.get_rect(center = pos)
    obstacle.hit = False
    obstacles.append(obstacle)

all_sprites = pygame.sprite.Group([ball, *obstacles])
text_sprites = pygame.sprite.Group()

text = font.render("+1", True, (0, 255, 0))
text_pos_and_time = []
pop_up_seconds = 1

player = pygame.Rect(0, 80, 40, 40)
coins = [pygame.Rect(i*100+100, 80, 40, 40) for i in range(3)]

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            ball.dir = pygame.Vector2(random.uniform(0.5, 1), random.uniform(0.5, 1))
            ball.dir.normalize_ip()
            ball.speed = 5

    keys = pygame.key.get_pressed()
    player.x = (player.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 3) % 300    

    ball.pos += ball.dir * ball.speed
    ball.rect.center = round(ball.pos.x), round(ball.pos.y)
    if not bounds.contains(ball.rect.inflate(2, 2)):
        if ball.rect.left <= bounds.left or ball.rect.right >= bounds.right:
            ball.dir.x *= -1
        if ball.rect.top <= bounds.top or ball.rect.bottom >= bounds.bottom:
            ball.dir.y *= -1
        ball.rect.clamp_ip(bounds)
        ball.pos = pygame.Vector2(ball.rect.center)

    current_time = pygame.time.get_ticks()
    for obstacle in obstacles:
        rel_hit_pos = pygame.sprite.collide_mask(ball, obstacle)
        if rel_hit_pos:
            if obstacle.hit == False:
                obstacle.hit = True
                hit_sprite = pygame.sprite.Sprite()
                hit_sprite.image = hit_text_image
                hit_pos = ball.rect.x + rel_hit_pos[0], ball.rect.y + rel_hit_pos[1]
                hit_sprite.rect = hit_sprite.image.get_rect(center = hit_pos)
                hit_sprite.end_time = current_time + pop_up_seconds * 1000
                text_sprites.add(hit_sprite)
        else:
            obstacle.hit = False

    for hit_sprite in text_sprites:
        if current_time > hit_sprite.end_time:
            hit_sprite.kill()

    window.fill(0)    
    pygame.draw.rect(window, "gray", bounds, 3)
    all_sprites.draw(window)
    text_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()