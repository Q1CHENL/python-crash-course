# 12-2, 12-4
import pygame

class Rocket:
    def __init__(self, game) -> None:
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        
        # Make the rocket at the center
        self.rect.right = self.screen_rect.right/2
        self.rect.bottom = self.screen_rect.bottom/2
        
        self.x = self.rect.x
        self.y = self.rect.y
        
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        
    def blitrocket(self):
        self.screen.blit(self.image, self.rect) 
    
    def update(self):
        if self.moving_up and self.rect.y > 0:
            self.y -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1
        elif self.moving_left and self.rect.x > 0:
            self.x -= 1
        elif self.moving_right and self.rect.right< self.screen_rect.right:
            self.x += 1
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        
        