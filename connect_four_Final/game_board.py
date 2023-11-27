from config import Config
from chips import Chips
import time


class GameBoard:
    '''draws the game board layout'''
    def __init__(self):
        self.chips = ([[None] * Config.BOARD_ROW_NUM
                      for _ in range(Config.BOARD_COL_NUM)])
        self.chips_at_max = True

    def get_col(self, mousex_pos):
        '''determines column you are placing the
        chip on the gameboard based on mouse pos'''
        return ((mousex_pos - Config.GAMEBOARD_LEFT_TOP[0]) //
                (Config.CHIP_EXTENT + Config.CHIP_DISTANCE))

    def check_win(self, player_color):
        '''checks all directions to see if there are 4 of a kind'''
        if self.count_chips(player_color) < 3:
            return False
        # checks these directions to find 4 in a row
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1),
                      (-1, -1), (-1, 1)]
        # ensures this is only checking within the board space
        for row in range(Config.BOARD_ROW_NUM):
            for col in range(Config.BOARD_COL_NUM):
                if self.chips[col][row] is not None:
                    for d in directions:
                        if self.check_direct_four(row, col, 0, d,
                                                  player_color):
                            return True
        for row in range(Config.BOARD_ROW_NUM):
            for col in range(Config.BOARD_COL_NUM):
                if self.chips[col][row] is None:
                    return False
        return 'Draw'

    def check_direct_four(self, row, col, count, direction, player_color):
        '''evals if four of a kind are in a row in any direction'''
        if (row < 0 or row >= Config.BOARD_ROW_NUM or col < 0 or
                col >= Config.BOARD_COL_NUM):
            return False

        if self.chips[col][row] is None or (self.chips[col][row].player_color
                                            != player_color):
            return False

        count += 1
        if count == 4:
            return True

        return (self.check_direct_four(row + direction[0], col + direction[1],
                count, direction, player_color))

    def display(self):
        '''shows the game board grid & chips that have been placed'''
        self.chips_at_max = True
        false_counter = 0
        for chips in self.chips:
            for chip in chips:
                if chip:
                    chip.display()
                    if (chip.at_max is not True):
                        false_counter += 1
        if false_counter != 0:
            self.chips_at_max = False
        rows = Config.BOARD_ROW_NUM
        cols = Config.BOARD_COL_NUM
        fill(*Config.BOARD_COLOR)
        rectMode(CENTER)
        # ensures no outline drawn
        noStroke()
        # postiions the location of the grid on the screen
        for x in range(0, Config.SCREEN_WIDTH+Config.SCREEN_WIDTH/cols,
                       Config.SCREEN_WIDTH/cols):
            for y in range(Config.SCREEN_HEIGHT/rows, Config.SCREEN_HEIGHT +
                           Config.SCREEN_HEIGHT/rows,
                           Config.SCREEN_HEIGHT/rows):
                if y < Config.SCREEN_HEIGHT:
                    fill(*Config.BACKGROUND_COLOR)
                    strokeWeight(20)
                    stroke(0, 0, 225)
                    line(x, y, x, y + Config.SCREEN_HEIGHT/rows)
                    line(x, y, x + Config.SCREEN_WIDTH/cols, y)
                else:
                    line(x, y, x + Config.SCREEN_WIDTH/cols, y)
                    fill(*Config.BACKGROUND_COLOR)

    def display_winner(self, player_color, is_a_draw):
        '''displays who won the game yellow/red'''
        txt = player_color + ' wins!' if is_a_draw != 'Draw' else 'Draw'
        fill(*Config.TEXT_COLOR)
        textSize(Config.TEXT_SIZE)
        text(txt, Config.TEXT_X, Config.TOP_ROW + (Config.CHIP_EXTENT +
                                                   Config.CHIP_DISTANCE)
             / 2)

    def put_chip(self, col, player_color):
        '''puts a chip into the column & row for a given player'''
        if self.count_chips_in_col(col) < Config.BOARD_ROW_NUM - 1:
            row = Config.BOARD_ROW_NUM - (self.count_chips_in_col(col) + 1)
            self.chips[col][row] = Chips(row, col, player_color)

    def count_chips(self, player_color):
        '''counts all the chips on the board for a given color'''
        count = 0
        for row in range(Config.BOARD_ROW_NUM):
            for col in range(Config.BOARD_COL_NUM):
                if self.chips[col][row] and (self.chips[col][row].player_color
                                             == player_color):
                    count += 1
        return count

    def count_chips_in_col(self, col):
        '''counts chips within a column'''
        count = 0
        for chip in self.chips[col]:
            if chip:
                count += 1
        return count

    def can_play(self, col):
        '''checks to see if a certain space can be played'''
        return (col >= 0 and col < Config.BOARD_COL_NUM and
                self.count_chips_in_col(col) < (Config.BOARD_ROW_NUM - 1))
