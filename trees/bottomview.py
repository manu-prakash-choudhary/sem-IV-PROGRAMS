# Python3 program to print Bottom
# View of Binary Tree

# deque supports efficient pish and pop on both ends
from collections import deque

# Tree node class
class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.hd = float('inf')
		self.left = None
		self.right = None

# Method that prints the bottom view.
def bottomView(root):

	if (root == None):
		return
	
	# Initialize a variable 'hd' with 0
	# for the root element.
	hd = 0
	
	# Store minimum and maximum horizontal distance
	# so that we do not have to sort keys at the end
	min_hd, max_hd = 0, 0
	
	hd_dict = dict()

	# Queue to store tree nodes in level
	# order traversal
	q = deque()

	# Assign initialized horizontal distance
	# value to root node and add it to the queue.
	root.hd = hd
	q.append(root) 

	# Loop until the queue is empty (standard
	# level order loop)
	while q:
		curr_node = q.popleft()
		
		# Extract the horizontal distance value
		# from the dequeued tree node.
		hd = curr_node.hd
		
		# Update the minimum and maximum hd
		min_hd = min(min_hd, hd)
		max_hd = max(max_hd, hd)

		# Put the dequeued tree node to dictionary
		# having key as horizontal distance. Every
		# time we find a node having same horizontal
		# distance we need to update the value in
		# the map.
		hd_dict[hd] = curr_node.data

		# If the dequeued node has a left child, add
		# it to the queue with a horizontal distance hd-1.
		if curr_node.left:
			curr_node.left.hd = hd - 1
			q.append(curr_node.left)

		# If the dequeued node has a right child, add
		# it to the queue with a horizontal distance
		# hd+1.
		if curr_node.right:
			curr_node.right.hd = hd + 1
			q.append(curr_node.right)

	# Traverse the map from least horizontal distance to
	# most horizontal distance.
	for i in range(min_hd, max_hd+1):
		print(hd_dict[i], end = ' ')
	print()
# Driver Code
if __name__=='__main__':
	
	root = Node(20)
	root.left = Node(8)
	root.right = Node(22)
	root.left.left = Node(5)
	root.left.right = Node(3)
	root.right.left = Node(4)
	root.right.right = Node(25)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)
	
	print("Bottom view of the given binary tree :")
	
	bottomView(root)
	
# This code is contributed by rutvik_56
