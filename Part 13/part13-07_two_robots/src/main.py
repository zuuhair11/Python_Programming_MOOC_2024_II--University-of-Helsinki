# WRITE YOUR SOLUTION HERE:
import pygame
import sys
import pathlib


pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Two robots')

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')

x1, x2 = 0 , 0
speed1 = 1
speed2 = 2


clock = pygame.time.Clock()


while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(robot, (x1, 50))
    screen.blit(robot, (x2, 200))
    pygame.display.flip()


    x1 += speed1
    if x1 == 0 or x1 + robot.get_width() == 640:
        speed1 = -speed1

    x2 += speed2
    if x2 == 0 or x2 + robot.get_width() == 640:
        speed2 = -speed2

    clock.tick(60)
