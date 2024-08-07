# Preorder(tree)
#
# Visit the root.
# Traverse the left subtree, i.e., call Preorder(left->subtree)
# Traverse the right subtree, i.e., call Preorder(right->subtree)


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorderTraversal(root):
    if root is None:
        return

    print(root.data, end=" ")

    preorderTraversal(root.left)

    preorderTraversal(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    preorderTraversal(root)
