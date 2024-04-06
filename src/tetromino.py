import random

from block import Block

TETROMINOES = {
    "i": [(0, 1), (0, -1), (0, -2)],
    "j": [(-1, 0), (0, -1), (0, -2)],
    "l": [(1, 0), (0, -1), (0, -2)],
    "o": [(0, -1), (1, 0), (1, -1)],
    "s": [(-1, 0), (0, -1), (1, -1)],
    "t": [(-1, 0), (1, 0), (0, -1)],
    "z": [(1, 0), (0, -1), (-1, -1)]
}


class Tetromino:
    def __init__(self, game):
        self.game = game

        # get a random shape
        shape = random.choice(list(TETROMINOES.keys()))

        # get image
        image = game.app.images[shape]

        # create blocks
        blocks = TETROMINOES[shape]
        blocks.insert(0, (0, 0))

        self.blocks = [Block(game, image, pos) for pos in blocks]

    def move(self, vel):
        # test for collisions
        for block in self.blocks:
            if self.game.test_block_collision(block.pos + vel):
                return True

        # move blocks
        for block in self.blocks:
            block.move(vel)

        return False

    def rotate(self):
        # get pos for first block
        pos = self.blocks[0].pos

        # test for collisions
        for block in self.blocks:
            if self.game.test_block_collision(block.rotate(pos)):
                return

        # move blocks
        for block in self.blocks:
            block.pos = block.rotate(pos)