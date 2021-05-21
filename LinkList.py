class Node:
    x=0
    def __init__(self, x= 0):
        self.x = x
        self.next = None
        

class LinkList:

    def __init__(self):
        self.head = None

    def print(self):
        printNode = self.head
        while printNode is not None:
            print(printNode.x)
            printNode = printNode.next

    def isEmpty(self):
        return self.head == None

    def insertAtStart(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, val):
        newNode = Node(val)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
    
    def insertAt(self, n, val):
        newNode = Node(val)
        temp = self.head
        previous = None
        for i in range(1, n):
            previous = temp
            temp = temp.next
        if temp == self.head:
            self.insertAtStart(val)
        else:
            previous.next = newNode
            newNode.next = temp

    def removeAtStart(self):
        newNode = self.head
        self.head = self.head.next
        del(newNode)
        
    def removeAtEnd(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        x = temp.next.x
        temp.next = None
        return x

    def removeAt(self, n):
        temp = self.head
        previous = None
        for i in range(1, n):
            previous = temp
            temp = temp.next
        if temp == self.head:
            return self.removeAtStart()
        else:
            previous.next = temp.next
            x = temp.x
            del(temp)
            return x

    def __del__(self):
        temp = self.head
        while temp is not None:
            t = temp
            temp = temp.next
            del (t)
        self.head = None
        



li = LinkList()
li.head = Node(1)
li.insertAtStart(3)
li.insertAtEnd(4)
li.insertAtEnd(6)
li.insertAtEnd(7)
li.insertAt(6, 10)
li.removeAt(2)
li.removeAtStart()
print("Removing : " + str(li.removeAtEnd()))
li.print()
    
    
    
        
            