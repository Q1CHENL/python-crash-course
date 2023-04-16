from pygame.sprite import Sprite
import pygame


class Missle(Sprite):
    def __init__(self, game) -> None:
        super().__init__()
        self.rect = pygame.Rect(0, 0, 20, 4.5)
        self.rect.midright = game.rocket.rect.midright
        self.screen = game.screen
        self.color = (60, 60, 60)
        self.x = float(self.rect.x)
        

    def update(self):
        self.x += 1.0
        self.rect.x = self.x

    def draw_missle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
