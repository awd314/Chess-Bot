import pygame as pg
from settings import *
from pieces import piecesDictionary

class Interface:
    """
    Opens a window to display the game.
    """
    def __init__(self):
        pg.init()
        pg.display.set_caption("Chess Bot")
        icon = pg.image.load("./images/bqueen.png")
        pg.display.set_icon(icon)
        
        self.screen = pg.display.set_mode([SIDE+MARGIN, SIDE])
        self.clock = pg.time.Clock()
        self.running = True
    

    def CheckEvents(self):
        """
        Listens key events to call the appropriate functions. All keybinds
        are about interacting with the board or the window.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False # Closes the window if the 'X' button or the 'esc' key are pressed
    

    def TestFunction(self, moves):
        """
        Displays a given set of moves for a piece on the board.
        """
        if moves is not None and len(moves) > 0:
            i, j = moves[0][0], moves[0][1]
            rectPos = (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pg.draw.rect(self.screen, "#A56161", rectPos)

            for move in moves:
                i, j = move[2], move[3]
                rectPos = (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pg.draw.rect(self.screen, "#AA0000", rectPos)
    

    def DrawBoard(self, board, flipped=-False):
        """
        Loops through a given board and draws the according piece for each square. The 
        'flipped' parameter draws the board from black's perspective.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                # Loops through the board
                rectPos = (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) # Destination surface of the piece to draw
                pg.draw.rect(self.screen, ["#AAAAAA", "#303030"][(i+j)%2], rectPos) # Draws square (black or white)
                if not flipped:
                    if board[i][j] != -1:
                        self.screen.blit(piecesDictionary[board[i][j]], rectPos) # Regular display
                elif board[SIZE-1-i][SIZE-1-j] != -1:
                    self.screen.blit(piecesDictionary[board[SIZE-1-i][SIZE-1-j]], rectPos) # Flipped display, from black's perspective