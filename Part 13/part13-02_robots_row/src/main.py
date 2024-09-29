# WRITE YOUR SOLUTION HERE:
import pygame
import sys
import os

pygame.init()

window = pygame.display.set_mode((640, 480))
window.fill((0, 0, 0))

dir_path = os.path.dirname(os.path.realpath(__file__))
robot = pygame.image.load(f'{dir_path}/robot.png')

for i in range(10):
    window.blit(robot, (50 + 50 * i, 100))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

