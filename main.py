import pygame, sys
#// from grid import Grid
#// from tetraminoes import *
#// from block import Block
from game import Game

pygame.init()
dark_blue = (44, 44, 127)

# GAME WINDOW   

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

#! In game the coordinate system starts from top left corner and if we move right then x increases and if we move down then y increases

clock = pygame.time.Clock()     #! This is used to control the frame rate of game.

# Using Grid Class
#// game_grid = Grid()

#// block = IBlock()
#// block.move(4,3)

game = Game()

# GAME LOOP
    # Event handling
    # Updating the positions
    # Drawing objects

# Here GMAE_UPDATE is the custom event name
GAME_UPDATE = pygame.USEREVENT      #! USEREVENT is a special event type in pygame that can be used to create custom events. In this case it is used to create an event that will be triggered every time the block's position need to be updated.
pygame.time.set_timer(GAME_UPDATE, 20)     #* set_timer(event_name, interval in miliseconds)

while True:     # This will run till the game is open
    for event in pygame.event.get():    # This will get all the events that pygame recognises and puths them in a list. Then we look through the list of events and check if any of the events is QUIT event. The QUIT event is when we click the close button of the window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()    #! Press any key to reset the game.

            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        
        #// keys = pygame.key.get_pressed()

        #// # Check if specific keys are held down and update position accordingly
        #// if keys[pygame.K_LEFT]:
        #//     game.move_left()
        #// if keys[pygame.K_RIGHT]:
        #//     game.move_right()
        #// if keys[pygame.K_DOWN]:
        #//     game.move_down()
        
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    
    # Drawing
    screen.fill(dark_blue)
    #// game_grid.draw(screen)
    #// block.draw(screen)
    game.draw(screen)

    pygame.display.update() 
    clock.tick(60)      # The tick() method takes an integer as an argument and that integer is the number of frames per sec

