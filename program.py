"""Program code"""

# David Barnes
# CIS 226
# 6-4-2023

# First-party imports
from droids import DroidCollection
from userinterface import UserInterface


def main(*args):
    """Method to run program"""

    # Create a new instance of droid collection
    droid_collection = DroidCollection()

    # Create a new instance of the user interface
    user_interface = UserInterface(droid_collection)

    # Display greeting to user
    user_interface.display_greeting()

    # Display main menu and get choice from user
    choice = user_interface.get_menu_choice(3, user_interface.display_main_menu)

    # While the choice is not 3 (exit)
    while choice < 3:
        # If 1, create droid
        if choice == 1:
            user_interface.create_droid()
        # Else if 2, print list
        elif choice == 2:
            user_interface.print_droid_list()
        # Re-prompt for input
        choice = user_interface.get_menu_choice(3, user_interface.display_main_menu)

    # Display exiting program message.
    user_interface.display_exit_message()
