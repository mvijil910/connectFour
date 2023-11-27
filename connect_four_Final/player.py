
class Player:
    '''class for players'''
    def __init__(self, player_color, game_board):
        '''initializes player_color and game_board'''
        self.player_color = player_color
        self.game_board = game_board

    def put_chip(self, col):
        '''places a chip on the board'''
        self.game_board.put_chip(col, self.player_color)
