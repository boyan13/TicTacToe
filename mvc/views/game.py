# ----- Standard
import os
# ----- External
from PyQt5 import QtCore, QtGui, QtWidgets


class TicTacToeSquares(QtWidgets.QWidget):

    def __init__(self, parent=None, square_size=100, border_size=1):
        super().__init__(parent)
        self.setFixedSize(square_size * 3 + border_size * 2 * 3, square_size * 3 + border_size * 2 * 3)

        # ===== Init Widgets =====
        self.squares = [[None for x in range(3)] for y in range(3)]

        for i in range(3):
            for j in range(3):
                btn = QtWidgets.QPushButton()
                btn.setFixedSize(square_size, square_size)
                self.squares[i][j] = btn

        # ===== Init Layout =====
        self.main_lout = QtWidgets.QGridLayout()

        for i in range(3):
            for j in range(3):
                self.main_lout.addWidget(self.squares[i][j], i, j, QtCore.Qt.AlignCenter)

        self.setLayout(self.main_lout)
