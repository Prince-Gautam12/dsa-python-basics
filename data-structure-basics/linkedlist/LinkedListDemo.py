class LinkedList :
    def __init__(self) -> None:
        self.__head = None
    def __str__(self) -> str:
        return f'{self.__head}'
    class Node:
        def __init__(self, data: int, next:  object) :
            self.data = data
            self.next = next
        def __str__(self) -> str:
            return f'[{self.data}] -> {self.next}'

    def traverse(self):
        if self.__head == None: print(None)
        else :
            currentNode = self.__head
            while currentNode != None:
                print(currentNode.data)
                currentNode = currentNode.next

    def insertAtBegining(self, data : int):
        newNode = LinkedList.Node(data, None)
        if self.__head == None :
            self.__head = newNode
        else :
            newNode.next = self.__head
            self.__head = newNode

    def insertAtEnd(self, data: int):
        newNode = LinkedList.Node(data, None)
        if self.__head == None :
            self.__head = newNode
        else :
            currentNode = self.__head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode

    def insertAtPosition(self, data, position):
        newNode = LinkedList.Node(data, None)
        if self.__head == None:
            self.__head == newNode
        else:
            currentNode = self.__head
            c = 0 
            while currentNode != None:
                currentNode = currentNode.next
                c+=1
                newNode.next = currentNode.next  
                currentNode.next = newNode
    
    def deleteAtBegining(self):
        pass
    def deleteAtEnd(self):
        if self.__head != None :
            if self.__head.next == None:
                self.__head = None
            else :
                currentNode = self.__head
                while currentNode.next != None and currentNode.next.next != None:
                    currentNode = currentNode.next
                currentNode.next = None 
    def deleteAtPosition(self, position):
        pass
    def search(self, data) -> bool:
        pass
    def getLength(self) -> int:
        length  = 0
        if self.__head == None : return length
        currentNode = self.__head
        while currentNode != None:
            length+=1
            currentNode = currentNode.next
        return length
    
    def delete(self) -> None:
        self.__head = None

class LinkedListDemo :
    linkedList = LinkedList()
    print(linkedList)
    linkedList.insertAtBegining(4)
    print(linkedList)
    linkedList.insertAtEnd(5)
    print(linkedList)
    linkedList.insertAtBegining(7)
    print(linkedList)
    linkedList.insertAtEnd(71)
    print(linkedList)
    linkedList.traverse()
    print("----- Delete Test ----")
    linkedList.deleteAtEnd()
    print(linkedList)
    linkedList.deleteAtEnd()
    print(linkedList)
    linkedList.deleteAtEnd()
    print(linkedList)
    linkedList.deleteAtEnd()
    print(linkedList)

    linkedList.insertAtPosition(150, 2)
    print(linkedList)
    