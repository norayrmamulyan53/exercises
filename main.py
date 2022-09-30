class Node:
    """
    A class to represent each node of the linked list.
    -----
    Args:
        data: any
            contains the value to be stored in the node
        nxt: Node
            contains a reference to the next node on the list
                by default is "None"
    """

    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __repr__(self):
        """
        Returns the data of the node
        """
        return self.data


class LinkedList:
    """
    This class is an ordered collection.
    It represents linked list.

    -------
    Methods:
        append: adds a new node at the end of the linked list
        prepend: prepending a new node from the start of the list.

    """

    def __init__(self, nodes=None):
        """
        Constructs all the necessary attributes for the LinkedList object.
        Also allows you to quickly create linked lists with some data,if
        in function passed a list of data.

        ----------
        Args:
            nodes : list[]
                list of data
        """
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        """Gives more helpful representation"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """Makes the instance to traverse through its nodes."""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def prepend(self, node):
        """
        Prepending a new node from the start of the list.

        ----------
        Args:
            node : Node
                new node that need to be added
        """
        node.next = self.head
        self.head = node

    def append(self, node):
        """
        Inserting a new node at the end of the list.

        ----------
        Args:
            node : Node
                new node that need to be added
        """
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def insert(self, data, position):
        """
        Inserting new node at the specified position

        ----
        Args:
            data: any
                new node data to insert into linked list
            position: int
                the position to insert the specified node
        """
        if self.head is None and position != 0:
            raise Exception("Specified position is not reachable !")

        newNode = Node(data)
        if position == 0:
            self.prepend(newNode)
        else:
            for index, current_node in enumerate(self):
                if index + 1 == position:
                    newNode.next = current_node.next
                    current_node.next = newNode

    def delete_node(self, target_node_data):
        """
        Deleting the linked list's node with specified data

        ----
        Args:
            target_node_data: any
                target node's data
        """
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)
