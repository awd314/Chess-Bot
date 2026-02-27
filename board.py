import moves.pawn_moves as pwn
import moves.knight_moves as knt
import moves.bishop_moves as bsp
import moves.rook_moves as rok
import moves.queen_moves as qun
import moves.king_moves as kng
from settings import *
from collections import deque


class Board:
    def __init__(self, mini_board, turn=0):
        self.mini_board = mini_board # Nested arrays representing the board, is always 8x8 (hardcoded)
        self.turn = turn # 0 (white to play) or 1 (black to play)
        self.en_passant = -1 # A flag indicating in which row the last two-squares-move pawn move occured
        self.white_pieces = [] # Arrays of white pieces, used to lcate them instantly when calculating moves rather than looking through the whole board
        self.black_pieces = [] # Same with black pieces
        self.game_over_flag = -1 # Flag to indicate if the game is over and how
        self.castle = [False, False]
        self.last_moves = deque([(), (), (), (), (), ()])
        self.get_pieces_from_board()

    
    def get_pieces_from_board(self):
        # Resets arrays
        self.white_pieces = []
        self.black_pieces = []

        # Main loop
        for i in range(8):
            for j in range(8):
                if self.mini_board[i][j] != 0:
                    if self.mini_board[i][j] % 2 == 1: # White piece represented by an odd number
                        self.white_pieces.append((i, j, self.mini_board[i][j]))
                    else: # Black piece (isn't 0)
                        self.black_pieces.append((i, j, self.mini_board[i][j]))
    

    def verify_repetition(self):
        repetition = True
        index = 0
        while repetition and index < 4:
            if self.last_moves[index][:2] != self.last_moves[index+2][2:4] or self.last_moves[index][2:4] != self.last_moves[index+2][:2]:
                repetition = False
            index += 1
        if repetition:
            self.game_over_flag = 3
    

    def verify_endgame(self):
        moves = self.get_moves()
        if len(moves) == 0:
            if self.turn == 0:
                if self.is_black_checked(self.get_king_pos(1-self.turn), self.mini_board):
                    self.game_over_flag = 0
                else:
                    self.game_over_flag = 2
            else:
                if self.is_white_checked(self.get_king_pos(1-self.turn), self.mini_board):
                    self.game_over_flag = 1
                else:
                    self.game_over_flag = 2
        self.verify_repetition()
    

    def play_move(self, move, turn):
        # Moves the given piece to its new location
        piece_tag = self.mini_board[move[0]][move[1]]
        if piece_tag in (7, 8, 11, 12):
            if piece_tag % 2:
                self.castle[0] = True
            else:
                self.castle[1] = True
        self.mini_board[move[2]][move[3]] = self.mini_board[move[0]][move[1]]
        self.mini_board[move[0]][move[1]] = 0 # Removes piece from old location
        if move[-1] == 12: # Castling
            if move[3] == 6: # Short castling
                self.mini_board[move[0]][5] = self.mini_board[move[0]][7]
                self.mini_board[move[0]][7] = 0
            elif move[3] == 2: # Long castling
                self.mini_board[move[0]][3] = self.mini_board[move[0]][0]
                self.mini_board[move[0]][0] = 0
            self.mini_board[move[0]][move[1]] = 0
        elif move[-1] > 7: # Pawn promotion
            self.mini_board[move[2]][move[3]] = move[-1] - 2 - (11 - move[-1]) + turn
        else: # Updates flag for en passant
            self.en_passant = move[-1]
        self.get_pieces_from_board()
        self.last_moves.pop()
        self.last_moves.appendleft(move)
    

    def get_king_pos(self, piece_flag):
        if piece_flag:
            for piece in self.white_pieces:
                if piece[2] == 11:
                    return piece[:2]
        else:
            for piece in self.black_pieces:
                if piece[2] == 12:
                    return piece[:2]


    def is_white_checked(self, pos, board):
        i, j = pos # Gets position coordinates
        checked = False

        # black checks white
        for y in range(8):
            for x in range(8):
                value = board[y][x]
                if value != 0 and value % 2 == 0:
                    piece = (y, x, value)
                    if piece[2] == 2: # Pawn case
                        if piece[0] == i-1 and abs(piece[1]-j) == 1:
                            checked = True
                    elif piece[2] == 4: # Knight case
                        if (i, j) in [move[2:4] for move in knt.get_black_knight_moves(piece[:2], board)]:
                            checked = True
                    elif piece[2] == 6 and abs(piece[0] - i) == abs(piece[1] - j): # Bishop case only verifies for a bishop that's on the same diagonal
                        if (i, j) in [move[2:4] for move in bsp.get_black_bishop_moves(piece[:2], board)]:
                            checked = True
                    elif piece[2] == 8 and (i == piece[0] or j == piece[1]): # Rook case, verifies if the piece is on the same row or column
                        if (i, j) in [move[2:4] for move in rok.get_black_rook_moves(piece[:2], board)]:
                            checked = True
                    elif piece[2] == 10 and (abs(piece[0] - i) == abs(piece[1] - j) or (i == piece[0] or j == piece[1])): # Queen case, combination of bishop and rook
                        if (i, j) in [move[2:4] for move in qun.get_black_queen_moves(piece[:2], board)]:
                            checked = True
                    elif piece[2] == 12 and abs(i - piece[0]) < 2 and abs(j - piece[1]) < 2: # King case, verifies if the king is one space next to the piece
                        checked = True
                    if checked:
                        break
        
        return checked


    def is_black_checked(self, pos, board):
        i, j = pos
        checked = False

        # white checks black
        for y in range(8):
            for x in range(8):
                value = board[y][x]
                if value % 2 == 1:
                    piece = (y, x, value)
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
                    elif piece[2] == 9 and (abs(piece[0] - i) == abs(piece[1] - j) or (i == piece[0] or j == piece[1])):
                        if (i, j) in [move[2:4] for move in qun.get_white_queen_moves(piece[:2], board)]:
                            checked = True
                    elif piece[2] == 11 and abs(i - piece[0]) < 2 and abs(j - piece[1]) < 2:
                        checked = True
                    if checked:
                        break
        
        return checked
    

    def get_moves(self):
        if self.turn:
            return self.get_black_moves()
        return self.get_white_moves()

    
    def get_white_moves(self):
        moves = []
        king_pos = None

        for piece in self.white_pieces:
            if piece[2] == 1:
                moves += pwn.get_white_pawn_moves(piece[:2], self.mini_board, self.en_passant)
            elif piece[2] == 3:
                moves += knt.get_white_knight_moves(piece[:2], self.mini_board)
            elif piece[2] == 5:
                moves += bsp.get_white_bishop_moves(piece[:2], self.mini_board)
            elif piece[2] == 7:
                moves += rok.get_white_rook_moves(piece[:2], self.mini_board)
            elif piece[2] == 9:
                moves += qun.get_white_queen_moves(piece[:2], self.mini_board)
            elif piece[2] == 11:
                moves += kng.get_white_king_moves(piece[:2], self.mini_board)
                king_pos = piece[:2]
        
        board_copy = [[self.mini_board[i][j] for j in range(8)] for i in range(8)]
        index = 0
        while index < len(moves):
            move = moves[index]
            if move[-1] == 12:
                valid = True
                if move[3] == 6:
                    for i in range(3):
                        if self.is_white_checked((move[0], move[1]+i), self.mini_board):
                            valid = False
                else:
                    for i in range(4):
                        if self.is_white_checked((move[0], move[1]-i), self.mini_board):
                            valid = False
                if not valid or self.castle[0]:
                    moves.pop(index)
                else:
                    index += 1
            else:
                board_copy[move[2]][move[3]] = board_copy[move[0]][move[1]]
                board_copy[move[0]][move[1]] = 0
                if (move[0], move[1]) == king_pos:
                    temp_king_pos = (move[2], move[3])
                else:
                    temp_king_pos = king_pos
                if self.is_white_checked(temp_king_pos, board_copy):
                    moves.pop(index)
                else:
                    index += 1
                board_copy[move[2]][move[3]] = self.mini_board[move[2]][move[3]]
                board_copy[move[0]][move[1]] = self.mini_board[move[0]][move[1]]

        return moves


    def get_black_moves(self):
        moves = []
        king_pos = None

        for piece in self.black_pieces:
            if piece[2] == 2:
                moves += pwn.get_black_pawn_moves(piece[:2], self.mini_board, self.en_passant)
            elif piece[2] == 4:
                moves += knt.get_black_knight_moves(piece[:2], self.mini_board)
            elif piece[2] == 6:
                moves += bsp.get_black_bishop_moves(piece[:2], self.mini_board)
            elif piece[2] == 8:
                moves += rok.get_black_rook_moves(piece[:2], self.mini_board)
            elif piece[2] == 10:
                moves += qun.get_black_queen_moves(piece[:2], self.mini_board)
            elif piece[2] == 12:
                moves += kng.get_black_king_moves(piece[:2], self.mini_board)
                king_pos = piece[:2]
        
        board_copy = [[self.mini_board[i][j] for j in range(8)] for i in range(8)]
        index = 0
        while index < len(moves):
            move = moves[index]
            if move[-1] == 12:
                valid = True
                if move[3] == 6:
                    for i in range(3): # O-O
                        if self.is_black_checked((move[0], move[1]+i), board_copy):
                            valid = False
                else:
                    for i in range(4): # O-O-O
                        if self.is_black_checked((move[0], move[1]-i), board_copy):
                            valid = False
                if not valid or self.castle[1]:
                    moves.pop(index)
                else:
                    index += 1
            else:
                board_copy[move[2]][move[3]] = board_copy[move[0]][move[1]]
                board_copy[move[0]][move[1]] = 0
                if (move[0], move[1]) == king_pos:
                    temp_king_pos = (move[2], move[3])
                else:
                    temp_king_pos = king_pos
                if self.is_black_checked(temp_king_pos, board_copy):
                    moves.pop(index)
                else:
                    index += 1
                board_copy[move[2]][move[3]] = self.mini_board[move[2]][move[3]]
                board_copy[move[0]][move[1]] = self.mini_board[move[0]][move[1]]

        return moves