import pygame
from turtledemo import clock


def MAIN():
    pygame.init()
    pygame.display.set_caption("mario_bro")

    # background img (mario photo)
    x_location = 0
    y_location = 0
    width = 800
    height = 700
    screen = pygame.display.set_mode((800, 700))
    img_path_1 = "photos/mario_photo.jpg"
    img_1 = pygame.image.load(img_path_1)
    img_1 = pygame.transform.scale(img_1, (width, height))
    screen.blit(img_1, (x_location, y_location))

    # play button photo
    x_location = 400
    y_location = 350
    width = 200
    height = 80
    img_path_2 = "photos/play_button.jpg"
    img_2 = pygame.image.load(img_path_2)
    img_2 = pygame.transform.scale(img_2, (width, height))
    screen.blit(img_2, (x_location, y_location))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(img_1, (0, 0))
        screen.blit(img_2, (400, 350))
        pygame.display.update()
    pygame.quit()
    quit()


MAIN()
