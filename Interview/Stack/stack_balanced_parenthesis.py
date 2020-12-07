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


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paranthesis_balanced(paren_str):
    s = Stack()  # creating the stack object
    is_balanced = True
    index = 0  # index variable to keep track of where we are in string we are looping through
    while index < len(paren_str) and is_balanced:
        paren = paren_str[index]
        if paren in "([{":
            s.push(paren)
        else:  # if it is in closing parenthesis
            if s.is_empty():  # if that stack is empty
                is_balanced = False
            else:
                top = s.pop()  # now we pop out the top element in stack and match with closing one
                # element top is the one we popped out and paren we are at now is not match
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced():
        return True
    else:
        return False


print(is_paranthesis_balanced("({[]})"))
