# ======================================================================================================================
#                                           MASTER STYLESHEET
#
#       The following stylesheets are concatenated into one master stylesheet and applied at the
#       top level of the app. Due to some styles failing to propagate properly or being overridden,
#       there also exist EXPLICIT STYLESHEETS that are to be applied directly wherever the master
#       sheet fails.
#
# ======================================================================================================================

MainWindow_stylesheet = """

MainWindow {
    background-color: #494550;
    min-width: 400px;
    min-height: 400px;
    max-width: 650px;
    max-height: 650px;
}

MainWindow QMenuBar {
    background-color: #2D2B31;
}

MainWindow QToolBar {
    background-color: #36343B;
    border-left: 0;
    border-right: 0;
    border-top: 1px;
    border-botton: 1px;
    border-color: black;
}

"""

TicTacToe_stylesheet = """

TicTacToeSquares QPushButton {
    background-color: #3F3C45;
    border: 1px solid #FF5B4C;
}

TicTacToeSquares QPushButton::hover {
    /* background-color: #937373; */
    background-color: #4F434D;
}

"""

master_stylesheet = MainWindow_stylesheet + TicTacToe_stylesheet

# ======================================================================================================================
#                                           EXPLICIT STYLESHEETS
#
#       Some styles from the MASTER STYLESHEET fail to propagate or get overridden, so the following
#       stylesheets are meant to be used directly inside the code in situations where putting the style
#       in the master sheet does not work. For the sake of easy styling, absolutely every stylesheet is
#       in this file.
#
# ======================================================================================================================

direct_stylesheet1 = """
    background-color: #FF5B4C;
"""
