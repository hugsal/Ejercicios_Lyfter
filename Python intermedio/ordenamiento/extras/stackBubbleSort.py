class Node:
    data: int

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    head: Node

    def __init__(self):
        self.head = None

    def bubble_sort(self):
        if not self.head or not self.head.next:
            return
        end = None
        while end != self.head.next:
            current = self.head
            has_changes = False
            while current.next != end:
                next_node = current.next
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    has_changes = True
                current = current.next
            if not has_changes:
                break
            end = current

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        current_node = self.head
        new_node.next = current_node
        self.head = new_node
        self.bubble_sort()

    def pop(self):
        if self.head:
            self.head = self.head.next


stack = Stack()
stack.push(Node(6))
stack.push(Node(5))
stack.push(Node(34))
stack.push(Node(12))
stack.print_structure()
print("--------------")
stack.pop()
stack.pop()
# stack.pop()
# stack.pop()
stack.print_structure()
