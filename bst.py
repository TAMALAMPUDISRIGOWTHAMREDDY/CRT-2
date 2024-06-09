class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.key:
        root.left=insert(root.left,key)
    elif key>root.key:

        root.right=insert(root.right,key)
    return root
def lca(root,n1,n2):
    if root in None:
        return
    if n1<root.data and n2<root.data:
        lca(root.left,n1,n2)
    elif n1>root.data and n2>root.data:
        lca(root.right,n1,n2)
    else:
        return root.data
root=Node(10)
root.left=Node(30)
root.right=Node(80)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(90)
root.left.left.left=Node(70)
root.left.left.right=Node(25)
root.right.left.left=Node(100)
root.right.right.left=Node(87)
lca(root,20,100)
