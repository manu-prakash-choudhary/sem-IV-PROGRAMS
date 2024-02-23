class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(node):
    if node is None:
        return 0
    else:
        left_depth = maxDepth(node.left)
        right_depth = maxDepth(node.right)
        return max(left_depth, right_depth) + 1

# Example Usage:
# Creating a simple binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

# root = TreeNode(value = 1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5


# Calculate the depth of the tree
print("Depth of tree:", maxDepth(a1))