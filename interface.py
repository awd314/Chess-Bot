import pygame as pg
from settings import *
from threading import Thread
from random import randint

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
        pg.display.set_icon(self.sprites[randint(1, 12)])
        self.test_func = test_func
        self.player_move = ()
        self.last_move = None
        self.promotion_selection = 0
        self.available_moves = None
    

    def read_user_input(self):
        x, y = pg.mouse.get_pos()
        if len(self.player_move) < 4 and 0 < x < SQUARES_SIZE * 8 and HEIGHT_OFFEST < y < SIDE - HEIGHT_OFFEST:
            i, j = y // SQUARES_SIZE - 1, int((x - HEIGHT_OFFEST) // SQUARES_SIZE) + 1
            if self.bot.turn == 0:
                i = 7 - i
                j = 7 - j
            self.player_move += (i, j)
        elif SQUARES_SIZE * 8 + SIDE // 10 < x < SQUARES_SIZE * 8 + SIDE // 10 + SQUARES_SIZE and SIDE//2 - SQUARES_SIZE * 2 < y < SIDE//2 + SQUARES_SIZE * 2:
            self.promotion_selection = (y - SIDE//2 + 2 * SQUARES_SIZE) // SQUARES_SIZE + 8
    

    def check_player_move(self):
        if len(self.player_move) == 4:
            for move in self.board.get_moves():
                if move[:4] == self.player_move:
                    if self.board.mini_board[move[0]][move[1]] < 3 and move[2] % 7 == 0:
                        if self.promotion_selection != 0:
                            self.player_move = move[:4] + (self.promotion_selection,)
                        else:
                            self.player_move = ()
                            return False
                    else:
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
                    self.available_moves = None
            elif self.board.turn == self.bot.turn and self.last_move is None and not self.bot.is_thinking:
                self.board.play_move(self.bot.tree.move, self.board.turn)
                self.last_move = self.bot.tree.move
                self.board.turn = 1 - self.board.turn
                self.promotion_selection = 0
            if not self.bot.is_thinking:
                self.bot.update_tree(self.last_move)
                self.last_move = None
                self.bot.is_thinking = True
                t = Thread(target=self.bot.expand_decision_tree, args=(self.bot.tree, 0,))
                t.start()

            self.screen.fill("#000000")
            self.draw_board(self.board.mini_board)
            self.draw_preview_move()
            #print(self.clock.get_fps())

            pg.display.flip()
    

    def draw_preview_move(self):
        if len(self.player_move) == 2:
            if self.available_moves is None:
                self.available_moves = self.board.get_moves()
            for move in self.available_moves:
                if move[:2] == self.player_move and move[3] < 8:
                    i, j = move[2], move[3]
                    if self.bot.turn == 0:
                        i = 7 - i
                        j = 7 - j
                    pg.draw.circle(self.screen, "#707070", (j * SQUARES_SIZE + SQUARES_SIZE // 2, HEIGHT_OFFEST + SQUARES_SIZE * i + SQUARES_SIZE // 2), SQUARES_SIZE // 10)
    

    def draw_board(self, board):
        for i in range(8):
            for j in range(8):
                x, y = j, i
                if self.bot.turn == 0:
                    x, y = 7-j, 7-i
                color = ["#FFFFFF", "#202020"][(i+j)%2]
                if (y, x) == self.player_move:
                    color = "#707070"
                pg.draw.rect(self.screen, color, (j*SQUARES_SIZE, HEIGHT_OFFEST+i*SQUARES_SIZE, SQUARES_SIZE, SQUARES_SIZE))
                if board[y][x] > 0:
                    self.screen.blit(self.sprites[board[y][x]], (j*SQUARES_SIZE + PIECES_OFFSET, HEIGHT_OFFEST+i*SQUARES_SIZE + PIECES_OFFSET, SQUARES_SIZE + PIECES_OFFSET, SQUARES_SIZE + PIECES_OFFSET))
        for i in range(4):
            x = 8 * SQUARES_SIZE + SIDE // 10
            y = SIDE // 2 - SQUARES_SIZE * 2
            color = "#202020"
            if self.promotion_selection == i + 8:
                color = "#707070"
            pg.draw.rect(self.screen, color, (x, y + SQUARES_SIZE * i, SQUARES_SIZE, SQUARES_SIZE))
            sprite_index = (i+1)*2+1+(1-self.bot.turn)
            self.screen.blit(self.sprites[sprite_index], (x+PIECES_OFFSET, y+i*SQUARES_SIZE+PIECES_OFFSET, SQUARES_SIZE+PIECES_OFFSET, SQUARES_SIZE+PIECES_OFFSET))
        pg.draw.circle(self.screen, ["#FFFFFF", "#202020"][self.board.turn], (SQUARES_SIZE * 8.5 + SIDE//10, HEIGHT_OFFEST + SIDE//10), SIDE//50)