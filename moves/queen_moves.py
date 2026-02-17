from moves import rook_moves, bishop_moves

### WHITE

def get_white_queen_moves(queen_pos, board):
    return rook_moves.get_white_rook_moves(queen_pos, board) + bishop_moves.get_white_bishop_moves(queen_pos, board)


### BLACK

def get_black_queen_moves(queen_pos, board):
    return rook_moves.get_black_rook_moves(queen_pos, board) + bishop_moves.get_black_bishop_moves(queen_pos, board)