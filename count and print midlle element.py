class abc:
    def __init__(self,data):
        self.data=data
        self.next=None

    def disp(self,head):
        newnode=newnode2
        head=newnode
        temp=head
        count=0
        a=[]
        
        while temp!=None:
            a.append(temp.data)
            mid=len(a)//2
        
            
            count+=1
            temp=temp.next
        print(count)
        print(a)
        print(a[mid])
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
