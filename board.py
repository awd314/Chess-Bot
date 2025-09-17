from random import random
from settings import SIZE

class Board:
    """
    Represents the game board, with 8 rows 8 columns. The pieces are represented
    by integers given in the pieces dictionary.
    """
    def __init__(self):
        #self.flipped = 1 if random() < 0.5 else 0
        self.flipped = 0
        self.miniBoard = [
            [ 7,  5,  3,  9, 11,  3,  5,  7],
            [ 1,  1,  1,  1,  1,  1,  1,  1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [ 6,  4,  2,  8, 10,  2,  4,  6]
        ]

        self.whiteCastle = False
        self.blackCastle = False
        self.enPassant = -1 # Indicates which pawn did en passant, represents the index of the column
    

    ## NOTE  White legal moves here

    def GetWhiteLegalMoves(self, board):
        """
        Returns a list of all legal moves that white can play. A move is in
        format [y_start, x_start, y_end, x_end] where the piece to move is at index
        (y_start, x_start) and its ending position (y_end, x_end). In case of castling,
        the king moves two spaces so it's recognized this way, and the according rook 
        is also moved.
        """
        for i in range(SIZE):
            for j in range(SIZE):
                if self.miniBoard[i][j] == 0:
                    pass


    def GetWhitePawnMoves(self, pos, board):
        """
        Returns all possible moves for a given pawn. The function takes in parameter a position
        in format (i, j) indicating a white pawn (i.e it is supposed that it's a white pawn). It 
        then checks all legal moves for this specific piece.
        """
        i, j = pos
        moves = []

        if board[i-1][j] == -1: # Checks if the square in front of the pawn is unoccupied
            moves.append((i, j, i-1, j))
        
        if i == 6 and board[i-2][j] == board[i-1][j] == -1: # Special case of moving two squares ahead on starting square
            moves.append((i, j, i-2, j))
        
        if j > 0 and board[i-1][j-1] != -1 and board[i-1][j-1] % 2 == 1: # Left capture
            moves.append((i, j, i-1, j-1))
        
        if j < SIZE-1 and board[i-1][j+1] != -1 and board[i-1][j+1] % 2 == 1: # Right Capture
            moves.append((i, j, i-1, j+1))
        
        if i == 3 and (self.enPassant == j-1 or self.enPassant == j+1) and board[2][self.enPassant] == -1: # Checks if the pawn that did en passant is on either side of the current pawn
            moves.append((i, j, 2, self.enPassant))
        
        return moves


    def GetWhiteBishopMoves(self, pos, board):
        """
        Returns all possible moves for a given bishop whose position is provided as a parameter of the
        function. The given position should point to a bishop as the function treats the given piece as
        one.
        """
        i, j = pos
        moves = []

        indicesSequence = ((1, 1), (1, -1), (-1, -1), (-1, 1)) # Sequence of directions to follow the bishop's possible moves

        for k in range(4):
            obstructedLane = False # Boolean to indicate if the current visited lane is obstructed or not (piece blocking the way or edge of the board)
            y, x = 0, 0
            while not obstructedLane:
                y += indicesSequence[k][0]
                x += indicesSequence[k][1]
                if 0 <= i+y < SIZE and 0 <= j+x < SIZE: # Checks if indices are oob
                    if board[i+y][j+x] != -1: # square blocked by white piece
                        obstructedLane = True
                    if board[i+y][j+x] % 2 == 1: # Black piece or empty square
                        moves.append((i, j, i+y, j+x))
                else:
                    obstructedLane = True
         
        return moves


    def GetWhiteKnightMoves(self, pos, board):
        """
        Returns all possible moves for a white knight on the position given in parameter. The square indicated
        by the position is supposed to be containing a white knight.
        """
        i, j = pos
        moves = []

        movesSequence = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)] # Complete set of knight movements
        for move in movesSequence:
            y = i + move[0]
            x = j + move[1]
            if 0 <= y < SIZE and 0 <= x < SIZE and board[y][x] % 2 == 1: # Checks if the current position is not oob and if it's occupied by nothing or an enemy piece
                moves.append((i, j, y, x)) # Adds to the possible moveset if so

        return moves
    

    def GetWhiteRookMoves(self, pos, board):
        """
        Returns a list of all possible rook moves for a white piece. The given position
        points to a rook and the given board is an 8x8 matrix.

        The algorithm to determine the legal moves is simimar to the bishop's.
        """
        i, j = pos
        moves = []

        indicesSequence = ((0, 1), (0, -1), (-1, 0), (1, 0))

        for k in range(4):
            obstructedLane = False
            y, x = 0, 0
            while not obstructedLane:
                y += indicesSequence[k][0]
                x += indicesSequence[k][1]
                if 0 <= i+y < SIZE and 0 <= j+x < SIZE:
                    if board[i+y][j+x] != -1: # square blocked by white piece
                        obstructedLane = True
                    if board[i+y][j+x] % 2 == 1: # Black piece or empty square
                        moves.append((i, j, i+y, j+x))
                else:
                    obstructedLane = True
         
        return moves


    def GetWhiteQueenMoves(self, pos, board):
        """
        Returns the list containing all possible moves for the white queen with a given board. Since
        the queen is just a combination of bishop and rook, we can just call both functions to get
        the list of moves.

        Also, no moves overlap between rook and bishop for a same position, therefore it is not necessary
        to check for two occurences of the same move.
        """
        bishopComponent = self.GetWhiteBishopMoves(pos, board)
        rookComponent = self.GetWhiteRookMoves(pos, board)

        return bishopComponent + rookComponent


    def GetWhiteKingMoves(self, pos, board):
        """
        Returns the list of the white king's legal moves. Takes castling into account and registers it as the
        king moving two spaces instead of one.
        """
        i, j = pos
        moves = []

        # Regular moves

        for y in range(-1, 2):
            for x in range(-1, 2):
                if y != 0 or x != 0:
                    if board[i+y][j+x] == -1 or board[i+y][j+x] % 2 == 0:
                        moves.append((i, j, i+y, j+x))
        
        # Left castle

        # Right castle

        return moves
    

    ## NOTE Black legal moves here


    def GetBlackLegalMoves(self, board):
        """
        Returns a complete list of all possible moves for black to play.
        """
        pass