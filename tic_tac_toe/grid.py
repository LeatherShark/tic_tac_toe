import numpy as np


class SetStateError(Exception):
    """Raised for State that has already been assigned."""


class Grid:
    """Representation of a Grid for Board Game."""

    def __init__(self):
        """Initialize the Grid."""

        self.createGrid()

    def createGrid(self):
        """Creates the Grid"""

        self.grid = np.zeros(shape=(3, 3), dtype="i4")

    def getStateAt(self, row: int, column: int) -> int:
        """Returns the State at given cell."""

        return self.grid[row, column]

    def setStateAt(self, row: int, column: int, state: int) -> None:
        """Sets the State at given cell."""

        self.grid[row, column] = state

    def getGridState(self) -> np.ndarray:
        """Returns Grid."""

        return self.grid

    def getRowStateAt(self, row: int) -> np.ndarray:
        """Returns State at given row."""

        return self.grid[row, :]

    def getColumnStateAt(self, column: int) -> np.ndarray:
        """Returns State at given column."""

        return self.grid[:, column]

    def getLeftRightDiagonal(self) -> np.ndarray:
        """Returns State at Left-Right Diagonal."""

        return np.diagonal(self.grid)

    def getRightLeftDiagonal(self) -> np.ndarray:
        """Returns State at Right-Left Diagonal."""

        return np.diagonal(np.fliplr(self.grid))
