# Circular Single Linked List - split list - ABCD... = AB... and CD... (...represent the circular linked list)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def __len__(self):  # this is overwriting len function in python to operate of cllist
        cur = self.head
        count = 0  # keep track of node of list
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)  # getting size of the list
        if size == 0:
            return None
        if size == 1:
            return self.head  # because that is only node in the list

        mid = size // 2
        count = 0

        prev = None
        cur = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next

        # print(prev.data)
        # print(cur.data)
        # the last node will point to head of list as this is circular list, first list is made
        prev.next = self.head

        split_cllist = CircularLinkedList()  # creating the second list
        while cur.next != self.head:  # this is when pointes is on C
            split_cllist.append(cur.data)
            cur = cur.next
        # the last node i.e. D is get included with this statement
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")

# print(len(cllist))
cllist.split_list()
