class LinkedList :
    class Node :
        def __init__(self, data, next) :
            self.data = data
            self.next = next

        def __str__(self) -> str:
            return f"{self.data} -> {self.next}"

    def __init__(self):
        self.head = None

    def insert(self, data) :
        newNode = LinkedList.Node(data, None)
        if self.head == None : self.head = newNode
        else :
            crowler = self.head
            while crowler.next != None :
                crowler = crowler.next
            crowler.next = newNode 
    
    def delete(self, data):
        pass

    def search(self, data):
        pass

    def printList(self) :
        print(self.head)
    

    
        

linkedList = LinkedList()
linkedList.printList()
for i in range(1, 10) :
    linkedList.insert(i)
    linkedList.printList()
    