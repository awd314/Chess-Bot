import moves.pawn_moves as pwn
import moves.knight_moves as kng

class Board:
    def __init__(self, mini_board, turn, en_passant, white_castle, black_castle):
        self.mini_board = mini_board
        self.turn = turn
        self.en_passant = en_passant
        self.white_castle = white_castle
        self.black_castle = black_castle
    

    def get_white_moves(self):
        pass