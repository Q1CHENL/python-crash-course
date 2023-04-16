# 12-1, 12-4
import sys
from rocket import Rocket
from missle import Missle
import pygame


class BlueWindow:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("Blue Window")
        self.screen.fill((0, 0, 255))
        self.missles = pygame.sprite.Group()
        self.rocket = Rocket(self)
        
    def run(self):
        while True:
            self._check_key_events()
            self.rocket.update()
            self._update_missles()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill((0, 0, 255))
        self.rocket.blitrocket()
        for missle in self.missles.sprites():
            missle.draw_missle()
            
        pygame.display.flip()
        
    def _update_missles(self):
        # Update missle positions
        self.missles.update()
       
        # Remove out of bounday missles
        for missle in self.missles.copy():
            if missle.rect.right > self.screen.get_rect().right:
                self.missles.remove(missle)

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
        elif event.key == pygame.K_SPACE:
            self._fire_missle()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
    
    def _fire_missle(self):
        if len(self.missles) < 5:
            new_missle = Missle(self)       
            self.missles.add(new_missle)
            
if __name__ == '__main__':
    bw = BlueWindow()
    bw.run()
