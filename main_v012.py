# Lancarkode game #001
# Title     : Shoot Factor!!! - V12
# Author    : Patuan P. T.
# Date      : 11/04/21

#################
# In this version, you will learn how to make your own event
# The idea is when the bullet is collide with the asteroids,
# the asteroid will remove from the screen after its hardness left only 1
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
BLACK = (0, 0, 0)

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
BULLET_VEL = 8

# The planet
PLANET = pygame.Rect(0, 0, 300, 600)

# Asteroids hit event
ASTEROIDS_ONE_EVENT = pygame.USEREVENT + 1
ASTEROIDS_TWO_EVENT = pygame.USEREVENT + 2
ASTEROIDS_THREE_EVENT = pygame.USEREVENT + 3

# Asteroid minimum hardness
MIN_HARDNESS = 1


# we make the screen drawing function
# the function need to be called inside the game function while running
def screen_draw(character, asteroid_one, asteroid_two, asteroid_three, bullet_list,
                asteroid_one_hardness, asteroid_two_hardness, asteroid_three_hardness):
    SCREEN.fill(WHITE)  # we fill the screen with white color
    pygame.draw.rect(SCREEN, BLUE, PLANET)  # drawing the plate
    SCREEN.blit(CHARACTER_IMAGE, (character.x, character.y))  # we blit the main character after the screen
    # we remove the asteroid if the hardness is 1
    if asteroid_one_hardness > MIN_HARDNESS:
        SCREEN.blit(ASTEROIDS_ONE, (asteroid_one.x, ASTEROIDS_ONE_INIT_Y))  # blit the asteroids one
    if asteroid_two_hardness > MIN_HARDNESS:
        SCREEN.blit(ASTEROIDS_TWO, (asteroid_two.x, ASTEROIDS_TWO_INIT_Y))  # blit the asteroids two
    if asteroid_three_hardness > MIN_HARDNESS:
        SCREEN.blit(ASTEROIDS_THREE, (asteroid_three.x, ASTEROIDS_THREE_INIT_Y))  # blit the asteroids three
    # bullet draw
    for one_bullet in bullet_list:
        pygame.draw.rect(SCREEN, BLACK, one_bullet)
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
# and the hardness is greater that 1
def asteroid_move(asteroid_object, vel, asteroid_hardness):
    if asteroid_object.x >= PLANET.width and asteroid_hardness > 1:
        asteroid_object.x -= vel


# bullet shoot
def bullet_shoot(bullet_list, asteroid_one, asteroid_two, asteroid_three,
                 asteroid_one_event, asteroid_two_event, asteroid_three_event,
                 asteroid_one_hardness, asteroid_two_hardness, asteroid_three_hardness):
    for one_bullet in bullet_list:
        one_bullet.x += BULLET_VEL
        # if the bullet is out side the screen we remove the bullet
        # for saving our RAM
        if one_bullet.x + BULLET_VEL > WIDTH:
            bullet_list.remove(one_bullet)

        # we remove the bullet when colliding with the asteroid
        # and the hardness greater than minimum hardness
        # and the asteroid health will be decreased by the bullet
        # this the way we use collide rectangular
        if asteroid_one.colliderect(one_bullet) and asteroid_one_hardness > MIN_HARDNESS:
            pygame.event.post(pygame.event.Event(asteroid_one_event))
            bullet_list.remove(one_bullet)
        elif asteroid_two.colliderect(one_bullet) and asteroid_two_hardness > MIN_HARDNESS:
            pygame.event.post(pygame.event.Event(asteroid_two_event))
            bullet_list.remove(one_bullet)
        elif asteroid_three.colliderect(one_bullet) and asteroid_three_hardness > MIN_HARDNESS:
            pygame.event.post(pygame.event.Event(asteroid_three_event))
            bullet_list.remove(one_bullet)
# after this we draw the bullet in the screen_draw


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

    # we create the bullet list
    bullet_list = []

    # the asteroid hardness information
    asteroid_one_hardness = 10
    asteroid_two_hardness = 4
    asteroid_three_hardness = 6

    while run:  # if run is True, then the game window appear and running until QUIT event happen
        CLOCK.tick(FPS)  # while run using the FPS setting
        for event in pygame.event.get():  # listening to every game event and creating all event
            # creating close the window event
            if event.type == pygame.QUIT:
                run = False  # if the user say to quit, then the variable run will be False

            # creating fire shooting event
            # the event is happened when the player pressed "F" key from the keyboard
            # then create rectangles
            # te event type is key down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    # create a bullet
                    bullet = pygame.Rect(character.x + character.width,
                                         character.y + character.height // 2, 10, 5)
                    # put the bullet in the list
                    bullet_list.append(bullet)

            # create event when the asteroids are hit
            if event.type == ASTEROIDS_ONE_EVENT:
                asteroid_one_hardness -= 1
            if event.type == ASTEROIDS_TWO_EVENT:
                asteroid_two_hardness -= 1
            if event.type == ASTEROIDS_THREE_EVENT:
                asteroid_three_hardness -= 1

        # Key get pressed function
        key_press = pygame.key.get_pressed()

        # we move the character. Now we input the key_press inside the character_move()
        character_move(character, key_press)

        # we move the asteroid
        # we add the hardness information
        asteroid_move(asteroid_one, ASTEROIDS_ONE_VEL, asteroid_one_hardness)
        asteroid_move(asteroid_two, ASTEROIDS_TWO_VEL, asteroid_two_hardness)
        asteroid_move(asteroid_three, ASTEROIDS_THREE_VEL, asteroid_three_hardness)

        # We use the list and velocity to draw it latter.
        # The 5 information that a bullet has is created here
        # we add the information of the asteroids that the bullet is colliding with
        bullet_shoot(bullet_list, asteroid_one, asteroid_two, asteroid_three,
                     ASTEROIDS_ONE_EVENT, ASTEROIDS_TWO_EVENT, ASTEROIDS_THREE_EVENT,
                     asteroid_one_hardness, asteroid_two_hardness, asteroid_three_hardness)

        # call the screen draw while running
        # we add the bullet_list to the screen draw
        screen_draw(character, asteroid_one, asteroid_two, asteroid_three, bullet_list,
                    asteroid_one_hardness, asteroid_two_hardness, asteroid_three_hardness)

    # quit the game
    pygame.display.quit()  # The while loop has finished (running is False) , so quit the display window


# calling the game, have fun!!!
if __name__ == "__main__":
    main()
