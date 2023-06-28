#!/usr/bin/python3
"""Definition of classes for a singly -linked
list."""

class Node:
    """This class represents or defines a node in
    singly-linked list.
    """
    def __init__(self, data, next_node=None):
        """This init method initializes a new Node

        Args:
            data (int): defines the data of the new Node
            next_node (Node): defines the next node of the new
            Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This method gets/sets the data of the
        Node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """this method Gets/sets the next_node of the
        Node.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """This class defines or represents
    a singly linked list."""
    def __init__(self):
        """This init method initializes a new Singly
        LinkedList.
        """
        self.__head = None

    def sorted_insert(self, value):
        """This method inserts a new node to the
        SinglyLinkedList.

        The node is inserted into the correct sorted position
        in the linked list.

        Args:
            value (Node): defines the new Node to insert.
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """This method defines the print() representation
        of a SinglyLinkedList.
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
