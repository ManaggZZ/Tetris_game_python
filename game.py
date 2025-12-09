from grid import Grid
from tetraminoes import *
import random

#! To improve code organization and make it easier to manage in the future we will create a game class to hold the grid and the block objects as well as various methods. The game will serve as container for all the elements of our game such as the grid, current and next block and game state. It will also holds methods that manage the game's logic such as updating the block's positions, checking for collisions, etc. By centralizing all the games functionality within this class it will be easier to understand maintain and expand upon in future.

class Game:
    def __init__(self):
        self.grid = Grid()
        # self.blocks = [IBlock(), IBlock(), IBlock(), OBlock(), OBlock(), OBlock(), IBlock()]
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
        #* We will cycle through the list of blocks ensuring that each block appears atleast once before repeating the cycle

    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside() == False or self.block_fits == False:
            self.current_block.move(0,1)    # If the block is outside the window, we undo teh move
    
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False or self.block_fits == False:
            self.current_block.move(0,-1)

    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
        
    def lock_block(self):   #! To lock the block when it reaches the bottom of the screen
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
    
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
        
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits == False:
            self.current_block.undo_rotation()
    
    def block_inside(self):     #! Method to check if the position of block if inside the window or not
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)