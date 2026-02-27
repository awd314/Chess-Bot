from board import *
from pieces_masks import *


class Bot:
    def __init__(self, board, turn=0, depth=3):
        self.turn = turn
        self.depth = depth
        self.tree = Node(board, None, None, None)
        self.is_thinking = False
    

    def evaluation_fuction(self, node):
        turn = node.board.turn
        ### White
        white_points = 0

        for piece in node.board.white_pieces: # Material
            white_points += mask_dict[piece[2]+1][piece[0]][piece[1]]
            white_points += MATERIAL_EVAL_DICT[piece[2]+1]
        

        ### Black
        black_points = 0
        for piece in node.board.black_pieces:
            black_points += mask_dict[piece[2]][piece[0]][piece[1]]
            black_points += MATERIAL_EVAL_DICT[piece[2]]

        
        # if node.successors == []: # Checkmate and stalemate
        #     king_pos = node.board.get_king_pos(turn) # Retreives king's position for the opposite color
        #     if turn:
        #         if node.board.is_black_checked(king_pos, node.board.mini_board): # black is checkmated
        #             return CHECKMATE_VALUE
        #         else: # Stalemate
        #             return 0
        #     else:
        #         if node.board.is_white_checked(king_pos, node.board.mini_board): # white is checkmated
        #             return -CHECKMATE_VALUE
        #         else: # Stalemate
        #             return 0
        node.board.verify_repetition()
        if node.successors == []:
            node.board.verify_endgame()
        if node.board.game_over_flag == node.board.turn:
            return CHECKMATE_VALUE * [-1, 1][node.board.turn]
        if node.board.game_over_flag > 2:
            return 0

        
        return white_points - black_points
    

    def update_tree(self, move):
        if move is not None:
            index = 0
            while index < len(self.tree.successors):
                if self.tree.successors[index].move == move:
                    self.tree = self.tree.successors[index]
                    return True
                index += 1
        return False
    

    def generate_node_successors(self, node):
        node.successors = []
        for move in node.board.get_moves():
            board_copy = Board([[node.board.mini_board[i][j] for j in range(8)] for i in range(8)], 1-node.board.turn)
            board_copy.play_move(move, 1-board_copy.turn)
            node.successors.append(Node(board_copy, move, None, None))
        if len(node.successors) == 0:
            node.value = self.evaluation_fuction(node)
        return None


    def expand_decision_tree(self, node, depth):
        if not self.is_thinking:
            return None
        if depth == self.depth:
            node.value = self.evaluation_fuction(node)
            return None
        if node.successors is None:
            self.generate_node_successors(node)
        index = 0
        while index < len(node.successors):
            self.expand_decision_tree(node.successors[index], depth+1)
            index += 1
        if node.successors is not None and len(node.successors) > 0:
            if node.board.turn:
                extremum_node = min(node.successors, key=lambda s : s.value)
            else:
                extremum_node = max(node.successors, key=lambda s : s.value)
            node.value = extremum_node.value

        if depth == 0: # Changes flag to indicate the bot's done (Thread bs)
            self.is_thinking = False
            for n in self.tree.successors:
                if n.value == self.tree.value:
                    self.tree.move = n.move


class Node:
    def __init__(self, board, move, alpha, beta, value=None, successors=None):
        self.board = board
        self.move = move
        self.alpha = alpha
        self.beta = beta
        self.value = value
        self.successors = successors