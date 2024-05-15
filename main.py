
def configure_game():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            win_length = int(input("Enter winning row length: "))

            if min(rows, cols) >= win_length > 0:
                return rows, cols, win_length
            else:
                print("Invalid winning row length. Please choose a length less than or equal to the minimum of rows "
                      "and columns.")
        except ValueError:
            print('Invalid input. Please enter valid integers.')
