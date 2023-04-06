import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dodge the Blocks")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the player
player_radius = 20
player_x = window_width / 2
player_y = window_height - player_radius - 10
player_speed = 5
player_color = (0, 255, 0)

# Set up the blocks
block_width = 30
block_height = 30
block_speed = 3
block_color = (255, 0, 0)
blocks = []

# Set up the score
score = 0
score_font = pygame.font.SysFont(None, 30)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_radius:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < window_width - player_radius:
        player_x += player_speed

    # Move the blocks and add new blocks
    for block in blocks:
        block[1] += block_speed
        if block[1] > window_height:
            blocks.remove(block)
            score += 1
    if random.random() < 0.1:
        blocks.append([random.randint(0, window_width - block_width), 0])

    # Check for collision with player
    for block in blocks:
        if (player_x - block[0]) ** 2 + (player_y - block[1]) ** 2 < (player_radius + block_width / 2) ** 2:
            pygame.quit()
            quit()

    # Clear the screen
    window.fill((255, 255, 255))

    # Draw the player and blocks
    pygame.draw.circle(window, player_color, (int(player_x), int(player_y)), player_radius)
    for block in blocks:
        pygame.draw.rect(window, block_color, (block[0], block[1], block_width, block_height))

    # Draw the score
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the game clock
    clock.tick(60)
