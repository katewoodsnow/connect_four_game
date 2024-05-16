# Import the methods from the connect_four file
from connect_four import ConnectFour, configure_game


def main():
    # Configure the game
    rows, cols, win_length = configure_game()

    # Initialize new game grid
    game = ConnectFour(rows, cols, win_length)

    while True:
        # Show player to play
        print(f"Current player: {game.get_current_player()}")
        # Show grid
        game.show_grid()
        # Add token to the game grid.
        # Try catch to check a valid values are entered
        try:
            col = int(input("Enter column to place token: "))
            # Check column is within the grid
            if 0 <= col < cols:
                # Add token of the current player
                if game.add_token(col, game.get_current_player()):
                    # Check if this move wins
                    winner = game.check_winner()
                    if winner:
                        print(f"Player {winner} wins!")
                        break  # Exit the loop if a player wins
                    # If not win, switch to other player
                    game.switch_players()
                else:
                    print("Invalid move. Please choose another column.")
            else:
                print("Invalid column index. Please enter a valid column index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for column index.")
    # Show final state of the grid
    game.show_grid()


if __name__ == "__main__":
    main()
