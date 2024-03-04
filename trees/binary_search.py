# 14. Write a Program to Build BST

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left = None
        self.right = None
    


def print_tree(root):
    q = [root]
    while len(q)>0:
        curr = q.pop(0)
        print(curr.data)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)



def insert_node(root, value):
    curr = root
    node_inserted = False
    while node_inserted == False:
        if value < curr.data:
            if curr.left is None:
                curr.left = Node(value)
                node_inserted = True
            else:
                curr = curr.left
        else:
            if curr.right is None:
                curr.right = Node(value)
                node_inserted = True
            else:
                curr = curr.right

list_node_values = [ 3, 7, 2, 4, 6, 8]
root = Node(5)
for value in list_node_values:
    insert_node(root, value)

print_tree(root)

# https://dpaste.org/t47Dm