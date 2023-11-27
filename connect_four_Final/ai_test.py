from ai import AI
import copy
from config import Config
from player import Player
from game_board import GameBoard


def test__init__():
    '''tests class is being initialized correctly'''
    game_board = GameBoard()
    ai = AI('yellow', game_board)
    assert isinstance(ai, Player)
    assert ai.opponent_color == 'red'
    assert ai.col_order[0] == 3
    assert len(ai.memo) == 0


def test_find_best_move():
    '''tests that AI is finding the best move, uses
    col_order and minimax in its algorithm'''
    game_board = GameBoard()
    ai = AI('yellow', game_board)
    ai.find_best_move()
    assert ai.find_best_move() == 3


def test_put_chip():
    '''ensures that put_chip is putting chips into the
    chips list using algorithm for best pos'''
    game_board = GameBoard()
    ai = AI('yellow', game_board)
    ai.put_chip()
    assert ai.game_board.chips[3][6].player_color == 'yellow'


def test_minimax():
    '''tests minimax algorithm using value, col'''
    game_board = GameBoard()
    ai = AI('yellow', game_board)
    ai.put_chip()
    value, col = ai.minimax(game_board, 1, 'yellow', float('-inf'),
                            float('inf'))
    assert value == -1
    assert col == 3


def test_board_to_memo_key():
    '''checks that memo_key is storing the chips on the board'''
    game_board = GameBoard()
    ai = AI('yellow', game_board)
    ai.put_chip()
    memo_key = ai.board_to_memo_key(game_board)
    assert memo_key[3][6] == 1
