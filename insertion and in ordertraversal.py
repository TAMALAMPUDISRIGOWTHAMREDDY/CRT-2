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
def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.key)
    inorderTraversal(root.right)
def preorderTraversal(root):
    if root is None:
        return
    print(root.key)
    preorderTraversal(root.left)
    preorderTraversal(root.right)
def postorderTraversal(root):
    if root is None:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.key)
root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(90)

inorderTraversal(root)
print("====================================================================")
preorderTraversal(root)
print("====================================================================")
postorderTraversal(root)


