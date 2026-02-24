from interface import *
from random import randint
from bot import *
from threading import Thread

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
    ], 0)
    brd.get_pieces_from_board()
    b = Bot(brd.turn, Board([[brd.mini_board[i][j] for j in range(8)] for i in range(8)], brd.turn))
    b.is_thinking = True
    b.expand_decision_tree(b.tree, 0)
    last_move = None

    def test_func(inter):
        global last_move
        # try:
        #     if inter.board.turn:
        #         moves = inter.board.get_black_moves()
        #     else:
        #         moves = inter.board.get_white_moves()
        #     move = moves[randint(0, len(moves)-1)]
        #     inter.board.play_move(move)
        #     inter.board.turn = 1 - inter.board.turn
        # except:
        #     pass
        move = None
        if inter.board.turn and last_move is None:
            moves = inter.board.get_black_moves()
            move = moves[randint(0, len(moves)-1)]
        elif inter.board.turn == 0 and not b.is_thinking:
            move = b.tree.move
        if move is not None:
            inter.board.play_move(move, inter.board.turn)
            last_move = move
        if not b.is_thinking:
            b.update_tree(last_move)
            inter.board.turn = 1 - inter.board.turn
            last_move = None
            b.is_thinking = True
            t = Thread(target=b.expand_decision_tree, args=(b.tree, 0,))
            t.start()
        

    inter = Interface("test interface", brd, test_func)

    inter.loop()

    pg.quit()