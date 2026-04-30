import sys
import numpy as np
from sense_hat import SenseHat

#global variables
ROW_COUNT = 8
COLUMN_COUNT = 8

#creates matrix full of zeros
def create_board():
    board = np.zeros((8,8))
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
    return board[7][col]==0 #look at the bottom cell of column col


#when player picks column, need to find lowest empty spot in that column
#returns that spot
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0: #is this spot empty?
            return r #yes? return that spot

sense = SenseHat()
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


def draw_board(board):
    pixels = []
    
    for r in range(ROW_COUNT):
        if board[r][c] == 0:
                pixels.append(BLACK)
            elif board[r][c] == 1:
                pixels.append(RED)
            elif board[r][c] == 2:
                pixels.append(BLUE)

    sense.set_pixels(pixels)

        
    
        turn += 1
        turn = turn % 2
        
        