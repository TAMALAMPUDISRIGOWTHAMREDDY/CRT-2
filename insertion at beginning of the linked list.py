class abc:
    def __init__(self,data):
        self.data=data
        self.next=None

    def disp(self,head):
        newnode=newnode2
        head=newnode
        temp=head
        
        
        while temp!=None:
            print(temp.data)
            temp=temp.next
        
head=abc(3)
second=abc(15)
third=abc(25)
fourth=abc(45)
newnode=abc(23)
newnode.next=head
newnode2=abc(45)          #adding two nodes at beginning of the linked list
newnode2.next=newnode
head.next=second
second.next=third
third.next=fourth
'''head.next.next=third
head.next.next.next=fourth'''
head.disp(head)
''' def insert(data,head):
newnode=node(data)
newnode.next=head
head=newnode
'''
