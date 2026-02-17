### WHITE

def get_white_king_moves(pos, board):
    moves = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if 0 <= pos[0] + i < 8 and 0 <= pos[1] + j < 8 and board[pos[0]+i][pos[1]+j] % 2 == 0:
                    moves.append((pos[0], pos[1], pos[0]+i, pos[1]+j, -1))
    
    if pos == (7, 4): # Castling
        # short castle
        if board[7][5] == 0 and board[7][6] == 0 and board[7][7] == 7:
            moves.append((pos[0], pos[1], 7, 6, 12))
        # long castle
        if board[7][3] == 0 and board[7][2] == 0 and board[7][1] == 0 and board[7][0] == 7:
            moves.append((pos[0], pos[1], 7, 1, 12))

    return moves


### BLACK

def get_black_king_moves(pos, board):
    moves = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if 0 <= pos[0] + i < 8 and 0 <= pos[1] + j < 8 and (board[pos[0]+i][pos[1]+j] % 2 == 1 or board[pos[0]+i][pos[1]+j] == 0):
                    moves.append((pos[0], pos[1], pos[0]+i, pos[1]+j, -1))
    
    if pos == (0, 4): # Castling
        # short castle
        if board[0][5] == 0 and board[0][6] == 0 and board[0][7] == 8:
            moves.append((pos[0], pos[1], 0, 6, 12))
        # long castle
        if board[0][3] == 0 and board[0][2] == 0 and board[7][1] == 0 and board[7][0] == 8:
            moves.append((pos[0], pos[1], 0, 1, 12))

    return moves