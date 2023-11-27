from chips import Chips
from game_board import GameBoard
from config import Config
from player import Player
from ai import AI
import os.path
from os import path


class GameController:
    '''handles order & display of grid, chips, and animation'''
    def __init__(self):
        self.game_board = GameBoard()
        self.player1 = Player('red', self.game_board)
        self.player2 = AI('yellow', self.game_board)
        self.current_player = self.player1
        print('It is ' + self.current_player.player_color + ' player\'s turn')
        self.top_chips = [[] for _ in range(Config.BOARD_COL_NUM)]
        self.win = None
        self.ai_countdown = 0
        self.write_to_file = True
        self.show_input_box = 0

    def is_ok_to_ask_name(self):
        '''ensures the prompt to ask for winner's name
        only appears if the user wins not the AI'''
        if not isinstance(self.win, AI):
            return True

    def update(self):
        '''displays the chips and board together'''
        # display the chips 'in play' on the board
        if isinstance(self.current_player, Player):
            if len(self.top_chips) > 0:
                for top_chips in self.top_chips:
                    for top_chip in top_chips:
                        top_chip.display()
            self.game_board.display()
            if self.win and self.game_board.chips_at_max:
                self.display_winner()

    def display_winner(self):
        '''displays winner as long as the game is not a draw, allows the
        input box to prompt the user if the winner is not the AI'''
        if self.win != 'Draw':
            self.game_board.display_winner(self.win.player_color, 'Nodraw')
        if self.is_ok_to_ask_name():
            self.show_input_box += 1

    def check_computer_turn(self):
        '''checks if it is the AI\'s turn and ensures that AIs chips
        display delayed'''
        if isinstance(self.current_player, AI):
            self.ai_countdown += 1
            if self.ai_countdown == 20:
                self.current_player.put_chip()
                self.check_win()
                self.switch_player()
                self.ai_countdown = 0

    def handle_score_keeping(self, winners_name, filename):
        '''writes the scorekeeping file and writes the names/scores
        of winners in order from most wins to least '''
        # writes a new file if none exists, replaces with new updates an
        # existing one
        score = 0
        high_scores = {}
        name = ''
        if self.write_to_file:
            if path.exists(filename):
                with open(filename) as f:
                    for line in f.readlines():
                        names_or_scores = line.split()
                        for n in names_or_scores:
                            if n.isalpha():
                                name = name + n + ' '
                            elif n.isnumeric():
                                score = int(n)
                        high_scores[name.rstrip()] = score
                        name = ''
                    f.close()
                # add 1 to the winners score if it is already in the file,
                # otherwise add a new winner to the file with 1 as the score
            if winners_name in high_scores.keys():
                high_scores[winners_name] += 1
            else:
                high_scores[winners_name] = 1
            # sort by higest score
            sorted_scores = sorted(high_scores, key=high_scores.__getitem__,
                                   reverse=True)

            # write file with highest score first
            with open(filename, 'w') as f:
                for sortedkey in sorted_scores:
                    winner = '{0} {1}\n'.format(sortedkey,
                                                high_scores[sortedkey])
                    f.write(winner)
                f.close()
            self.write_to_file = False

    def handle_mouse_pressed(self, mousePressed, mouseDragged, mouseReleased,
                             mousex_pos):
        '''handles all mouse related events'''
        if self.win or isinstance(self.current_player, AI):
            return
        if mousePressed:
            col = int(self.game_board.get_col(mousex_pos))
            if self.game_board.count_chips_in_col(col) < (Config.BOARD_ROW_NUM
                                                          - 1):
                if len(self.top_chips[col]) <= Config.BOARD_COL_NUM - 1:
                    row = Config.TOP_ROW
                    (self.top_chips[col].append(Chips(row, col,
                     self.current_player.player_color)))

        elif mouseReleased:
            self.top_chips = [[] for _ in range(Config.BOARD_COL_NUM)]
            col = int(self.game_board.get_col(mousex_pos))
            if col >= 0 and col < Config.BOARD_COL_NUM:
                if (self.game_board.count_chips_in_col(col) <
                        Config.BOARD_ROW_NUM - 1):
                    row = Config.BOARD_ROW_NUM - (len
                                                  (self.game_board.chips[col])
                                                  + 1)
                    self.current_player.put_chip(col)
                    self.check_win()
                    if self.win:
                        return
                    self.switch_player()

        elif mouseDragged:
            col = int(self.game_board.get_col(mousex_pos))
            if col < 0 or col >= Config.BOARD_COL_NUM:
                self.top_chips = [[] for _ in range(Config.BOARD_COL_NUM)]
            if col < Config.BOARD_COL_NUM and col >= 0:
                if (self.game_board.count_chips_in_col(col) <
                        Config.BOARD_ROW_NUM - 1):
                    if len(self.top_chips[col]) < Config.BOARD_COL_NUM - 1:
                        row = Config.TOP_ROW
                        self.top_chips = [[] for _ in
                                          range(Config.BOARD_COL_NUM)]
                        (self.top_chips[col].append(Chips(row, col,
                         self.current_player.player_color)))

    def switch_player(self):
        '''switches turns from user to ai and back'''
        self.current_player = self.player2 if self.current_player == \
            self.player1 else self.player1
        print("It is " + self.current_player.player_color + " player's turn")

    def check_win(self):
        '''checks to see who won the game or if it is a draw'''
        check_win = self.game_board.check_win(self.current_player.player_color)
        if check_win is True:
            self.win = self.current_player
        if check_win == 'Draw':
            self.win = 'Draw'
