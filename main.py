from interface import *
from random import randint
from bot import *


class Main:
    def __init__(self):
        self.board = Board([
        [8, 4, 6, 10, 12, 6, 4, 8],
        [2, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [7, 3, 5, 9, 11, 5, 3, 7]
    ])
        self.board.get_pieces_from_board()
        self.bot = Bot(self.board, turn=1)
        self.interface = Interface("test interface", self.board, self.bot)
        self.bot.is_thinking = True
        self.bot.expand_decision_tree(self.bot.tree, 0)



if __name__ == "__main__":
    mn = Main()
    mn.interface.loop()
    pg.quit()