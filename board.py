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
    

    def GetWhiteLegalMoves(self):
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
    

    def CheckMoveCheck(self, move, flag=-1):
        """
        Returns a boolean indicating whether or not a given move creates a check on the king or not.
        The given flag indicates if it's about the white king or the black king.
        """
        pass


    def GetWhitePawnMoves(self, pos):
        """
        Returns all possible moves for a given pawn. The function takes in parameter a position
        in format (i, j) indicating a white pawn (i.e it is supposed that it's a white pawn). It 
        then checks all legal moves for this specific piece.
        """
        i, j = pos
        moves = []

        if self.miniBoard[i-1][j] == -1: # Checks if the square in front of the pawn is unoccupied
            moves.append((i, j, i-1, j))
        
        if i == 6 and self.miniBoard[i-2][j] == self.miniBoard[i-1][j] == -1: # Special case of moving two squares ahead on starting square
            moves.append((i, j, i-2, j))
        
        if j > 0 and self.miniBoard[i-1][j-1] != -1 and self.miniBoard[i-1][j-1] % 2 == 1: # Left capture
            moves.append((i, j, i-1, j-1))
        
        if j < SIZE-1 and self.miniBoard[i-1][j+1] != -1 and self.miniBoard[i-1][j+1] % 2 == 1: # Right Capture
            moves.append((i, j, i-1, j+1))
        
        if i == 3 and (self.enPassant == j-1 or self.enPassant == j+1) and self.miniBoard[2][self.enPassant] == -1: # Checks if the pawn that did en passant is on either side of the current pawn
            moves.append((i, j, 2, self.enPassant))
        
        return moves


    def GetWhiteBishopMoves(self, pos):
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
                    if self.miniBoard[i+y][j+x] != -1: # square blocked by white piece
                        obstructedLane = True
                    if self.miniBoard[i+y][j+x] % 2 == 1: # Black piece or empty square
                        moves.append((i, j, i+y, j+x))
                else:
                    obstructedLane = True
         
        return moves