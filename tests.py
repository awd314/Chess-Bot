from interface import *
from board import *

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
        for move in kng.get_black_king_moves((0, 4), inter.board.mini_board):
            pg.draw.rect(inter.screen, "red", (move[3]*SQUARES_SIZE, move[2]*SQUARES_SIZE+HEIGHT_OFFEST, SQUARES_SIZE, SQUARES_SIZE))

    inter = Interface("test interface", brd, test_func)

    inter.loop()

    pg.quit()