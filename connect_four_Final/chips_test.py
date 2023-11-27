from chips import Chips
from config import Config


def test__init__():
    '''ensures that chips is pulling in the correct values
    from Config'''
    chips = Chips(3, 1, 'red')
    assert chips.drop_velocity == Config.DROP_VELOCITY
    assert chips.player_color == 'red'
    assert chips.row == 3
    assert chips.col == 1
    assert chips.x == 150.0
    assert chips.y == Config.START_Y_POS
    assert chips.max_y == 355.0
    assert chips.at_max is True
