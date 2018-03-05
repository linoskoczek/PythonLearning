class Node:
    """Single node in Binary Tree"""

    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None

    @staticmethod
    def count_elements(node):
        if node is None:
            return 0
        return Node.count_elements(node.left) + Node.count_elements(node.right) + 1


one = Node(None)
two = Node(one)
four = Node(two)
three = Node(two)
five = Node(one)
six = Node(five)

one.left = two
one.right = five
two.left = four
two.right = three
five.right = six

assert Node.count_elements(one) == 6
assert Node.count_elements(two) == 3
assert Node.count_elements(None) == 0
assert Node.count_elements(six) == 1
