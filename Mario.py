from typing import List
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
        if self.gravity != 0:
            return

        self.y = self.y - 5
        if not self.jumping:
            self.gravity = -5
            self.jumping = True

    def is_on_ground(self, ground: Object):
        return (ground.x <= self.x <= ground.x + ground.width or ground.x <= self.x + self.width <= ground.x + ground.width) and ground.y <= self.y + self.height <= ground.y + ground.height

    def update_grounded_state(self, ground_list : List[Object]):
        for ground in ground_list:
            if self.is_on_ground(ground):
                self.gravity = 0
                return

        if not self.jumping:
            self.gravity = 2

    def mario_move_right_false(self):
        self.moving_right = False

    def mario_move_left_false(self):
        self.moving_left = False

    def display_image(self, pipe_list: List[Object], platform_1_1):
        if self.moving_left:
            if self.x >= 0:
                self.x -= 1

        if self.moving_right:
            self.x += 1

        if self.jumping:
            if self.y + self.height >= Y_LOCATION_3:
                self.jumping = False
                self.gravity = 1
                self.y = Y_LOCATION_3 - self.height

            for pipe in pipe_list:
                if pipe.x <= self.x <= pipe.x + pipe.width:
                    if self.y + self.height >= pipe.y:
                        self.jumping = False
                        self.gravity = 1
                        self.y = pipe.y - self.height

                if platform_1_1.x <= self.x <= platform_1_1.x + platform_1_1.width or platform_1_1.x <= self.x + self.width <= platform_1_1.x + platform_1_1.width:
                    if self.y + self.height >= platform_1_1.y:
                        self.jumping = False
                        self.gravity = 1
                        self.y = platform_1_1.y - self.height

        if self.gravity != 0:
            self.gravity = self.gravity + 0.1
            self.y += self.gravity
        screen.blit(self.image, (self.x, self.y))


