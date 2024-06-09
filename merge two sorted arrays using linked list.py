#11->22->33
#12->21->34
#11->12->21->22->33->34
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def dis(self):
        while 
a=Node(11)
a.next=Node(22)
a.next.next=Node(33)
b=Node(12)
b.next=Node(21)
b.next.next=Node(34)'''
'''class Node:
	def __init__(self, key):
		self.key = key
		self.next = None
def newNode(key):
    return Node(key)

a = Node(5)
a.next = Node(10)
a.next.next = Node(15)
a.next.next.next = Node(40)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)

v = []
while(a is not None):
	v.append(a.key)
	a = a.next

while(b is not None):
	v.append(b.key)
	b = b.next

v.sort()
result = Node(-1)
temp = result
for i in range(len(v)):
	result.next = Node(v[i])
	result = result.next

temp = temp.next
print("Resultant Merge Linked List is : ")
while(temp is not None):
	print(temp.key, end=" ")
	temp = temp.next'''


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node
def mergeLists(head1, head2):
	temp = None
	if head1 is None:
		return head2
	if head2 is None:
		return head1
	if head1.data <= head2.data:
		temp = head1
		temp.next = mergeLists(head1.next, head2)
	else:
		temp = head2
		temp.next = mergeLists(head1, head2.next)
	return temp
if __name__ == '__main__':
	list1 = LinkedList()
	list1.append(5)
	list1.append(10)
	list1.append(15)
	list2 = LinkedList()
	list2.append(2)
	list2.append(3)
	list2.append(20)
	list3 = LinkedList()
	list3.head = mergeLists(list1.head, list2.head)
	print("Merged List is:")
	list3.printList()



