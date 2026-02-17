from interface import *
from board import *
from random import randint

if __name__ == "__main__":
    brd = Board([
        [8, 4, 6, 10, 12, 6, 4, 8],
        [2, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [7, 3, 5, 9, 11, 5, 3, 7]
    ], 0, -1)
    brd.get_pieces_from_board()

    def test_func(inter):
        if inter.timer == 0:
            moves = brd.get_white_moves(inter.board.mini_board)
            move = moves[randint(0, len(moves)-1)]
            print(move)
            inter.board.play_move(move, inter.board.mini_board)

    inter = Interface("test interface", brd, test_func)

    inter.loop()

    pg.quit()