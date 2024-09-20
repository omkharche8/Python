# Drawing the degenerate Binary tree
# It just has left and right, basically only one node for one node

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def insert(root, data):
    if root is None:
        root = Node(data)
    else:
        root.right = insert(root.right, data)
    return root

def printTree(node):
    if node is not None:
        print(node.data)
        printTree(node.right)


root = None
root = insert(root, 1)
insert(root, 2)
insert(root, 3)
insert(root, 4)
insert(root, 5)

# Function call
printTree(root)



