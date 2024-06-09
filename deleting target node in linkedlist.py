def delete(t,head):
    temp=head
    while temp.next!=None:
        if temp.next.data==t:
            temp.next=temp.next.next
        temp=temp.next
