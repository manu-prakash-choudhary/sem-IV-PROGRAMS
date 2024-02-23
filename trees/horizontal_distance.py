# program to calculate horizontal distance

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def find_depth(self, root):
        if root is None:
            return 0, None
        else:
            left_depth = self.find_depth(root.left)[0]
            right_depth = self.find_depth(root.right)[0]
            if left_depth > right_depth:
                return left_depth + 1, 'left'
            else:
                return right_depth + 1, 'right'



    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        
        # insert on basis of arrival of elements not on basis of value
        if current_node.left is None:
            current_node.left = Node(data)
        elif current_node.right is None:
            current_node.right = Node(data)
        else:
            depth, direction = self.find_depth(current_node)
            if direction == 'left':
                self._insert(data, current_node.left)
            else:
                self._insert(data, current_node.right)
        

    def horizontal_distance(self, root, hd, hd_dict):
        if root is None:
            return
        if hd in hd_dict:
            hd_dict[hd].append(root.data)
        else:
            hd_dict[hd] = [root.data]
        self.horizontal_distance(root.left, hd-1, hd_dict)
        self.horizontal_distance(root.right, hd+1, hd_dict)

    def print_horizontal_distance(self):
        hd_dict = {}
        self.horizontal_distance(self.root, 0, hd_dict)
        for key in sorted(hd_dict):
            print(hd_dict[key])

t = tree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)

t.print_horizontal_distance()
