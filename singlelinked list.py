class abc:
    def __init__(self,data):
        self.data=data
        self.next=None

    def disp(self,head):

        temp=head
        
        while temp!=None:
            print(temp.data)
            temp=temp.next
head=abc(3)
second=abc(15)
third=abc(25)
fourth=abc(45)
head.next=second
second.next=third
third.next=fourth
'''head.next.next=third
head.next.next.next=fourth'''
head.disp(head)

        
