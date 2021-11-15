# Lancarkode game #001
# Title     : Shoot Factor!!! - V9
# Author    : Patuan P. T.
# Date      : 11/04/21

#################
# In this version, we block the movement of the object
# We draw a rectangle in the screen to represent the planet
# the main character cannot move outside the planet
# the asteroid will move to the surface of the planet
# pay attention to the screen_draw(), the character_move() and asteroid_move()
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
BLUE = (0, 0, 255)

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

# The FPS is 30
FPS = 30

# The clock function
CLOCK = pygame.time.Clock()  # After this we use the FPS with this clock while the game is running

# The velocity
CHARACTER_VEL = 5
ASTEROIDS_ONE_VEL = 2
ASTEROIDS_TWO_VEL = 1
ASTEROIDS_THREE_VEL = 1

# The planet
PLANET = pygame.Rect(0, 0, 300, 600)


# we make the screen drawing function
# the function need to be called inside the game function while running
def screen_draw(character, asteroid_one, asteroid_two, asteroid_three):
    SCREEN.fill(WHITE)  # we fill the screen with white color
    pygame.draw.rect(SCREEN, BLUE, PLANET)  # drawing the plate
    SCREEN.blit(CHARACTER_IMAGE, (character.x, character.y))  # we blit the main character after the screen
    SCREEN.blit(ASTEROIDS_ONE, (asteroid_one.x, ASTEROIDS_ONE_INIT_Y))  # blit the asteroids one
    SCREEN.blit(ASTEROIDS_TWO, (asteroid_two.x, ASTEROIDS_TWO_INIT_Y))  # blit the asteroids two
    SCREEN.blit(ASTEROIDS_THREE, (asteroid_three.x, ASTEROIDS_THREE_INIT_Y))  # blit the asteroids three
    pygame.display.update()  # we update the display every time


# Move the character
# The character can move forward, backward, upward, dan downward
def character_move(character_object, key_press):
    # moving forward if the right arrow key is pressed
    if key_press[pygame.K_RIGHT] and character_object.x + character_object.width <= PLANET.width:
        character_object.x += CHARACTER_VEL
    # moving backward if the left arrow key is pressed
    if key_press[pygame.K_LEFT] and character_object.x - CHARACTER_VEL >= 0:
        character_object.x -= CHARACTER_VEL
    # moving upward if the up arrow key is pressed
    if key_press[pygame.K_UP] and character_object.y - CHARACTER_VEL >= 0:
        character_object.y -= CHARACTER_VEL
    # moving downward if the down arrow key is pressed
    if key_press[pygame.K_DOWN] and character_object.y + character_object.width + CHARACTER_VEL <= PLANET.height:
        character_object.y += CHARACTER_VEL


# Move the asteroid
# we only move the asteroid to the left only
def asteroid_move(asteroid_object, vel):
    if asteroid_object.x >= PLANET.width:
        asteroid_object.x -= vel


# game function
# remember that all your game will be running in this function, not at the other functions
def main():
    run = True
    # we create a rectangle as same as the object
    # we do this to retrieve the coordinate of the object
    character = pygame.Rect(CHARACTER_INIT_X, CHARACTER_INIT_Y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    asteroid_one = pygame.Rect(ASTEROIDS_ALL_INIT_X, ASTEROIDS_ONE_INIT_Y, ASTEROID_WIDTH, ASTEROID_HEIGHT)
    asteroid_two = pygame.Rect(ASTEROIDS_ALL_INIT_X, ASTEROIDS_TWO_INIT_Y, ASTEROID_WIDTH, ASTEROID_HEIGHT)
    asteroid_three = pygame.Rect(ASTEROIDS_ALL_INIT_X, ASTEROIDS_THREE_INIT_Y, ASTEROID_WIDTH, ASTEROID_HEIGHT)

    while run:  # if run is True, then the game window appear and running until QUIT event happen
        CLOCK.tick(FPS)  # while run using the FPS setting
        for event in pygame.event.get():  # listening to every game event and creating all event
            # creating close the window event
            if event.type == pygame.QUIT:
                run = False  # if the user say to quit, then the variable run will be False

        # Key get pressed function
        key_press = pygame.key.get_pressed()

        # we move the character. Now we input the key_press inside the character_move()
        character_move(character, key_press)

        # we move the asteroid
        asteroid_move(asteroid_one, ASTEROIDS_ONE_VEL)
        asteroid_move(asteroid_two, ASTEROIDS_TWO_VEL)
        asteroid_move(asteroid_three, ASTEROIDS_THREE_VEL)

        # call the screen draw while running
        # we add the object to the screen draw
        screen_draw(character, asteroid_one, asteroid_two, asteroid_three)

    # quit the game
    pygame.display.quit()  # The while loop has finished (running is False) , so quit the display window


# calling the game, have fun!!!
if __name__ == "__main__":
    main()
