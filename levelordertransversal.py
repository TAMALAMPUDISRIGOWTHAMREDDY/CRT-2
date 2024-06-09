from collections import deque

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

def levelorderTraversal(root):
    dq=deque()
    dq.append(root)
    while len(dq)>0:
        r=dq[0]
        print(r.key)
        dq.popleft()
        if r.left!=None:
            dq.append(r.left)
        if r.right!=None:
            dq.append(r.right)

    '''while dq:
        if dq[0].left:
            dq.append(dq[0].left)    
        if  dq[0].right:
            dq.append(dq[0].right)
        print(dq.popleft().key)  ''' 
root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(90)
levelorderTraversal(root)




