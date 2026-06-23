class Node:
    data: str

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    head: Node

    def __init__(self):
        self.head = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        current_node = self.head
        new_node.next = current_node
        self.head = new_node

    def pop(self):
        if self.head:
            self.head = self.head.next


stack = Stack()
stack.push(Node("Hola"))
stack.push(Node("Como"))
stack.push(Node("Estas"))
stack.push(Node("Bye"))
stack.print_structure()
print("--------------")
stack.pop()
stack.pop()
# stack.pop()
# stack.pop()
stack.print_structure()
