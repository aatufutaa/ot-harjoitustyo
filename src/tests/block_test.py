import unittest
from block import Block

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block("s")

    def test_set_x(self):
        self.block.set_x(0)
        self.assertEqual(self.block.get_x(), 0)

        self.block.set_x(1)
        self.assertEqual(self.block.get_x(), 1)

    def test_set_y(self):
        self.block.set_y(0)
        self.assertEqual(self.block.get_y(), 0)

        self.block.set_y(1)
        self.assertEqual(self.block.get_y(), 1)