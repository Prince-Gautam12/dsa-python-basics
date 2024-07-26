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
            crawler = self.head
            while crawler.next != None :
                crawler = crawler.next
            crawler.next = newNode 
    
    def delete(self, data):
        pass

    def search(self, data):
        if self.head == None : return False
        crawler = self.head
        while crawler != None :
           if crawler.data == data : return True
           crawler = crawler.next
        return False

    def searchByIndex(self, index) :
        crawler = self.head
        while (index > 0 and crawler != None) :
            crawler = crawler.next
            index-=1
        if crawler == None  : return None
        return crawler.data

    def printList(self) :
        print(self.head)
    

    
        

linkedList = LinkedList()
print(linkedList.search(5))

linkedList.printList()
for i in range(1, 10) :
    linkedList.insert(i)
linkedList.printList()

print(linkedList.search(5))
print(linkedList.search(15))
print(linkedList.searchByIndex(5))
    