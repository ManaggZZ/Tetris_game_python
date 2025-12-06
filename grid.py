import pygame

# Create the grid 
# In tetris the gameplay area is a grid consisting of 20 rows and 10 columns.
# The game pieces or tetraminoes fall down the grid and player must arrange them to form the complete rows without any gaps. 
# We will continue the rows from top to bottom and the column from left to right with the top left center at row 0 and column 0 being the origin. To represent the grid we will use a 2D array which can be implemented as a list of list. 
# In our implementation empty cell will be represented by the value 0 when a tetromino a block is permanently placed on the grid by the player the corresponding cells will be assigned a value reflecting a color. 
# For example if we place a red teromino on the grid it will give a value 2. Similarly if you place a yellow block we will assign the value 4 to its corresponding cells. Each color has a unique numerical value.
# Since there are seven different colors in the game the values used in the 2D array will be ranged from 0 to 7 0 for an empty cell and 1 to 7 for the colors of the blocks.
# However the current block that can still be controlled by the player will not be reflected in the array and will instead be sorted and managed separately in the game logic.

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
        # we will us ethe index of this list of colors to get the color.

# How pygame draws - Display surface, Regular surface and Rect.
# The display surface is the surface where we see all the game objets. It is like a blank canvas. We can have only one per game. The display surface is created when we call the set_mode function and it's the object we use when we call the update function. 
# A regular surface is a surface like the display surface that we can draw on it, we can have as many surfaces as we want in the game unlike the display surface which we can only have one per game. We are going to use the surfaces to draw text on a display. 
# A rect is a rectangle area, it has a position and a size. We use rect for collision detection, each manipulation of objects and for easy drawing on a surface.

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # SYNTAX -> cell_rect = pygame.Rect(x, y, w, h) x and y are coordinates of top left corner
                cell_rect = pygame.Rect(column*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size)
                # SYNTAX -> pygame.draw.rect(surface , color, rect)  surface is to draw obj on i.e, the display surface in the main file
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
                # pygame.draw.rect(screen, (50, 50, 50), cell_rect, 1)
                
                # pygame.Rect is used to define teh structure only and pygame.draw.rect is used to actually draw something