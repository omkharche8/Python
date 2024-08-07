# Algorithm Postorder(tree)
#
# Traverse the left subtree, i.e., call Postorder(left->subtree)
# Traverse the right subtree, i.e., call Postorder(right->subtree)
# Visit the root

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorderTraversal(node):
    if node is None:
        return

    postorderTraversal(node.left)

    postorderTraversal(node.right)

    print(node.data, end=' ')


# Main function
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Postorder traversal: ", end='')
    postorderTraversal(root)
    print()


if __name__ == "__main__":
    main()
