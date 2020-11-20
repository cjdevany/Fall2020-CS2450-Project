#-------------------------------------------------------------------
# game_window.py - Launches a game_window with a board in it.
#                  This class also has GUI widgets 
#
# Authors: Shadrac Reyes, Kelton Palmer, Kory Adams, Corey De Vany
#-------------------------------------------------------------------

import sys
from PyQt5 import QtWidgets, uic
from src.SudokuWindow import SudokuWindow

class Game_Window(QtWidgets.QMainWindow, SudokuWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(SudokuWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)        


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Game_Window()
    window.show()
    app.exec()
