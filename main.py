# ----- Standard
import sys
import os
# ----- External
from PyQt5 import QtCore, QtGui, QtWidgets
# ----- Internal
from mvc.views.core import MainWindow
from stylesheets import master_stylesheet


# rgb(181, 209, 42)


class TicTacToeApp(QtWidgets.QApplication):

    def __init__(self, args):
        super().__init__(args)

        self.window = MainWindow()
        self.window.setStyleSheet(master_stylesheet)
        self.window.show()

        self.exec_()  # enter event loop


if __name__ == '__main__':
    app = TicTacToeApp(sys.argv)
