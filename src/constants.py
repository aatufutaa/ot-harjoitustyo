import pygame  # for global access

FPS = 60  # how many frams per sec
BLOCK_SIZE = 50  # how many pixels is one block
GRID_W = 10  # how many blocks horizontally
GRID_H = 18  # how many blocks vertically

SIDE_SIZE = 4 # how many blocks on the sides
WINDOW_SIZE = ((GRID_W + SIDE_SIZE * 2) * BLOCK_SIZE, GRID_H * BLOCK_SIZE)

vec = pygame.math.Vector2

# move direction
MOVE_LEFT = vec(-1, 0)
MOVE_UP = vec(0, -1)
MOVE_RIGHT = vec(1, 0)
MOVE_DOWN = vec(0, 1)
