"""
Reverse Linked List

Write a function that takes in the head of a Singly Linked List, reverses the
list in place (i.e., doesn't create a brand new list), and returns its new
head.

Each LinkedList node has an integer value as well as a next node pointing to
the next node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node;
in other words, the head will never be None / null.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5
// the head node with value 0

Sample Output
5 -> 4 -> 3 -> 2 -> 1 -> 0
// the head node with value 5
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def set_next(self, node):
        self.next = node


class LinkedList:
    def __init__(self):
        self.head = None

    def set_head(self, node):
        self.head = node

    def traverse(self):
        """Display according to the output's structure given:
        0 -> 1 -> ... -> n
        """
        display = []

        current_node = self.head
        while current_node:
            display.append(str(current_node.value))
            current_node = current_node.next

        print(' -> '.join(display))

    def reverse(self):
        """Reverses the node order."""
        current_node = self.head
        previous_node = None

        while current_node.next:
            next_node = current_node.next
            current_node.set_next(previous_node)
            previous_node = current_node
            current_node = next_node
        else:
            current_node.set_next(previous_node)
            self.set_head(current_node)


def generate_linked_list_integers(max_value=5):
    """Generate a linked list of integer values.
    :param max_value: tail node's value
    :type max_value: int
    :return: generated linked list
    :rtype: LinkedList
    """
    linked_list = LinkedList()
    previous_node = None

    for node_value in range(max_value + 1):
        node = Node(node_value)

        # Set head on first iteration
        if not linked_list.head:
            linked_list.set_head(node)

        # Set previous node's next attribute to current node
        if previous_node:
            previous_node.set_next(node)

        previous_node = node

    return linked_list


def main(max_value):
    if max_value < 0:
        print('!!! Only non-negative integers !!!')
        return
    linked_list = generate_linked_list_integers(max_value=max_value)
    linked_list.traverse()
    linked_list.reverse()
    linked_list.traverse()


def _run_suite():
    # Just for testing purposes
    suite_max_values = [-5, 0, 1, 3, 5, 10]
    for max_value in suite_max_values:
        print(f'MAX VALUE: {max_value}')
        main(max_value)
        print('=' * 10)


_run_suite()
