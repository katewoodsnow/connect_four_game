class ConnectFour:

    # Initialise a new game grid
    def __init__(self, rows, columns, win_length):
        self.rows = rows
        self.columns = columns
        self.win_length = win_length
        self.grid = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.current_player = 'R'

    # returns the value
    def get_grid(self):
        return self.grid
