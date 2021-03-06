# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import time
from settings import config
from enemy import Enemy
from player import Player

from pygame.locals import (
    K_ESCAPE,
    KEYUP,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


pygame.init()

background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
background2 = pygame.transform.flip(background, True, False)
background_size = (800, 600)
background_rect = (800, 600)

w, h = background_size
x = 0
y = 0

x1 = w
y1 = 0

score_font = pygame.font.SysFont(None, 24)
score_color = (255, 0, 0)
current_score = 0

screen = pygame.display.set_mode([config.SCREEN_WIDTH, config.SCREEN_HEIGHT])

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

start_time = time.time()
current_time = time.time()
# Run until the user asks to quit
running = True
while running:
    current_score = round(current_time - start_time) * 10
    screen.blit(background, background_rect)
    current_time = time.time()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYUP:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()
    x1 -= config.BG_SPEED
    x -= config.BG_SPEED
    if x <= -w:
        x = w
    if x1 <= -w:
        x1 = w

    screen.blit(background, (x, y))
    screen.blit(background2, (x1, y1))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    # score
    score_img = score_font.render("{}".format(current_score),
                                  True, score_color)
    screen.blit(score_img, (config.SCREEN_WIDTH - 60, 20))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
print(current_score)
pygame.quit()