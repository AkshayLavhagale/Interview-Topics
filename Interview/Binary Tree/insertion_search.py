# elements with less value than root will go to left and more value than root goes to right
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
                self._insert(data, cur_node.left)

        else:  # data == cur_node.data, if the data is already present in the binary tree we don't allow such duplicate data in binary tree
            print("Value is already present in the tree")

    def find_search(self, data):  # node have data and we are putting that in function
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


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find_search(4))  # returns True
