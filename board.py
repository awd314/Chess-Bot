import moves.pawn_moves as pwn
import moves.knight_moves as knt
import moves.bishop_moves as bsp
import moves.rook_moves as rok
import moves.queen_moves as qun
import moves.king_moves as kng

class Board:
    def __init__(self, mini_board, turn, en_passant, white_pieces=[], black_pieces=[]):
        self.mini_board = mini_board
        self.turn = turn
        self.en_passant = en_passant
        self.white_pieces = white_pieces
        self.black_pieces = black_pieces

    
    def get_pieces_from_board(self):
        for i in range(8):
            for j in range(8):
                if self.mini_board[i][j] != 0:
                    if self.mini_board[i][j] % 2 == 1:
                        self.white_pieces.append((i, j, self.mini_board[i][j]))
                    else:
                        self.black_pieces.append((i, j, self.mini_board[i][j]))
    

    def update_pieces(self, move, pieces):
        pass
    

    def play_move(self, move, board, pieces):
        pass


    def is_white_checked(self, pos, board):
        i, j = pos
        checked = False

        # black checks white
        for piece in self.black_pieces:
            if piece[2] == 2:
                if piece[0] == i-1 and abs(piece[1]-j) == 1:
                    checked = True
            elif piece[2] == 4:
                if (i, j) in [move[2:4] for move in knt.get_black_knight_moves(piece[:2], board)]:
                    checked = True
            elif piece[2] == 6 and (i + j) % 2 == (piece[0] + piece[1]) % 2:
                if (i, j) in [move[2:4] for move in bsp.get_black_bishop_moves(piece[:2], board)]:
                    checked = True
            elif piece[2] == 8 and (i == piece[0] or j == piece[1]):
                if (i, j) in [move[2:4] for move in rok.get_black_rook_moves(piece[:2], board)]:
                    checked = True
            elif piece[2] == 10 and ((i + j) % 2 == (piece[0] + piece[1]) % 2 or (i == piece[0] or j == piece[1])):
                if (i, j) in [move[2:4] for move in qun.get_black_queen_moves(piece[:2], board)]:
                    checked = True
            elif piece[2] == 11 and abs(i - piece[0]) < 2 and abs(j - piece[1]) < 2:
                checked = True
            if checked:
                break
        
        return checked


    def is_black_checked(self, pos, board):
        i, j = pos
        checked = False

        # white checks black
        for piece in self.white_pieces:
            if piece[2] == 1:
                if piece[0] == i+1 and abs(piece[1]-j) == 1:
                    checked = True
            elif piece[2] == 3:
                if (i, j) in [move[2:4] for move in knt.get_white_knight_moves(piece[:2], board)]:
                    checked = True
            elif piece[2] == 5 and (i + j) % 2 == (piece[0] + piece[1]) % 2:
                if (i, j) in [move[2:4] for move in bsp.get_white_bishop_moves(piece[:2], board)]:
                    checked = True
            elif piece[2] == 7 and (i == piece[0] or j == piece[1]):
                if (i, j) in [move[2:4] for move in rok.get_white_rook_moves(piece[:2], board)]:
                    checked = True
            elif piece[2] == 9 and ((i + j) % 2 == (piece[0] + piece[1]) % 2 or (i == piece[0] or j == piece[1])):
                if (i, j) in [move[2:4] for move in qun.get_white_queen_moves(piece[:2], board)]:
                    checked = True
            elif piece[2] == 11 and abs(i - piece[0]) < 2 and abs(j - piece[1]) < 2:
                checked = True
            if checked:
                break
        
        return checked

    
    def get_white_moves(self, board):
        moves = []
        king_pos = None

        for piece in self.white_pieces:
            if piece[2] == 1:
                moves += pwn.get_white_pawn_moves(piece[:2], board, self.en_passant)
            elif piece[2] == 3:
                moves += knt.get_white_knight_moves(piece[:2], board)
            elif piece[2] == 5:
                moves += bsp.get_white_bishop_moves(piece[:2], board)
            elif piece[2] == 7:
                moves += rok.get_white_rook_moves(piece[:2], board)
            elif piece[2] == 9:
                moves += qun.get_white_queen_moves(piece[:2], board)
            elif piece[2] == 11:
                moves += kng.get_white_king_moves(piece[:2], board)
                king_pos = piece[:2]
        
        board_copy = [[self.mini_board[i][j] for j in range(8)] for i in range(8)]
        index = 0
        while index < len(moves):
            move = moves[index]
            if move[-1] == 12:
                valid = True
                if move[3] == 6:
                    for i in range(3):
                        if self.is_white_checked((move[0], move[1]+i), board):
                            valid = False
                else:
                    for i in range(4):
                        if self.is_white_checked((move[0], move[1]-i), board):
                            valid = False
                if not valid:
                    moves.pop(index)
                else:
                    index += 1
            else:
                temp_start = board_copy[move[0]][move[1]]
                temp_end = board_copy[move[2]][move[3]]
                board_copy[move[2]][move[3]] = temp_start
                board_copy[move[0]][move[1]] = 0
                if self.is_white_checked(king_pos, board_copy):
                    moves.pop(index)
                else:
                    index += 1
                board_copy[move[2]][move[3]] = temp_end
                board_copy[move[0]][move[1]] = temp_start

        return moves


    def get_black_moves(self, board):
        pass