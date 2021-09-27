import numpy as np
from random import choice


class SetStateError(Exception):
    """Raised for State that has already been assigned."""


class Grid:
    """Representation of a Grid for Board Game."""

    def __init__(self):
        """Initialize the Grid."""

        self.grid = np.array(
            [{"row": row, "column": column, "state": 0} for row in range(3) for column in range(3)]
        ).reshape(3, 3)

    def getStateAt(self, row: int, column: int) -> int:
        """Returns State of Cell."""

        return self.grid[row][column]["state"]

    def setStateAt(self, row: int, column: int, state: int) -> None:
        """Sets State at Cell."""

        # Checks if State is Unassigned
        if self.getStateAt(row, column) != 0:
            raise SetStateError("Cannot Assign State to a Cell twice.")

        self.grid[row][column]["state"] = state

    def getStateGrid(self):
        """Returns Grid of States."""

        return np.array(
            [self.getStateAt(row=row, column=column) for row in range(3) for column in range(3)]
        ).reshape(3, 3)

    def getStateColumn(self, column: int):
        """Returns a numpy array of States of the given column."""

        # return self.grid

        # return np.array(
        #     [self.getStateAt(row=row, column=column) for row in range(3)]
        # ).reshape(3, 1)

    def getStateRow(self, row: int):
        """Returns a numpy array of States of the given row."""

        return np.array(
            [self.getStateAt(row=row, column=column) for column in range(3)]
        ).reshape(1, 3)
    
    def getStateLeftRightDiagonal(self):
        """Returns a numpy array of States of the Left-Right Diagonal"""
        print("Hello")
        return self.grid.diagonal(-1, 0, 1)

        # return np.array([
        #     self.getStateAt(row=0, column=0),
        #     self.getStateAt(row=1, column=1),
        #     self.getStateAt(row=2, column=2)
        # ]).reshape(3, 1)
        

    def getStateRightLeftDiagonal(self):
        """Returns a numpy array of States of the Right-Left Diagonal"""

        return np.array([
            self.getStateAt(row=0, column=2),
            self.getStateAt(row=1, column=1),
            self.getStateAt(row=2, column=0)
        ]).reshape(3, 1)


def tests():
    testGrid = Grid()

    print(testGrid.grid)
    for xCoord in range(3):
        for yCoord in range(3):
            randomState = choice([-1, 1, 0])
            print(f"{randomState:.0f} at row {xCoord}, column {yCoord}")
            testGrid.setStateAt(xCoord, yCoord, randomState)
            # print(testGrid.getStateGrid())
    # testGrid.setStateAt(0, 0, 1)
    print(testGrid.getStateGrid())

    print(testGrid.getStateColumn(0))
    print(testGrid.getStateColumn(1))
    print(testGrid.getStateColumn(2))

    print(testGrid.getStateRow(0))
    print(testGrid.getStateRow(1))
    print(testGrid.getStateRow(2))

    print(testGrid.getStateLeftRightDiagonal())
    print(testGrid.getStateRightLeftDiagonal())


if __name__ == "__main__":
    tests()