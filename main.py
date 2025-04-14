
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Follow the Cursor")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Square properties
square_size = 40
square_x = WIDTH // 2
square_y = HEIGHT // 2
move_speed = 5

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Move square towards mouse
    if square_x < mouse_x:
        square_x += move_speed
    elif square_x > mouse_x:
        square_x -= move_speed
    
    if square_y < mouse_y:
        square_y += move_speed
    elif square_y > mouse_y:
        square_y -= move_speed
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw square
    pygame.draw.rect(screen, BLUE, (square_x - square_size//2, square_y - square_size//2, square_size, square_size))
    
    # Update display
    pygame.display.flip()
    
    # Control game speed
    clock.tick(60)
