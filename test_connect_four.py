# Tests the methods behave as expected using TDD. If the assertion passes,
# it means the method is working correctly.

# Test for initializing the game grid and that it is empty of tokens
def test_initialization():
    game = ConnectFour(rows=6, columns=7, win_length=4)
    assert game.rows == 6
    assert game.columns == 7
    assert game.win_length == 4
    assert game.current_player == 'R'
    assert game.grid == [[' ' for _ in range(7)] for _ in range(6)]

