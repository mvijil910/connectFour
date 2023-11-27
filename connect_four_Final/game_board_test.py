from game_board import GameBoard


def test_init_():
    '''tests that chips is greater than zero and
    value of list is None'''
    game_board = GameBoard()
    assert len(game_board.chips) > 0
    assert game_board.chips[3][1] is None
    assert game_board.chips_at_max is True


def test_get_col():
    '''gives fictional mouse position to test
    get_col'''
    mousex_pos = 150
    game_board = GameBoard()
    col = game_board.get_col(mousex_pos)
    assert col == 1


def test_check_win():
    '''gives four chip locations in a row
    to test if function detects win'''
    game_board = GameBoard()
    game_board.put_chip(0, 'red')
    game_board.put_chip(1, 'red')
    game_board.put_chip(2, 'red')
    game_board.put_chip(3, 'red')
    assert game_board.check_win('red')


def test_check_direct_four():
    '''checks in every direction to see if there are 4 in a row'''
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, -1),
                  (-1, 1)]
    game_board = GameBoard()
    game_board.put_chip(0, 'red')
    game_board.put_chip(1, 'red')
    game_board.put_chip(2, 'red')
    game_board.put_chip(3, 'red')
    assert game_board.check_direct_four(6, 0, 0, (0, 1), 'red') is True


def test_put_chip():
    '''ensures that chips are being dropped in the correct location'''
    game_board = GameBoard()
    game_board.put_chip(0, 'red')
    game_board.put_chip(1, 'red')
    assert game_board.chips[0][6].player_color == 'red'


def test_count_chips():
    '''places chips on the board and ensures that the
    correct number of chips is being counted'''
    game_board = GameBoard()
    game_board.put_chip(0, 'red')
    game_board.put_chip(1, 'red')
    game_board.put_chip(3, 'yellow')
    game_board.put_chip(4, 'yellow')
    assert game_board.count_chips('red') == 2
    assert game_board.count_chips('yellow') == 2


def test_count_chips_in_col():
    '''puts chips in a column then checks to see if
    the counter is counting the correct num of chips'''
    game_board = GameBoard()
    game_board.put_chip(1, 'red')
    game_board.put_chip(1, 'red')
    game_board.put_chip(1, 'yellow')
    game_board.put_chip(1, 'yellow')
    game_board.put_chip(0, 'red')
    game_board.put_chip(0, 'red')
    assert game_board.count_chips_in_col(1) == 4
    assert game_board.count_chips_in_col(0) == 2


def test_can_play():
    '''checks to see which spaces are filled to eval
    if the chip can drop in a certain location'''
    game_board = GameBoard()
    game_board.put_chip(1, 'red')
    game_board.put_chip(1, 'red')
    game_board.put_chip(1, 'yellow')
    game_board.put_chip(1, 'yellow')
    game_board.put_chip(0, 'red')
    game_board.put_chip(0, 'red')
    assert game_board.can_play(1) is True
    assert game_board.can_play(-1) is False
