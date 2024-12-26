import pygame
import sys
import pathlib
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Robot Invasion')

robot_image = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')
robot_width, robot_height = robot_image.get_width(), robot_image.get_height()

clock = pygame.time.Clock()

robots = []

def spawn_robot():
    x = random.randint(0, 640 - robot_width)
    y = random.randint(-480, -robot_height)

    if x > 320:
        direction = 'right'
    else:
        direction = 'left'

    print(len(robots))
    return { 'x': x, 'y': y, 'direction': direction }

for _ in range(5):
    robots.append(spawn_robot())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((0, 0, 0))

    for robot in robots:
        if robot['y'] < 480 - robot_height:
            robot['y'] += 1
        else:
            if robot['direction'] == 'left':
                robot['x'] -= 1
            else:
                robot['x'] += 1

        screen.blit(robot_image, (robot['x'], robot['y']))

    robots = [r for r in robots if -robot_width <= r['x'] <= 640]

    if random.randint(1, 100) <= 1:
        robots.append(spawn_robot())

    pygame.display.flip()

    clock.tick(60)
