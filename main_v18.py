import pygame

pygame.init()

# screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 30
VEL = 10


def move(player_a, player_b):
    player_a.y += VEL
    player_b.y -= VEL


def draw_screen(player_a, player_b):
    SCREEN.fill(WHITE)
    box_a = pygame.draw.rect(SCREEN, BLACK, player_a).move()
    box_b = pygame.draw.rect(SCREEN, BLACK, player_b)
    SCREEN.blit(box_a)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player_a = pygame.Rect(100, 100, 20, 20)
        player_b = pygame.Rect(100, 500, 20, 20)

        move(player_a, player_b)

        draw_screen(player_a, player_b)

    pygame.display.quit()


if __name__ == "__main__":
    main()
