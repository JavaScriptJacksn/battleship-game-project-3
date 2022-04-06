

def begin_game():
    """
    Begins new game, prints beginning message and asks for user name input
    """

    print("""
    ------------------------------------\n
    TACTICAL SIMULATION TRAINER\n
    TOP SECRET\n
    ------------------------------------\n
    Welcome, operative.\n
    Our great organisation is under a great threat,\n
    with enemy ships approaching our\n
    vessels positioned in the pacific ocean.\n
    As you know, they guard a hidden treasure… The Lost City of Atlantis.\n
    It is your mission to practise and perfect tactical ship placement\n
    and offensive manuevers in this cutting-edge simulation.\n
    Our livelyhoods rest on your shoulders.\n
    Good Luck.
    ------------------------------------
    """)

    name = input("To begin, enter your operative ID (name):\n")

    print(f"Operative {name}, your training begins.")


begin_game()
