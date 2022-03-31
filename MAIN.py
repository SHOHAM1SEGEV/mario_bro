import pygame
from helpers import screen, X_LOCATION1, Y_LOCATION1, WIDTH1, HEIGHT1, \
    X_LOCATION2, Y_LOCATION2, WIDTH2, HEIGHT2, mouse_in_button
from click_button import click_mouse_button


def MAIN():
    pygame.init()
    pygame.display.set_caption("mario bro")

    img_path_3 = "photo/background-2.png"
    img_3 = pygame.image.load(img_path_3)
    img_3 = pygame.transform.scale(img_3, (WIDTH1, HEIGHT1))
    screen.blit(img_3, (X_LOCATION1, Y_LOCATION1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(img_3, (X_LOCATION1, Y_LOCATION1))

        pygame.display.update()
    pygame.quit()
    quit()


def enter_game():
    pygame.init()
    pygame.display.set_caption("mario_bro")

    # background img (mario photo)
    img_path_1 = "photo/mario_photo.jpg"
    img_1 = pygame.image.load(img_path_1)
    img_1 = pygame.transform.scale(img_1, (WIDTH1, HEIGHT1))
    screen.blit(img_1, (X_LOCATION1, Y_LOCATION1))

    # play button photo
    img_path_2 = "photo/play_button.jpg"
    img_2 = pygame.image.load(img_path_2)
    img_2 = pygame.transform.scale(img_2, (WIDTH2, HEIGHT2))
    screen.blit(img_2, (X_LOCATION2, Y_LOCATION2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(click_mouse_button, event.pos):
                    MAIN()

        screen.blit(img_1, (X_LOCATION1, Y_LOCATION1))
        screen.blit(img_2, (X_LOCATION2, Y_LOCATION2))
        pygame.display.update()
    pygame.quit()
    quit()
enter_game()
MAIN()
