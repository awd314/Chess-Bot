from board import *
from pieces_masks import *


class Bot:
    def __init__(self, board, turn=0, depth=3):
        self.turn = turn
        self.depth = depth
        self.tree = Node(board, None)
        self.is_thinking = False
    

    def evaluation_fuction(self, node):
        white_points = 0
        black_points = 0

        for piece in node.board.white_pieces: # Material
            white_points += mask_dict[piece[2]+1][piece[0]][piece[1]]
            white_points += MATERIAL_EVAL_DICT[piece[2]+1]
            # if node.board.is_white_checked(piece[:2], node.board.mini_board):
            #     black_points += MATERIAL_EVAL_DICT[piece[2]+1]
        
        for piece in node.board.black_pieces:
            black_points += mask_dict[piece[2]][piece[0]][piece[1]]
            black_points += MATERIAL_EVAL_DICT[piece[2]]
            # if node.board.is_black_checked(piece[:2], node.board.mini_board):
            #     white_points += MATERIAL_EVAL_DICT[piece[2]]


        node.board.verify_repetition()
        if node.successors == []:
            node.board.verify_endgame()
        if node.board.game_over_flag == node.board.turn:
            return CHECKMATE_VALUE * [-1, 1][node.board.turn]
        if node.board.game_over_flag > 2:
            return 0

        return white_points - black_points + [-1, 1][node.board.turn] * node.capture_index
    

    def update_tree(self, move):
        if move is not None:
            index = 0
            #print("\n", move, "\n")
            while index < len(self.tree.successors):
                #print(self.tree.successors[index].move)
                if self.tree.successors[index].move == move:
                    self.tree = self.tree.successors[index]
                    return None
                index += 1
    

    def generate_node_successors(self, node):
        node.successors = []
        for move in node.board.get_moves():
            board_copy = Board([[node.board.mini_board[i][j] for j in range(8)] for i in range(8)], 1-node.board.turn)
            capture_index = 0
            if board_copy.mini_board[move[2]][move[3]] != 0:
                starting_square_piece_key = board_copy.mini_board[move[2]][move[3]]
                ending_square_piece_key = board_copy.mini_board[move[0]][move[1]]
                capture_index = MATERIAL_EVAL_DICT[starting_square_piece_key + starting_square_piece_key%2] - MATERIAL_EVAL_DICT[ending_square_piece_key + ending_square_piece_key%2]
            board_copy.play_move(move, 1-board_copy.turn)
            if node.board.turn == 0: # Max
                alpha, beta = -CHECKMATE_VALUE, node.beta
            else:
                alpha, beta = node.alpha, CHECKMATE_VALUE
            node.successors.append(Node(board_copy, move, alpha, beta, capture_index=capture_index))
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
        while index < len(node.successors) and node.alpha < node.beta:
            successor = node.successors[index]
            # if successor.exploration > node.exploration:
            #     successor.exploration = 0
            self.expand_decision_tree(successor, depth+1)
            if node.board.turn == 0: # Max
                node.alpha = max(node.alpha, successor.value)
                node.value = node.alpha
            else: # Min
                node.beta = min(node.beta, successor.value)
                node.value = node.beta
            index += 1

        if depth == 0: # Changes flag to indicate the bot's done (Thread bs)
            self.is_thinking = False
            if self.turn == 0:
                self.tree.move = self.tree.get_max_successor().move
            else:
                self.tree.move = self.tree.get_min_successor().move


class Node:
    def __init__(self, board, move, alpha=-CHECKMATE_VALUE, beta=CHECKMATE_VALUE, value=None, successors=None, capture_index=0):
        self.board = board
        self.move = move
        self.alpha = alpha
        self.beta = beta
        self.value = value
        self.successors = successors
        self.capture_index = capture_index
    

    def get_min_successor(self):
        minmum_successor_index = 0
        for i in range(len(self.successors)):
            if self.successors[minmum_successor_index].value is None or \
                (self.successors[i].value is not None and self.successors[minmum_successor_index].value > self.successors[i].value):
                minmum_successor_index = i
        return self.successors[minmum_successor_index]


    def get_max_successor(self):
        maximum_successor_index = 0
        for i in range(len(self.successors)):
            if self.successors[maximum_successor_index].value is None or \
                (self.successors[i].value is not None and self.successors[maximum_successor_index].value < self.successors[i].value):
                maximum_successor_index = i
        return self.successors[maximum_successor_index]