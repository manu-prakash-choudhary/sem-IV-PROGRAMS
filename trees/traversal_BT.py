# Write a Program to Understand and implement Tree traversals i.e. Pre-Order Post-Order, In-Order

# binary tree traversal
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binary_tree:
    def __init__(self, root):
        self.root = root
    
    def add_node(self, node):
        # will insert the node in the first available position
        # in the tree
        queue = [self.root]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left == None:
                current.left = node
                return
            elif current.right == None:
                current.right = node
                return
            else:
                queue.append(current.left)
                queue.append(current.right)
    
    def print_tree(self):
        # will print the tree in a breadth first search manner
        queue = [self.root]
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.value)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
    
    def in_order_traversal(self, node):
        if node == None:
            return
        self.in_order_traversal(node.left)
        print(node.value)
        self.in_order_traversal(node.right)
    
    def pre_order_traversal(self, node):
        if node == None:
            return
        print(node.value)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)
    
    def post_order_traversal(self, node):
        if node == None:
            return
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(node.value)

# Example
root = node(1)
tree = binary_tree(root)
tree.add_node(node(2))
tree.add_node(node(3))
tree.add_node(node(4))
tree.add_node(node(5))
tree.add_node(node(6))

tree.print_tree()
print("In order traversal")
tree.in_order_traversal(root)
print("Pre order traversal")
tree.pre_order_traversal(root)
print("Post order traversal")
print(tree.post_order_traversal(root))