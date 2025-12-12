class Board:
    def __init__(self, miniBoard, turn=True, whiteMoves=[], whiteChecks=[], blackMoves=[], blackChecks=[], enPassant=-1):
        self.miniBoard = miniBoard

        self.turn = turn # Indicates whose turn it is to play (True for white, False for black)

        self.whiteMoves = whiteMoves
        self.whiteChecks = whiteChecks # White moves sequences that check the black king

        self.blackMoves = blackMoves
        self.blackChecks = blackChecks # Black moves sequences that check the white king

        self.enPassant = enPassant # Index of the column where enPassant has been performed (by default -1 to indicate no en passant has been performed)
    

    def GetAllAttributes(self) -> tuple:
        return (self.miniBoard, self.whiteMoves, self.whiteChecks, self.blackMoves, self.blackChecks, self.enPassant)


    def ComputeWhitePawnMoves(self, i, j):
        moves = []

        if i == 6 and self.miniBoard[i-2][j] == 0 and self.miniBoard[i-1][j] == 0:
            moves.append((i, j, i-2, j, 2)) # 2 is en passant flag
            moves.append((i, j, i-1, j, 0))
        if i < 6:
            if self.miniBoard[i-1][j] % 2 == 1:
                if i-1 == 0:
                    moves.append((i, j, i-1, j, 3)) # 3 is promotion flag
                else:
                    moves.append((i, j, i-1, j, 0))
            if j > 0 and (self.miniBoard[i-1][j-1] % 2 == 0 or self.miniBoard[i][j-1] % 2 == 0 and self.enPassant == j-1):
                if i-1 == 0:
                    moves.append((i, j, i-1, j-1, 3))
                else:
                    moves.append((i, j, i-1, j-1, 1)) # 1 is capture flag
            if j < 7 and (self.miniBoard[i-1][j+1] % 2 == 0 or self.miniBoard[i][j+1] % 2 == 0 and self.enPassant == j+1):
                if i-1 == 0:
                    moves.append((i, j, i-1, j+1, 3))
                else:
                    moves.append((i, j, i-1, j+1, 1))

        return moves