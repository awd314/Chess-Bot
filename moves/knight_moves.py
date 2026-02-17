
### WHITE

def get_white_knight_moves(knight_pos, board):
    moves = []

    seq = [(-2, -1), (-2, 1), (1, 2), (-1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
    i, j = knight_pos
    for k in range(8):
        if 0 <= i + seq[k][0] < 8 and 0 <= j + seq[k][1] < 8 and board[i + seq[k][0]][j + seq[k][1]] % 2 == 0:
            moves.append((i, j, i + seq[k][0], j + seq[k][1], -1))  

    return moves


### BLACK

def get_black_knight_moves(knight_pos, board):
    moves = []

    seq = [(-2, -1), (-2, 1), (1, 2), (-1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
    i, j = knight_pos
    for k in range(8):
        if 0 <= i + seq[k][0] < 8 and 0 <= j + seq[k][1] < 8 and (board[i + seq[k][0]][j + seq[k][1]] == 0 or board[i + seq[k][0]][j + seq[k][1]] % 2 == 1):
            moves.append((i, j, i + seq[k][0], j + seq[k][1], -1))
                    
    return moves