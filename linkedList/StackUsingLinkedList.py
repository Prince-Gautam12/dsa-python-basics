class Stack:
    class Node:
        def __init__(self, data: int, next:  object) :
            self.data = data
            self.next = next
        def __str__(self) -> str:
            return f'[{self.data}] -> {self.next}'
        
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def push(self, element):
        newNode = Stack.Node(element, None)
        if self.__head == None :
            self.__head = newNode
        else :
            newNode.next = self.__head
            self.__head = newNode
        self.size+=1

    def pop(self) -> int :
        deletedNode = None
        if self.__head != None:
            if self.__head.next == None:
                deletedNode = self.__head
                self.__head = None
            else:
                self.__head = self.__head.next
        else :
            
        self.size-=1

    def size(self) -> int :
        return self.size

    def __str__(self) -> str:
        return f''
        
class StackUsingLinkedList :
    stack = Stack()
    stack.push(10)
    print(stack)
    pass
