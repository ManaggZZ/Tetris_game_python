from grid import Grid
from tetraminoes import *
import random

#! To improve code organization and make it easier to manage in the future we will create a game class to hold the grid and the block objects as well as various methods. The game will serve as container for all the elements of our game such as the grid, current and next block and game state. It will also holds methods that manage the game's logic such as updating the block's positions, checking for collisions, etc. By centralizing all the games functionality within this class it will be easier to understand maintain and expand upon in future.

class Game:
    def __init__(self):
        self.grid = Grid()
        # self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
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

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)