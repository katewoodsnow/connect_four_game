class ConnectFour:

    # Initialise a new game grid
    def __init__(self, rows, columns, win_length):
        self.rows = rows
        self.columns = columns
        self.win_length = win_length
        # Ensure grid is empty
        self.grid = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.current_player = 'R'

    # Returns the value
    def get_grid(self):
        return self.grid

    # Add a token to the game grid
    def add_token(self, column, token):
        # Check to see if the column entered by the player is within the
        # grid bounds
        while True:
            if column < 0 or column >= self.columns:
                print("Invalid column index. Please enter a valid column index.")
            else:
                # Check row in reverse order as token drops to the bottom first
                for row in range(self.rows - 1, -1, -1):
                    # Check to see if cell is empty
                    if self.grid[row][column] == ' ':
                        self.grid[row][column] = token
                        # Token added successfully
                        return True
                print("Column is full. Please choose another column.")

    # Switches the player either red or yellow
    def switch_players(self):
        self.current_player = 'Y' if self.current_player == 'R' else 'R'

    # Return the string representation of the grid to show the state.
    def show_grid(self):
        for row in self.grid:
            print('|'.join(cell.center(3) if cell != ' ' else '   ' for cell in row))
            # Line to seperate cells
            print('-' * (self.columns * 3 - 1))

    # check the winner. Iterate through the game grid and check
    # for consecutive tokens in a row that equal win_length.
    def check_winner(self):
        # Check horizontally
        for row in range(self.rows):
            for col in range(self.columns - self.win_length + 1):
                if all(self.grid[row][col + i] == self.grid[row][col] != ' ' for i in range(1, self.win_length)):
                    return self.grid[row][col]

        # Check vertically
        for col in range(self.columns):
            for row in range(self.rows - self.win_length + 1):
                if all(self.grid[row + i][col] == self.grid[row][col] != ' ' for i in range(1, self.win_length)):
                    return self.grid[row][col]

        # Check diagonally (from bottom-left to top-right)
        for row in range(self.rows - self.win_length + 1):
            for col in range(self.columns - self.win_length + 1):
                if all(self.grid[row + i][col + i] == self.grid[row][col] != ' ' for i in range(1, self.win_length)):
                    return self.grid[row][col]

        # Check diagonally (from bottom-right to top-left)
        for row in range(self.win_length - 1, self.rows):
            for col in range(self.columns - self.win_length + 1):
                if all(self.grid[row - i][col + i] == self.grid[row][col] != ' ' for i in range(1, self.win_length)):
                    return self.grid[row][col]

        # If no winner is found, return None
        return None
