"""Data Structures module"""

# David Barnes
# CIS 226
# 6-4-2023


class NodeDataStructure:
    """Base class for Data Structures that need to use a Node"""

    class Node:
        """Used to store data inside a data structure"""

        def __init__(self):
            """Constructor"""
            self.data = None
            self.next = None


class Stack(NodeDataStructure):
    """Stack allowing push and pop functionality"""

    def __init__(self):
        """Constructor"""
        self._head = None
        self._size = 0

    @property
    def is_empty(self):
        """Return whether stack is empty."""
        return self._head is None

    def push(self, data):
        """Push method"""
        # Create a new node that points to the same place that head points to.
        old_head = self._head
        # Create a new node and assign it to the head variable. Now head points
        # to the new node, and old_head points to the old head node.
        self._head = self.Node()
        # Set the data that was passed in on the new node
        self._head.data = data
        # Set the next property of the first node to the old head, which will
        # finish the work of adding a new node to the start of the list (stack)
        self._head.next = old_head
        # Increase the size
        self._size += 1

    def pop(self):
        """Pop method"""
        # Check to make sure the list is not empty. Can't pop if it is empty.
        if not self.is_empty:
            # Get the data out of the first node and put it in a local variable
            data = self._head.data
            # Set the head pointer to head's next property
            self._head = self._head.next
            # Decrement the size
            self._size -= 1
            # Return the data
            return data
        # Return None as the size must already be zero.
        # Alternatively, could raise an exception.
        return None


class Queue(NodeDataStructure):
    """Queue allowing enqueue and dequeue functionality"""

    def __init__(self):
        """Constructor"""
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def is_empty(self):
        """Return whether queue is empty."""
        return self._head is None

    def enqueue(self, data):
        """Push method"""
        # Create a new node that points to the same place that tail points to.
        old_tail = self._tail
        # Create a new node and assign it to the tail variable. Now tail points
        # to the new node, and old_tail points to the old tail node.
        self._tail = self.Node()
        # Set the data that was passed in on the new node
        self._tail.data = data
        # If the list is empty, and this add will be the first node in the list
        if self.is_empty:
            # Set the first to equal the last that was just created.
            self._head = self._tail
        else:
            # This is not the only item, so set old tail's next to the new node
            # pointed to by tail.
            old_tail.next = self._tail
        # Increase the size
        self._size += 1

    def dequeue(self):
        """Pop method"""
        # Check to make sure the list is not empty. Can't pop if it is empty.
        if not self.is_empty:
            # Get the data out of the first node and put it in a local variable
            data = self._head.data
            # Set the head pointer to head's next property
            self._head = self._head.next
            # Decrement the size
            self._size -= 1
            # If the queue is empty after taking out the lst node
            if self.is_empty:
                # Set the last pointer to None
                self._tail = None
            # Return the data
            return data
        # Return None as the size must already be zero.
        # Alternatively, could raise an exception.
        return None
