
import pygame
from PIL import Image, ImageSequence
import io
import requests

# Initialize Pygame
pygame.init()

# Set up display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpongeBob GIF")

# Download SpongeBob GIF
url = "https://media.tenor.com/Qq0qkUqtib4AAAAi/spongebob-meme.gif"
response = requests.get(url)
gif = Image.open(io.BytesIO(response.content))

# Get the frames from GIF
frames = []
for frame in ImageSequence.Iterator(gif):
    # Convert frame to pygame surface
    frame = frame.convert('RGBA')
    frame = frame.resize((300, 300))  # Resize for better display
    pygame_image = pygame.image.fromstring(
        frame.tobytes(), frame.size, frame.mode)
    frames.append(pygame_image)

# Game loop
clock = pygame.time.Clock()
frame_index = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill((255, 255, 255))
    
    # Calculate position to center the GIF
    x = (WIDTH - frames[frame_index].get_width()) // 2
    y = (HEIGHT - frames[frame_index].get_height()) // 2
    
    # Draw current frame
    screen.blit(frames[frame_index], (x, y))
    
    # Update frame index
    frame_index = (frame_index + 1) % len(frames)
    
    pygame.display.flip()
    clock.tick(10)  # Control animation speed

pygame.quit()
