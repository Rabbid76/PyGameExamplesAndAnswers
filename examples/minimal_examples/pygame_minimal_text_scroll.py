# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# Pygame when adding new text it appears on bottom and rest of text goes up
# https://stackoverflow.com/questions/70102350/when-adding-new-text-it-appears-on-bottom-and-rest-of-text-goes-up/70128422#70128422
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Scroll Text
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md

import pygame, random

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

def draw_scroll_text_box(surf, font, box_rect, text_surf_list):
    surf.set_clip(box_rect)
    text_y = box_rect.bottom - font.get_height() - 10
    for text_surf in reversed(text_surf_list[:]):
        if text_y <= box_rect.top: 
            text_surf_list.remove(text_surf)
        else:
            surf.blit(text_surf, (box_rect.left + 10, text_y))
        text_y -= font.get_height()
    pygame.draw.rect(surf, (164, 164, 164), box_rect, 5)
    surf.set_clip(None)

font = pygame.font.SysFont(None, 50)
text_box_rect = pygame.Rect(20, 20, 250, 360)
text_surf_list = []
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 200)
scroll_timer = True

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (32, 32, 32), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == timer_event:
            names = ["Daniel", "Jenny", "Patrick", "Sandy", "Bob"]
            text_surf = font.render(random.choice(names), True, (255, 255, 0))
            text_surf_list.append(text_surf)
        if event.type == pygame.KEYDOWN:
            scroll_timer = not scroll_timer
            pygame.time.set_timer(timer_event, 200 if scroll_timer else 0)

    window.blit(background, (0, 0))
    draw_scroll_text_box(window, font, text_box_rect, text_surf_list)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()