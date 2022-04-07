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
        print(self.board)
    
    def construct_print_board(self):
        """
        Converts the bord 3d array into a printable string.
        It also adds number axis values
        """
        board_str = ""
        y_axis = 1
        for i in range(int(self.size)):
            row_str = ""
            row_str += f"{y_axis} | "
            for x in range(int(self.size)):
                row_str += (self.board[i][x] + " | ")
            print(row_str)
            y_axis += 1
        if len(board_str) == self.size:  # Checks to see if board is finished
            self.print_board = board_str
        else:
            board_str += (row_str + "\n")


begin_game()

board = Board()
board.get_size()
board.build_board()
board.construct_print_board()
print(board.print_board)
