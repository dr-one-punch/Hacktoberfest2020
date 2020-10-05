# program to print height and diameter of a binary tree

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def calc_height_diameter(root, diameter):

    if root is None:
        return -1

    left_h = calc_height_diameter(root.left, diameter)
    right_h = calc_height_diameter(root.right, diameter)

    if (1+left_h+right_h > diameter[0]):
        diameter[0] = 1+ left_h +right_h

    return 1 + max(left_h, right_h)

class Tree:
    def __init__(self, root):
        self.root = node(root)

    def print_height(self, node, isBalanced):

        if node is None:
            return -1

        # print(node.value)
        left_height = self.print_height(node.left, isBalanced)
        # print("lh", left_height)
        right_height = self.print_height(node.right, isBalanced)
        # print("rh", right_height)

        if abs(left_height-right_height)>1:
            isBalanced[0] = False

        return 1 + max(left_height, right_height)


tr = Tree(4)
tr.root.left = node(10)
tr.root.left.right = node(11)
tr.root.left.left = node(12)
tr.root.left.right.left = node(10)
# tr.root.left.right.left.left = node(10)
tr.root.right = node(10)
isBalanced = [True]
print(tr.print_height(tr.root,isBalanced))

if isBalanced[0]==False:
    print("The tree is not balanced")
else:
    print("The tree is balanced")

diameter = [0]
calc_height_diameter(tr.root, diameter)
print("Diameter of the tree is: ",diameter[0])