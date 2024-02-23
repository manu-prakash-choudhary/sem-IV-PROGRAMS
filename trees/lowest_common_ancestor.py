class Node:
    def __init__(self, data) -> None:
        self.value = data
        self.left = None 
        self.right = None

def findLCA(root, n1, n2):
    if root is None:
        return None
    if root.value == n1 or root.value == n2:
        return root
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca

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
