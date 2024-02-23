# N'arry tree creation
class node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_node(self, node):
        self.children.append(node)

class tree:
    def __init__(self, root):
        self.root = root
    
    def add_node(self, node):
        self.root.add_node(node)


# Example
root = node(1)
tree = tree(root)
node2 = node(2)
tree.add_node(node2)
tree.add_node(node(3))
tree.add_node(node(4))
node2.add_node(node(25))
node2.add_node(node(26))


print(tree.root.value)
print(tree.root.children[0].value)
print(tree.root.children[1].value)
print(tree.root.children[2].value)
print(tree.root.children[0].children[0].value)
print(tree.root.children[0].children[1].value)


