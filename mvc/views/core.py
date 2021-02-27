# ----- Standard
import os
# ----- External
from PyQt5 import QtCore, QtGui, QtWidgets
# ----- Internal
from mvc.views.game import TicTacToeSquares
from stylesheets import direct_stylesheet1


class MainWindow(QtWidgets.QMainWindow):

    # Paths
    # ------------------------------
    resources_path = "." + os.path.sep + "resources" + os.path.sep
    icon_name = "icon.png"

    # Configs
    # ------------------------------
    w = 500
    h = 500
    flags = QtCore.Qt.WindowFlags(
        QtCore.Qt.WindowCloseButtonHint
        | QtCore.Qt.WindowMinimizeButtonHint
        | QtCore.Qt.MSWindowsFixedSizeDialogHint
    )

    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== Setup Window =====
        self.setWindowTitle("Tic Tac Toe!")
        self.setWindowIcon(QtGui.QIcon(self.resources_path + self.icon_name))
        self.setWindowFlags(self.flags)
        self.setGeometry(100, 100, self.w, self.h)

        # ===== Init Menus and Tabs =====
        self._init_menu()
        self._init_tool_bar()
        self._init_status_bar()

        # ===== Init Widgets =====
        self._init_widgets()
        self.central_widget = QtWidgets.QWidget(parent=self)

        # ===== Init layout =====
        self.main_lout = QtWidgets.QVBoxLayout()
        self.hbox_lout = QtWidgets.QHBoxLayout()
        self.main_lout.addLayout(self.hbox_lout, QtCore.Qt.AlignVCenter)
        self.hbox_lout.addWidget(TicTacToeSquares(parent=self.central_widget), QtCore.Qt.AlignHCenter)

        # This needs to happen after the layouting
        self.central_widget.setLayout(self.main_lout)
        self.setCentralWidget(self.central_widget)

    def _init_menu(self):
        # menuBar() returns the menu of the MainWindow
        self.menu = self.menuBar().addMenu('&Menu')
        self.menu.addAction('&Exit', self.close)

    def _init_tool_bar(self):
        tools = QtWidgets.QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _init_status_bar(self):
        status = QtWidgets.QStatusBar()
        status.showMessage("I'm the Status Bar")
        status.setStyleSheet(direct_stylesheet1)
        self.setStatusBar(status)

    def _init_widgets(self):
        pass
