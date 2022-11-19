# mathplotlib
# https://matplotlib.org/
#  
# How can I integrate a Line Chart Viewer in PyGame?
# https://stackoverflow.com/questions/70493951/how-can-i-integrate-a-line-chart-viewer-in-pygame/70494476#70494476
# 
# GitHub - PyGameExamplesAndAnswers - PyGame in combination with other libraries - MathPlotLib
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_and_othere_libraries.md

import matplotlib.pyplot as plt
import pygame
import io

plt.plot(Generation=[], Points=[])
plt.title('Points per Generation')
plt.xlabel('Generation')
plt.ylabel('Points')

plot_stream = io.BytesIO()
plt.savefig(plot_stream, formatstr='png')
plot_stream.seek(0)

pygame.init()
plot_surface = pygame.image.load(plot_stream, 'PNG')

window = pygame.display.set_mode(plot_surface.get_size())
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.fill(0)
    window.blit(plot_surface, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()