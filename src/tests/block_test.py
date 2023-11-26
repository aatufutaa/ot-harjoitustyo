import unittest
from constants import *

from main import App
from game import Game
from block import Tetromino, Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        app = App()
        game = Game(app)
        tetromino = Tetromino(game)
        self.block = Block(tetromino, vec(0, 0))

    def test_move(self):
        self.block.move(MOVE_RIGHT)
        pos = self.block.pos
        self.assertEqual(pos, vec(5, 0))

        self.block.move(MOVE_UP)
        pos = self.block.pos
        self.assertEqual(pos, vec(5, -1))

        self.block.move(MOVE_DOWN)
        pos = self.block.pos
        self.assertEqual(pos, vec(5, 0))

        self.block.move(MOVE_LEFT)
        pos = self.block.pos
        self.assertEqual(pos, vec(4, 0))

    def test_rotate(self):
        pos = self.block.rotate(vec(0, 0))
        self.assertEqual(pos, vec(0, 4))
