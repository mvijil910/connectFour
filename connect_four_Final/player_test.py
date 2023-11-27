from player import Player
from game_board import GameBoard
from chips import Chips


def test__init__():
    '''tests init is initialized correctly'''
    game_board = GameBoard()
    player = Player('red', game_board)
    assert player.player_color == 'red'
    assert isinstance(player.game_board, GameBoard)


def put_chip_test():
    '''tests that chip has been placed on board'''
    game_board = GameBoard()
    player = Player('red', game_board)
    player.put_chip(2)
    assert isinstance(player.game_board.chips[2][6], Chips)
