import pygame as pg
from settings import *
from threading import Thread

class Interface:
    def __init__(self, title, board, bot, test_func=None):
        pg.init()

        self.screen = pg.display.set_mode([SIDE+UI_MARGIN_WIDTH, SIDE])
        pg.display.set_caption(title)
        self.closed = False
        self.clock = pg.time.Clock()
        self.board = board
        self.bot = bot
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
        self.player_move = ()
        self.last_move = None
    

    def read_user_input(self):
        x, y = pg.mouse.get_pos()
        if len(self.player_move) < 4 and 0 < x < SQUARES_SIZE * 8 and HEIGHT_OFFEST < y < SIDE - HEIGHT_OFFEST:
            i, j = y // SQUARES_SIZE - 1, int((x - HEIGHT_OFFEST) // SQUARES_SIZE) + 1
            self.player_move += (i, j)
    

    def check_player_move(self):
        if len(self.player_move) == 4:
            for move in self.board.get_moves():
                if move[:4] == self.player_move:
                    self.player_move = move
                    return True
            self.player_move = ()
        return False

    
    def loop(self):
        while not self.closed:
            self.clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.closed = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.read_user_input()

            if self.board.turn != self.bot.turn and self.last_move is None:
                if self.check_player_move():
                    self.board.play_move(self.player_move, self.board.turn)
                    self.last_move = self.player_move
                    self.player_move = ()
                    self.board.turn = 1 - self.board.turn
            elif self.board.turn == self.bot.turn and self.last_move is None and not self.bot.is_thinking:
                self.board.play_move(self.bot.tree.move, self.board.turn)
                self.last_move = self.bot.tree.move
                self.board.turn = 1 - self.board.turn
            if not self.bot.is_thinking:
                self.bot.update_tree(self.last_move)
                self.last_move = None
                self.bot.is_thinking = True
                t = Thread(target=self.bot.expand_decision_tree, args=(self.bot.tree, 0,))
                t.start()
            



            # move = None
            # if self.board.turn != self.bot.turn and self.last_move is None:
            #     if self.check_player_move():
            #         move = self.player_move
            # elif self.board.turn == self.bot.turn and not self.bot.is_thinking:
            #     move = self.bot.tree.move
            # if move is not None:
            #     self.board.play_move(move, self.board.turn)
            #     self.last_move = move
            # if not self.bot.is_thinking:
            #     self.bot.update_tree(self.last_move)
            #     self.board.turn = 1 - self.board.turn
            #     self.last_move = None
            #     self.bot.is_thinking = True
            #     t = Thread(target=self.bot.expand_decision_tree, args=(self.bot.tree, 0,))
            #     t.start()

            self.screen.fill("#000000")
            self.draw_board(self.board.mini_board)
            #print(self.clock.get_fps())

            pg.display.flip()
    

    def draw_board(self, board):
        for i in range(8):
            for j in range(8):
                pg.draw.rect(self.screen, ["white", "#303030"][(i+j)%2], (j*SQUARES_SIZE, HEIGHT_OFFEST+i*SQUARES_SIZE, SQUARES_SIZE, SQUARES_SIZE))
                if self.bot.turn == 0:
                    reversed_board_index = 7-i
                else:
                    reversed_board_index = i
                if board[reversed_board_index][j] > 0:
                    self.screen.blit(self.sprites[board[i][j]], (j*SQUARES_SIZE + PIECES_OFFSET, HEIGHT_OFFEST+i*SQUARES_SIZE + PIECES_OFFSET, SQUARES_SIZE + PIECES_OFFSET, SQUARES_SIZE + PIECES_OFFSET))