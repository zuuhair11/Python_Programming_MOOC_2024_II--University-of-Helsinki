# WRITE YOUR SOLUTION HERE:
import pygame
import sys
import pathlib

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Vertical movement')

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')
x, y = 0, 0
direction = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += direction

    if direction > 0 and y + robot.get_height() >= 480:
        direction = -direction

    if direction < 0 and y <= 0:
        direction = -direction

    clock.tick(60)
