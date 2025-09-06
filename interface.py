import pygame as pg
from settings import SIDE, SQUARE_SIZE
from pieces import piecesDictionary

class Interface:
    """
    [docstring]
    """
    def __init__(self):
        pg.init()
        
        self.screen = pg.display.set_mode([SIDE, SIDE])
        self.clock = pg.time.Clock()
        self.running = True
    

    def CheckEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False
    

    def DrawBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                rectPos = (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pg.draw.rect(self.screen, ["#AAAAAA", "#303030"][(i+j)%2], rectPos)
                if board[i][j] != -1:
                    self.screen.blit(piecesDictionary[board[i][j]], rectPos)