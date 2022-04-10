import pygame

# the main screen
WIDTH_OF_SCREEN = 1290
HEIGHT_OF_SCREEN = 670
screen = pygame.display.set_mode((WIDTH_OF_SCREEN, HEIGHT_OF_SCREEN))

# the location of the screen
# PHOTO OF MARIO

X_LOCATION_1 = 0
Y_LOCATION_1 = 0
WIDTH_1 = 1290
HEIGHT_1 = 670

# PHOTO OF PLAY BUTTON
X_LOCATION_2 = 520
Y_LOCATION_2 = 335
WIDTH_2 = 200
HEIGHT_2 = 100

# PHOTO OF GROUND
X_LOCATION_3 = 600 - 180
Y_LOCATION_3 = 500
WIDTH_3 = 250
HEIGHT_3 = 165

# IMG CLOUD_1 PART 1
X_LOCATION_CLOUD_1_PART_1 = 150
Y_LOCATION_CLOUD_1_PART_1 = 120

# IMG CLOUD_1 PART 2
X_LOCATION_CLOUD_1_PART_2 = 700
Y_LOCATION_CLOUD_1_PART_2 = 120

# IMG CLOUD_2 PART 1
X_LOCATION_CLOUD_2_PART_1 = 400
Y_LOCATION_CLOUD_2_PART_1 = 210

# IMG CLOUD_2 PART 2
X_LOCATION_CLOUD_2_PART_2 = 1000
Y_LOCATION_CLOUD_2_PART_2 = 210


def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True
