import pygame

# the main screen
WIDTH_OF_SCREEN = 1290
HEIGHT_OF_SCREEN = 670
screen = pygame.display.set_mode((WIDTH_OF_SCREEN, HEIGHT_OF_SCREEN))

# the location of the screen
# PHOTO OF MARIO

X_LOCATION1 = 0
Y_LOCATION1 = 0
WIDTH1 = 1290
HEIGHT1 = 670

# PHOTO OF PLAY BUTTON
X_LOCATION2 = 520
Y_LOCATION2 = 335
WIDTH2 = 200
HEIGHT2 = 100




def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True
