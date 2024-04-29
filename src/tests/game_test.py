import unittest

from main import App
from constants import Vec, GRID_WIDTH, GRID_HEIGHT
from tetromino import TETROMINOES
from block import Block


class TestGame(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_if_assets_are_loaded(self):
        self.assertEqual(len(self.app.images), 7)

    def test_if_block_collision_works(self):
        for i in range(0, 7):
            self.app.game.tetromino.move(Vec(-1, 0))

        self.assertGreaterEqual(self.app.game.tetromino.blocks[0].pos[0], 0)

        for i in range(0, 11):
            self.app.game.tetromino.move(Vec(0, 1))

        self.assertEqual(self.app.game.tetromino.blocks[0].pos[1], 11)

    def test_if_timer_works(self):
        self.app.game.tick(1)
        self.assertEqual(self.app.game.timer, 1)
        self.app.game.tick(1000)
        self.assertEqual(self.app.game.timer, 0)

    def test_if_full_row_check_works(self):
        image = self.app.images["i"]
        points = self.app.game.points
        for i in range(0, GRID_WIDTH):
            self.app.game.collisions[0][i] = Block(self.app.game, image, (0, i))
        self.app.game.check_for_full_rows()
        self.assertGreater(self.app.game.points, points)

    def test_if_block_landing_works(self):
        self.app = App()
        points = self.app.game.points
        for i in range(0, GRID_HEIGHT):
            for j in range(0, GRID_HEIGHT):
                self.app.game.tick(1000)
        self.assertGreater(self.app.game.points, points)