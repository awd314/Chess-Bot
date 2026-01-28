def get_white_pawn_moves(board, en_passant):
    """
    Returns all white_pawn_moves, including illegal ones. To get the legal
    ones, the program filters the moves that end up in an illegal situation.
    """
    moves = []

    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1: # Looks for white pawns in the board
                count += 1
                # Moving
                if board[i-1][j] == 0: # Looks if the square in front of the pawn is free
                    moves.append((i, j, i-1, j, 0, 0, 0))
                    if i == 6 and board[5][j] == 0: # Starting rank, the pawn can moves twice
                        moves.append((i, j, i-2, j, i, 0, 0))
                
                # Capture
                if (j > 0 and board[i-1][j-1] > 0 and board[i-1][j-1] % 2 == 0) or (i == 1 and en_passant == j-1): # Left capture
                    moves.append((i, j, i-1, j-1, 0, 0, 0))
                
                if (j < 7 and board[i-1][j+1] > 0 and board[i-1][j+1] % 2 == 0) or (i == 1 and en_passant == j+1): # Right capture
                    moves.append((i, j, i-1, j+1, 0, 0, 0))

                if count == 8:
                    break
    
    return moves
    