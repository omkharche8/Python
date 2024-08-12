# Jus get the left view of GFG

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def left_view(root):
    if root is None:
        return None

    queue = []
    output = []

    queue.append(root)
    while len(queue) > 0:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)

            if i == 0:
                print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    left_view(root)

