# Lancarkode game #001
# Title     : Shoot Factor!!! - V1
# Author    : Patuan P. T.
# Date      : 11/04/21

#################
# In this version, I make the game window
# there are two differences of variables type font
# all CAPITAL variables are the variables for global game settings for creating the games
# all lowercase variables are the variables for the game values
#################

import pygame  # This is the way we import the pygame framework to our code
# Make sure you already have installed the pygame into your environment

pygame.init()  # This is the way we initiate the pygame

# game window size
# you can adjust the game window size by your own self
WIDTH = 1200
HEIGHT = 800

# screen, make the screen with the defined size above
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


# game function
# remember that all your game will be running in this function, not at the other functions
def main():
    run = True
    while run:  # if run is True, then the game window appear and running until QUIT event happen
        for event in pygame.event.get():  # listening to every game event and creating all event
            # creating close the window event
            if event.type == pygame.QUIT:
                run = False  # if the user say to quit, then the variable run will be False

    # quit the game
    pygame.display.quit()  # The while loop has finished (running is False) , so quit the display window


# calling the game, have fun!!!
if __name__ == "__main__":
    main()
