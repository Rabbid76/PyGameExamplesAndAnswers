# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# How can i shoot a bullet with space bar?
# https://stackoverflow.com/questions/59687250/how-can-i-shoot-a-bullet-with-space-bar/59689297#59689297 
#  
# How do I stop more than 1 bullet firing at once?
# https://stackoverflow.com/questions/60122492/how-do-i-stop-more-than-1-bullet-firing-at-once/60125448#60125448
#   
# GitHub - PyGameExamplesAndAnswers - Keys and keyboard events- Detecting key states and events - Time - Shoot bullet
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_keys_and_keyboard_event.md
# 
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Time - Lock for a period of time
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md
#
# https://replit.com/@Rabbid76/PyGame-ShootBullet

import pygame
pygame.init()

window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()

tank_surf = pygame.Surface((60, 40), pygame.SRCALPHA)
pygame.draw.rect(tank_surf, (0, 96, 0), (0, 00, 50, 40))
pygame.draw.rect(tank_surf, (0, 128, 0), (10, 10, 30, 20))
pygame.draw.rect(tank_surf, (32, 32, 96), (20, 16, 40, 8))
tank_rect = tank_surf.get_rect(midleft = (20, window.get_height() // 2))

bullet_surf = pygame.Surface((10, 10), pygame.SRCALPHA)
pygame.draw.circle(bullet_surf, (64, 64, 62), bullet_surf.get_rect().center, bullet_surf.get_width() // 2)
bullet_list = []
max_bullets = 4
next_bullet_time = 0
bullet_delta_time = 200 # milliseconds

run = True
while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if len(bullet_list) < max_bullets and current_time >= next_bullet_time:
                next_bullet_time = current_time + bullet_delta_time
                bullet_list.insert(0, tank_rect.midright)

    for i, bullet_pos in enumerate(bullet_list):
        bullet_list[i] = bullet_pos[0] + 5, bullet_pos[1]
        if bullet_surf.get_rect(center = bullet_pos).left > window.get_width():
            del bullet_list[i:]
            break

    window.fill((224, 192, 160))
    window.blit(tank_surf, tank_rect)
    for bullet_pos in bullet_list:
        window.blit(bullet_surf, bullet_surf.get_rect(center = bullet_pos))
    pygame.display.flip()

pygame.quit()
exit()