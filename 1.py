class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def reverse(self,head,n):
        count=0
        prev = None
        current = self.head
        while current!=None and count<n :
            next = current.next
            current.next = prev
            prev = current
            current = next
            count+=1
        if next!=None:
            head.next=reverse(next,n)
        self.head = prev
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print ("Given linked list")
llist.printList()
1list=reverse(LinkedList(),3)
print ("\nReversed linked list")
1list.printList()
