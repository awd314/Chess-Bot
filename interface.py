import pygame as pg
from settings import *

class Interface:
    def __init__(self, title, board, test_func):
        pg.init()

        self.screen = pg.display.set_mode([SIDE+UI_MARGIN_WIDTH, SIDE])
        pg.display.set_caption(title)
        self.closed = False
        self.clock = pg.time.Clock()
        self.board = board
        self.sprites = {
            1 : pg.transform.scale(pg.image.load("./images/wpawn.png"), (PIECES_SIZE, PIECES_SIZE)),
            2 : pg.transform.scale(pg.image.load("./images/bpawn.png"), (PIECES_SIZE, PIECES_SIZE)),
            3 : pg.transform.scale(pg.image.load("./images/wknight.png"), (PIECES_SIZE, PIECES_SIZE)),
            4 : pg.transform.scale(pg.image.load("./images/bknight.png"), (PIECES_SIZE, PIECES_SIZE)),
            5 : pg.transform.scale(pg.image.load("./images/wbishop.png"), (PIECES_SIZE, PIECES_SIZE)),
            6 : pg.transform.scale(pg.image.load("./images/bbishop.png"), (PIECES_SIZE, PIECES_SIZE)),
            7 : pg.transform.scale(pg.image.load("./images/wrook.png"), (PIECES_SIZE, PIECES_SIZE)),
            8 : pg.transform.scale(pg.image.load("./images/brook.png"), (PIECES_SIZE, PIECES_SIZE)),
            9 : pg.transform.scale(pg.image.load("./images/wqueen.png"), (PIECES_SIZE, PIECES_SIZE)),
            10 : pg.transform.scale(pg.image.load("./images/bqueen.png"), (PIECES_SIZE, PIECES_SIZE)),
            11 : pg.transform.scale(pg.image.load("./images/wking.png"), (PIECES_SIZE, PIECES_SIZE)),
            12 : pg.transform.scale(pg.image.load("./images/bking.png"), (PIECES_SIZE, PIECES_SIZE))
        }
        self.test_func = test_func
        self.timer = 0

    
    def loop(self):
        while not self.closed:
            self.clock.tick(FPS)
            self.timer += 1
            self.timer %= 300

            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.closed = True
            
            self.screen.fill("#000000")
            self.test_func(self)
            self.draw_board(self.board.mini_board)

            pg.display.flip()
    

    def draw_board(self, board):
        for i in range(8):
            for j in range(8):
                pg.draw.rect(self.screen, ["white", "#303030"][(i+j)%2], (j*SQUARES_SIZE, HEIGHT_OFFEST+i*SQUARES_SIZE, SQUARES_SIZE, SQUARES_SIZE))
                if board[i][j] > 0:
                    self.screen.blit(self.sprites[board[i][j]], (j*SQUARES_SIZE + PIECES_OFFSET, HEIGHT_OFFEST+i*SQUARES_SIZE + PIECES_OFFSET, SQUARES_SIZE + PIECES_OFFSET, SQUARES_SIZE + PIECES_OFFSET))