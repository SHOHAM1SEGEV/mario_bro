import pygame


def main():
    pygame.init()
    pygame.display.set_caption("mario_bro")

    clock = pygame.time.Clock
    img_path = "images (1).jpg"
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (800, 1000))
    screen = pygame.display.set_mode((800, 1000))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(img, (0, 0))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


main()
