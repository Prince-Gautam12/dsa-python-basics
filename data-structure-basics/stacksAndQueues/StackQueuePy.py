class Stack :
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.stack = []

    def push(self, value):
        if self.isFull(): 
            raise Exception("Overflow exception: Stack is full")
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Underflow exception: Stack is empty")
        return self.stack.pop()

    def getSize(self):
        return len(self.stack)

    def getTop(self):
        if self.isEmpty():
            raise Exception("Underflow exception: Stack is empty")
        return self.stack.index(-1)

    def isFull(self):
        return len(self.stack) == self.capacity

    def isEmpty(self):
        return len(self.capacity) == 0
        