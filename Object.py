import pygame


class object:
# Constructor
def __init__(self, x, y, height, width, pic):

    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.pic = pic
    self.pic = pygame.image.load(self.pic)
    self.image = pygame.transform.scale(pic, (height, width) )
# Method
def display_image(self):
    screen.blit(self.image, (height, width))

