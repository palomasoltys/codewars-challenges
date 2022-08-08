# Write a function that can reverse a string using stack data structure

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


def reverse_string(string):
    stack = Stack()
    s_reversed = ''

    for letter in string:
        stack.push(letter)

    while not stack.is_empty():
        s_reversed += stack.pop()

    return s_reversed


print(reverse_string('Paloma Soltys'))
