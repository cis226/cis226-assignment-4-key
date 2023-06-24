"""Abstract Droid module"""
from abc import ABC, abstractmethod


class AbstractDroid(ABC):
    """Provides Interface like functionality for Droid subclasses

    You must ensure that your droids are inheriting from this Abstract Base Class.
    You must also make sure that you do NOT change any of the code in this file.
    You must use this abstract class as-is, which means that your code may need
    to be written in a way that you are not expecting.
    NOTE: calculate_total_cost returns None, and should continue to return None
    in child classes, meaning that access to the total cost value must be done
    by use of the total_cost attribute once the calculate_total_cost method has
    been called.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Set up total_cost var for all children"""
        super().__init__(*args, **kwargs)
        self.total_cost = 0

    @abstractmethod
    def calculate_total_cost(self) -> None:
        """Calculate the total cost of a droid

        Children should override this method to inspect all attributes of a
        child class and calculate the total cost based on those attributes."""
        raise NotImplementedError()
