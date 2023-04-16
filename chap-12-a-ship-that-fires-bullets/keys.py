# 12-5
import pygame
import sys
class Keys:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Keys')
        
    def run(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                print(e)
        
        
if __name__ == '__main__':
    k = Keys()
    k.run()
    