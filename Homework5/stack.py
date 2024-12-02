
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack=Stack()
print(stack.pop())
print(stack.peek())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
print(stack.pop())
print(stack.is_empty())
