import pygame, sys
from grid import Grid
from tetraminoes import *
# from block import Block

pygame.init()
dark_blue = (44, 44, 127)

# GAME WINDOW   

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

#! In game the coordinate system starts from top left corner and if we move right then x increases and if we move down then y increases

clock = pygame.time.Clock()     #! This is used to control the frame rate of game.

# Using Grid Class
game_grid = Grid()

block = LBlock()
# block.move(4,3)

# GAME LOOP
    # Event handling
    # Updating the positions
    # Drawing objects

while True:     # This will run till the game is open
    for event in pygame.event.get():    # This will get all the events that pygame recognises and puths them in a list. Then we look through the list of events and check if any of the events is QUIT event. The QUIT event is when we click the close button of the window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update() 
    clock.tick(60)      # The tick() method takes an integer as an argument and that integer is the number of frames per sec

