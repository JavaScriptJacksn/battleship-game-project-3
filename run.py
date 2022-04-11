def begin_game():
    """
    Begins new game, prints beginning message and asks for user name input
    """

    print("""
--------------------------------------------------------------------------------\n
TACTICAL SIMULATION TRAINER\n
TOP SECRET\n
--------------------------------------------------------------------------------\n
Welcome, operative.\n
Our great organisation is under a great threat,\n
with enemy ships approaching our\n
vessels positioned in the pacific ocean.\n
As you know, they guard a hidden treasure… The Lost City of Atlantis.\n
It is your mission to practise and perfect tactical ship placement\n
and offensive manuevers in this cutting-edge simulation.\n
Our livelyhoods rest on your shoulders.\n
Good Luck.
--------------------------------------------------------------------------------
""")

    name = input("To begin, enter your operative ID (name):\n")

    print(f"\nOperative {name}, your training begins.")


class Board:
    """
    Creates an instance of board
    """
    def __init__(self):
        self.size = 5  # Default size
        self.board = []
        self.print_board = ""
    
    def get_size(self):
        """
        Requests user for size of board
        """

        print("""
--------------------------------------------------------------------------------
Boards sizes are use as the length and\n
width of the board to make a square.\n
Please enter a board size between 5-9./\
""")

        temp_size = input("Please enter a board size:\n")

        # Validation of input
        while temp_size not in ["5", "6", "7", "8", "9"]:
            print("Invalid board size, please enter a value between 5-9:")
            temp_size = input()
    
        self.size = temp_size
        print(self.size)

    def build_board(self):
        """
        Builds the game board based on
        selected size
        """
        for i in range(int(self.size)):
            board_row = []
            for x in range(int(self.size)):
                board_row.append("-")
            self.board.append(board_row)

    def construct_print_board(self):
        """
        Converts the bord 3d array into a printable string.
        It also adds number axis values
        """
        board_str = ""
        board_str_x_axis = ""
        x_axis = "   "

        # x-axis construction
        for i in range(int(self.size)):
            x_axis += (f" {i +1} |")
        board_str_x_axis += (x_axis + "\n")
        # Adds x axis string to print_board string
        self.print_board += board_str_x_axis

        # y-axis and main board construction
        y_axis = 1
        for i in range(int(self.size)):
            row_str = ""
            row_str += f"{y_axis} | "
            for x in range(int(self.size)):
                row_str += (self.board[i][x] + " | ")

            # Checks to see if board is finished
            if y_axis == int(self.size):
                board_str += (row_str + "\n")
                self.print_board += board_str
            else:
                board_str += (row_str + "\n")
            y_axis += 1

    def check_for_ship(self, y_value, x_value):
        """
        Checks to see if ship is at coordinates
        """
        if self.board[int(y_value)][int(x_value)] == "#":
            return True

        return False

    def place_ships(self):
        """
        Generates the ships for each board and returns an array
        of each axis placements
        """
        number_of_ships = 5 if int(self.size) < 7 else 9
        print(f"Your avalible ships are: {number_of_ships}")

        user_ships_x = []
        user_ships_y = []

        for i in range(number_of_ships):

            used_location = True
            while used_location is True:

                # Gets y-axis placement
                print(f"Please enter the x coordinate of ship {i+1}\n")
                x_axis_placement = input()
                while x_axis_placement not in "123456789":
                    print(f"Please enter a value between 1-{self.size}")
                    x_axis_placement = input()

                # Gets y-axis placement
                print(f"Please enter the y coordinate of ship {i+1}\n")
                y_axis_placement = input()
                while y_axis_placement not in "123456789":
                    print(f"Please enter a value between 1-{self.size}")
                    y_axis_placement = input()

                # Validates chosen location which ends/starts the outer loop
                used_location = (self.check_for_ship(int(y_axis_placement)-1,
                                                     int(x_axis_placement)-1))

                if used_location is True:
                    print("Ship cannot be in the same place as another")

            user_ships_x.append(int(x_axis_placement))
            user_ships_y.append(int(y_axis_placement))
            print(f"ship x axis values {user_ships_x}")
            print(f"ship y axis values {user_ships_y}")
            self.update_board(x_axis_placement, y_axis_placement)

        return user_ships_x, user_ships_y

    def update_board(self, x_axis, y_axis):
        """
        Updates the board with the user ship placement
        The print board must be re-constructed to
        include new additions
        """
        for y_num, x_num in zip(y_axis, x_axis):
            self.board[int(y_num)-1][int(x_num)-1] = "#"


begin_game()
 
board = Board()
board.get_size()
board.build_board()
board.construct_print_board()
print("Here is your constructed board:")
print(getattr(board, "print_board"))
user_x, user_y = board.place_ships()
board.update_board(user_x, user_y)
board.construct_print_board()
print("Here is your constructed board:")
print(getattr(board, "print_board"))
