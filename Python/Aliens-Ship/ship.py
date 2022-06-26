import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.moving_right = False
        self.moving_left = False

        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.rect.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            if self.moving_left:
                self.rect.x -= self.settings.ship_speed

