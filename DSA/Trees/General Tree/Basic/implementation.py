# Implementing a Tree

class TreeNode:
    def __init__(self, data):
        self.data = data  # defining the data
        self.children = []  # this is the children, and every child is a tree in itself
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)  # append the children in the list


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
    pass
