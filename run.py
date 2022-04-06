

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
        self.size = 10  # Default size
    
    def get_size(self):
        """
        Requests user for size of board
        """

        print("""
--------------------------------------------------------------------------------
Boards sizes are use as the length and\n
width of the board to make a square.\n
Please enter a board size between 10-15./\
""")

        temp_size = input("Please enter a board size:\n")

        # Validation of input
        while temp_size not in ["10", "11", "12", "13", "14", "15"]:
            print("Invalid board size, please enter a value between 10-15:")
            temp_size = input()
        
        self.size = temp_size
        print(self.size)


begin_game()

board = Board()
board.get_size()
