# # WRITE YOUR SOLUTION HERE:
import pygame
import sys
import pathlib

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Round the perimeter')

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')

x, y = 0, 0
direction = 'right'

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()

    if direction == 'right':
        x += 1
        if x + robot.get_width() >= 640:
            direction = 'down'

    if direction == 'down':
        y += 1
        if y + robot.get_height() >= 480:
            direction = 'left'

    if direction == 'left':
        x -= 1
        if x <= 0:
            direction = 'top'

    if direction == 'top':
        y -= 1
        if y <= 0:
            direction = 'right'

    # Logic here
    

    clock.tick(60)
