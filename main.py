class Node:
    """
    Node is a linked list item
    -----
    Args:
        data: contains the value to be stored in the node
    Methods:
        __repr__: gives more helpful representation in string
            type (when using "repr()" build-in function)
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    """
    Linked list is an ordered collection.
    Linked lists store references as part of their own nodes.
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

