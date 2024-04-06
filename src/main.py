import sys
import os

from constants import *
from game import Game
from tetromino import TETROMINOES


class App:
    def __init__(self):
        # init pygame
        pygame.init()

        # init screen
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE))

        # get clock
        self.clock = pygame.time.Clock()

        # load images
        self.images = {}
        self.load_assets()

        # create a new game
        self.game = Game(self)

    def load_assets(self):
        # find png files

        # loop through files
        assets_path = os.path.dirname(os.path.abspath(__file__))
        for x in TETROMINOES.keys():
            # load image
            image = pygame.image.load(assets_path + "/assets/" + x + "_block.png")

            # scale image
            image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))

            # store image using shape as key
            self.images[x] = image

    def process_events(self):
        for event in pygame.event.get():

            # handle app exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # handle key input
            elif event.type == pygame.KEYDOWN:
                self.game.handle_input(event.key, True)
            elif event.type == pygame.KEYUP:
                self.game.handle_input(event.key, False)

    def tick(self):
        dt = self.clock.tick(FPS)  # wait for next frame

        self.game.tick(dt)  # tick game with delta time

    def draw(self):
        self.game.draw()

        # update screen
        pygame.display.flip()

    def start(self):
        # start a game loop
        while True:
            self.process_events()
            self.tick()
            self.draw()


if __name__ == "__main__":
    app = App()
    app.start()
