class TreeNode:
    """A class for a tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValid(root, low=float('-inf'), high=float('inf')):
    """
    Validate if a tree is a binary search tree (BST).
    
    Args:
    - root: TreeNode, the root of the binary tree.
    - low: Lower bound for the current node's value.
    - high: Upper bound for the current node's value.
    
    Returns:
    - bool: True if the tree is a valid BST, False otherwise.
    """
    # Base case: An empty tree is a valid BST.
    if not root:
        return True

    # The value of the current node must be within the range (low, high).
    if not (low < root.val < high):
        return False

    # Recursively check the left subtree, updating the upper bound.
    # The left child's value must be less than the current node's value.
    leftIsValid = isValid(root.left, low, root.val)

    # Recursively check the right subtree, updating the lower bound.
    # The right child's value must be greater than the current node's value.
    rightIsValid = isValid(root.right, root.val, high)

    # The current subtree is a BST if both left and right subtrees are BSTs.
    return leftIsValid and rightIsValid


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(isValid(root))
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)



print(isValid(root))