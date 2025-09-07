from random import random
from settings import SIZE

class Board:
    def __init__(self):
        self.flipped = 1 if random() < 0.5 else 0
        self.miniBoard = [
            [7, 5, 3, 9, 11, 3, 5, 7],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [6, 4, 2, 8, 10, 2, 4, 6]
        ]

        self.whiteCastle = False
        self.blackCastle = False
    

    def GetWhiteLegalMoves(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if self.miniBoard[i][j] == 0:
                    pass