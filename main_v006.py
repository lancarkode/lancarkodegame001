# Lancarkode game #001
# Title     : Shoot Factor!!! - V6
# Author    : Patuan P. T.
# Date      : 11/04/21

#################
# In this version, I add the asteroids
# The process is the same with version 4 and 5 (blit and transform)
# We will put them in right side of the screen
# Pay attention with the coordinates value each of them
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

# We will transform the main character
# The ratio of the scale is 1:10. This is the result size.
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 42
# Now we scale the image
CHARACTER_IMAGE = pygame.transform.scale(CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
# we see that the spaceship is facing downward, we need it facing to the right.
# the angle is 90 degree
DEGREE = 90
CHARACTER_IMAGE = pygame.transform.rotate(CHARACTER_IMAGE, DEGREE)
# after this we update the screen_draw() below

# Adding the Asteroids
# The height of the space screen is 600 pixels.
# The x coordinate will be 100 pixels.
# the distance to the next asteroids is 150 pixels
# The y coordinate will be the max width minus the width of the character
ASTEROID_WIDTH = 86
ASTEROID_HEIGHT = 82
ASTEROIDS_ALL_INIT_X = WIDTH - ASTEROID_WIDTH
ASTEROIDS_ONE_INIT_Y = 100
ASTEROIDS_TWO_INIT_Y = ASTEROIDS_ONE_INIT_Y + 150
ASTEROIDS_THREE_INIT_Y = ASTEROIDS_ONE_INIT_Y + 300
# Load the asteroids image
ASTEROIDS_ONE = pygame.image.load("./Assets/asteroids1.png")
ASTEROIDS_TWO = pygame.image.load("./Assets/asteroids2.png")
ASTEROIDS_THREE = pygame.image.load("./Assets/asteroids3.png")
# Scale the asteroids
ASTEROIDS_ONE = pygame.transform.scale(ASTEROIDS_ONE, (ASTEROID_WIDTH, ASTEROID_HEIGHT))
ASTEROIDS_TWO = pygame.transform.scale(ASTEROIDS_TWO, (ASTEROID_WIDTH, ASTEROID_HEIGHT))
ASTEROIDS_THREE = pygame.transform.scale(ASTEROIDS_THREE, (ASTEROID_WIDTH, ASTEROID_HEIGHT))
# After this we blit all the asteroids in the screen_draw() function below


# we make the screen drawing function
# the function need to be called inside the game function while running
def screen_draw():
    SCREEN.fill(WHITE)  # we fill the screen with white color
    SCREEN.blit(CHARACTER_IMAGE, (CHARACTER_INIT_X, CHARACTER_INIT_Y))  # we blit the main character after the screen
    SCREEN.blit(ASTEROIDS_ONE, (ASTEROIDS_ALL_INIT_X, ASTEROIDS_ONE_INIT_Y))  # blit the asteroids one
    SCREEN.blit(ASTEROIDS_TWO, (ASTEROIDS_ALL_INIT_X, ASTEROIDS_TWO_INIT_Y))  # blit the asteroids two
    SCREEN.blit(ASTEROIDS_THREE, (ASTEROIDS_ALL_INIT_X, ASTEROIDS_THREE_INIT_Y))  # blit the asteroids three
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
