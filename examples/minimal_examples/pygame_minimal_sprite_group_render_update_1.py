# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Background image change glitches
# https://stackoverflow.com/questions/70271511/background-image-change-glitches/70281354#70281354

import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

background_gray = pygame.Surface(screen.get_size())
ts, w, h, c1, c2 = 40, *background_gray.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background_gray, color, rect) for rect, color in tiles]

background_color = pygame.Surface(screen.get_size())
ts, w, h, c1, c2 = 40, *background_color.get_size(), (255, 255, 0), (255, 0, 0)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background_color, color, rect) for rect, color in tiles]

player = pygame.sprite.Sprite()
player.image = pygame.Surface((40, 40))
player.image.set_colorkey((0, 0, 0))
pygame.draw.circle(player.image, (255, 255, 255), (20, 20), 20)
pygame.draw.circle(player.image, (0, 0, 255), (20, 20), 17)
player.rect = player.image.get_rect(center = (100, 100))

all = pygame.sprite.RenderUpdates(player)

def swap_background():
    if player.rect.top < 5 and player.rect.left < 10:
        screen.blit(background_gray, (0, 0))
        pygame.display.flip()
        background.blit(background_color, (0, 0))
    if player.rect.top < 5 and player.rect.right > screen.get_width() - 10:
        screen.blit(background_color, (0, 0))
        pygame.display.flip()
        background.blit(background_gray, (0, 0))

background = background_color.copy()
screen.blit(background_gray, (0, 0))
pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    vel = 5
    player.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    player.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
    player.rect.clamp_ip(screen.get_rect())
    swap_background()

    all.clear(screen, background)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    clock.tick(60)

pygame.quit()
exit()