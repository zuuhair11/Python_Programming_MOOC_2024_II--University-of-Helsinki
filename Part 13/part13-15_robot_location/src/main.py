# WRITE YOUR SOLUTION HERE:
import pygame
import pathlib
import sys
import random


pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('The location of the robot')

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')

def get_coordinate():
    x = random.randint(0, 640 - robot.get_width()) 
    y = random.randint(0, 480 - robot.get_height())

    return (x, y)

robot_x, robot_y = get_coordinate()
screen.blit(robot, (robot_x, robot_y))
pygame.display.flip()


clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_x = event.pos[0]
            clicked_y = event.pos[1]

            if clicked_x >= robot_x and clicked_x <= robot_x + robot.get_width():
                if clicked_y >= robot_y and clicked_y <= robot_y + robot.get_height():
                    robot_x, robot_y = get_coordinate()

            screen.fill((0, 0, 0))
            screen.blit(robot, (robot_x, robot_y))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

    clock.tick(60)
