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
        self.image = pygame.transform.scale(self.pic, (height, width))

    def display_image(self):
        screen.blit(self.image, (self.x, self.y))

    def move_cloud_left(self):
        # cloud back to start
        if self.x <= -100:
            self.x = 1300
        self.x -= 0.8