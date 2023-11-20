import pygame
import os

class Block(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()

        # get asset
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "./", "assets", type + "_block.png")
        )

        # set rect
        self.rect = self.image.get_rect()

    # set x of the sprite
    def set_x(self, x):
         self.rect.x = x
    
    # set y of the sprite
    def set_y(self, y):
         self.rect.y = y

    # get x of the sprite
    def get_x(self):
        return self.rect.x
    
    # get y of the sprite
    def get_y(self):
        return self.rect.y
    
    # rotate image 90 deg to the right
    def rotate(self):
        self.image = pygame.transform.rotate(self.image, 90)