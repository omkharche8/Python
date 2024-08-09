# If we take a look at certain examples, we can notice that tree nodes need to be printed top to down level by level and by the definition of the tree,
# we can access nodes also from top to down (Note that we are given root and from root we traverse down the tree).
# So this order is First in First out. Therefore we use queue to implement level order traversal.

class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printlevelordertraversal(root):

    if root is None:
        return

    queue = []

    queue.append(root)

    while len(queue) > 0:
        print(queue[0].data, end=" ")
        node = queue.pop(0)

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
    printlevelordertraversal(root)