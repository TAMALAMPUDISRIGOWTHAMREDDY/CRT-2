# a tree is called as balanced tree is the absoluate value of  diff b/w lheight and right height should be lessthan or equal to 1 then it is self balanced or avl trees
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
    height(root.left)
    height(root.right)
    lheight=height(root.left)
    rheight=height(root.right)
    if lheight>rheight:
        lheight+=1
    else:
        rheight+=1
    if abs(lheight-rheight)==1 or abs(lheight-rheight)==-1 or abs(lheight-rheight)==0:
        return True
    else:
        return False
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
# root.right.right=Node(90)
height(root)
print(height(root))




