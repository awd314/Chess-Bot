### WHITE

def get_white_bishop_moves(bishop_pos, board):
    moves = []

    seq = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    i, j = bishop_pos
    for k in range(4):
        move = seq[k]
        pos = (i, j)
        stopped = False
        while not stopped:
            pos = (pos[0] + move[0], pos[1] + move[1])
            if (not 0 <= pos[0] < 8) or not(0 <= pos[1] < 8) or board[pos[0]][pos[1]] % 2 == 1:
                stopped = True
            else:
                pos_value = board[pos[0]][pos[1]]
                moves.append((i, j, pos[0], pos[1], -1))
                if pos_value != 0 and pos_value % 2 == 0:
                    stopped = True
    return moves


### BLACK

def get_black_bishop_moves(bishop_pos, board):
    moves = []

    seq = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    i, j = bishop_pos
    for k in range(4):
        move = seq[k]
        pos = (i, j)
        stopped = False
        while not stopped:
            pos = (pos[0] + move[0], pos[1] + move[1])
            if (not 0 <= pos[0] < 8) or not(0 <= pos[1] < 8) or (board[pos[0]][pos[1]] != 0 and board[pos[0]][pos[1]] % 2 == 0):
                stopped = True
            else:
                moves.append((i, j, pos[0], pos[1], -1))
                if board[pos[0]][pos[1]] % 2 == 1:
                    stopped = True
    return moves