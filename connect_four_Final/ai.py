import copy
from config import Config
from player import Player
from chips import Chips
import time


class AI(Player):
    '''creates the AI player class'''
    def __init__(self, player_color, game_board):
        '''initializes AI player as yellow and opponent color as red'''
        Player.__init__(self, player_color, game_board)
        # confirms the ai's color and opponent color
        if self.player_color == 'red':
            self.opponent_color = 'yellow'
        else:
            self.opponent_color = 'red'
        self.col_order = [3, 2, 4, 1, 5, 0, 6]
        self.memo = {}

    def find_best_move(self):
        '''uses minimax algorithm to find the best move'''
        value, col = self.minimax(self.game_board, Config.AI_DEPTH,
                                  self.player_color, float('-inf'),
                                  float('inf'))
        return col

    def put_chip(self):
        '''puts the chip in the col'''
        col = self.find_best_move()
        self.game_board.put_chip(col, self.player_color)

    def minimax(self, board, depth, player_color, alpha, beta):
        '''code for minimax algorithm'''
        previous_player_color = 'red' if player_color == 'yellow' else 'red'
        # maximizing the AI's score
        is_maximizing = self.player_color == player_color
        if depth == 0 or board.check_win(previous_player_color):
            count = board.count_chips(player_color)
            if is_maximizing:
                return Config.AI_DEPTH - count, -1
            else:
                return count - Config.AI_DEPTH, -1
        memo_key = self.board_to_memo_key(board)
        if memo_key in self.memo:
            return self.memo[memo_key]

        future_boards = [copy.deepcopy(board) for _ in
                         range(Config.BOARD_COL_NUM)]
        for col in range(Config.BOARD_COL_NUM):
            future_boards[col].put_chip(col, player_color)
        if is_maximizing:
            max_val = float('-inf')
            # best_col to play
            best_col = 0
            for col in self.col_order:
                if (not board.can_play(col)):
                    continue
                child_board = future_boards[col]
                next_player_color = ('red' if player_color ==
                                     'yellow' else 'red')
                value, col_played = self.minimax(child_board, depth - 1,
                                                 next_player_color, alpha,
                                                 beta)
                if value > max_val:
                    max_val = value
                    best_col = col
                alpha = max(alpha, value)
                if beta <= alpha:
                    break

            self.memo[memo_key] = (max_val, best_col)
            return max_val, best_col
        else:
            min_val = float('inf')
            best_col = 0
            for col in self.col_order:
                if (not board.can_play(col)):
                    continue
                child_board = future_boards[col]
                next_player_color = ('red' if player_color == 'yellow'
                                     else 'red')
                value, col_played = self.minimax(child_board, depth - 1,
                                                 next_player_color, alpha,
                                                 beta)
                if value < min_val:
                    min_val = value
                    best_col = col
                beta = min(beta, value)
                if beta <= alpha:
                    break

            self.memo[memo_key] = (min_val, best_col)
            return min_val, best_col

    def board_to_memo_key(self, board):
        '''stores current state of the board, chip locations as 1 AI
        chips(maximizing) and 2 for user chips (minimizing)'''
        new_chips = [[0] * Config.BOARD_ROW_NUM for _ in
                     range(Config.BOARD_COL_NUM)]
        for row in range(Config.BOARD_ROW_NUM):
            for col in range(Config.BOARD_COL_NUM):
                # checks to see if their is a chip in the pos
                if board.chips[col][row]:
                    # if yellow, save as 1
                    if board.chips[col][row].player_color == self.player_color:
                        new_chips[col][row] = 1
                    else:
                        # if red, save as 2
                        new_chips[col][row] = 2
        return tuple(map(tuple, new_chips))
