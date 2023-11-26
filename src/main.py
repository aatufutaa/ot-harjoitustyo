import sys
import pathlib

from constants import *

from game import Game


class App:
    def __init__(self):
        # initialize pygame
        pygame.init()

        # set title for window
        pygame.display.set_caption("Tetris")

        # set size for window
        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        # get ref to clock
        self.clock = pygame.time.Clock()

        # load assets
        self.load_assets()

        # create font
        self.font = pygame.font.SysFont('arial', 20)

        # create game instance
        self.game = Game(self)

    def load_assets(self):
        self.images = {}

        # find png files
        files = [item for item in pathlib.Path(
            "src/assets").rglob("*.png") if item.is_file]

        # loop through files
        for file in files:
            # load image
            image = pygame.image.load(file)

            # scale image
            image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))

            # store file using name
            self.images[file.name] = image

    def tick(self):
        dt = self.clock.tick(FPS)  # wait for next tick

        # tick game
        self.game.tick(dt)

    def draw(self):
        # set bg color
        self.screen.fill("blue")

        # set bg color
        self.screen.fill("black", rect=(SIDE_SIZE * BLOCK_SIZE,
                         0, GRID_W * BLOCK_SIZE, GRID_H * BLOCK_SIZE))

        # draw game
        self.game.draw()

        # update screen
        pygame.display.flip()

    def process_events(self):
        for event in pygame.event.get():

            # handle quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # handle input
            elif event.type == pygame.KEYDOWN:
                self.game.handle_input(event.key, True)
            elif event.type == pygame.KEYUP:
                self.game.handle_input(event.key, False)

    def start(self):
        # game loop
        while True:
            self.process_events()
            self.tick()
            self.draw()


if __name__ == "__main__":
    app = App()
    app.start()
