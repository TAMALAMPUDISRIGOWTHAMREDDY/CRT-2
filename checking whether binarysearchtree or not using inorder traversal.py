class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def display(root):
    if root==None:
        return None
    else:
        print(root.key)
        print(root.left.key)
        print(root.right.key)
        print(root.left.left.key)
        print(root.left.right.key)
        print("====================================================")
def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.data:
        root.left=insert(root.left,key)
    elif key>root.data:

        root.right=insert(root.right,key)
    return root
def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.key)
    inorderTraversal(root.right)
root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(90)
inorderTraversal(root)
if display(root)==inorderTraversal(root):
    print(True)
else:
    print(False)