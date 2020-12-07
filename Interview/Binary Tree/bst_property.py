# The BST property states that every node on the right subtree has to be larger than the current node and
# every node on the left subtree has to be smaller than the current node.
# here will use the inorder traversal
# Predecessor - predecessor of node is the immediate previous node in inorder traversal of binary tree
# Successor - successor of node is the immediate next node in inorder traversal of binary tree

class Node:
    def __init__(self, data=None):  # data element stored in node . Initially set to None
        self.data = data
        self.left = None
        self.right = None


class BST:  # binary search tree
    def __init__(self):
        self.root = None  # we need to find the root of the tree and set to none

    def insert(self, data):
        if self.root is None:
            # if there is no data we will create the node and make it as root
            self.root = Node(data)
        else:  # if there is at least one node previously we need to check where to add new node in tree
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:  # so in this case it will go to left
            if cur_node.left is None:  # before adding the node at left we need to check there is no node at the left children place
                cur_node.left = Node(data)  # we added the data in left
            else:  # there is data
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:  # data == cur_node.data, if the data is already present in the binary tree we don't allow such duplicate data in binary tree
            print("Value is already present in the tree")

    def inorder_print_tree(self):
        if self.root:
            # _inorder functions are the helper functions
            self._inorder_print_tree(
                self.root)  # in inorder it will be """ Left -> Root -> Right """

    # function take the cur_node we are looking at
    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    def find(self, data):  # node have data and we are putting that in function
        if self.root:
            # boolean function True or False
            # if _find does not find anything it will return None
            is_found = self._find(data, self.root)
            if is_found:  # if it is true
                return True
            return False  # it does not found
        else:  # if there is no node in tree
            return None

    # here will check the left and right child depend on data of node we are searching
    def _find(self, data, cur_node):
        # checking if data is greater and in right side already there is data
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    def is_bst_satisfied(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.data)

            if is_satisfied is None:
                return True
            return False
        return True

    def _is_bst_satisfied(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:  # checking whether 8 > 3
                return self._is_bst_satisfied(cur_node.left, cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.data:
                return self._is_bst_satisfied(cur_node.right, cur_node.right.data)
            else:
                return False


bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

tree = BST()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
# tree.root.left.left = Node(-5)
# tree.root.left.right = Node(0)
# tree.root.right.left = Node(2)
# tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(-8)

print(bst.is_bst_satisfied())  # return True
print(tree.is_bst_satisfied())  # return False
