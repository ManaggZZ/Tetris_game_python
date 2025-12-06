import pygame

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
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
    
    def get_cell_colors(self):
        dark_grey = (26, 31, 40)       # color of empty cell
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (116, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]
        #! we will us ethe index of this list of colors to get the color.

#* How Pygame draws: Display Surface, Regular Surface, and Rect
# The display surface (created with set_mode) is the main canvas we see on screen. We can have only one per game.
# Regular surfaces are additional drawable surfaces (e.g., for text) and we can create many of them.
# A Rect represents a rectangular area with position and size, used for drawing, positioning, and collision detection.

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # SYNTAX -> cell_rect = pygame.Rect(x, y, w, h) x and y are coordinates of top left corner
                cell_rect = pygame.Rect(column*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size)
                # SYNTAX -> pygame.draw.rect(surface , color, rect)  surface is to draw obj on i.e, the display surface in the main file
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
                #alt pygame.draw.rect(screen, (50, 50, 50), cell_rect, 1)
                
                #* pygame.Rect is used to define the structure only and pygame.draw.rect is used to actually draw something