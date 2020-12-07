# Single Linked List - rotate the list - 123456Null - if k = 4 = 561234Null
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

    def print_helper(self, node, name):
        if node is None:
            print(name + ":None")
        else:
            print(name + ":" + node.data)

    def revere_iterative(self):
        # here we need to know the previous node of current node
        prev = None  # keep track of previous node
        curr = self.head  # initially current node is head and it is move along with list
        while curr:  # means while current node is not Null means we are not at end of list. Once it is Null it stops the loop
            nxt = curr.next  # temporary variable or pointer we set to B so it will not mess up the position and will sync with C
            curr.next = prev  # we are flipping the arrow from B to A A <- B
            # print helper helps to identify what happening in each of the loop
            self.print_helper(prev, "PREV")
            self.print_helper(curr, "CURR")
            self.print_helper(nxt, "NEXT")
            print("\n")  # gives the line between two results
            prev = curr
            curr = nxt
        self.head = prev  # now we are setting the head to D as this is our reversed list, we are coming out of the while loop

    def reverse_recursive(self):
        def _reverse_recursive(cur, pre):
            if not cur:  # means we reached end of list
                return pre  # base condition
            # now till line 162 is similar like 144 to 151 line
            nxt = cur.next  # temporary variable or pointer we set to B so it will not mess up the position and will sync with C
            cur.next = pre  # we are flipping the arrow from B to A A <- B
            pre = cur
            cur = nxt
            # to call the function and print the data of that function we need return statement
            return _reverse_recursive(cur, pre)

        # this what we did at 141 and 142 line
        self.head = _reverse_recursive(cur=self.head, pre=None)

    def merge_sorted(self, llist):
        p = self.head  # head of first list
        q = llist.head  # head of the second list
        s = None
        if not p:
            return q  # if p does not exist, q is already sorted so we are return q directly
        if not q:
            return p
        if p and q:  # if p and q are not null means both list exist
            if p.data <= p.data:
                s = p  # the data at head in p is lower than in q. so pointer s goes to p
                p = s.next  # as s is pointed to lower data now in p list. the p moves to next node of s
            else:
                s = q
                q = s.next

            new_head = s  # then we are pointing the s to head so it keep track
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q  # if we reach at null in p then it just add the list from q
        if not q:
            s.next = p
        return new_head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()  # we are saving it in dictionary (we can use the hashtable as well), so next time we can track the value
        while cur:  # current is not Null
            if cur.data in dup_values:  # if current data we are on is already in dup_value dictionary
                prev.next = cur.next  # pointing the node 6 to 4 and removing the pointer from 6 to 1
                cur = None  # now we are removing that node from the list i.e. second occurrence of 1
            else:
                # in our dictionary this is the first time this data encounters
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next  # if either if or else condition pass we assign current to next node

    def print_nth_from_last(self, n):
        # # Method 1 - a. Calculate length of linked list b. count down from the total length until "n" is reached
        # total_len = self.len_iterative()
        # # print(total_len)
        # cur = self.head
        # while cur:  # while current is not Null
        #     if total_len == n:
        #         print(cur.data)
        #         return cur
        #     total_len -= 1  # this is else statement only.
        #     cur = cur.next
        # if cur is None:
        #     return
        # Method 2 - Two pointers a. P:Head node b. Q:n nodes beyond head node
        p = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(str(n) + " is greater than the number of nodes in the list")
            return

        while p and q:
            p = p.next
            q = q.next
        return p.data

    def rotate(self, k):
        p = self.head  # first we are pointing out the p and q to head
        q = self.head
        prev = None
        count = 0  # this will keep track of when we hit k
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        # print(p.data) # printing the p data right now. Now p is at 4 and q is at 5. We want to move q to last node of list not the null
        while q:
            prev = q
            q = q.next  # to move it along in the linked list
        q = prev
        # print(q.data)  # it will get us to last node i.e. 6

        q.next = self.head  # we are pointing the q from 6 to head now
        self.head = p.next  # next element of p is now head of the list i.e. 5
        p.next = None  # the node after 4 should be None


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.print_list()  # printing out the list before function
print("\n")
llist.rotate(4)
llist.print_list() # printing out the list after function
