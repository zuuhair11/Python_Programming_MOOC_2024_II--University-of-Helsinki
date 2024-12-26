# WRITE YOUR SOLUTION HERE:
import pygame
import sys
import pathlib
import math

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Robots in a circle')

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')

clock = pygame.time.Clock()
angle1 = 0
angle2 = 0.7
angle3 = 1.4
angle4 = 2.1
angle5 = 2.8
angle6 = 3.5
angle7 = 4.2
angle8 = 4.9
angle9 = 5.6
angle10 = 6.3

# x1, y1 = 0, 0
# x2, y1 = 0, 0
# x1, y1 = 0, 0
# x1, y1 = 0, 0
# x1, y1 = 0, 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the elements
    x1 = 320 + math.cos(angle1) * 100 - robot.get_width() / 2
    y1 = 240 + math.sin(angle1) * 100 - robot.get_height() / 2

    x2 = 320 + math.cos(angle2) * 100 - robot.get_width() / 2
    y2 = 240 + math.sin(angle2) * 100 - robot.get_height() / 2

    x3 = 320 + math.cos(angle3) * 100 - robot.get_width() / 2
    y3 = 240 + math.sin(angle3) * 100 - robot.get_height() / 2

    x4 = 320 + math.cos(angle4) * 100 - robot.get_width() / 2
    y4 = 240 + math.sin(angle4) * 100 - robot.get_height() / 2

    x5 = 320 + math.cos(angle5) * 100 - robot.get_width() / 2
    y5 = 240 + math.sin(angle5) * 100 - robot.get_height() / 2

    x6 = 320 + math.cos(angle6) * 100 - robot.get_width() / 2
    y6 = 240 + math.sin(angle6) * 100 - robot.get_height() / 2

    x7 = 320 + math.cos(angle7) * 100 - robot.get_width() / 2
    y7 = 240 + math.sin(angle7) * 100 - robot.get_height() / 2

    x8 = 320 + math.cos(angle8) * 100 - robot.get_width() / 2
    y8 = 240 + math.sin(angle8) * 100 - robot.get_height() / 2

    x9 = 320 + math.cos(angle9) * 100 - robot.get_width() / 2
    y9 = 240 + math.sin(angle9) * 100 - robot.get_height() / 2

    x10 = 320 + math.cos(angle10) * 100 - robot.get_width() / 2
    y10 = 240 + math.sin(angle10) * 100 - robot.get_height() / 2

    screen.fill((0, 0, 0))
    screen.blit(robot, (x1, y1))
    screen.blit(robot, (x2, y2))
    screen.blit(robot, (x3, y3))
    screen.blit(robot, (x4, y4))
    screen.blit(robot, (x5, y5))
    screen.blit(robot, (x6, y6))
    screen.blit(robot, (x7, y7))
    screen.blit(robot, (x8, y8))
    screen.blit(robot, (x9, y9))
    screen.blit(robot, (x10, y10))


    pygame.display.flip()

    angle1 += 0.01
    angle2 += 0.01
    angle3 += 0.01
    angle4 += 0.01
    angle5 += 0.01
    angle6 += 0.01
    angle7 += 0.01
    angle8 += 0.01
    angle9 += 0.01
    angle10 += 0.01
    clock.tick(60)
