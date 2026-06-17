class Node:
    data: str

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    root: Node

    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if new_node.data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

    def print_tree(self):
        current = self.root

        while current is not None:
            if current.left is None:
                print(current.data, end=" ")
                current = current.right
            else:
                predecessor = current.left
                while (
                    predecessor.right is not None and predecessor.right is not current
                ):
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    print(current.data, end=" ")
                    current = current.right
        print()


tree = BinaryTree()

tree.insert(Node("Hola"))
tree.insert(Node("Como"))
tree.insert(Node("Estas"))
tree.insert(Node("Bye"))

tree.print_tree()
