import random

from block import Block

TETROMINOES = {
    "i": [(0, 0), (0, 1), (0, -1), (0, -2)],
    "j": [(0, 0), (-1, 0), (0, -1), (0, -2)],
    "l": [(0, 0), (1, 0), (0, -1), (0, -2)],
    "o": [(0, 0), (0, -1), (1, 0), (1, -1)],
    "s": [(0, 0), (-1, 0), (0, -1), (1, -1)],
    "t": [(0, 0), (-1, 0), (1, 0), (0, -1)],
    "z": [(0, 0), (1, 0), (0, -1), (-1, -1)]
}


class Tetromino:
    """
    Class that handles blocks, moves them and rotates them
    """
    def __init__(self, game):
        """
        Constructor for Tetromino that gets a random shape and creates blocks for it
        :param game:
        """
        self.game = game

        # get a random shape
        shape = random.choice(list(TETROMINOES.keys()))

        # get image
        image = game.app.images[shape]

        # create blocks
        blocks = TETROMINOES[shape]

        self.blocks = [Block(game, image, pos) for pos in blocks]

    def reset_pos(self):
        """
        Resets block position to default
        """
        for block in self.blocks:
            block.reset_pos()

    def move(self, vel):
        """
        Moves block with velocity
        :param vel:
        """
        # test for collisions
        for block in self.blocks:
            if self.game.test_block_collision(block.pos + vel):
                return True

        # move blocks
        for block in self.blocks:
            block.move(vel)

        return False

    def rotate(self):
        """
        Rotates all blocks
        """
        # get pos for first block
        pos = self.blocks[0].pos

        # test for collisions
        for block in self.blocks:
            if self.game.test_block_collision(block.rotate(pos)):
                return

        # move blocks
        for block in self.blocks:
            block.pos = block.rotate(pos)
