# Lancarkode game #001
# Title     : Shoot Factor!!! - V4
# Author    : Patuan P. T.
# Date      : 11/04/21

#################
# In this version, I put the main character or the spaceship
# we will use the "blit" function
# the blit function is one of the important function in game development
# all the object will be drawn in every frame on the screen
# Blit means that the character will be in the screen not at the top of the screen surface
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

# set caption
pygame.display.set_caption("Shooting Factor!!!")  # this is the way we set the caption

# set icon
ICON = pygame.image.load("./Assets/icon.png")  # this is the way we load images from our directories to pygame
pygame.display.set_icon(ICON)  # this is the way we put the icon to the window

# colors
# we populate all the colors here
WHITE = (255, 255, 255)

# the main character
CHARACTER_IMAGE = pygame.image.load("./Assets/spaceship_red.png")  # load the image of the character
CHARACTER_INIT_X = 100      # x position on the screen
CHARACTER_INIT_Y = 600/2   # y position on the screen
# after this we update the screen_draw() below


# we make the screen drawing function
# the function need to be called inside the game function while running
def screen_draw():
    SCREEN.fill(WHITE)  # we fill the screen with white color
    SCREEN.blit(CHARACTER_IMAGE, (CHARACTER_INIT_X, CHARACTER_INIT_Y))  # we blit the main character after the screen
    pygame.display.update()  # we update the display every time


# game function
# remember that all your game will be running in this function, not at the other functions
def main():
    run = True
    while run:  # if run is True, then the game window appear and running until QUIT event happen
        for event in pygame.event.get():  # listening to every game event and creating all event
            # creating close the window event
            if event.type == pygame.QUIT:
                run = False  # if the user say to quit, then the variable run will be False

        # call the screen draw while running
        screen_draw()

    # quit the game
    pygame.display.quit()  # The while loop has finished (running is False) , so quit the display window


# calling the game, have fun!!!
if __name__ == "__main__":
    main()
