import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYUP,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)
from settings import config


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("pirate.jpg").convert()
        self.surf = pygame.transform.scale(self.surf, (config.PLAYER_HEIGHT, config.PLAYER_WIDTH))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -config.PLAYER_SPEED)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, config.PLAYER_SPEED)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-config.PLAYER_SPEED, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(config.PLAYER_SPEED, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > config.SCREEN_HEIGHT:
            self.rect.bottom = config.SCREEN_HEIGHT
