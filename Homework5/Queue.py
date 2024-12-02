class Queue:
    def __init__(self):
        self.items = []

    def push(self,*elements):
        self.items.extend(elements)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
queue.push(1)
queue.push(2, 3, 4)

print(queue.items)
print(queue.pop())
print(queue.peek())
print(queue.pop())
print(queue.items)
