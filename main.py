import pygame, sys
#// from grid import Grid
#// from tetraminoes import *
#// from block import Block
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)     #* None is for default font
score_surface = title_font.render("Score", True, Colors.white)
next_suface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
 

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# GAME WINDOW   

#// screen = pygame.display.set_mode((300, 600))
screen = pygame.display.set_mode((500, 620))
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
pygame.time.set_timer(GAME_UPDATE, 200)     #* set_timer(event_name, interval in miliseconds)

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
                game.update_score(0, 1)
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
    score_value_surface = title_font.render(str(game.score), True, Colors.white)    #* As the score is not statis

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))  #! blit() method is block image transfer
    screen.blit(next_suface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update() 
    clock.tick(60)      # The tick() method takes an integer as an argument and that integer is the number of frames per sec

