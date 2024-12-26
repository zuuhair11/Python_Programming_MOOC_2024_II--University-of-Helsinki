# WRITE YOUR SOLUTION HERE:
import pygame
import pathlib
import sys


pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Draw robot!')

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')

robot_x = 0
robot_y = 0

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            robot_x = event.pos[0] - (robot.get_width() / 2)
            robot_y = event.pos[1] - (robot.get_height() / 2)

            screen.fill((0, 0, 0))
            screen.blit(robot, (robot_x, robot_y))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
