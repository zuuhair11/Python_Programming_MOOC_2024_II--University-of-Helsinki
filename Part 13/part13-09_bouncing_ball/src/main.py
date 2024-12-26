# WRITE YOUR SOLUTION HERE:
import pygame
import sys
import pathlib

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Bouncing ball')

ball = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/ball.png')
x, y = 0, 0
x_helper, y_helper = 2, 2

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(ball, (x, y))
    pygame.display.flip()

    x += x_helper
    y += y_helper

    if x == 0 or x + ball.get_width() == 640:
        x_helper = -x_helper
    if y == 0 or y + ball.get_height() == 480:
        y_helper = -y_helper


    clock.tick(60)
