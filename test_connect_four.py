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


# Test switch player method
def test_alternate_players():
    game = ConnectFour(6, 7)
    assert game.get_current_player() == 'R'
    game.add_token(0, 'R')
    assert game.get_current_player() == 'Y'
    game.add_token(1, 'Y')
    assert game.get_current_player() == 'R'

# Checks if the show_grid method returns the expected string representation
# of the grid.
def test_show_grid():
    game = ConnectFour(6, 7)
    game.add_token(0, 'R')
    game.add_token(1, 'Y')
    grid_state = game.show_grid()
    assert grid_state == ("\n"
                          " \n"
                          "\n"
                          "\n"
                          "\n"
                          "RY")
def test_winner_horizontal():
    game = ConnectFour(rows=6, columns=7, win_length=4)
    for col in range(4):
        game.add_token(col, 'R')
    assert game.check_winner() == 'R'

if __name__ == "__main__":
    test_initialization()
    test_add_token()
    test_show_grid()
    test_alternate_players()
    test_winner_horizontal()
    print("All tests passed.")
