import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()

        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
