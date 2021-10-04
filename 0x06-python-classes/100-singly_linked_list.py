#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""100-singly_linked_list
A Node class storing integers, and a Singly Linked List class implementing a
sorted insertion.
"""


class Node:
    """A Node class. Stores a number and a type Node.
    Attributes:
        __data (int): The size of the square.
        __next_node (:obj:`Node`): A 'pointer' to the next node.
    """

    def __init__(self, data, next_node=None):
        """Initialization of Node object with data and next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The data stored.
        For the setter:
        Args:
            value (int): The data of the Node.
        Raises:
            TypeError: Data entered must be an integer.
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The 'pointer' to the next node.
        For the setter:
        Args:
            value (:obj:`Node`): A Node.
        Raises:
            TypeError: Next node has to be Node or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A Singly Linked List Class. It sorts the inserted items and
    preps the list to be printed by print()
    Attributes:
        __head (:obj:`Node`): The head of the list.
    """

    def __init__(self):
        """Initialization of List object with a None head.
        """
        self.__head = None

    def __str__(self):
        """Formats the string to be printed by print()
        Returns:
            The formatted string.
        """
        current = self.__head
        string = ""

        while (current is not None):
            string += str(current.data)
            if (current.next_node is not None):
                string += "\n"
            current = current.next_node
        return string

    def sorted_insert(self, value):
        """Inserts a node with its value in the correct order.
        Args:
            value (int): The value of the Node to be inserted.
        """
        node = Node(value)
        current = self.__head

        if current is None:
            self.__head = node
            return

        if value < current.data:
            node.next_node = self.__head
            self.__head = node
            return

        while (current.next_node is not None and
               value >= current.next_node.data):
            current = current.next_node
        node.next_node = current.next_node
        current.next_node = node
