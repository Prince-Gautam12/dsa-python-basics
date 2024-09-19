class NthNodeFromEnd:
    class ListNode:
        def __init__(self, x, next):
            self.val = x
            self.next = next
        def __str__(self) -> str:
            return f"{self.val}->{self.next}"
        

    def removeNthFromEndOptimized(self, A, B):
        slow, fast = A, A
        while B > 0 and fast != None:
            fast = fast.next
            B-=1
        if fast == None:
            A = A.next 
            return A
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return A

    def removeNthFromEnd(self, A, B):
        length = self.getLength(A)
        if length <= B : 
            A = A.next
            return A
 
        position = length-B-1
        curr = A
        while position > 0:
            curr = curr.next
            position-=1
        if curr != None and  curr.next != None:
            curr.next = curr.next.next
        return A


    def getLength(self, A): 
        length  = 0
        if A == None : return length
        currentNode = A
        while currentNode != None:
            length+=1
            currentNode = currentNode.next
        return length


nthNodeFromEnd = NthNodeFromEnd()

ll = NthNodeFromEnd.ListNode(1, NthNodeFromEnd.ListNode(2, NthNodeFromEnd.ListNode(3, 
                                                                                   NthNodeFromEnd.ListNode(4, 
                                                                                                           NthNodeFromEnd.ListNode(5, None)))))

print(ll)

print(nthNodeFromEnd.removeNthFromEndOptimized(ll, 4))

    
