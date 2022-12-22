#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private size

"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self._next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = ''
        current_node = self.head
        while current_node is not None:
            s += str(current_node.data) + '\n'
            current_node = current_node.next_node
        return s

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current
