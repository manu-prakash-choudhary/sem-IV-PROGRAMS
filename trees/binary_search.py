# 14. Write a Program to Build BST

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left = None
        self.right = None
    def value_of_node(self):
        return self.data
    

a1 = Node(5)
a2 = Node(3)
a3 = Node(7)
a4 = Node(2)
a5 = Node(4)
a6 = Node(6)
a7 = Node(8)

a1.value_of_node()

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7

def print_tree(root):
    q = [root]
    while len(q)>0:
        curr = q.pop(0)
        print(curr.data)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

print_tree(a1)

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

