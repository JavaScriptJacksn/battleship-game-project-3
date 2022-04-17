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
Our great organisation is under a great threat,
with enemy ships approaching our
vessels positioned in the pacific ocean.\n
As you know, they guard a hidden treasure… The Lost City of Atlantis.\n
It is your mission to practise and perfect tactical ship placement
and offensive manuevers in this cutting-edge simulation.\n
Our livelyhoods rest on your shoulders.\n
Note: Games last until the final ship is hit, game length/difficulty
scales with the size of board.\n
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
    print("""
--------------------------------------------------------------------------------\n
""")
    print("Your board:")
    print(getattr(player_board, "print_board"))
    player_board.place_ships()

    computer_board = Board(game_board_size)
    computer_board.build_board()
    computer_board.place_random_ships()
    computer_board.construct_print_board()

    # Main gameplay loop until victory
    while (player_board.number_of_ships != 0 and
           computer_board.number_of_ships != 0):
        new_round(player_board, computer_board, game_board_size)

    # Checks for winner
    if (player_board.number_of_ships == 0 and
       computer_board.number_of_ships != 0):
        print("You Lost!\nTraining ceased.")

    elif (player_board.number_of_ships != 0 and
          computer_board.number_of_ships == 0):
        print(f"You Won!\nTraining ceased.\nGood work operative {name}")

    else:
        print("""
It's a draw! \n Training ceased.\n at least you took them down with you...
""")

    print("Do you wish to play again?\n")
    play_again = " "
    while play_again not in "YyNn":
        play_again = input("Please enter a Y or N: \n")
    if play_again in "Nn":
        print("Battleship training simuation finished.")
    else:
        begin_game()


def new_round(player_board, computer_board, board_size):
    """
    Starts a new round, checking for hit or miss
    and updates the board giving feedback to the user
    """
    print("----------------------------------------------" +
          "----------------------------------")
    print("Do you wish to continue?\n")
    continue_round = " "
    while continue_round not in "YyNn":
        continue_round = input("Please enter a Y or N: \n")
        if continue_round in "Nn":
            print("Battleship training simuation finished.")
            exit()
        else:
            print("\n\n\n\n\n")

    print_round(player_board, computer_board)
    user_guess_x, user_guess_y = get_guess(computer_board, board_size)
    hit = computer_board.check_for_ship(user_guess_x, user_guess_y)

    # Player  turn
    if hit is True:
        computer_board.update_board(user_guess_x, user_guess_y, "X")
        print("---------------------------------" +
              "-----------------------------------------------")
        print("Hit!")
        computer_board.number_of_ships -= 1
    else:
        print("---------------------------------" +
              "-----------------------------------------------")
        print("Miss!")
        computer_board.update_board(user_guess_x, user_guess_y, "O")
    print(f"Your enemy has {computer_board.number_of_ships} ships left.")

    # Computer turn
    computer_guess_x, computer_guess_y = computer_guess(computer_board,
                                                        board_size)
    hit = player_board.check_for_ship(computer_guess_x, computer_guess_y)
    if hit is True:
        player_board.update_board(computer_guess_x, computer_guess_y, "X")
        print("The enemy hit your ship!")
        player_board.number_of_ships -= 1
    else:
        print("The enemy missed your ship!")
        player_board.update_board(computer_guess_x, computer_guess_y, "O")
    print(f"You have {player_board.number_of_ships} ships left.\n")
    player_board.construct_print_board()
    computer_board.construct_print_board()


def print_round(player_board, computer_board):
    """
    Prints each round boards
    """
    print("\n\n\n\n\n")
    print("----------------------------------------------" +
          "----------------------------------")
    print("Enemy board:\n" + (getattr(computer_board, "print_board")))

    print("Your board:\n" + (getattr(player_board, "print_board")))


def get_size():
    """
    Requests user for size of board
    """

    print("""
--------------------------------------------------------------------------------
Please enter a Board size between 5-9.

Note: Boards sizes are used as the length and\n
width of the board to make a square.
Games with larger board sizes have more ships.
These larger size games will take longer to finish
--------------------------------------------------------------------------------\n
""")
    size = 0
    while size not in [5, 6, 7, 8, 9]:
        print("Please enter a value between 5-9:")
        try:
            size = int(input())
        except ValueError:
            print("Board size must be a number.\n")
    return size


def get_guess(board, board_size):
    """
    Gets the coordinates of users guess
    """
    print("Enter coordinates to attack.")
    x_guess = "0"
    y_guess = "0"

    used_position = True
    # Passed computer board to check if position already guessed
    while used_position is True:

        # X guess
        x_guess = 0
        while x_guess not in range(1, board_size+1):
            print(f"Please enter a value between 1 - {board_size}")
            try:
                x_guess = int(input("X coordinate of guess:\n"))
            except ValueError:
                print("Please enter a number.")

        # Y guess
        while y_guess not in range(1, board_size+1):
            print(f"Please enter a value between 1 - {board_size}")
            try:
                y_guess = int(input("Y coordinate of guess:\n"))
            except ValueError:
                print("Please enter a number.")

        used_position = board.check_used_position(x_guess, y_guess)

        if used_position is True:
            print("\nYou cannot attack the same location twice!")

    return str(x_guess), str(y_guess)


def computer_guess(board, board_size):
    """
    Returns random y and x axis values
    """
    x_value = random.randint(1, board_size)
    y_value = random.randint(1, board_size)
    # Passed player board to check if position already guessed
    while board.check_used_position(x_value, y_value):
        x_value = random.randint(1, board_size)
        y_value = random.randint(1, board_size)
    return x_value, y_value


class Board():
    """
    Creates an instance of board
    """
    def __init__(self, size):
        self.size = size  # Default size
        self.number_of_ships = 5  # Default number
        self.board = []
        self.print_board = ""
        self.ship_locations = []

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
        Checks to see if ship is at coordinates,
        separate from check position function as the computer board
        does not store ships on the board itself
        """
        if [str(x_value), str(y_value)] in self.ship_locations:
            return True
        return False

    def place_ships(self):
        """
        Generates the ships for each board and returns an array
        of each axis placements
        """
        self.number_of_ships = 5 if int(self.size) < 7 else 9
        print(f"Your avalible ships are: {self.number_of_ships}")

        for i in range(self.number_of_ships):

            used_location = True
            while used_location is True:

                x_axis_placement = "0"
                y_axis_placement = "0"

                # Validates x input to be between 1-board size
                while int(x_axis_placement) not in range(1, int(self.size)+1):
                    try:
                        # Gets x-axis placement
                        # Uses str, int to prompt exception
                        print(f"Please enter the x coordinate of ship {i+1}\n")
                        x_axis_placement = str(int(input()))
                    except ValueError:
                        print(f"Please enter a value between 1-{self.size}")

                # Validates y input to be between 1-board size
                while int(y_axis_placement) not in range(1, int(self.size)+1):
                    try:
                        # Gets y-axis placement
                        # Uses str, int to prompt exception
                        print(f"Please enter the y coordinate of ship {i+1}\n")
                        y_axis_placement = str(int(input()))
                    except ValueError:
                        print(f"Please enter a value between 1-{self.size}")
                # Validates y input to be between 1-board size

                # Validates chosen location which ends/starts the outer loop
                used_location = (self.check_for_ship(int(x_axis_placement),
                                 int(y_axis_placement)))

                if used_location is True:
                    print("Ship cannot be in the same place as another")

            self.ship_locations.append([x_axis_placement, y_axis_placement])

            self.update_board(x_axis_placement, y_axis_placement, "#")
            self.construct_print_board()
            print("\n\n\n\n\n")
            print("----------------------------------------------" +
                  "----------------------------------")
            print("Ship placed. Your current board:\n")
            print(self.print_board)

    def place_random_ships(self):
        """
        Randomly assigns ship locations to object
        For use only with computer board
        Random ranges start from 1 as
        indexing in update board function minuses 1
        """
        for i in range(self.size):
            used_position = True
            while used_position is True:
                rand_x = random.randint(1, int(self.size))
                rand_y = random.randint(1, int(self.size))
                used_position = self.check_for_ship(rand_x, rand_y)
            self.ship_locations.append([str(rand_x), str(rand_y)])

    def update_board(self, x_axis, y_axis, icon):
        """
        Updates the board with icon passed as argument
        The print board must be re-constructed to
        include new additions
        """
        self.board[int(y_axis)-1][int(x_axis)-1] = icon

    def check_used_position(self, x_axis, y_axis):
        """
        Function to check if the actual position on the board
        data structure is occupied by X or O
        """
        if self.board[int(y_axis)-1][int(x_axis)-1] != ("-" or "#"):
            return True
        else:
            return False


begin_game()
