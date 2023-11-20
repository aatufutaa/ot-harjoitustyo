import pygame
from block import Block

def main():
    # initialize pygame
    pygame.init()
    
    # set title for window
    pygame.display.set_caption("Tetris")

    block_size = 50

    # set size for window
    screen = pygame.display.set_mode((block_size * 12, 800))

    clock = pygame.time.Clock()

    # bool for checking if game is running
    running = True

    # add sprites
    sprites = pygame.sprite.Group()
    current_block = Block("s")
    sprites.add(current_block)

    # current game tick
    tick = 0

    # game loop
    while running:
        # handle events
        for event in pygame.event.get():
            # handle quit
            if event.type == pygame.QUIT:
                running = False
            # handle input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_block.set_x(current_block.get_x() - block_size)
                elif event.key == pygame.K_RIGHT:
                    current_block.set_x(current_block.get_x() + block_size)
                elif event.key == pygame.K_UP:
                     current_block.rotate()
                elif event.key == pygame.K_DOWN:
                      current_block.set_y(current_block.get_y() + block_size)
        
        dt = clock.tick(60) # 60 fps

        # tick game
        tick += 1
        if (tick % 60 == 0):
            current_block.set_y(current_block.get_y() + block_size)

        # set bg color
        screen.fill("black")

        # draw sprites
        sprites.draw(screen)

        # update screen
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()