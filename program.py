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

    # Load default droids to make testing easier
    droid_collection.load_default_droids()

    # Create a new instance of the user interface
    user_interface = UserInterface(droid_collection)

    # Display greeting to user
    user_interface.display_greeting()

    # Display main menu and get choice from user
    choice = user_interface.get_menu_choice(5, user_interface.display_main_menu)

    # While the choice is not 3 (exit)
    while choice < 5:
        # If 1, create droid
        if choice == 1:
            user_interface.create_droid()
        # Else if 2, print list
        elif choice == 2:
            user_interface.print_droid_list()
        # Else if 3, sort into categories
        elif choice == 3:
            droid_collection.sort_into_categories()
            user_interface.display_sort_into_categories_success_message()
        # Else if 4, sort by total cost
        elif choice == 4:
            droid_collection.sort_by_total_cost()
            user_interface.display_sort_by_total_cost_success_message()
        # Re-prompt for input
        choice = user_interface.get_menu_choice(5, user_interface.display_main_menu)

    # Display exiting program message.
    user_interface.display_exit_message()
