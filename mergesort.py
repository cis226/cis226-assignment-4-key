"""Module for Merge Sort"""


class MergeSort:
    """Merge Sort Class"""

    def __init__(self):
        """Constructor"""
        self._aux = []

    def sort(self, iterable):
        """Public sort method"""

        # Initialize aux list to a bunch of Nones.
        # That way we will not encounter any indexing errors.
        self._aux = [None for i in range(len(iterable))]
        self._sort(iterable, 0, len(iterable) - 1)

    def _sort(self, iterable, lo, hi):
        """Private recursive sort method"""

        # If the hi is <= the low, we are down to a single element sub list.
        # Time to return. This is the base case for the recursive call.
        if hi <= lo:
            return

        # Calculate the mid point. Note that the mid point for the sub list
        # might not be between zero and some other number. That is why we are
        # adding the lo back into the calculation.
        mid = lo + int((hi - lo) / 2)

        # Make a recursive call to sort the left side
        self._sort(iterable, lo, mid)

        # Make a recursive call to sort the right side
        self._sort(iterable, mid + 1, hi)

        # Merge the two halves together into a sorted whole.
        self._merge(iterable, lo, mid, hi)

    def _merge(self, iterable, lo, mid, hi):
        """Merge method to merge 2 sorted sub lists into a single sorted list"""

        # Set the i index that will be used to walk through the left half to
        # the lo that is passed in.
        i = lo
        # Set the j index that will be used to walk through the right half to
        # the mid point + 1
        j = mid + 1

        # Loop through all indices and copy the data to the aux list.
        for k in range(lo, hi + 1):
            self._aux[k] = iterable[k]

        # Loop from lo to hi using a separate variable than the i and j that
        # mark the current index in the sub-list.
        for k in range(lo, hi + 1):
            # If i index is greater than the mid point, then the only elements
            # left are those in the right sub-list.
            if i > mid:
                # Copy the right list current index element to the finished
                # list and increment the index counter for the right sub-list.
                iterable[k] = self._aux[j]
                j += 1

            # If j is greater than the hi point, then the only elements left are
            # those in the left sub-list.
            elif j > hi:
                # Copy the left list current index element to the finished
                # list and increment the index counter for the left sub-list.
                iterable[k] = self._aux[i]
                i += 1
            # If both indices are valid, need to compare the two elements to
            # see which one is smaller.
            # NOTE: This requires that the object being sorted has a valid
            # __lt__ dunder method defined.
            elif self._aux[j] < self._aux[i]:
                # Do the same as above to move the correct element to the
                # finished list.
                iterable[k] = self._aux[j]
                j += 1
            # Else we need to move the other element.
            else:
                # Do the same as above to move the correct element to the
                # finished list.
                iterable[k] = self._aux[i]
                i += 1
