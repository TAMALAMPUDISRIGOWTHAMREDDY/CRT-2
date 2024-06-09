class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def display(root):
    if root==None:
        return None
    else:
        print(root.val)
        print(root.left.val)
        print(root.right.val)
        print(root.left.left.val)
        print(root.left.right.val)
root=node(3)
first=node(4)
second=node(5)
third=node(6)
fourth=node(8)
root.left=first
root.right=second
first.left=third
first.right=fourth
display(root)


        
