import pygame
from helpers import screen


class Object:
    def __init__(self, x, y, height, width, pic):
        # Constructor
        self.Location = None
        self.x = x
        self.y = y
        self.height = width
        self.width = height
        self.pic = pic
        self.pic = pygame.image.load(self.pic)
        self.image = pygame.transform.scale(self.pic, (height, width))
        self.direction = True

    def display_image(self):
        screen.blit(self.image, (self.x, self.y))

    def move_cloud_left(self):
        # cloud back to start
        if self.x <= -100:
            self.x = 1300
        self.x -= 0.8

    def squidge1_moving(self):
        if self.x <= 450:
            self.direction = True

        if self.x >= 600:
            self.direction = False

        if self.direction:
            self.x += 0.6

        if not self.direction:
            self.x -= 0.6

    def accident(self, mario):
        if self.x <= mario.x <= self.x + self.width or self.x <= mario.x + mario.width <= self.x + self.width:
            if mario.y >= self.y <= mario.y + mario.height:
                return True
            else:
                return False
