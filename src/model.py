from src.grid import Grid


class TicTacToeModel(Grid):
    """A class to represent a Tic-Tac-Toe Grid"""

    def __init__(self):
        super().__init__()
        self.X = 1
        self.O = -1

    def setStateX(self, row: int, column: int):
        """Sets X at Given Cell"""

        self.setStateAt(row=row, column=column, state=self.X)

    def setState0(self, row: int, column: int):
        """Sets O at Given Cell"""

        self.setStateAt(row=row, column=column, state=self.O)

    def resetGrid(self):
        """Resets the Grid back to its initial state"""

        self.createGrid()
