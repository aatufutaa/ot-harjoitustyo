from constants import *

from tetromino import Tetromino


class Game:
    def __init__(self, app):
        self.app = app

        # create a group for all sprites
        self.sprites = pygame.sprite.Group()

        # create first tetromino
        self.tetromino = Tetromino(self)

        # set timer to 0
        self.timer = 0.0

        # create a list for collisions
        self.collisions = [[0 for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]

        self.speed = 18  # base multiplier for speed
        self.speed_up = False

    def tick(self, dt):
        self.timer += dt

        # calc a tetromino tick time
        mul = self.speed
        if self.speed_up:
            mul = 1  # if speed up use 1
        threshold = 1000.0 / FPS * mul

        if self.timer >= threshold:
            self.check_for_full_rows()

            # move tetromino 1 block down
            if self.tetromino.move(vec(0, 1)):
                print("tetromino hit ground!")
                pass  # tetromino landed here!!!

            # reset timer to 0
            self.timer = 0.0

        # update sprites
        self.sprites.update()

    def check_for_full_rows(self):
        pass

    def draw(self):
        # fill bg
        self.app.screen.fill("black")

        # draw grid
        for x in range(0, GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                pygame.draw.rect(self.app.screen,
                                 (12, 12, 12),
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                                 1)

        # draw sprites
        self.sprites.draw(self.app.screen)

    def handle_input(self, key, down):
        if down:
            # move left
            if key == pygame.K_LEFT:
                self.tetromino.move(vec(-1, 0))
            # move right
            elif key == pygame.K_RIGHT:
                self.tetromino.move(vec(1, 0))
            # rotate
            elif key == pygame.K_UP:
                self.tetromino.rotate()
            # speed up
            elif key == pygame.K_DOWN:
                self.speed_up = True
        else:
            # dont speed up
            if key == pygame.K_DOWN:
                self.speed_up = False

    def test_block_collision(self, pos):
        x = int(pos.x)
        y = int(pos.y)

        # check x in area
        if x < 0 or x >= GRID_WIDTH:
            print("colliding x " + str(x))
            return True

        # check y in area
        if y >= GRID_HEIGHT:
            print("colliding y " + str(y))
            return True

        # check for already fallen blocks
        if self.collisions[y][x]:
            return True

        return False
