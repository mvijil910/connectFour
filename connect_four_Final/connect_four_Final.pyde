'''name: Marcela Vijil
github repo:
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-MarcelaVijil'''

from config import Config
from game_controller import GameController


game_controller = GameController()


def setup():
    '''sets screen size'''
    size(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)


def draw():
    '''draws game board and chips, checks if computer turn, 
    and displays the board with the user updates'''
    background(*Config.BACKGROUND_COLOR)
    if game_controller.show_input_box == 1:
        ask_winners_name()
        noLoop()
    check_computer_turn()
    game_controller.update()


def mouseDragged():
    '''handles the chip drag functionality'''
    game_controller.handle_mouse_pressed(False, True, False, mouseX)


def mouseReleased():
    '''drops the chips once mouse released'''
    game_controller.handle_mouse_pressed(False, False, True, mouseX)


def mousePressed():
    '''makes chip appear once mouse is pressed, on top row'''
    game_controller.handle_mouse_pressed(True, False, False, mouseX)


def check_computer_turn():
    '''checks to see if it is the ai\'s turn'''
    game_controller.check_computer_turn()


def ask_winners_name():
    '''prompts the user to enter their name if they've won'''
    if game_controller.show_input_box == 1:
        answer = input('enter your name')
        if answer:
            game_controller.handle_score_keeping(answer, Config.FILE_NAME)
        elif answer == '':
            answer = input('you must enter your name or cancel')
        else:
            return


def input(message=''):
    '''allows for the user input'''
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
