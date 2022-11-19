# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# How can I show explosion image when collision happens?
# https://stackoverflow.com/questions/64305426/how-can-i-show-explosion-image-when-collision-happens/64305746#64305746
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - For a period of time
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))

def create_rectangles():
    global rectangles
    w, h = window.get_size()
    rectangles = []
    for x in range(0, w - 60, 60):
        for y in range(0, h - 60, 60):
            rectangles.append(pygame.Rect(x + 30, y + 30, 30, 30))

create_rectangles()
hit_list = []
fade_out_time = 3000

run = True
while run:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    point = pygame.mouse.get_pos()
    collideindex = pygame.Rect(point, (1, 1)).collidelist(rectangles)
    if collideindex >= 0:
        end_time = current_time + fade_out_time
        hit_list.insert(0, (end_time, rectangles[collideindex].center))
        del rectangles[collideindex]
    if not hit_list and not rectangles:
        create_rectangles()

    window.fill(0)
    for r in rectangles:
        pygame.draw.rect(window, (255, 0, 0), r)
    for i in range(len(hit_list)):
        delta_time = hit_list[i][0] - current_time
        if delta_time > 0:
            radius = round(30 * delta_time / fade_out_time)
            pygame.draw.circle(window, (255, 255, 0), hit_list[i][1], radius)
        else:
            hit_list = hit_list[:i]
            break
    pygame.display.flip()

pygame.quit()
exit()
