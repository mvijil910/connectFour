class Config:
    '''defines constants'''
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 700
    CENTER_X = SCREEN_WIDTH / 2
    CENTER_Y = SCREEN_HEIGHT / 2
    CHIP_EXTENT = 90
    CHIP_DISTANCE = 10
    BOARD_ROW_NUM = 7
    BOARD_COL_NUM = 7
    SIDE_COLOR = {'red': (255, 0, 0), 'yellow': (255, 255, 0)}
    BOARD_COLOR = (0, 0, 255)
    BACKGROUND_COLOR = (128, 128,
                        128)
    GAMEBOARD_HEIGHT = ((CHIP_EXTENT + CHIP_DISTANCE) * BOARD_ROW_NUM +
                        CHIP_DISTANCE) - (SCREEN_HEIGHT/BOARD_ROW_NUM)
    GAMEBOARD_WIDTH = ((CHIP_EXTENT + CHIP_DISTANCE) * BOARD_COL_NUM +
                       CHIP_DISTANCE)
    GAMEBOARD_LEFT_TOP = (CENTER_X - GAMEBOARD_WIDTH / 2,
                          CENTER_Y - GAMEBOARD_HEIGHT / 2)
    TOP_ROW = 0
    DROP_VELOCITY = 7
    AI_DEPTH = 5
    TEXT_SIZE = 60
    TEXT_X = CENTER_X/2
    TEXT_COLOR = (255, 128, 0)
    FILE_NAME = 'scores.txt'
    START_Y_POS = 50
