# three recursive depth-first search traversal algorithms (preorder, inorder, and postorder) and implement those recursively in Python.
# tree traversal - process of visiting (checking and/or updating) each node in tree data structure, exactly once.
# unlike linked list and arrays which are traversed in linear order.
# binary trees traversed in multiple ways like depth first or breadth first
class Node(object):
    def __init__(self, value):  # type of value we will store in node
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)  # the data comes in Node is stored as root

    # traversal type will check the preorder inorder postorder and iterative type as well
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            # traversal pass in empty string in beginning and then with each recursive call the value keep storing with each node
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type" + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """ Root -> Left -> Right"""
        if start:
            # print out the value and append to -
            # traversal type is string # first root
            traversal += (str(start.value) + " - ")
            traversal = self.preorder_print(
                start.left, traversal)  # second left
            traversal = self.preorder_print(
                start.right, traversal)  # third right
        return traversal

    def inorder_print(self, start, traversal):
        """ Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)  # first left
            traversal += (str(start.value) + " - ")  # then root
            traversal = self.inorder_print(
                start.right, traversal)  # then right
        return traversal

    def postorder_print(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.postorder_print(
                start.left, traversal)  # first left
            traversal = self.postorder_print(
                start.right, traversal)  # 2nd right
            traversal += (str(start.value) + " - ")  # then root
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))  # return 1 - 2 - 4 - 5 - 3 - 6 - 7 - 8 -
print(tree.print_tree("inorder"))  # return 4 - 2 - 5 - 1 - 6 - 3 - 7 - 8 -
print(tree.print_tree("postorder"))  # return 4 - 5 - 2 - 6 - 8 - 7 - 3 - 1 -
