import pygame

from helpers import screen


class Object:
    def __init__(self, x, y, height, width, pic):
        # Constructor
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.pic = pic
        self.pic = pygame.image.load(self.pic)
        self.image = pygame.transform.scale(pic, (height, width) )

    # Method
    def display_image(self):
        screen.blit(self.image, (self.height, self.width))

