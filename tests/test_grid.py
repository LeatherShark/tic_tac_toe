import sys

sys.path.append(r"C:\python_projects\tic_tac_toe")

import pytest
import numpy as np

import src.grid


@pytest.fixture
def gridFixture():
    mock_grid = src.grid.Grid()
    state = 0
    for row in range(3):
        for column in range(3):
            mock_grid.setStateAt(row, column, state)
            state += 1
    print(mock_grid.grid)
    return mock_grid

def test_grid(gridFixture: src.grid.Grid):
    mock_grid_2 = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
    print(mock_grid_2)
    assert np.array_equal(gridFixture.grid, mock_grid_2)
