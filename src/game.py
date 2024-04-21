from constants import pygame, GRID_WIDTH, GRID_HEIGHT, Vec, FPS, BLOCK_SIZE, STATS_PAGE_WIDTH

from tetromino import Tetromino


class Game:
    def __init__(self, app):
        self.app = app

        # create a group for all sprites
        self.sprites = pygame.sprite.Group()

        # create first tetromino
        self.tetromino = Tetromino(self)
        self.tetromino.reset_pos()

        # create next tetromino
        self.next_tetromino = Tetromino(self)

        # set timer to 0
        self.timer = 0.0

        # create a list for collisions
        self.collisions = [[0 for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]

        self.speed = 18  # base multiplier for speed
        self.speed_up = False

        self.points = 0

    def tick(self, dt):
        self.timer += dt

        # calc a tetromino tick time
        mul = self.speed
        if self.speed_up:
            mul = 1  # if speed up use 1
        threshold = 1000.0 / FPS * mul

        if self.timer < threshold:
            # update sprites
            self.sprites.update()
            return

        self.check_for_full_rows()

        # move tetromino 1 block down
        if self.tetromino.move(Vec(0, 1)):
            if self.tetromino.blocks[0].pos.y == 0:  # if block did not move
                # game ended
                print("game ended")

                # wait for a while
                pygame.time.wait(200)

                # reset points text
                self.app.points_text = self.app.font.render("Points: 0", True, (255, 255, 255))
                # update last points
                self.app.last_points_text = self.app.font.render("Last Points: " + str(self.points),
                                                                 True,
                                                                 (255, 255, 255))

                self.app.game = Game(self.app)  # start a new game
                return

            # add collision blocks
            for block in self.tetromino.blocks:
                x = int(block.pos.x)
                y = int(block.pos.y)
                if y >= 0:
                    self.collisions[y][x] = block

            # create new tetromino
            self.tetromino = self.next_tetromino
            self.tetromino.reset_pos()
            self.next_tetromino = Tetromino(self)

            # add point
            self.points += 1
            self.app.points_text = self.app.font.render("Points: " + str(self.points),
                                                        True,
                                                        (255, 255, 255))

        # reset timer to 0
        self.timer = 0.0

        # update sprites
        self.sprites.update()

    def check_for_full_rows(self):
        row = GRID_HEIGHT - 1
        # start from bottom
        for y in range(GRID_HEIGHT - 1, -1, -1):
            # check if all blocks in row exist
            count = 0
            for x in range(GRID_WIDTH):
                if self.collisions[row][x]:
                    count += 1
                else:
                    break

            # not a full row move on
            if count != GRID_WIDTH:
                row -= 1
                continue

            # remove blocks
            for x in range(GRID_WIDTH):
                self.collisions[row][x].kill()
                self.collisions[row][x] = 0

            # move blocks above down 1 block
            for i in range(row - 1, -1, -1):
                for x in range(GRID_WIDTH):
                    if not self.collisions[i][x]:
                        continue
                    self.collisions[i][x].pos = Vec(x, i + 1)  # move block down
                    self.collisions[i + 1][x] = self.collisions[i][x]  # move collision down
                    self.collisions[i][x] = 0  # remove old collision

            # add point
            self.points += 100
            self.app.points_text = self.app.font.render("Points: " + str(self.points),
                                                        True,
                                                        (255, 255, 255))

    def draw(self):
        # fill bg
        self.app.screen.fill("black")

        # fill stats area
        self.app.screen.fill((20, 20, 20), (GRID_WIDTH * BLOCK_SIZE,
                                            0, STATS_PAGE_WIDTH * BLOCK_SIZE,
                                            GRID_HEIGHT * BLOCK_SIZE))

        # draw next block
        self.app.screen.blit(self.app.next_block_text, self.app.next_block_pos)

        # draw points
        self.app.screen.blit(self.app.points_text, self.app.points_pos)

        # draw last points
        self.app.screen.blit(self.app.last_points_text, self.app.last_points_pos)

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
                self.tetromino.move(Vec(-1, 0))
            # move right
            elif key == pygame.K_RIGHT:
                self.tetromino.move(Vec(1, 0))
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
            return True

        # check y in area
        if y >= GRID_HEIGHT:
            return True

        # check for already fallen blocks
        if y >= 0 and self.collisions[y][x]:
            return True

        return False
