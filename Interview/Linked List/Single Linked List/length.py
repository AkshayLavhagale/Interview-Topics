# Single Linked List - length of the list with both iterative as well as recursive way
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # we are initiating the head node as new linked list

    def print_list(self):   # to check or verify the list we have
        cur_node = self.head
        while cur_node:
            print(cur_node.data)  # print out data field of each of node
            cur_node = cur_node.next  # here next shows that our current node is Null

    def len_iterative(self): 
        count = 0
        cur_node = self.head
        while cur_node:  # this means current node is not null yet
            count += 1
            cur_node = cur_node.next
        return count  # how many elements in the list

    def len_recursive(self, node): # will start with head and with each recursive call will move it to next one
        if node is None: # base condition
            return 0 
        return 1 + self.len_recursive(node.next) # we call recursive itself and will pass to the next node,  self is a class method

    def append(self, data):  # appending the node with data in it
        # we are using the Node class to add first node in list assuming this is new list
        new_node = Node(data)
        if self.head is None:  # if head is None means there are no node in it
            self.head = new_node  # then we are just setting as new_node we created on line 12
            return

        # in case we have already nodes in the list will traverse head node till end and add node there
        last_node = self.head
        while last_node.next:  # till we reach the last node which will detect by Null
            last_node = last_node.next
        last_node.next = new_node  # this will append the node at end of list

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node  # making the new node as head

    def insert_between_node(self, prev_node, data):
        if not prev_node:  # checking whether the node after we are adding new node is present or not
            print("Previous node is not in the list")
            return
        # adding new node as we do in all insertion methods
        new_node = Node(data)
        new_node.next = prev_node.next  # instead of B refer to C we are referring E to C
        prev_node.next = new_node  # we are referring B to E now

    def delete(self, key):
        # 1. Delete head node - ABCDNull = BCDNull
        curr_node = self.head
        if curr_node and curr_node.data == key:  # we are checking the head node is not empty
            self.head = curr_node.next  # from A we are setting head to B
            curr_node = None  # And then we are setting A to None
            return

        # 2. Delete between node - ABCDNull = ACDNull
        prev = None  # checking As the head is not none, and also as we move with head node further to find key we also keep note of prev node
        while curr_node and curr_node.data != key:  # current node and data of it is not we are looking for
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:  # if current node is not in the list
            return

        prev.next = curr_node.next  # if current is in the list
        curr_node = None  # we declare the B the one we want to remove as Null

    def delete_node_at_position(self, pos):
        # 1. Delete node at position 0 - ABCDNull = BCDNull
        curr_node = self.head
        if pos == 0:  # if position is 0 i.e. head
            self.head = curr_node.next
            curr_node = None
            return

        # 2. Delete node at position 1 - ABCDNull = ACDNull
        prev = None
        count = 0  # we already took the consideration of position 0
        while curr_node and count != pos:
            prev = curr_node
            curr_node = curr_node.next
            count += 1

        if curr_node is None:
            return

        prev.next = curr_node.next  # we assigned the reference to C from A insted of B
        curr_node = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(llist.len_recursive(llist.head)) # passing head of the list in recursive function
#print(llist.len_iterative())
# llist.print_list()
