# WRITE YOUR SOLUTION HERE:
import pygame
import pathlib
import sys


pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Two players')

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')
x1, x2 = (640 / 2) - (robot.get_width() / 2), (640 / 2) - (robot.get_width() / 2)
y1, y2 = 0, 480 - robot.get_height()

to_top1 = False
to_right1 = False
to_bottom1 = False
to_left1 = False

to_top2 = False
to_right2 = False
to_bottom2 = False
to_left2 = False

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_top1 = True
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_DOWN:
                to_bottom1 = True
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_w:
                to_top2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_s:
                to_bottom2 = True
            if event.key == pygame.K_a:
                to_left2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_top1 = False
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_DOWN:
                to_bottom1 = False
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_w:
                to_top2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_s:
                to_bottom2 = False
            if event.key == pygame.K_a:
                to_left2 = False

        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

    if to_top1:
        y1 -= 2
    if to_right1:
        x1 += 2
    if to_bottom1:
        y1 += 2
    if to_left1:
        x1 -= 2

    if to_top2:
        y2 -= 2
    if to_right2:
        x2 += 2
    if to_bottom2:
        y2 += 2
    if to_left2:
        x2 -= 2

    screen.fill((0, 0, 0))
    screen.blit(robot, (x1, y1))
    screen.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
