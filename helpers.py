import pygame

# the main screen
screen = pygame.display.set_mode((800, 700))

# the location of the screen
# the 1 screen

X_LOCATION1 = 0
Y_LOCATION1 = 0
WIDTH1 = 800
HEIGHT1 = 680

# the button
X_LOCATION2 = 275
Y_LOCATION2 = 300
WIDTH2 = 200
HEIGHT2 = 100

def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True

