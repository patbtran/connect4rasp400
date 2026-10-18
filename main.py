import sys
import numpy as np
from sense_hat import SenseHat

#global variables
ROW_COUNT = 6
COLUMN_COUNT = 8
RED = (255, 0, 0,)
BLUE = (0, 0, 255)
EMPTY = (0, 0, 0)

#creates matrix full of zeros
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


#shows before players enter game
def beginning_screen():
    sense.set_rotation(180)
    sense.show_message("CONNECT", text_colour=(0, 0, 255))
    sense.show_message("4", text_colour=(255, 0, 0), scroll_speed=0.05)
    sense.show_message("PRESS2PLAY", text_colour=(255, 0, 0))

#places players piece on board
def drop_piece(board, row, col, piece):
    board[row][col]= piece
    
def drop_check(board, col):
    #if true, allows piece to be dropped here
    #if not true, the spot, col is not vacant
    return board[ROW_COUNT - 1][col]==0 #look at the bottom cell of column col
#-1 incase i decide to resize the board again


#when player picks column, need to find lowest empty spot in that column
#returns that spot
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0: #is this spot empty?
            return r #yes? return that spot

sense = SenseHat()
sense.set_rotation(180)
board = create_board()

            
def winner(board, piece):
    #to help imagine how these checks work, think of x&y coordinate, r being x and c being y
    #checks horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
            
    #checks vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
            
    #checks positvely sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
            
    #check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

#takes the current connect4 board and displas it on the LED matrix
def update_board(board):
    pixels = []
    
    #these top two rows are for the piece indicator and spacing
    for r in range(2):
        for c in range(COLUMN_COUNT):
            pixels.append(EMPTY)
            
                    #range(start, stop, increment/decrement)
    for r in range(ROW_COUNT -1, -1, -1):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 0:
                pixels.append(EMPTY)
            elif board[r][c] == 1:
                pixels.append(RED)
            elif board[r][c] == 2:
                pixels.append(BLUE)

    sense.set_pixels(pixels) #this sends the list of 64 colors to LED matrix, updating all at once
    
    #takes 3 arguments: (current matrix, the col the player is currently selecting, current players piece
    # players piece: 1 for red, else for blue
def show_selection(board, selected_col, piece):
    update_board(board)
        
    if piece == 1:
        color = RED
    else:
        color = BLUE
            
    sense.set_pixel(selected_col, 0, color)
        

#joystick movement
def move_selection(board, piece):
    selected_col = 3 #indicator light's starting position
    
    show_selection(board, selected_col, piece)
    
    while True: #loop that continuously checks for joystick movement
        for event in sense.stick.get_events(): #retrieves joystick movements
            if event.action == "pressed":
                
                if event.direction == "left":
                    selected_col = max(0, selected_col - 1)
                    
                elif event.direction == "right":
                    selected_col = min(COLUMN_COUNT - 1, selected_col + 1)
                    
                show_selection(board,selected_col, piece)
                
move_selection(board, 1)