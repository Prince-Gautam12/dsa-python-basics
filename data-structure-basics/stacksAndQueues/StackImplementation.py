class Stack:
    class Node:
        def __init__(self, data, down) -> None:
            self.data = data
            self.down = down

    def __init__(self, size: int) -> None:
        self.top = None
        self.maxSize = size
        self.size = 0

    def push(self, value):
        if self.isFull():
            raise Exception("Overflow exception: Stack is full")
        self.size +=1 
        newNode = Stack.Node(value, None)
        if self.top == None:
            self.top = newNode
        else :
            newNode.down = self.top
            self.top = newNode

    def pop(self):
        if self.isEmpty():
            raise Exception("Underflow exception: Stack is empty")
        self.size -= 1
        value = self.top.data
        self.top = self.top.down
        return value

    def getSize(self):
        return self.size

    def getTop(self):
        if self.isEmpty():
            raise Exception("Underflow exception: Stack is empty")
        return self.top.data

    def isFull(self):
        return self.size == self.maxSize

    def isEmpty(self):
        return self.top == None


class StackA:
    def __init__(self, size: int) -> None:
        self.top = -1
        self.maxSize = size
        self.size = 0
        self.array = [0]*20


    def push(self, value):
        if self.isFull():
            raise Exception("Overflow Error: Stack is Full")
        else:
            self.top += 1
            self.array[self.top] = value
            self.size += 1


    def pop(self):
        if self.isEmpty():
            raise Exception("Underflow Error: Stack is Empty")
        value = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        self.size -= 1
        return value

    def getSize(self):
        return self.size

    def getTop(self):
        if self.isEmpty():
            raise Exception("Under Flow Error: Stack is Empty")
        return self.array[self.top]

    def isFull(self):
        return self.size == self.maxSize
        
    def isEmpty(self):
        return self.top == -1
    
        
    

    

class User:
    def testStackArray(self):
        try:

            stack = StackA(20)
            print(stack.pop())
            stack.push(5)
            stack.push(6)
            stack.push(7)
            stack.push(8)
            stack.push(9)        
            print(stack.getTop())

            print(stack.pop())
        
        except Exception as e:
            print(f"An error occured: {e}")







    
    def testStackLinkedList(self):
        try :
            stack = Stack(4)
            # print(stack.pop())
            stack.push(1)
            stack.push(124)
            stack.push(12)
            stack.push(14)
            print(stack.getSize())
            print(stack.isFull())
            stack.push(45)
            print(stack.pop())
            print(stack.getSize())
            print(stack.getSize())
            print(stack.isEmpty())
            print(stack.isFull())
        except Exception as e:
            print(f"An error happened: {e}") 


user = User()
user.testStackArray()