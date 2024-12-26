# WRITE YOUR SOLUTION HERE:
import pygame
import pathlib
import sys


pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Four walls')

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')
x = (640 / 2) - (robot.get_width() / 2)
y = (480 / 2) - (robot.get_height() / 2)

to_top = False
to_right = False
to_bottom = False
to_left = False

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_top = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_DOWN:
                to_bottom = True
            if event.key == pygame.K_LEFT:
                to_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_top = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_bottom = False
            if event.key == pygame.K_LEFT:
                to_left = False
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

    if to_top and y >= 0:
        y -= 2
    if to_right and x <= 640 - robot.get_width():
        x += 2
    if to_bottom and y <= (480 - robot.get_height()):
        y += 2
    if to_left and x >= 0:
        x -= 2
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
