import pygame, sys
from settings import *
from level import Level

class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):

        while True:

                self.check_events()
                self.screen.fill('black')
                self.level.run()
                pygame.display.update()
                self.clock.tick(fps)

    def check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



if __name__ == '__main__':
    game = Game()
    game.run()