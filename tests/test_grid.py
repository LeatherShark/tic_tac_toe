import sys

sys.path.append(r"C:\python_projects\tic_tac_toe")

import numpy as np
import pytest

from src.grid import *


@pytest.fixture
def mockGrid():
    """
    Creates Mock Grid:
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    """
    mock_grid = Grid()
    state = 0
    for row in range(3):
        for column in range(3):
            mock_grid.setStateAt(row, column, state)
            state += 1

    return mock_grid


def test_getStateAt(mockGrid: Grid):
    """Tests Grid.getStateAt"""

    state = 0
    for row in range(3):
        for column in range(3):

            assert mockGrid.getStateAt(row=row, column=column) == state

            state += 1


def test_getGridState(mockGrid: Grid):
    """Tests Grid.getGridState"""

    mockGrid2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    assert np.array_equal(mockGrid.getGridState(), mockGrid2)


def test_getRowStateAt(mockGrid: Grid):
    """Test Grid.getRowStateAt"""

    mockRow = np.array([0, 1, 2])
    assert np.array_equal(mockGrid.getRowStateAt(row=0), mockRow)

    mockRow = np.array([3, 4, 5])
    assert np.array_equal(mockGrid.getRowStateAt(row=1), mockRow)

    mockRow = np.array([6, 7, 8])
    assert np.array_equal(mockGrid.getRowStateAt(row=2), mockRow)


def test_getColumnStateAt(mockGrid: Grid):
    """Tests Grid.getColumnStateAt"""

    mockColumn = np.array([0, 3, 6])
    assert np.array_equal(mockGrid.getColumnStateAt(column=0), mockColumn)

    mockColumn = np.array([1, 4, 7])
    assert np.array_equal(mockGrid.getColumnStateAt(column=1), mockColumn)

    mockColumn = np.array([2, 5, 8])
    assert np.array_equal(mockGrid.getColumnStateAt(column=2), mockColumn)


def test_getLeftRightDiagonal(mockGrid: Grid):
    """Tests Grid.getLeftRightDiagonal"""

    mockLeftRightDiagonal = np.array([0, 4, 8])
    assert np.array_equal(mockGrid.getLeftRightDiagonal(), mockLeftRightDiagonal)



def test_getRightLeftDiagonal(mockGrid: Grid):
    """Tests Grid.getRightLeftDiagonal"""

    mockRightLeftDiagonal = np.array([2, 4, 6])
    assert np.array_equal(mockGrid.getRightLeftDiagonal(), mockRightLeftDiagonal)
    