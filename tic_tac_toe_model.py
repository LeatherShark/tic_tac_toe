import numpy as np


class SetStateError(Exception):
    """Raised for State that has already been assigned."""


class TicTacToeGrid:
    """Representation of a Tic-Tac-Toe Grid"""

    def __init__(self):
        """Initialize the Grid"""

        self.grid = np.array(
            [{"x": x, "y": y, "state": 0} for x in range(3) for y in range(3)]
        ).reshape(3, 3)

    def getStateAt(self, xCoord: int, yCoord: int) -> int:
        """Return the State of the Cell"""

        return self.grid[xCoord][yCoord]["state"]

    def setStateAt(self, xCoord: int, yCoord: int, state: int):
        """Sets the State at Cell"""

        # Checks if State is Unassigned
        if self.getStateAt(xCoord, yCoord) != 0:
            raise SetStateError("Cannot Assign State to a Cell twice.")

        self.grid[xCoord][yCoord]["state"] = state

    def getStateGrid(self):
        """Returns Grid of States"""

        return np.array(
            [self.getStateAt(xCoord=x, yCoord=y) for x in range(3) for y in range(3)]
        ).reshape(3, 3)


testGrid = TicTacToeGrid()

print(testGrid.grid)
testGrid.setStateAt(0, 0, 1)
testGrid.setStateAt(0, 0, 1)
print(testGrid.getStateGrid())
