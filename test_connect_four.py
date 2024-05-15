# Tests the methods behave as expected using TDD. If the assertion passes,
# it means the method is working correctly.

# Import class and methods from implement file
from connect_four import ConnectFour

# Test for initializing the game grid and that it is empty of tokens
def test_initialization():
    game = ConnectFour(rows=6, columns=7, win_length=4)
    assert game.rows == 6
    assert game.columns == 7
    assert game.win_length == 4
    assert game.current_player == 'R'
    assert game.grid == [[' ' for _ in range(7)] for _ in range(6)]

# Test add token function by adding values.
def test_add_token():
    game = ConnectFour(rows=6, cols=7, win_length=4)
    # Don't need to specify row as can only go to last row
    assert game.add_token(0, 'R')
    grid = game.get_grid()
    # Ensures token is bottom row
    assert grid[5][0] == 'R'
