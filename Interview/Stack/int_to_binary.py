# 242 / 2 = 121 - 0
# 121 % 2 = 1
# 121 // 2 = 60 - 1
# 121 / 2 = 60.5
# int('11110010', 2) = 242
# from stack import Stack
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):  # checking the top element of the stack
        if not self.is_empty():  # if stack is not empty
            return self.items[-1]

    def get_stack(self):
        return self.items


def div_by_two(dec_num):
    s = Stack()
    while dec_num > 0:  # until the division get us to 0
        remainder = dec_num % 2  # till then will get remainder
        s.push(remainder)
        dec_num = dec_num // 2  # to ignore the fraction we use double division

    bin_num = ""  # string will hold the binary representation
    while not s.is_empty():
        bin_num += str(s.pop)  # concatenate popped element and binary number

    return bin_num


print(div_by_two(242))  # return 11110010
