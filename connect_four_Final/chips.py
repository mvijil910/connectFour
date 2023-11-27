from config import Config


class Chips:
    '''class to draw playing chips and
    display chip animation'''
    def __init__(self, row, col, player_color):
        '''sets rows and columns where chips should appear and
        initializes chip parameters'''
        self.drop_velocity = Config.DROP_VELOCITY
        self.player_color = player_color
        self.row = row
        self.col = col
        self.color = Config.SIDE_COLOR[player_color]
        # takes column number and centers the chip within the column
        self.x = (col * (Config.SCREEN_WIDTH/Config.BOARD_COL_NUM) +
                        ((Config.CHIP_EXTENT + Config.CHIP_DISTANCE)/2))
        # top y pos
        self.y = Config.START_Y_POS
        # bottom y pos
        self.max_y = (Config.GAMEBOARD_LEFT_TOP[1] + Config.CHIP_DISTANCE +
                      self.row * (Config.CHIP_EXTENT + Config.CHIP_DISTANCE))
        self.at_max = True

    def display(self):
        '''draws the chip drop animation'''
        self.y = min(self.y + self.drop_velocity, self.max_y)
        fill(*self.color)
        noStroke()
        circle(self.x, self.y, Config.CHIP_EXTENT)
        # how fast the chips will fall
        self.drop_velocity += 5
        if self.y == self.max_y:
            self.at_max = True
        else:
            self.at_max = False
