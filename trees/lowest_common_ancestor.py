# 13. Write a program for Lowest Common Ancestors

class Node:
    def __init__(self, data) -> None:
        self.value = data
        self.left = None 
        self.right = None

def findLCA(curr_node, n1, n2):
    if curr_node is None:
        return None
    if curr_node.value == n1 or curr_node.value == n2:
        return curr_node
    left_lca = findLCA(curr_node.left, n1, n2)
    right_lca = findLCA(curr_node.right, n1, n2)
    if left_lca is not None and right_lca is not None:
        return curr_node
    
    if left_lca is not None:
        return left_lca
    elif right_lca is not None:
        return right_lca
    else:
        return None

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
n1 = 10; n2 = 14
t = findLCA(root, n1, n2)
print(f"LCA of {n1} and {n2} is {t.value}") # 12


#           20  
#         /    \
#        8      22
#      /   \
#     4    12
#         /   \
#       10    14

# https://dpaste.org/FSsrO