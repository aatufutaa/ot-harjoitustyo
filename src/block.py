from constants import *
import random


class Block(pygame.sprite.Sprite):

    def __init__(self, tetromino, pos):
        super().__init__(tetromino.game.sprites)

        self.tetromino = tetromino

        # set pos to top center
        self.pos = vec(pos) + vec(GRID_W / 2 - 1, 0)

        # bool to check if block has been killed as a result of full row
        self.dead = False

        # set asset
        self.image = tetromino.image
        self.rect = self.image.get_rect()

    def update(self):
        # if block is removed kill sprite
        if self.dead:
            self.kill()

        if self.tetromino.next:
            # if block is currently waiting
            self.rect.topleft = vec(
                SIDE_SIZE * 2 + GRID_W/2 - SIDE_SIZE / 2, GRID_H / 2) * BLOCK_SIZE + self.pos * BLOCK_SIZE
        else: 
             # update pos for block
            self.rect.topleft = vec(
                SIDE_SIZE * BLOCK_SIZE, 0) + self.pos * BLOCK_SIZE

    def test_collision(self, pos):
        x = int(pos.x)
        y = int(pos.y)

        # check if x and y in grid
        if 0 <= x < GRID_W and y < GRID_H:
            # check for collision
            if (y < 0 or not self.tetromino.game.collisions[y][x]):
                return False
        return True

    def move(self, vec):
        self.pos += vec  # move with vec

    def rotate(self, pos):
        # rotate 90 deg to the right
        translated = self.pos - pos
        rotated = translated.rotate(90)
        return rotated + pos

# dict of all shapes
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

    def __init__(self, game, next=True):
        self.game = game

        # get a random shape
        shape = random.choice(list(TETROMINOES.keys()))

        # get image
        self.image = game.app.images[shape + "_block.png"]

        # bool to check if tetromino is next
        self.next = next

        # create blocks
        blocks = TETROMINOES[shape]
        blocks.insert(0, (0, 0))
        self.blocks = [Block(self, pos) for pos in blocks]

        # bool to check if tetromino hit the ground
        self.landed = False

    def tick(self):
        # move 1 block down
        self.move(MOVE_DOWN)

    def move(self, vec):
        # get new pos for all blocks
        new_pos = [block.pos + vec for block in self.blocks]

        # check for collision
        if not self.test_collision(new_pos):
            # then update pos
            for block in self.blocks:
                block.move(vec)

        elif vec == MOVE_DOWN:
            self.landed = True

    def test_collision(self, new_pos):
        # check if any of the blocks has collision
        return any(map(Block.test_collision, self.blocks, new_pos))

    def rotate(self):
        # get pos for first block
        pos = self.blocks[0].pos
        # rotate all blocks along first block
        new_pos = [block.rotate(pos) for block in self.blocks]

        # test if after rotation any of blocks has collision
        if not self.test_collision(new_pos):
            # update pos for blocks
            for i, block in enumerate(self.blocks):
                block.pos = new_pos[i]
