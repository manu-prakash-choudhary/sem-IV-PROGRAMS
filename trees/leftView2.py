# 18. Write a Program to view a tree from left View
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.left = Node(7)
root.right = Node(3)
root.right.right = Node(8)
root.right.right.left = Node(9)
root.right.right.left.right = Node(10)
root.right.right.left.right.left = Node(11)

def leftView(node):
    q = [(0, node)]
    level_Nodes_dict = dict()
    while len(q) > 0 :
        curr_tuple = q.pop(0)
        curr_level = curr_tuple[0]
        curr_node = curr_tuple[1]

        if curr_level in level_Nodes_dict:
            level_Nodes_dict[curr_level].append(curr_node.data)
        else:
            level_Nodes_dict[curr_level] = []
            level_Nodes_dict[curr_level].append(curr_node.data)
        if curr_node.left:
            q.append((curr_level+1, curr_node.left))
        if curr_node.right:
            q.append((curr_level+1, curr_node.right))

    return level_Nodes_dict

returned_dict = leftView(root)
# for key,values in returned_dict.items():
#     print(values[0])
for key in returned_dict:
    print(returned_dict[key][0], end=" ")

print()

# https://dpaste.org/WxxL6
    
# Algorithm for left View in above code

    # 1. Create a class Node Responsible for creating Node
    # 2. Create your root Node
    # 3. Design you desired tree with the help of root Node only

    #            1
    #           / \
    #          2   3
    #         / \   \
    #        4   5   8
    #           /   /   
    #          6   9

    # 4. write a function leftView which takes root node as input
        # 4.1 Inside the function initialize a list which will store the level and node address as tuple begining with (0, root)

        # 4.2 Initialize a dictionary which will store the level as key and the nodes at that level as value
        # 4.3 while the queue is not empty
            # pop the first element from the queue and store it in curr(or any) variable
            # if the level is already present in the dictionary then append the node data to the value of that level
            # else create a new key with the level and and a list with the node data to the value of that level/key
            # if the node has left child then append the level+1 and left child(object) to the queue
            # if the node has right child then append the level+1 and right child(node object) to the queue
