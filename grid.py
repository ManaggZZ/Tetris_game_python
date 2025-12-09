import pygame
from colors import Colors

#* Create the grid
# Tetris uses a 20×10 grid (20 rows, 10 columns) with (0,0) at the top-left.
# We'll represent it as a 2D list. Each cell stores:
#   0 → empty
#   1–7 → colors of permanently placed blocks
# The active tetromino (still moving) is handled separately and not stored in the grid.

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
        
    def is_inside(self, row, column):   #! This method is to set the boundary while moving the blocks out of the window
        if row >= 0 and row < self.num_rows and column >= 0 and column <self.num_cols:
            return True
        return False

    def is_empty(self, row, column):     #! To handle the collision of falling and locking blocks
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):     #! To check if any row is completed
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0
    
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0
    
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):   #* To move up while checking the rows
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed


#* How Pygame draws: Display Surface, Regular Surface, and Rect
# The display surface (created with set_mode) is the main canvas we see on screen. We can have only one per game.
# Regular surfaces are additional drawable surfaces (e.g., for text) and we can create many of them.
# A Rect represents a rectangular area with position and size, used for drawing, positioning, and collision detection.

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # SYNTAX -> cell_rect = pygame.Rect(x, y, w, h) x and y are coordinates of top left corner
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                # SYNTAX -> pygame.draw.rect(surface , color, rect)  surface is to draw obj on i.e, the display surface in the main file
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
                #> pygame.draw.rect(screen, (50, 50, 50), cell_rect, 1)
                
                #* pygame.Rect is used to define the structure only and pygame.draw.rect is used to actually draw something