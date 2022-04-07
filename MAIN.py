import pygame

from Mario import Mario
from Object import Object
from click_button import click_mouse_button
from helpers import screen, X_LOCATION_1, Y_LOCATION_1, WIDTH_1, HEIGHT_1, \
    X_LOCATION_2, Y_LOCATION_2, WIDTH_2, HEIGHT_2, mouse_in_button, HEIGHT_3, WIDTH_3, Y_LOCATION_3, X_LOCATION_3


def MAIN():
    from helpers import X_LOCATION_CLOUD_1_PART_1, Y_LOCATION_CLOUD_1_PART_1, X_LOCATION_CLOUD_1_PART_2, \
        Y_LOCATION_CLOUD_1_PART_2, X_LOCATION_CLOUD_2_PART_1, Y_LOCATION_CLOUD_2_PART_1, X_LOCATION_CLOUD_2_PART_2, \
        Y_LOCATION_CLOUD_2_PART_2
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("mario bro")

    # IMG BACKGROUND
    background = Object(X_LOCATION_1, Y_LOCATION_1, WIDTH_1, HEIGHT_1, "photo/background-2.png")

    # IMG GROUND
    ground_1 = Object(X_LOCATION_3, Y_LOCATION_3,WIDTH_3, HEIGHT_3, "photo/wall-1.png")
    ground_2 = Object(0, 500, WIDTH_3, HEIGHT_3, "photo/wall-1.png")

    # IMG PLATFORM
    platform_1_1 = Object(X_LOCATION_3 - 145, 420, 120, 20, "photo/moving-platformlong.png")

    # IMG CLOUD_1
    cloud_1_1 = Object(X_LOCATION_CLOUD_1_PART_1, Y_LOCATION_CLOUD_1_PART_1, 120, 50, "photo/cloud.png")
    cloud_1_2 = Object(X_LOCATION_CLOUD_1_PART_2, Y_LOCATION_CLOUD_1_PART_2, 120, 50, "photo/cloud.png")

    # IMG CLOUD_2
    cloud_2_1 = Object(X_LOCATION_CLOUD_2_PART_1, Y_LOCATION_CLOUD_2_PART_1, 150, 70, "photo/dobbelclouds.png")
    cloud_2_2 = Object(X_LOCATION_CLOUD_2_PART_2, Y_LOCATION_CLOUD_2_PART_2, 150, 70, "photo/dobbelclouds.png")
    cloud_2_3 = Object(1300, Y_LOCATION_CLOUD_2_PART_1 - 50, 150, 70, "photo/dobbelclouds.png")

    cloud_list = [cloud_1_1, cloud_1_2, cloud_2_1, cloud_2_2, cloud_2_3]

    # IMG FLOWER 1
    flower_1_1 = Object(40, 460, 20, 40, "photo/flower0.png")
    flower_1_2 = Object(450, 460, 20, 40, "photo/flower0.png")

    # IMG FLOWER 2
    flower_2_1 = Object(200, 460, 20, 40, "photo/flower1.png")
    flower_2_2 = Object(600, 460, 20, 40, "photo/flower1.png")

    flower_list = [flower_1_1, flower_1_2, flower_2_1, flower_2_2]

    # IMG SQUIDGE 1
    squidge_1 = Object(535, 460, 30, 40, "photo/squidge1.png")

    # IMG PIPE
    pipe_1 = Object(665, 450, 50, 200, "photo/pipe-big.png")
    pipe_2 = Object(716, 400, 50, 250, "photo/pipe-big.png")
    pipe_3 = Object(767, 350, 50, 300, "photo/pipe-big.png")
    pipe_4 = Object(818, 300, 50, 350, "photo/pipe-big.png")

    pipe_list = [pipe_2, pipe_1, pipe_3, pipe_4]

    # MARIO IMG
    mario = Mario(10, Y_LOCATION_3 - 40, 30, 40, "photo/Mario/mario.png")

    running = True
    while running:

        # cloud moving
        for cloud in cloud_list:
            cloud.move_cloud_left()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # press on any key
            if event.type == pygame.KEYDOWN:
                # press on left key
                if event.key == pygame.K_LEFT:
                    mario.mario_move_left()
                # press on right key
                if event.key == pygame.K_RIGHT:
                    mario.mario_move_right()

                if event.key == pygame.K_UP:
                    mario.start_jump()

            # leave the press
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    mario.mario_move_left_false()
                if event.key == pygame.K_RIGHT:
                    mario.mario_move_right_false()

        # IMG BACKGROUND
        background.display_image()

        # IMG GROUND
        ground_1.display_image()
        ground_2.display_image()

        # IMG CLOUDS
        for clouds in cloud_list:
            clouds.display_image()

        # IMG PLATFORM
        platform_1_1.display_image()

        # IMG FLOWERS
        for flower in flower_list:
            flower.display_image()

        # IMG SQUIDGE 1
        squidge_1.display_image()

        # IMG PIPE
        for pipe in pipe_list:
            pipe.display_image()

        # MARIO IMG
        mario.display_image()

        pygame.display.update()
        clock.tick(100)
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
