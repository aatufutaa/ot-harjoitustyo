import sys
import os

from constants import pygame, GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE, FPS, STATS_PAGE_WIDTH
from game import Game
from tetromino import TETROMINOES


class App:
    def __init__(self):
        # init pygame
        pygame.init()

        # init screen
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode(((GRID_WIDTH + STATS_PAGE_WIDTH) * BLOCK_SIZE,
                                               GRID_HEIGHT * BLOCK_SIZE))

        # get clock
        self.clock = pygame.time.Clock()

        # load images
        self.images = {}
        self.load_assets()

        # create font
        self.font = pygame.font.SysFont('arial', 20)

        # next block text
        self.next_block_text = self.font.render("Next", True, (255, 255, 255))
        self.next_block_pos = (((GRID_WIDTH+STATS_PAGE_WIDTH/2) * BLOCK_SIZE
                                - self.font.size("Next")[0] / 2),
                               GRID_HEIGHT / 5.0 * BLOCK_SIZE)

        # points text
        self.points_text = self.font.render("Points: 0", True, (255, 255, 255))
        self.points_pos = (((GRID_WIDTH + STATS_PAGE_WIDTH / 2) * BLOCK_SIZE
                            - self.font.size("Points: 0")[0] / 2),
                               self.next_block_pos[1] + BLOCK_SIZE * 6)

        # last points text
        self.last_points_text = self.font.render("Last Points: -", True, (255, 255, 255))
        self.last_points_pos = (((GRID_WIDTH + STATS_PAGE_WIDTH / 2) * BLOCK_SIZE
                                 - self.font.size("Last Points: -")[0] / 2),
                           self.next_block_pos[1] + BLOCK_SIZE * 7)

        # create a new game
        self.game = Game(self)

    def load_assets(self):
        # find png files

        # loop through files
        assets_path = os.path.dirname(os.path.abspath(__file__))
        for x in TETROMINOES:
            # load image
            image = pygame.image.load(assets_path + "/assets/" + x[0] + "_block.png")

            # scale image
            image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))

            # store image using shape as key
            self.images[x[0]] = image

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
