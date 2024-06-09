class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.data:
        root.left=insert(root.left,key)
    elif key>root.data:

        root.right=insert(root.right,key)
    return root
def height(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    if lheight>rheight:
        return 1+lheight
    else:
        return 1+rheight
    

root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(90)
c=height(root)
print(c)



