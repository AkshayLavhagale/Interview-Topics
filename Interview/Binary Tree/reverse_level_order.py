# by using the queue and stack - here we add the right node first as this is reverse level order traversal
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):  # to get the top element of the stack
        if not self.is_empty():
            return self.items[-1]  # accessing the final element in the list

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


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
        # elif traversal_type == "levelorder":
        #     # it is not in iterative way so no strings
        #     return self.levelorder_print(tree.root)
        if traversal_type == "reverse_levelorder":
            return self.reverse_level_order_print(tree.root)
        else:
            print("Traversal type" + str(traversal_type) + " is not supported.")
            return False

    def reverse_level_order_print(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)  # getting the root

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()  # removing the front of the queue
            # now what we removed from front of queue we will append in stack
            stack.push(node)

            if node.right:  # as this is reverse level order right node comes first
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:  # while lenth of stack is not empty
            node = stack.pop()  # now we are popping out from the stack and store in string of traversal
            traversal += str(node.value) + "-"
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("reverse_levelorder"))  # return 4-5-2-3-1-   
