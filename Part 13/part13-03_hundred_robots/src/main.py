# WRITE YOUR SOLUTION HERE:
import pygame
import pathlib

pygame.init()

window = pygame.display.set_mode((640, 480))
window.fill((0, 0, 0))

robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')

# Draw the robots now
for x in range(10):
    for y in range(10):
        window.blit(robot, (50 + (40 * y) + (x * 10), 100 + (x * 20)))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
