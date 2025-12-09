from colors import Colors
import pygame
from position import Position

#! We will use inheritance and make a block class which will be used to make different blocks as child classes.
#! This is the parent class and tertaminoes are the child classes.
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}     # We will use this dictionary to store the occupied cells in the bounding grid for each rotation state of the block
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
        
    #! So to move the block we will move the origin of the block which is at top left corner for this we will use row_offset and column_offset
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
    
    def get_cell_positions(self):    # This method is used to calc the actual position after offset is applied
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        #// self.rotation_state += 1
        #// if self.rotation_state == len(self.cells):
        # //    self.rotation_state = 0
        if not self.cells:
            return
        self.rotation_state = (self.rotation_state + 1) % len(self.cells)

    #! This method is to prevent tetraminoes to move outside the screen while rotating
    def undo_rotation(self):
        #// self.rotation_state -= 1
        #// if self.rotation_state == -1:
        #//     self.rotation_state = len(self.cells) - 1
        if not self.cells:
            return
        self.rotation_state = (self.rotation_state - 1) % len(self.cells)

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

