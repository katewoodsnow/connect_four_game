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
                for row in range(self.rows - 1, -1, -1):
                    # Check to see if cell is empty
                    if self.grid[row][column] == ' ':
                        self.grid[row][column] = token
                        return True  # Token added successfully
                print("Column is full. Please choose another column.")
