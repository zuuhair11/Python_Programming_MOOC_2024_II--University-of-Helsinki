# WRITE YOUR SOLUTION HERE:
import pygame
import pathlib
import sys
import random


pygame.init()

rock_list = []
def get_rock():
    x = random.randint(0, 640 - rock.get_width())
    y = random.randint(-480, -rock.get_height())

    return { 'x': x, 'y': y }

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption(('Asteroids'))

game_font = pygame.font.SysFont('Arial', 24)
text = game_font.render('Points:', True, (255, 0, 0))

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')
points = 0
x = (640 / 2) - (robot.get_width() / 2)
y = 480 - robot.get_height()

moving_to_left = False
moving_to_right = False

rock = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/rock.png')

for _ in range(2):
    rock_list.append(get_rock())


clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_to_left = True
            if event.key == pygame.K_RIGHT:
                moving_to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_to_left = False
            if event.key == pygame.K_RIGHT:
                moving_to_right = False

        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

    if moving_to_left and x >= 0:
        x -= 2
    if moving_to_right and x <= 640 - robot.get_width():
        x += 2

    screen.fill((0, 0, 0))

    # For the text
    text = game_font.render(f'Points: { points }', True, (255, 0, 0))
    screen.blit(text, (515, 10))

    # For the robot
    screen.blit(robot, (x, y))

    # For the rock
    for r in rock_list:
        print(rock)
        if r['y'] <= 480:
            r['y'] += 1
        if r['y'] + rock.get_height() >= 480 - robot.get_height():
            if r['x'] >= x and r['x'] <= x + robot.get_width():
                points += 1

                # Hide it, so later in rock_list I can get ride of it easly because its already r['y'] > 480
                r['y'] = 480 + 1

        screen.blit(rock, (r['x'], r['y']))

    rock_list = [r for r in rock_list if r['y'] <= 480]
    pygame.display.flip()

    # Get ride of the robots
    if random.randint(1, 150) == 1:
        rock_list.append(get_rock())

    clock.tick(60)
