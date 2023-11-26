from constants import *
from block import Tetromino


class Game:
    def __init__(self, app):
        self.app = app
        
        # create group for all sprites
        self.sprites = pygame.sprite.Group()

        # create first tetromino
        self.tetromino = Tetromino(self, False)
        
        # create next tetromino
        self.next_block = Tetromino(self)

        # set timer to 0
        self.timer = 0.0

        # create list for collisions
        self.collisions = [[0 for x in range(GRID_W)] for y in range(GRID_H)]

        # bool to check if game should be sped up
        self.speed_up = False

        # render text for next
        self.next_text = app.font.render("Next", True, (255, 255, 255))

    def tick(self, dt):
        # add dt to timer
        self.timer += dt

        # check if tetromino should be ticked
        if self.speed_up or self.timer > 300:
            # check for full row
            self.check_for_full_rows()

            # tick tetromino
            self.tetromino.tick()
            self.timer = 0.0

            # check if tetromino hit the ground
            if self.tetromino.landed:
                # if block y did not change
                if self.tetromino.blocks[0].pos.y == 0:
                    pygame.time.wait(200)
                    self.__init__(self.app)
                else:

                    # add collisions
                    for block in self.tetromino.blocks:
                        x = int(block.pos.x)
                        y = int(block.pos.y)
                        self.collisions[y][x] = block

                    self.next_block.next = False
                    self.tetromino = self.next_block

                    # create new tetromino
                    self.next_block = Tetromino(self)

        # update sprites
        self.sprites.update()

    def draw(self):

        # draw grid
        for x in range(SIDE_SIZE, GRID_W + SIDE_SIZE):
            for y in range(GRID_H):
                pygame.draw.rect(self.app.screen, (12, 12, 12), (x *
                                 BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        # draw sprites
        self.sprites.draw(self.app.screen)

        # draw next block text
        self.app.screen.blit(self.next_text, ((
            SIDE_SIZE * 2 + GRID_W - SIDE_SIZE / 2) * BLOCK_SIZE, (GRID_H/2-4)*BLOCK_SIZE))

    def handle_input(self, key, down):
        if down:
            # left key
            if key == pygame.K_LEFT:
                self.tetromino.move(MOVE_LEFT)
            # right key
            elif key == pygame.K_RIGHT:
                self.tetromino.move(MOVE_RIGHT)
            # up key
            elif key == pygame.K_UP:
                self.tetromino.rotate()
            # down ley
            elif key == pygame.K_DOWN:
                self.speed_up = True
        else:
            if key == pygame.K_DOWN:
                self.speed_up = False

    def check_for_full_rows(self):
        row = GRID_H - 1  # row to check

        # go through all blocks
        for y in range(GRID_H - 1, -1, -1):
            for x in range(GRID_W):
                self.collisions[row][x] = self.collisions[y][x]

                if self.collisions[y][x]:
                    self.collisions[row][x].pos = vec(x, y)

            # if is not full row
            if sum(map(bool, self.collisions[y])) < GRID_W:
                row -= 1
                continue

            # remove blocks
            for x in range(GRID_W):
                self.collisions[row][x].dead = True
                self.collisions[row][x] = 0
