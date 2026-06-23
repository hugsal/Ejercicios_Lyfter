class Node:
    data: str

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def pop_right(self):
        if self.tail is None:
            return None

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None


doubleEndedQueue = DoubleEndedQueue()
doubleEndedQueue.push_right(Node("Hola"))
doubleEndedQueue.push_right(Node("Como"))
doubleEndedQueue.push_left(Node("Estas"))
doubleEndedQueue.push_left(Node("Bye"))
doubleEndedQueue.print_structure()
print("--------------")
doubleEndedQueue.pop_left()
doubleEndedQueue.pop_right()
# doubleEndedQueue.pop_right()
# doubleEndedQueue.pop_right()
# doubleEndedQueue.pop_right()
doubleEndedQueue.print_structure()

# stack.print_structure()
