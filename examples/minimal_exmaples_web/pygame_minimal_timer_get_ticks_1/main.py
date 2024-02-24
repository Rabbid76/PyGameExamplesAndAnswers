# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# I define a movement method for a character, but I don't know how to itmake it pause for a moment between each move
# https://stackoverflow.com/questions/71546585/i-define-a-movement-method-for-a-character-but-i-dont-know-how-to-itmake-it-pa/71546649#71546649
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame
import asyncio

async def main():
    pygame.init()
    window = pygame.display.set_mode((400, 200))
    clock = pygame.time.Clock()
    rect = pygame.Rect(0, 80, 20, 20)

    time_interval = 500 # 500 milliseconds == 0.1 seconds
    next_step_time = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        current_time = pygame.time.get_ticks()
        if current_time > next_step_time:
            next_step_time += time_interval
            rect.x = (rect.x + 20) % window.get_width()

        window.fill('black')
        pygame.draw.rect(window, (255, 0, 0), rect)
        pygame.display.flip()
        clock.tick(100)
        await asyncio.sleep(0)

    pygame.quit()
    exit()

asyncio.run(main())
