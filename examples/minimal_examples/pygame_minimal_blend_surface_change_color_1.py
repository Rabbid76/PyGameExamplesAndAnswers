# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Trying to make sections of sprite change colour, but whole sprite changes instead
# https://stackoverflow.com/questions/58385570/trying-to-make-sections-of-sprite-change-colour-but-whole-sprite-changes-instea/58402923#58402923
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Change color of an image - Change the color of a surface area (mask)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md
#
# https://replit.com/@Rabbid76/PyGame-ChangeColorOfSurfaceArea


import pygame

colour = (0, 0, 255, 0)

pygame.init()
window = pygame.display.set_mode((500, 500))

font = pygame.font.SysFont('Times New Roman', 20)

image = pygame.Surface((64, 64), pygame.SRCALPHA)
image.fill((0, 0, 0, 0))
pygame.draw.circle(image, (255, 255, 255, 255), (32, 32), 32)
pygame.draw.rect(image, (255, 0, 0, 255), (16, 16, 32, 32))

mask = pygame.Surface((64, 64), pygame.SRCALPHA)
mask.fill((0, 0, 0, 0))
pygame.draw.rect(mask, (255, 255, 255, 255), (16, 16, 32, 32))


# Create coloured image the size of the entire sprite
coloured_image = pygame.Surface(image.get_size())
coloured_image.fill(colour)

# create mask area
masked = mask.copy()
masked.blit(coloured_image, (0, 0), None, pygame.BLEND_RGBA_MULT)


# create the final image
final_image = image.copy()
final_image.blit(masked, (0, 0), None)

#final_image =  mask.copy()
#final_image.blit(coloured_image, (0, 0), None, pygame.BLEND_RGBA_MULT)

#masked = final_image.copy()

# put the source image on top of the colored aread
#final_image.blit(image, (0, 0), None)


# main application loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    window.blit(image, (20, 20))
    window.blit(font.render("image", True, (255, 255, 255)), (100, 35))

    window.blit(mask, (20, 90))
    window.blit(font.render("mask", True, (255, 255, 255)), (100, 105))

    window.blit(coloured_image, (20, 160))
    window.blit(font.render("coloured_image", True, (255, 255, 255)), (100, 175))

    window.blit(masked, (20, 230))
    window.blit(font.render("masked", True, (255, 255, 255)), (100, 245))

    window.blit(final_image, (20, 310))
    window.blit(font.render("final image", True, (255, 255, 255)), (100, 325))

    pygame.display.flip()

pygame.quit()
exit()