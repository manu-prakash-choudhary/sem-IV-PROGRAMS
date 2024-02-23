# printing left view of a binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leftView(root, level, max_level):
    if root is None:
        return
    if max_level[0] < level:
        print(root.value)
        max_level[0] = level
    leftView(root.left, level+1, max_level)
    leftView(root.right, level+1, max_level)

if __name__=='__main__':
    root = Node(12)
    root.left = Node(10)
    root.right = Node(30)
    root.right.left = Node(25)
    root.right.right = Node(40)
    max_level = [0]
    leftView(root, 1, max_level)

# Agorithm for left View of Binary Tree
# Create class Node with value, left and right attributes
# Create root Node
#  with the help of root node generate your tree

# create a function leftView with root, level and max_level as parameters
#   if root is None return
#   if max_level is less than level print root.value and update max_level
#   call leftView with root.left, level+1 and max_level
#   call leftView with root.right, level+1 and max_level

# create a max_level list with 0 as its first element
# call leftView with root, 1 and max_level as parameters
