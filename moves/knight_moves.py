
### WHITE

def get_white_knight_moves(board):
    moves = []

    seq = [(-2, -1), (-2, 1), (1, 2), (-1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
    for i in range(8):
        for j in range(8):
            if board[i][j] == 3:
                for k in range(8):
                    if 0 <= i + seq[k][0] < 8 and 0 <= j + seq[k][1] < 8 and board[i + seq[k][0]][j + seq[k][1]] % 2 == 0:
                        moves.append((i, j, i + seq[k][0], j + seq[k][1], 0, 0))

    return moves


### BLACK

def get_black_knight_moves(board):
    moves = []

    seq = [(-2, -1), (-2, 1), (1, 2), (-1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
    for i in range(8):
        for j in range(8):
            if board[i][j] == 4:
                for k in range(8):
                    if 0 <= i + seq[k][0] < 8 and 0 <= j + seq[k][1] < 8 and (board[i + seq[k][0]][j + seq[k][1]] == 0 or board[i + seq[k][0]][j + seq[k][1]] % 2 == 1):
                        moves.append((i, j, i + seq[k][0], j + seq[k][1], 0, 0))

    return moves