# 12-1, 12-4
import sys
from rocket import Rocket
import pygame


class BlueWindow:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("Blue Window")
        self.screen.fill((0, 0, 255))
        self.rocket = Rocket(self)

    def run(self):
        while True:
            self._check_key_events()
            self.rocket.update()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill((0, 0, 255))
        self.rocket.blitrocket()
        pygame.display.flip()

    def _check_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False


if __name__ == '__main__':
    bw = BlueWindow()
    bw.run()
