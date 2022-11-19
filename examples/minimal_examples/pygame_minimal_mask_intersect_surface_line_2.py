# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# Overlap between mask and fired beams in Pygame [AI car model vision]
# https://stackoverflow.com/questions/62008457/overlap-between-mask-and-fired-beams-in-pygame-ai-car-model-vision/62082726#62082726
#
# GitHub - PyGameExamplesAndAnswers - Mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SurfaceLineMaskIntersect-2

import math
import pygame

def draw_beam(surface, angle, pos):
    c = math.cos(math.radians(angle))
    s = math.sin(math.radians(angle))

    flip_x = c < 0
    flip_y = s < 0
    filpped_mask = flipped_masks[flip_x][flip_y]
    
    # compute beam final point
    x_dest = surface.get_width() * abs(c)
    y_dest = surface.get_height() * abs(s)

    beam_surface.fill((0, 0, 0, 0))

    # draw a single beam to the beam surface based on computed final point
    pygame.draw.line(beam_surface, (0, 0, 255), (0, 0), (x_dest, y_dest))
    beam_mask = pygame.mask.from_surface(beam_surface)

    # find overlap between "global mask" and current beam mask
    offset_x = surface.get_width()-1 - pos[0] if flip_x else pos[0]
    offset_y = surface.get_height()-1 - pos[1] if flip_y else pos[1]
    hit = filpped_mask.overlap(beam_mask, (offset_x, offset_y))
    if hit is not None and (hit[0] != pos[0] or hit[1] != pos[1]):
        hx = surface.get_width()-1 - hit[0] if flip_x else hit[0]
        hy = surface.get_height()-1 - hit[1] if flip_y else hit[1]
        hit_pos = (hx, hy)

        pygame.draw.line(surface, (0, 0, 255), pos, hit_pos)
        pygame.draw.circle(surface, (0, 255, 0), hit_pos, 3)
        #pygame.draw.circle(surface, (255, 255, 0), mouse_pos, 3)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

beam_surface = pygame.Surface(window.get_rect().center, pygame.SRCALPHA)
mask_surface = pygame.Surface(window.get_size(), pygame.SRCALPHA)
mask_surface.fill((255, 0, 0))
pygame.draw.circle(mask_surface, (0, 0, 0, 0), (window.get_rect().center), 100)
rect_shape = pygame.Rect(0, 0, 170, 170)
rect_shape.center = mask_surface.get_rect().center
pygame.draw.rect(mask_surface, (0, 0, 0, 0), rect_shape)

mask = pygame.mask.from_surface(mask_surface)
mask_fx = pygame.mask.from_surface(pygame.transform.flip(mask_surface, True, False))
mask_fy = pygame.mask.from_surface(pygame.transform.flip(mask_surface, False, True))
mask_fx_fy = pygame.mask.from_surface(pygame.transform.flip(mask_surface, True, True))
flipped_masks = [[mask, mask_fy], [mask_fx, mask_fx_fy]]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_pos = pygame.mouse.get_pos()

    window.fill((0, 0, 0))
    window.blit(mask_surface, mask_surface.get_rect())

    for angle in range(0, 359, 30):
        draw_beam(window, angle, mouse_pos)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
exit()
