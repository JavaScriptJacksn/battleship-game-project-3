import random


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

    # Initial setup of boards and ships
    game_board_size = get_size()
    player_board = Board(game_board_size)
    player_board.build_board()
    player_board.construct_print_board()
    print("Game board:")
    print(getattr(player_board, "print_board"))
    player_board.place_ships()

    computer_board = Board(game_board_size)
    computer_board.build_board()
    computer_board.place_random_ships()
    computer_board.construct_print_board()

    # Main gameplay loop until victory
    while (player_board.number_of_ships != 0 and
           computer_board.number_of_ships != 0):
        new_round(player_board, computer_board)

    # Checks for winner
    if (player_board.number_of_ships == 0 and
       computer_board.number_of_ships != 0):
        print("You Lost!\n Training ceased.")

    elif (player_board.number_of_ships != 0 and
          computer_board.number_of_ships == 0):
        print(f"You Won!\n Training ceased.\n Good work operative {name}")

    else:
        print("""
It's a draw! \n Training ceased.\n at least you took them down with you...
""")


def new_round(player_board, computer_board):
    """
    Starts a new round, checking for hit or miss
    and updates the board giving feedback to the user
    """
    print_round(player_board, computer_board)
    user_guess_x, user_guess_y = get_guess()
    hit = computer_board.check_for_ship(user_guess_x, user_guess_y)
    if hit is True:
        computer_board.update_board(user_guess_x, user_guess_y, "X")
        print("Hit!")
        computer_board.number_of_ships -= 1
        print(f"Your enemy has {computer_board.number_of_ships} ships left.")
    else:
        print("Miss!")
        computer_board.update_board(user_guess_x, user_guess_y, "O")
        print(f"Your enemy has {computer_board.number_of_ships} ships left.")
    player_board.construct_print_board()
    computer_board.construct_print_board()


def print_round(player_board, computer_board):
    """
    Prints each round boards
    """
    print("""
--------------------------------------------------------------------------------
Enemy board:
--------------------------------------------------------------------------------
    """)
    print(getattr(computer_board, "print_board"))

    print("""
--------------------------------------------------------------------------------
Your final board:
--------------------------------------------------------------------------------
    """)
    print(getattr(player_board, "print_board"))


def get_size():
    """
    Requests user for size of board
    """

    print("""
--------------------------------------------------------------------------------
Boards sizes are use as the length and\n
width of the board to make a square.\n
Please enter a board size between 5-9./\
""")

    size = int(input("Please enter a board size:\n"))

    # Validation of input
    while size not in [5, 6, 7, 8, 9]:
        print("Invalid board size, please enter a value between 5-9:")
        size = input()
    print(size)
    return size


def get_guess():
    """
    Gets the coordinates of users guess
    """
    print("Enter coordinates to attack.")
    x_guess = input("X coordinate of guess:")
    y_guess = input("Y coordinate of guess:")

    return (x_guess, y_guess)


class Board():
    """
    Creates an instance of board
    """
    def __init__(self, size):
        self.size = size  # Default size
        self.number_of_ships = 5  # Default number
        self.board = []
        self.print_board = ""
        self.ship_locations_x = []
        self.ship_locations_y = []

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
        It begins by setting the board to an empty string as
        to not add boards together
        """
        self.print_board = ""
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

    def check_for_ship(self, x_value, y_value):
        """
        Checks to see if ship is at coordinates
        """
        for x, y in zip(self.ship_locations_x, self.ship_locations_y):
            if (int(x_value) == x and int(y_value) == y):
                return True

        return False

    def place_ships(self):
        """
        Generates the ships for each board and returns an array
        of each axis placements
        """
        self.number_of_ships = 5 if int(self.size) < 7 else 9
        print(f"Your avalible ships are: {self.number_of_ships}")

        user_ships_x = []
        user_ships_y = []

        for i in range(self.number_of_ships):

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
                used_location = (self.check_for_ship(int(x_axis_placement),
                                 int(y_axis_placement)))

                if used_location is True:
                    print("Ship cannot be in the same place as another")

            user_ships_x.append(int(x_axis_placement))
            user_ships_y.append(int(y_axis_placement))
            self.ship_locations_x = user_ships_x
            self.ship_locations_y = user_ships_y

            self.update_board(x_axis_placement, y_axis_placement, "#")
            self.construct_print_board()
            print("----------------------------------------------" +
                  "----------------------------------")
            print("Ship placed.")
            print("----------------------------------------------" +
                  "----------------------------------")
            print(self.print_board)

    def place_random_ships(self):
        """
        Randomly assigns ship locations to object
        For use only with computer board
        Random ranges start from 1 as
        indexing in update board function minuses 1
        """
        for i in range(self.size):
            rand_x = random.randint(1, int(self.size))
            rand_y = random.randint(1, int(self.size))
            while self.check_for_ship(rand_y, rand_x) is True:
                rand_x = random.randint(1, int(self.size))
                rand_y = random.randint(1, int(self.size))
            self.ship_locations_x.append(rand_x)
            self.ship_locations_y.append(rand_y)
        print(self.ship_locations_x)
        print(self.ship_locations_y)

    def update_board(self, x_axis, y_axis, icon):
        """
        Updates the board with icon passed as argument
        The print board must be re-constructed to
        include new additions
        """
        for y_num, x_num in zip(y_axis, x_axis):
            self.board[int(y_num)-1][int(x_num)-1] = icon


begin_game()
