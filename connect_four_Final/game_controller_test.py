from game_controller import GameController
from chips import Chips
from config import Config
from player import Player
from ai import AI
from game_board import GameBoard
import random


def test__init__():
    '''tests initialized variables in game_controller'''
    game_controller = GameController()
    assert isinstance(game_controller.game_board, GameBoard)
    assert isinstance(game_controller.player1, Player)
    assert isinstance(game_controller.player2, AI)
    assert game_controller.current_player.player_color == 'red'
    # seven empty lists
    assert len(game_controller.top_chips) == 7
    assert game_controller.win is None
    assert game_controller.ai_countdown == 0
    assert game_controller.write_to_file is True
    assert game_controller.show_input_box == 0


def test_is_okay_to_ask_name():
    '''tests that name box only pops if the user wins,  not the AI'''
    game_controller = GameController()
    for i in range(Config.BOARD_COL_NUM - 1):
        w = 1
        for j in range(Config.BOARD_ROW_NUM - 1):
            game_controller.switch_player()
            game_controller.handle_mouse_pressed(False, False, True, w)
            inc_num = Config.SCREEN_WIDTH/Config.BOARD_COL_NUM
            w += inc_num
    game_controller.switch_player()
    game_controller.check_win()
    assert game_controller.is_ok_to_ask_name() is True


def test_check_computer_turn():
    '''ensures that if this is True, player_color should be yellow'''
    game_controller = GameController()
    game_controller.switch_player()
    game_controller.check_computer_turn()
    for chips in game_controller.game_board.chips:
        for chip in chips:
            if chip:
                assert chip.player_color == 'yellow'


def test_handle_score_keeping():
    '''tests that file is created if none exists, wins by the user
    are being added to the file in the right order, existing wins
    are being accumulated'''
    game_controller = GameController()
    filenumber = int(random.randint(0, 100))
    filename = 'scores_test' + filenumber.__str__() + '.txt'
    game_controller.handle_score_keeping('Marcela', filename)
    game_controller.write_to_file = True
    game_controller.handle_score_keeping('Marcela', filename)
    game_controller.write_to_file = True
    game_controller.handle_score_keeping('Veronica', filename)
    entries_in_file = 0
    name = ''
    with open(filename) as f:
        for line in f.readlines():
            names_or_scores = line.split()
            for n in names_or_scores:
                if n.isalpha():
                    name = n
                    if entries_in_file == 0:
                        assert name == 'Marcela'
                    else:
                        assert name == 'Veronica'
                elif n.isnumeric():
                    score = int(n)
                    if entries_in_file == 0:
                        assert score == 2
                    else:
                        assert score == 1
            entries_in_file += 1


def test_handle_mouse_pressed():
    '''ensures correct that chip appears at the top of the board
    when the users presses the mouse'''
    game_controller = GameController()
    game_controller.handle_mouse_pressed(True, False, False, 40)
    assert len(game_controller.top_chips[0]) > 0
    chip = game_controller.top_chips[0][0]
    assert chip.row == 0
    game_controller.handle_mouse_pressed(True, False, False, 140)
    assert len(game_controller.top_chips[1]) > 0
    chip1 = game_controller.top_chips[1][0]
    assert chip1.col == 1


def test_handle_mouse_dragged():
    '''ensures that chip is not dropped and that the user is
    able to drag the chip while the mouse is still pressed'''
    game_controller = GameController()
    game_controller.handle_mouse_pressed(True, False, False, 40)
    game_controller.handle_mouse_pressed(False, True, False, 140)
    assert len(game_controller.top_chips[1]) > 0
    chip = game_controller.top_chips[1][0]
    assert chip.row == 0
    assert chip.col == 1


def test_handle_mouse_released():
    '''ensures that the chip is dropped once the mouse is released'''
    game_controller = GameController()
    assert game_controller.current_player.player_color == 'red'
    game_controller.handle_mouse_pressed(False, False, True, 40)
    assert game_controller.game_board.chips[0][6] is not None
    chip = game_controller.game_board.chips[0][6]
    assert game_controller.current_player.player_color == 'yellow'
    game_controller.handle_mouse_pressed(False, False, True, 40)
    assert game_controller.game_board.chips[0][5] is None
    game_controller.switch_player()
    game_controller.handle_mouse_pressed(False, False, True, 40)
    assert game_controller.game_board.chips[0][5] is not None
    chip = game_controller.game_board.chips[0][5]


def test_switch_player():
    '''ensures that the player switches after every turn'''
    game_controller = GameController()
    game_controller.switch_player()
    assert game_controller.current_player.player_color == 'yellow'


def test_check_win():
    '''tests that the game is detecting when there is a winner'''
    game_controller = GameController()
    for i in range(Config.BOARD_COL_NUM - 1):
        w = 1
        for j in range(Config.BOARD_ROW_NUM - 1):
            game_controller.handle_mouse_pressed(False, False, True, w)
            game_controller.switch_player()
            inc_num = Config.SCREEN_WIDTH/Config.BOARD_COL_NUM
            w += inc_num
    game_controller.check_win()
    assert isinstance(game_controller.win, Player)
