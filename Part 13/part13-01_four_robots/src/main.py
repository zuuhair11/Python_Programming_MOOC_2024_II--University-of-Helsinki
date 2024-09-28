# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:
import pygame
import os

pygame.init()
window = pygame.display.set_mode((640, 480))

dir_path = os.path.dirname(os.path.realpath(__file__))
robot = pygame.image.load(f'{dir_path}/robot.png')

robot_width = robot.get_width()
robot_height = robot.get_height()

window.fill((0, 0, 0))

window.blit(robot, (0, 0))
window.blit(robot, (640 - robot_width, 0))
window.blit(robot, (0, 480 - robot_height))
window.blit(robot, (640 - robot_width, 480 - robot_height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
