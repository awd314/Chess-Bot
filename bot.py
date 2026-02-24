from board import *
import sys
from numpy import random
sys.setrecursionlimit(RECURSION_LIMIT)


class Bot:
    def __init__(self, turn, board, depth=2):
        self.turn = turn
        self.depth = depth
        self.tree = Node(board, None, None, None)
        self.is_thinking = False
    

    def evaluation_fuction(self, node):
        ### White
        white_points = 0

        for piece in node.board.white_pieces: # Material
            white_points += MATERIAL_EVAL_DICT[piece[2]+1]
        

        ### Black
        black_points = 0
        for piece in node.board.black_pieces:
            black_points += MATERIAL_EVAL_DICT[piece[2]]

        
        return white_points - black_points + random.random()
    

    def update_tree(self, move):
        if move is not None:
            index = 0
            while index < len(self.tree.successors):
                if self.tree.successors[index].move == move:
                    self.tree = self.tree.successors[index]
                    return True
                index += 1
        return False


    def expand_decision_tree(self, node, depth):
        if not self.is_thinking:
            return None
        if depth == self.depth:
            node.value = self.evaluation_fuction(node)
            return None
        if node.successors is None:
            node.successors = []
            for move in node.board.get_moves():
                board_copy = Board([[node.board.mini_board[i][j] for j in range(8)] for i in range(8)], 1-node.board.turn)
                board_copy.play_move(move, 1-board_copy.turn)
                node.successors.append(Node(board_copy, move, None, None))
        index = 0
        while index < len(node.successors):
            if node.successors[index].value is None:
                self.expand_decision_tree(node.successors[index], depth+1)
            index += 1
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