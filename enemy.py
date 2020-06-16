import pygame
import random
from settings import config


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((15, 15))
        pygame.draw.circle(self.surf, (255, 0, 0), (7, 7), 7)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(config.SCREEN_WIDTH + 20, config.SCREEN_WIDTH + 100),
                random.randint(0, config.SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(config.MIN_SPEED, config.MAX_SPEED)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
