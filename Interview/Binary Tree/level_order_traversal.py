# level order traversal = Mostly we do through queue data structure
class Queue(object):
    def __init__(self):  # basically we are going to modify the pythons list to queue
        self.items = []

    def enqueue(self, item):  # adding items to queue
        self.items.insert(0, item)

    def dequeue(self):  # removing the items
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0  # if it is empty it will return True

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):  # len(q)
        return self.size()

    def size(self):
        return len(self.items)


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
        # if traversal_type == "preorder":
        #     # traversal pass in empty string in beginning and then with each recursive call the value keep storing with each node
        #     return self.preorder_print(tree.root, "")
        # elif traversal_type == "inorder":
        #     # these strings "" are because we call them recursively
        #     return self.inorder_print(tree.root, "")
        # elif traversal_type == "postorder":
        #     return self.postorder_print(tree.root, "")
        if traversal_type == "levelorder":
            # it is not in iterative way so no strings
            return self.levelorder_print(tree.root)
        else:
            print("Traversal type" + str(traversal_type) + " is not supported.")
            return False

    # def preorder_print(self, start, traversal):
    #     """ Root -> Left -> Right"""
    #     if start:
    #         # print out the value and append to -
    #         # traversal type is string # first root
    #         traversal += (str(start.value) + " - ")
    #         traversal = self.preorder_print(
    #             start.left, traversal)  # second left
    #         traversal = self.preorder_print(
    #             start.right, traversal)  # third right
    #     return traversal

    # def inorder_print(self, start, traversal):
    #     """ Left -> Root -> Right"""
    #     if start:
    #         traversal = self.inorder_print(start.left, traversal)  # first left
    #         traversal += (str(start.value) + " - ")  # then root
    #         traversal = self.inorder_print(
    #             start.right, traversal)  # then right
    #     return traversal

    # def postorder_print(self, start, traversal):
    #     """Left -> Right -> Root"""
    #     if start:
    #         traversal = self.postorder_print(
    #             start.left, traversal)  # first left
    #         traversal = self.postorder_print(
    #             start.right, traversal)  # 2nd right
    #         traversal += (str(start.value) + " - ")  # then root
    #     return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()  # we are defining queue object
        queue.enqueue(start)  # we start with root in levelorder

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()  # we are taking out the childrens of that root

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal  # this will be string of level order traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("levelorder"))  # return 1-2-3-4-5-
