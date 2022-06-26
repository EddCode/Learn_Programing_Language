import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.bullets = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))

        pygame.display.set_caption(self.settings.screen_title)

        self.ship = Ship(self)
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._check_updates()

    def _check_updates(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self._update_fire()
        pygame.display.flip()

    def _update_fire(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_q:
            sys.exit()

        if event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)



if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
