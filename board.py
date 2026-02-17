import moves.pawn_moves as pwn
import moves.knight_moves as knt
import moves.bishop_moves as bsp
import moves.rook_moves as rok

class Board:
    def __init__(self, mini_board, turn, en_passant, white_castle, black_castle):
        self.mini_board = mini_board
        self.turn = turn
        self.en_passant = en_passant
        self.white_castle = white_castle
        self.black_castle = black_castle
        self.white_pieces = []
        self.black_pieces = []

    
    def get_pieces_from_board(self):
        for i in range(8):
            for j in range(8):
                if self.mini_board[i][j] != 0:
                    if self.mini_board[i][j] % 2 == 1:
                        self.white_pieces.append((i, j, self.mini_board[i][j]))
                    else:
                        self.black_pieces.append((i, j, self.mini_board[i][j]))
    

    def play_move(move):
        pass


    def get_white_moves(self):
        pass