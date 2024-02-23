# lets create a binary tree

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

# Example
root = node(1)
tree = binary_tree(root)
tree.add_node(node(2))
tree.add_node(node(3))
tree.add_node(node(4))
tree.add_node(node(5))
tree.add_node(node(6))

tree.print_tree()

