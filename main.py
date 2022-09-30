class IteratorCheck:
    def __init__(self):
        self.count = 0

    def __repr__(self):
        return "This is my cutie"

    def __next__(self):
        if self.count != 10:
            self.count += 1
            return self.count
        else:
            raise StopIteration
        return self

    def __next__(self):


bla = IteratorCheck()

for i in bla:
    print(i)


class Node:
    """
    Node is a linked list item
    -----
    Args:
        data: contains the value to be stored in the node
        nxt: contains a reference to the next node on the list
            by default is "None"
    Methods:
        __repr__: gives more helpful representation
    """

    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __repr__(self):
        return self.data


class LinkedList:
    """
    Linked list is an ordered collection.
    Linked lists store references as part of their own nodes.
    """

    def __init__(self, nodes=None):
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
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """Gives a list with nodes (ordered)"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def prepend(self, node):
        """
        Prepending a new node from the start of the list.

        ----
        Args:
            node: new node that need to be added
        """
        node.next = self.head
        self.head = node

    def append(self, node):
        """
        Appending a new node at the end of the list.

        ----
        Args:
            node: new node that need to be added
        """
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def insert(self, val, position):
        """
        Inserting new node at specified position

        ----
        Args:
            val: new node data to insert into linked list
            position: the position to insert the specified node
        """
        if self.head is None and position != 0:
            raise Exception("Specified position is not reachable !")

        newNode = Node(val)
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
            target_node_data: target node's data
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
