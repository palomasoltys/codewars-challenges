# Write a function in python that checks if paranthesis in the string are balanced or not.
# Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def is_balanced(string):

    stack = Stack()
    parens = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in parens.values():
            stack.push(char)
        elif not stack.is_empty() and char in parens and parens[char] == stack.peek():
            stack.pop()
        elif char in parens.keys():
            stack.push(char)

    return stack.is_empty()


print(is_balanced("({a+b})"))  # --> True
print(is_balanced("))((a+b}{"))  # --> False
print(is_balanced("((a+b))"))  # --> True
print(is_balanced("))"))  # --> False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # --> True
