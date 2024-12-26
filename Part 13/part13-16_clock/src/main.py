# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = min(WIDTH, HEIGHT) // 2 - 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")

# Clock to control frame rate
clock = pygame.time.Clock()

def draw_hand(surface, center, angle, length, color, width=2):
    """Draws a clock hand."""
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(surface, color, center, (end_x, end_y), width)

def draw_clock():
    """Draws the clock face and hands."""
    # Clear screen
    screen.fill(BLACK)
    
    # Draw clock face
    pygame.draw.circle(screen, RED, CENTER, RADIUS, 3)
    pygame.draw.circle(screen, RED, CENTER, 5)  # Center dot
    
    # Get current time
    now = datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second
    
    # Calculate angles
    second_angle = 90 - seconds * 6
    minute_angle = 90 - minutes * 6 - seconds * 0.1
    hour_angle = 90 - hours * 30 - minutes * 0.5
    
    # Draw hands
    draw_hand(screen, CENTER, hour_angle, RADIUS * 0.5, BLUE, 6)  # Hour hand
    draw_hand(screen, CENTER, minute_angle, RADIUS * 0.7, BLUE, 4)  # Minute hand
    draw_hand(screen, CENTER, second_angle, RADIUS * 0.9, WHITE, 2)  # Second hand

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_clock()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
