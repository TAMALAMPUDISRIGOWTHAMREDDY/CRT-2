class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    def disp(self,head):
        head=newnode
        temp=head
        while temp!=None:
            print(temp.data)
            temp=temp.next
head=Node(3)
a=Node(4)
b=Node(5)
head.next=a
a.next=b
#head.prev=None
a.prev=head
b.prev=a
newnode=Node(143)
head.prev=newnode
newnode.next=head

head.next.next=b
print(b.prev.data)
print(head.next.prev.data)

head.disp(head)
            
