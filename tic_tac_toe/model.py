import numpy as np
from random import randint

from tic_tac_toe.grid import Grid


class TicTacToeModel(Grid):
    """A class to represent a Tic-Tac-Toe Grid"""

    def __init__(self):
        super().__init__()
        self.X = 1
        self.O = -1

    def setStateX(self, row: int, column: int):
        """Sets X at Given Cell"""

        self.setStateAt(row=row, column=column, state=self.X)

    def setStateO(self, row: int, column: int):
        """Sets O at Given Cell"""

        self.setStateAt(row=row, column=column, state=self.O)

    def resetGrid(self):
        """Resets the Grid back to its initial state"""

        self.createGrid()

    def checkGridPopulated(self) -> bool:
        """Checks if the Grid is Fully Populated"""

        return np.all(self.grid != 0)

    def checkWinner(self):
        """Checks for Winner"""

        winDict = {
            "row-0": self.getRowStateAt(0).sum(),
            "row-1": self.getRowStateAt(1).sum(),
            "row-2": self.getRowStateAt(2).sum(),
            "column-0": self.getColumnStateAt(0).sum(),
            "column-1": self.getColumnStateAt(1).sum(),
            "column-2": self.getColumnStateAt(2).sum(),
            "diagonal-lr": self.getLeftRightDiagonal().sum(),
            "diagonal-rl": self.getRightLeftDiagonal().sum(),
        }

        if -3 in winDict.values() or 3 in winDict.values():
            print("Winner")

        print(f"{self.getRowStateAt(0).sum() = }")
        print(f"{self.getRowStateAt(1).sum() = }")
        print(f"{self.getRowStateAt(2).sum() = }")
        print(f"{self.getColumnStateAt(0).sum() = }")
        print(f"{self.getColumnStateAt(1).sum() = }")
        print(f"{self.getColumnStateAt(2).sum() = }")
        print(f"{self.getLeftRightDiagonal().sum() = }")
        print(f"{self.getRightLeftDiagonal().sum() = }")
        print(winDict)


testModel = TicTacToeModel()

print(testModel.grid)

for row in range(3):
    for column in range(3):

        randomState = randint(-1, 1)
        if randomState == 1:
            testModel.setStateX(row=row, column=column)
        elif randomState == -1:
            testModel.setStateO(row=row, column=column)
        # else:
        #     continue
        # testModel.setStateO(row=row, column=column)


print(testModel.grid)
print(testModel.checkWinner())
