# WRITE YOUR SOLUTION HERE:
import pygame
import pathlib
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen.fill((0, 0, 0))

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')
robot_width = robot.get_width()
robot_height = robot.get_height()

for _ in range(1000):
    screen.blit(robot, (random.randint(0, 640 - robot_width), random.randint(0, 480 - robot_height)))

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
