# stack reverse string - Hello - olleH
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


def reverse_string(stack, input_str):
    # loop through the string and push contents character by character onto stack
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()  # will append character by character
    return rev_str


stack = Stack()
input_str = "Hello"
# print(input_str[::-1]) - python function to reverse string directly
print(reverse_string(stack, input_str))
