# Single Linked List - Node swap - 1. Node 1 and node 2 are not head nodes 2. either node 1 or node 2 are head nodes
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

    # will start with head and with each recursive call will move it to next one
    def len_recursive(self, node):
        if node is None:  # base condition
            return 0
        # we call recursive itself and will pass to the next node,  self is a class method
        return 1 + self.len_recursive(node.next)

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

    def swap_node(self, key_1, key_2):
        if key_1 == key_2:
            return  # there is nothing to return as both keys are already same
        prev_1 = None  # initially set to None
        curr_1 = self.head  # initially set to head
        while curr_1 and curr_1.data != key_1:  # curr_1 which set to head is not at end of list; and curr_1.data is not at position where we seek the data
            prev_1 = curr_1  # previous node now assigned to current node
            curr_1 = curr_1.next  # and current node assigned to next node
        # print(prev_1.data) # prints A
        # print(curr_1.data) # prints B
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:  # if either of these things is None will return nothing as we cannot swap the element
            return
        if prev_1:  # previous node exist
            prev_1.next = curr_2  # changing the connection from A = B to A = C
        else:  # node_1 is head node. Node_2 is not
            self.head = curr_2  # head is moved from A to B

        if prev_2:
            prev_2.next = curr_1  # changing the connection from B = C to C = A
        else:
            self.head = curr_1
        # we are doing the same thing and connecting B to D as we did before like C to A
        # shorthand of python (eg. a, b = b, a)
        curr_1.next, curr_2.next = curr_2.next, curr_1.next


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

# llist.swap_node("B", "C")  # B is key 1
llist.swap_node("A", "C") # condition where A is head
llist.print_list()
