import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import pyqtSlot as Slot
from PyQt5.QtGui import QFont, QIcon, QImage
from PyQt5.QtWidgets import (
    QApplication,
    QDesktopWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QPushButton,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class TicTacToeUi(QWidget):
    """View Class for Tic-Tac-Toe"""

    def __init__(self, *args, **kwargs):
        """Initialize the Ui"""

        super().__init__(*args, **kwargs)

        self.createWindow(windowTitle="Tic-Tac-Toe", windowWidth=100, windowHeight=100)

        self.createWidgets()

        # Starts Window (must be called at the end of __init__)
        self.show()

    def createWindow(self, windowTitle: str, windowWidth: int, windowHeight: int) -> None:
        """Creates The Window"""

        def centerWindow(self: QWidget):

            """Centers the Window"""

            screenCenter = QDesktopWidget().screenGeometry().center()  # Center of The Monitor
            frameCenter = self.frameGeometry().center()  # Center of The Application Window

            # Move Application Window to Center of Monitor
            self.move(screenCenter.x() - frameCenter.x(), screenCenter.y() - frameCenter.y())

        self.setWindowTitle(windowTitle)

        self.setMinimumSize(windowWidth, windowHeight)
        centerWindow(self)

    def createWidgets(self):
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self._createButtons()

    def _createButtons(self):
        self.gameButtonsLayout = QGridLayout()
        # gameButtonSize = QSize()
        # gameButtonSize.setWidth(130)
        # gameButtonSize.setHeight(130)
        # gameButtonSize.scaled(130, 130, Qt.AspectRatioMode())

        self.gameButton00 = QPushButton()
        self.gameButton01 = QPushButton()
        self.gameButton02 = QPushButton()
        self.gameButton10 = QPushButton()
        self.gameButton11 = QPushButton()
        self.gameButton12 = QPushButton()
        self.gameButton20 = QPushButton()
        self.gameButton21 = QPushButton()
        self.gameButton22 = QPushButton()

        self.gameButton00.setFixedSize(130, 130)
        self.gameButton01.setFixedSize(130, 130)
        self.gameButton02.setFixedSize(130, 130)
        self.gameButton10.setFixedSize(130, 130)
        self.gameButton11.setFixedSize(130, 130)
        self.gameButton12.setFixedSize(130, 130)
        self.gameButton20.setFixedSize(130, 130)
        self.gameButton21.setFixedSize(130, 130)
        self.gameButton22.setFixedSize(130, 130)

        self.gameButtonsLayout.addWidget(self.gameButton00, 0, 0)
        self.gameButtonsLayout.addWidget(self.gameButton01, 0, 1)
        self.gameButtonsLayout.addWidget(self.gameButton02, 0, 2)
        self.gameButtonsLayout.addWidget(self.gameButton10, 1, 0)
        self.gameButtonsLayout.addWidget(self.gameButton11, 1, 1)
        self.gameButtonsLayout.addWidget(self.gameButton12, 1, 2)
        self.gameButtonsLayout.addWidget(self.gameButton20, 2, 0)
        self.gameButtonsLayout.addWidget(self.gameButton21, 2, 1)
        self.gameButtonsLayout.addWidget(self.gameButton22, 2, 2)

        self.mainLayout.addLayout(self.gameButtonsLayout)


def main():
    app = QApplication(sys.argv)
    view = TicTacToeUi()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
