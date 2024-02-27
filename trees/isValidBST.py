class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValid(curr_node, low, high):

    # Base case: An empty tree is a valid BST.
    if curr_node is None:
        return True
    
    # The value of the current node must be within the range (low, high).
    if not (low < curr_node.val < high):
        return False

    # Recursively check the left subtree, updating the upper bound.
    # The left child's value must be less than the current node's value.
    leftIsValid = isValid(curr_node.left, low, curr_node.val)

    # Recursively check the right subtree, updating the lower bound.
    # The right child's value must be greater than the current node's value.
    rightIsValid = isValid(curr_node.right, curr_node.val, high)

    # The current subtree is a BST if both left and right subtrees are BSTs.
    return leftIsValid and rightIsValid


root = Node(5)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)
result = isValid(root, float('-inf'), float('inf'))
if result == True:
    print("Given Binary Tree is valid BST")
else:
    print("Given Binary tree is not a valid BST")

# Lets take example of below tree
#      5
#     / \
#    1    7
#  / \   /  \
#       3    6
#      / \  / \
# The above tree is not a valid BST because the right child of 4 is 3 which is less than 4.
