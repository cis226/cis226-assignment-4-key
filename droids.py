"""Droid classes"""

# David Barnes
# CIS 226
# 6-4-2023

# System Imports
import os
from abc import ABC, abstractmethod

# First-party Imports
from abstract_droid import AbstractDroid
from datastructures import Stack, Queue
from mergesort import MergeSort


class Droid(AbstractDroid, ABC):
    """Base Droid class. Also abstract as it does not make sense to allow it
    to be instantiated."""

    MODEL_COST = 0
    model_name = "Droid"

    def __init__(self, material, color, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self._material = material
        self._color = color

    def __str__(self):
        """String method"""
        return (
            f"Model: {self.model_name}{os.linesep}"
            f"Material: {self._material}{os.linesep}"
            f"Color: {self._color}{os.linesep}"
            f"{self._droid_info_str()}"
            f"Total Cost: ${self.total_cost:.2f}"
        )

    class Materials:
        """Storage of materials constants"""

        def __new__(cls):
            raise TypeError("Can not make instances of Materials class")

        CARBONITE = "Carbonite"
        VANADIUM = "Vanadium"
        QUADRANIUM = "Quadranium"
        TEARS_OF_A_JEDI = "Tears Of A Jedi"

    class Colors:
        """Storage of color constants"""

        def __new__(cls):
            raise TypeError("Can not make instance of Colors class")

        WHITE = "White"
        RED = "Red"
        GREEN = "Green"
        BLUE = "Blue"

    @abstractmethod
    def calculate_total_cost(self):
        """Calculate the total cost and store it in the total_cost attribute"""
        self.total_cost = (
            self.MODEL_COST + self._get_material_cost() + self._get_color_cost()
        )

    @abstractmethod
    def _droid_info_str(self):
        """Returns subclass specific attributes as a string"""
        raise NotImplementedError()

    def _get_material_cost(self):
        """Get the material cost based on value of instance's material"""
        material_cost = 50.00

        if self._material == self.Materials.CARBONITE:
            material_cost = 100.00
        elif self._material == self.Materials.VANADIUM:
            material_cost = 120.00
        elif self._material == self.Materials.QUADRANIUM:
            material_cost = 150.00
        elif self._material == self.Materials.TEARS_OF_A_JEDI:
            material_cost = 200.00
        else:
            raise ValueError("Unknown material type.")

        return material_cost

    def _get_color_cost(self):
        """Get the color cost based on value of instance's color"""
        color_cost = 5.00

        if self._color == self.Colors.WHITE:
            color_cost = 10.00
        elif self._color == self.Colors.RED:
            color_cost = 20.00
        elif self._color == self.Colors.GREEN:
            color_cost = 40.00
        elif self._color == self.Colors.BLUE:
            color_cost = 50.00
        else:
            raise ValueError("Unknown color")

        return color_cost

    # Rich comparison methods. Required if we want to be able to compare
    # one droid with another.
    # NOTE: Skipping the eq and ne methods as having the same total cost does
    # not mean that they are the same object or instance.
    def __lt__(self, other):
        """Less than rich comparison method"""
        return self.total_cost < other.total_cost

    def __le__(self, other):
        """Less than or equal rich comparison method"""
        return self.total_cost <= other.total_cost

    def __gt__(self, other):
        """Greater than rich comparison method"""
        return self.total_cost > other.total_cost

    def __ge__(self, other):
        """Greater than or equal rich comparison method"""
        return self.total_cost >= other.total_cost


class ProtocolDroid(Droid):
    """Represent a Protocol Droid"""

    MODEL_COST = 120.00
    COST_PER_LANGUAGE = 25.00
    model_name = "Protocol"

    def __init__(self, material, color, number_of_languages):
        """Constructor"""
        super().__init__(material, color)

        # Set the number of languages
        self._number_of_languages = number_of_languages

    def _droid_info_str(self):
        """Return droid specific attributes as a string. Overrides parent."""
        return f"Number of Languages: {self._number_of_languages}{os.linesep}"

    def _calculate_language_cost(self):
        """Calculate and return the cost of languages"""
        return self._number_of_languages * self.COST_PER_LANGUAGE

    def calculate_total_cost(self):
        """Calculate the total cost and store it in the total_cost attribute"""
        super().calculate_total_cost()
        self.total_cost += self._calculate_language_cost()


class UtilityDroid(Droid):
    """Represents a Utility Droid"""

    MODEL_COST = 130.00
    COST_PER_OPTION = 35.00
    model_name = "Utility"

    def __init__(
        self, material, color, has_toolbox, has_computer_connection, has_scanner
    ):
        """Constructor"""
        super().__init__(material, color)

        # Set the option bools
        self._has_toolbox = has_toolbox
        self._has_computer_connection = has_computer_connection
        self._has_scanner = has_scanner

    def _droid_info_str(self):
        """Return droid specific attributes as a string. Overrides parent."""
        return (
            f"Has Tool Box: {self._has_toolbox}{os.linesep}"
            f"Has Computer Connection: {self._has_computer_connection}{os.linesep}"
            f"Has Scanner: {self._has_scanner}{os.linesep}"
        )

    def _calculate_options_cost(self):
        """Calculate and return the cost of options selected for the droid"""
        options_cost = 0

        if self._has_toolbox:
            options_cost += self.COST_PER_OPTION
        if self._has_computer_connection:
            options_cost += self.COST_PER_OPTION
        if self._has_scanner:
            options_cost += self.COST_PER_OPTION

        return options_cost

    def calculate_total_cost(self):
        """Calculate the total cost and store it in the total_cost attribute"""
        super().calculate_total_cost()
        self.total_cost += self._calculate_options_cost()


class JanitorDroid(UtilityDroid):
    """Represents a Janitor Droid"""

    MODEL_COST = 160.00
    model_name = "Janitor"

    def __init__(
        self,
        material,
        color,
        has_toolbox,
        has_computer_connection,
        has_scanner,
        has_broom,
        has_vacuum,
    ):
        """Constructor"""
        super().__init__(
            material, color, has_toolbox, has_computer_connection, has_scanner
        )

        # Set the option bools
        self._has_broom = has_broom
        self._has_vacuum = has_vacuum

    def _droid_info_str(self):
        """Return droid specific attributes as a string. Overrides parent."""
        return (
            f"{super()._droid_info_str()}"
            f"Has Broom: {self._has_broom}{os.linesep}"
            f"Has Vacuum: {self._has_vacuum}{os.linesep}"
        )

    def _calculate_options_cost(self):
        """Calculate and return the cost of options selected for the droid"""
        options_cost = super()._calculate_options_cost()

        if self._has_broom:
            options_cost += self.COST_PER_OPTION
        if self._has_vacuum:
            options_cost += self.COST_PER_OPTION

        return options_cost


class AstromechDroid(UtilityDroid):
    """Represents a Astromech Droid"""

    MODEL_COST = 200.00
    COST_PER_SHIP = 45.00
    model_name = "Astromech"

    def __init__(
        self,
        material,
        color,
        has_toolbox,
        has_computer_connection,
        has_scanner,
        has_navigation,
        number_of_ships,
    ):
        """Constructor"""
        super().__init__(
            material, color, has_toolbox, has_computer_connection, has_scanner
        )

        # Set the option bools
        self._has_navigation = has_navigation
        self._number_of_ships = number_of_ships

    def _droid_info_str(self):
        """Return droid specific attributes as a string. Overrides parent."""
        return (
            f"{super()._droid_info_str()}"
            f"Has Navigation: {self._has_navigation}{os.linesep}"
            f"Number Of Ships: {self._number_of_ships}{os.linesep}"
        )

    def _calculate_options_cost(self):
        """Calculate and return the cost of options selected for the droid"""
        options_cost = super()._calculate_options_cost()

        if self._has_navigation:
            options_cost += self.COST_PER_OPTION

        return options_cost

    def _calculate_ships_cost(self):
        """Calculate and return the cost of ships"""
        return self.COST_PER_SHIP * self._number_of_ships

    def calculate_total_cost(self):
        """Calculate the total cost and store it in the total_cost attribute"""
        super().calculate_total_cost()
        self.total_cost += self._calculate_ships_cost()


class DroidCollection:
    """Stores droids that have been created"""

    def __init__(self):
        """Constructor"""
        self._collection = []

    def add_protocol(self, material, color, number_of_languages):
        """Add protocol droid to internal collection"""
        self._collection.append(
            ProtocolDroid(material, color, number_of_languages),
        )

    def add_utility(self, material, color, toolbox, computer_connection, scanner):
        """Add Utility droid to internal collection"""
        self._collection.append(
            UtilityDroid(material, color, toolbox, computer_connection, scanner)
        )

    def add_janitor(
        self, material, color, toolbox, computer_connection, scanner, broom, vacuum
    ):
        """Add Janitor droid to internal collection"""
        self._collection.append(
            JanitorDroid(
                material,
                color,
                toolbox,
                computer_connection,
                scanner,
                broom,
                vacuum,
            ),
        )

    def add_astromech(
        self,
        material,
        color,
        toolbox,
        computer_connection,
        scanner,
        navigation,
        number_of_ships,
    ):
        """Add Astromech droid to internal collection"""
        self._collection.append(
            AstromechDroid(
                material,
                color,
                toolbox,
                computer_connection,
                scanner,
                navigation,
                number_of_ships,
            )
        )

    def is_empty(self):
        """Whether the collection is empty or not"""
        return len(self._collection) <= 0

    def __str__(self):
        """String method"""

        # Init the return string.
        return_string = ""
        # Loop through all droids and form the return string.
        for droid in self._collection:
            # Calculate the total cost of the droid. Since we are using inheritance
            # an polymorphism, the program will automatically know which version
            # of calculate_total_cost it needs to call based on which particular
            # type it is looking at during the for loop.
            droid.calculate_total_cost()
            # Create the string now that the total cost has been calculated
            return_string += f"****************************{os.linesep}"
            return_string += f"{str(droid)}{os.linesep}"
            return_string += f"****************************{os.linesep}"
            return_string += f"{os.linesep}"
        # Return completed string.
        return return_string

    def sort_into_categories(self):
        """Sort the collection of droids by category"""

        # Create a stack for each type of droid.
        protocol_stack = Stack()
        utility_stack = Stack()
        janitor_stack = Stack()
        astromech_stack = Stack()

        # Create a queue to hold the droids as we pop them off the stacks
        droid_queue = Queue()

        # For each Droid in the droid collection
        for droid in self._collection:
            # The testing of the droids must occur in this order.
            # It must be done in the order of most specific to least.

            # If we were to test a droid that IS of type Astromech against
            # Utility BEFORE we test against Astromech, it would pass and be put
            # into the Utility stack and not the Astromech. That is why it is
            # important to test from most specific to least.

            # If the droid is an Astromech, push it on the astromech stack
            if isinstance(droid, AstromechDroid):
                astromech_stack.push(droid)
            # Else if the droid is a Janitor droid, push it on the janitor stack.
            elif isinstance(droid, JanitorDroid):
                janitor_stack.push(droid)
            # Check for Utility
            elif isinstance(droid, UtilityDroid):
                utility_stack.push(droid)
            # Check for Protocol
            elif isinstance(droid, ProtocolDroid):
                protocol_stack.push(droid)
            # Unknown type of droid
            else:
                raise TypeError("Unknown droid type.")

        # Now that the droids are all in their respective stacks, we can do
        # the work of popping them off of the stacks and adding them to the
        # queue.
        # It is required that they be popped off from each stack in this
        # order so that they have the correct order going into the queue.

        # This is a primer pop. It gest the first droid off the stack.
        # Which could be None if the stack is empty.
        current_astromech = astromech_stack.pop()
        # While the droid that is popped off is not None
        while current_astromech is not None:
            # Add the popped droid to the queue
            droid_queue.enqueue(current_astromech)
            # Pop off the next droid for the loop test
            current_astromech = astromech_stack.pop()

        # See above lines for Astromech. It is the same except for Janitor
        current_janitor = janitor_stack.pop()
        while current_janitor is not None:
            droid_queue.enqueue(current_janitor)
            current_janitor = janitor_stack.pop()

        # See above lines for Astromech. It is the same except for Utility
        current_utility = utility_stack.pop()
        while current_utility is not None:
            droid_queue.enqueue(current_utility)
            current_utility = utility_stack.pop()

        # See above lines for Astromech. It is the same except for Protocol
        current_protocol = protocol_stack.pop()
        while current_protocol is not None:
            droid_queue.enqueue(current_protocol)
            current_protocol = protocol_stack.pop()

        # Now that the droids have all been removed from the stacks and put
        # into the queue, we need to dequeue them all and put them back into
        # the original list

        # Set a counter to 0
        counter = 0

        # This is primer dequeue that will get the first droid out of the
        # queue.
        droid = droid_queue.dequeue()
        # While the dequeued droid is not None.
        while droid is not None:
            # Add the droid to the droid collection using the int counter
            # as the index.
            self._collection[counter] = droid
            # Increment the counter
            counter += 1
            # Dequeue the next droid off the queue so it can be used in the
            # while condition
            droid = droid_queue.dequeue()

    def sort_by_total_cost(self):
        """Sort the droids by the total cost using Merge Sort."""

        # Create a new merger sorter instance
        merge_sorter = MergeSort()
        # Make sure that `calculate_total_cost` gets called on each droid
        # before sorting. Otherwise, they will all be zero and the sort won't
        # do anything.
        for droid in self._collection:
            droid.calculate_total_cost()

        # Call the sort method on the MergeSort instance and pass it the
        # list to sort.
        merge_sorter.sort(self._collection)

    def load_default_droids(self):
        """Load some default droids into the collection so it is not empty"""
        self.add_protocol(
            Droid.Materials.CARBONITE,
            Droid.Colors.WHITE,
            12,
        )
        self.add_utility(
            Droid.Materials.VANADIUM,
            Droid.Colors.RED,
            True,
            True,
            True,
        )
        self.add_janitor(
            Droid.Materials.QUADRANIUM,
            Droid.Colors.BLUE,
            True,
            True,
            True,
            True,
            True,
        )
        self.add_astromech(
            Droid.Materials.TEARS_OF_A_JEDI,
            Droid.Colors.GREEN,
            True,
            True,
            False,
            True,
            80,
        )
        self.add_protocol(
            Droid.Materials.TEARS_OF_A_JEDI,
            Droid.Colors.BLUE,
            22,
        )
        self.add_janitor(
            Droid.Materials.QUADRANIUM,
            Droid.Colors.RED,
            False,
            False,
            False,
            False,
            True,
        )
        self.add_utility(
            Droid.Materials.VANADIUM,
            Droid.Colors.WHITE,
            True,
            True,
            False,
        )
        self.add_astromech(
            Droid.Materials.CARBONITE,
            Droid.Colors.GREEN,
            False,
            True,
            False,
            True,
            150,
        )
        self.add_janitor(
            Droid.Materials.CARBONITE,
            Droid.Colors.GREEN,
            False,
            True,
            True,
            True,
            True,
        )
        self.add_utility(
            Droid.Materials.VANADIUM,
            Droid.Colors.WHITE,
            True,
            False,
            True,
        )
        self.add_astromech(
            Droid.Materials.QUADRANIUM,
            Droid.Colors.RED,
            True,
            False,
            False,
            True,
            100,
        )
        self.add_protocol(
            Droid.Materials.TEARS_OF_A_JEDI,
            Droid.Colors.BLUE,
            24,
        )
