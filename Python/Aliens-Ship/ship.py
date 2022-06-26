import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.moving_right = False
        self.moving_left = False

        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1


