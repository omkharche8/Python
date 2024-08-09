# The idea is to use a deque(double-ended queue) to get the reverse level order.
# A deque allows insertion and deletion at both ends.
# If we do normal level order traversal and instead of printing a node, push the node to a stack and then print the contents of the deque,
# we get “5 4 3 2 1” for the above example tree, but the output should be “4 5 2 3 1”.
# So to get the correct sequence (left to right at every level), we process the children of a node in reverse order,
# we first push the right subtree to the deque, then process the left subtree.

from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reverseLevelOrder(root):
    q = deque()  # This is the calculation deque
    q.append(root)
    ans = deque()  # Printing the ans in this
    while q:
        node = q.popleft()
        if node is None:   #
            continue

        ans.appendleft(node.data)

        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)


    return ans


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

deq = reverseLevelOrder(root)
for key in deq:
    print(key, end=" ")
