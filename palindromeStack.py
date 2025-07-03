class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.items[-1]

    def __len__(self):
        return len(self.items)

def is_palindrome_using_stack(s: str) -> bool:
    stack = []

    if 1 <= len(s) <= 50:
        for char in s:
            stack.append(char)


        for char in s:
            if char != stack.pop():
                return False

        return True
    else:
        print("Please enter valid string")

print(is_palindrome_using_stack("racecar"))
print(is_palindrome_using_stack("hello"))



