from Object import Object
from helpers import screen, WIDTH_OF_SCREEN, Y_LOCATION_3


class Mario(Object):
    def __init__(self, x, y, height, width, pic):
        Object.__init__(self, x, y, height, width, pic)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.jumping = False
        self.gravity = 1

    def mario_move_left(self):
        if self.x >= 0:
            self.moving_left = True

    def mario_move_right(self):
        if self.x <= WIDTH_OF_SCREEN:
            self.moving_right = True

    def start_jump(self):
        self.y = self.y - 5
        if not self.jumping:
            self.gravity = -5
            self.jumping = True

    def mario_move_right_false(self):
        self.moving_right = False

    def mario_move_left_false(self):
        self.moving_left = False

    def display_image(self):
        if self.moving_left:
            if self.x >= 0:
                self.x -= 1

        if self.moving_right:
            self.x += 1

        if self.jumping:
            if self.y - 40 >= Y_LOCATION_3:
                self.jumping = False
                self.y = Y_LOCATION_3 - 40
                self.gravity = 1
            else:
                self.gravity = self.gravity + 0.1
                self.y += self.gravity

        screen.blit(self.image, (self.x, self.y))
