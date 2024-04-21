import unittest

from main import App
from constants import Vec

class TestGame(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_if_assets_are_loaded(self):
        self.assertEqual(len(self.app.images), 7)

    def test_if_block_collision_works(self):
        self.app.game.tetromino.move(Vec(-1, 0))
        self.app.game.tetromino.move(Vec(-1, 0))
        self.app.game.tetromino.move(Vec(-1, 0))
        self.app.game.tetromino.move(Vec(-1, 0))
        self.app.game.tetromino.move(Vec(-1, 0))
        self.app.game.tetromino.move(Vec(-1, 0))
        self.app.game.tetromino.move(Vec(-1, 0))

        self.assertGreaterEqual(self.app.game.tetromino.blocks[0].pos[0], 0)

        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))
        self.app.game.tetromino.move(Vec(0, 1))

        self.assertEqual(self.app.game.tetromino.blocks[0].pos[1], 11)

    def test_if_timer_works(self):
        self.app.game.tick(1)

        self.assertEqual(self.app.game.timer, 1)