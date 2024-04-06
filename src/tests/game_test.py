import unittest

from main import App

class TestGame(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_if_assets_are_loaded(self):
        self.assertEqual(len(self.app.images), 7)
