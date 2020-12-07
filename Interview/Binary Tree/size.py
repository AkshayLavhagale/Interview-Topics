# The "size" of a binary tree is the total number of nodes present in the binary tree.
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


class Node(object):
    def __init__(self, value):  # type of value we will store in node
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def size_iterative(self):
        # iterative method
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)

        size = 1  # as we have pushed the root earlier so the size is 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size

    def size_recursive(self, node):  # node is going to call itself recursively
        if node is None:
            return 0

        # 1 because root is there. now we go to left and right subtree
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.size_iterative())  # return 5
print(tree.size_recursive(tree.root))  # root is node value returns 5
