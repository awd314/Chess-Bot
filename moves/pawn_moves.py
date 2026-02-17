### WHITE

def get_white_pawn_moves(pawns_list, board, en_passant):
    moves = []

    for pawn_info in pawns_list:
        i, j = pawn_info[:2]
        # Moving
        if board[i-1][j] == 0: # Looks if the square in front of the pawn is free
            moves.append((i, j, i-1, j, -1, 0))
            if i == 6 and board[4][j] == 0: # Starting rank, the pawn can moves twice
                moves.append((i, j, i-2, j, i, 0))
        
        # Capture
        if (j > 0 and board[i-1][j-1] > 0 and board[i-1][j-1] % 2 == 0) or (i == 3 and en_passant == j-1): # Left capture
            moves.append((i, j, i-1, j-1, -1, 0))
        
        if (j < 7 and board[i-1][j+1] > 0 and board[i-1][j+1] % 2 == 0) or (i == 3 and en_passant == j+1): # Right capture
            moves.append((i, j, i-1, j+1, -1, 0))
    
    moves_with_promotions = []
    for move in moves:
        if move[2] == 0: # Verifies if a move implies a promotion
            for i in range(8, 12):
                moves_with_promotions.append((move[0], move[1], move[2], move[3], i, 0)) # includes other promotions
        else:
            moves_with_promotions.append((move))
    moves = moves_with_promotions

    return moves

### BLACK

def get_black_pawn_moves(pawns_list, board, en_passant):
    moves = []

    for pawn_info in pawns_list:
        i, j = pawn_info[:2]
        if board[i][j] == 2: # Looks for black pawns in the board
            count += 1
            # Moving
            if board[i+1][j] == 0: # Looks if the square in front of the pawn is free
                moves.append((i, j, i+1, j, -1, 0))
                if i == 1 and board[3][j] == 0: # Starting rank, the pawn can moves twice
                    moves.append((i, j, i+2, j, i, 0))
            
            # Capture
            if (j > 0 and board[i+1][j-1] > 0 and board[i+1][j-1] % 2 == 1) or (i == 4 and en_passant == j-1): # Left capture
                moves.append((i, j, i+1, j-1, -1, 0))
            
            if (j < 7 and board[i+1][j+1] > 0 and board[i+1][j+1] % 2 == 1) or (i == 4 and en_passant == j+1): # Right capture
                moves.append((i, j, i+1, j+1, -1, 0))
    
    moves_with_promotions = []
    for move in moves:
        if move[2] == 7: # Verifies if a move implies a promotion
            for i in range(8, 12):
                moves_with_promotions.append((move[0], move[1], move[2], move[3], i, 0)) # includes other promotions
        else:
            moves_with_promotions.append((move))
    moves = moves_with_promotions

    return moves
    