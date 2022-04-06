import pygame
from click_button import click_mouse_button
from helpers import screen, X_LOCATION_1, Y_LOCATION_1, WIDTH_1, HEIGHT_1, \
    X_LOCATION_2, Y_LOCATION_2, WIDTH_2, HEIGHT_2, mouse_in_button, HEIGHT_3, WIDTH_3, Y_LOCATION_3, X_LOCATION_3


def MAIN():
    from helpers import X_LOCATION_CLOUD_1_PART_1, Y_LOCATION_CLOUD_1_PART_1, X_LOCATION_CLOUD_1_PART_2, \
        Y_LOCATION_CLOUD_1_PART_2, X_LOCATION_CLOUD_2_PART_1, Y_LOCATION_CLOUD_2_PART_1, X_LOCATION_CLOUD_2_PART_2, \
        Y_LOCATION_CLOUD_2_PART_2
    pygame.init()
    pygame.display.set_caption("mario bro")

    # IMG BACKGROUND
    img_path_background = "photo/background-2.png"
    img_background = pygame.image.load(img_path_background)
    img_background = pygame.transform.scale(img_background, (WIDTH_1, HEIGHT_1))
    screen.blit(img_background, (X_LOCATION_1, Y_LOCATION_1))

    # IMG GROUND
    img_path_ground = "photo/wall-1.png"
    img_ground = pygame.image.load(img_path_ground)
    img_ground = pygame.transform.scale(img_ground, (WIDTH_3, HEIGHT_3))

    # # IMG PLATFORM problem !!!!!!!!!!!!!
    # img_path_platform = "photo/moving-platformlong.png"
    # img_platform = pygame.image.load(img_path_platform)
    # img_platform = pygame.transform.scale(img_platform, (200, 100))

    # IMG CLOUD_1
    img_path_cloud_1 = "photo/cloud.png"
    img_cloud_1 = pygame.image.load(img_path_cloud_1)
    img_cloud_1 = pygame.transform.scale(img_cloud_1, (120, 50))

    # IMG CLOUD_2
    img_path_cloud_2 = "photo/dobbelclouds.png"
    img_cloud_2 = pygame.image.load(img_path_cloud_2)
    img_cloud_2 = pygame.transform.scale(img_cloud_2, (150, 70))

    # IMG FLOWER 1
    img_path_plower_1 = "photo/flower0.png"
    img_plower_1 = pygame.image.load(img_path_plower_1)
    img_plower_1 = pygame.transform.scale(img_plower_1, (20, 40))

    # IMG FLOWER 2
    img_path_plower_2 = "photo/flower1.png"
    img_plower_2 = pygame.image.load(img_path_plower_2)
    img_plower_2 = pygame.transform.scale(img_plower_2, (20, 40))



    running = True
    while running:
        X_LOCATION_CLOUD_1_PART_1 -= 0.1
        X_LOCATION_CLOUD_1_PART_2 -= 0.1
        X_LOCATION_CLOUD_2_PART_1 -= 0.1
        X_LOCATION_CLOUD_2_PART_2 -= 0.1

        # לעשות שהעננים יחזרו אחורה במקום להמשיך
        if X_LOCATION_CLOUD_1_PART_1 == 0:
            X_LOCATION_CLOUD_1_PART_1 = 1000
        elif X_LOCATION_CLOUD_1_PART_2 == 0:
            X_LOCATION_CLOUD_1_PART_2 = 200

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # IMG BACKGROUND
        screen.blit(img_background, (X_LOCATION_1, Y_LOCATION_1))

        # IMG GROUND
        screen.blit(img_ground, (X_LOCATION_3, Y_LOCATION_3))
        screen.blit(img_ground, (0, 500))

        # IMG CLOUD_1
        screen.blit(img_cloud_1, (X_LOCATION_CLOUD_1_PART_1, Y_LOCATION_CLOUD_1_PART_1))
        screen.blit(img_cloud_1, (X_LOCATION_CLOUD_1_PART_2, Y_LOCATION_CLOUD_1_PART_2))

        # IMG CLOUD_2
        screen.blit(img_cloud_2, (X_LOCATION_CLOUD_2_PART_1, Y_LOCATION_CLOUD_2_PART_1))
        screen.blit(img_cloud_2, (X_LOCATION_CLOUD_2_PART_2, Y_LOCATION_CLOUD_2_PART_2))

        # # IMG PLATFORM
        # screen.blit(img_platform, (X_LOCATION_3 + 100, Y_LOCATION_3 + 400))

        # IMG FLOWER 1
        screen.blit(img_plower_1, (40, 460))
        screen.blit(img_plower_1, (450, 460))

        # IMG FLOWER 2
        screen.blit(img_plower_2, (200, 460))
        screen.blit(img_plower_2, (600, 460))

        pygame.display.update()
    pygame.quit()
    quit()


def enter_game():
    pygame.init()
    pygame.display.set_caption("mario_bro")

    # background img (mario photo)
    img_path_1 = "photo/mario_photo.jpg"
    img_1 = pygame.image.load(img_path_1)
    img_1 = pygame.transform.scale(img_1, (WIDTH_1, HEIGHT_1))
    screen.blit(img_1, (X_LOCATION_1, Y_LOCATION_1))

    # play button photo
    img_path_2 = "photo/play_button.jpg"
    img_2 = pygame.image.load(img_path_2)
    img_2 = pygame.transform.scale(img_2, (WIDTH_2, HEIGHT_2))
    screen.blit(img_2, (X_LOCATION_2, Y_LOCATION_2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(click_mouse_button, event.pos):
                    MAIN()

        screen.blit(img_1, (X_LOCATION_1, Y_LOCATION_1))
        screen.blit(img_2, (X_LOCATION_2, Y_LOCATION_2))
        pygame.display.update()
    pygame.quit()
    quit()


enter_game()
MAIN()
