import sys
import numpy as np
from sense_hat import SenseHat

#beginning screen

def beginning_screen():
    sense.set_rotation(180)
    sense.show_message("CONNECT", text_colour=(0, 0, 255))
    sense.show_message("4", text_colour=(255, 0, 0), scroll_speed=0.05)
    sense.show_message("PRESS2PLAY", text_colour=(255, 0, 0))

#creates matrix full of zeros
def create_board():
    board = np.zeros((6,7))
    return board

sense = SenseHat()
board = create_board()

#while True:
 #   beginning_screen();
sense.clear()

#this is a test change

