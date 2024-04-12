from constants import Vec, GRID_WIDTH, BLOCK_SIZE, pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, game, image, pos):
        super().__init__(game.sprites)

        self.image = image
        self.rect = image.get_rect()

        # set pos to center
        self.pos = Vec(pos) + Vec(GRID_WIDTH / 2 - 1, 0)

    def update(self):
        self.rect.topleft = self.pos * BLOCK_SIZE

    def move(self, vel):
        self.pos += vel

    def rotate(self, start_pos):
        # rotate 90 deg to the right
        translated = self.pos - start_pos
        rotated = translated.rotate(90)
        return rotated + start_pos
