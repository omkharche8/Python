# Implementing a Tree

class TreeNode:
    def __init__(self, data):
        self.data = data  # defining the data
        self.children = []  # this is the children, and every child is a tree in itself
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)  # append the children in the list

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if len(self.children):     # as the leaf node has no children so we have to put this case
            for child in self.children:
                child.print_tree()

    def get_level(self):   # Getting 0,1,2 level of the tree.
        level = 0
        p = self.parent
        while p:   # Go to parent, parent's parent, parent's parent's parent and then increment on that
            level += 1
            p = p.parent
        return level


def build_product_tree():
    root = TreeNode("Electronics")  # don't touch the root, its supreme

    laptop = TreeNode("Laptop")  # Now the branching starts
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("ThinkPad"))

    cellphone = TreeNode("CellPhone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("VU"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
