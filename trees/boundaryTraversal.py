# https://dpaste.org/d3K7w
class Node:
	# Constructor to create a new node
	def __init__(self, value):
		self.value = value 
		self.left = None
		self.right = None


# A simple function to print leaf nodes of a Binary Tree
def printLeaves(root):
	if root is None:
		return
	
	printLeaves(root.left)
	
	# Print it if it is a leaf node
	if root.left is None and root.right is None:
		print(root.value),

	printLeaves(root.right)

# A function to print all left boundary nodes, except a 
# leaf node. Print the nodes in TOP DOWN manner
def printBoundaryLeft(node):
	if node is None:
		return
	# if(node):
	if (node.left):
		print(node.value)
		printBoundaryLeft(node.left)
	
	elif(node.right):
		print(node.value)
		printBoundaryLeft(node.right)
	else:
		print(node.value)
		# do nothing if it is a leaf node, this way we
		# avoid duplicates in output


# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):
	if(root):
		if (root.right):
			# to ensure bottom up order, first call for
			# right subtree, then print this node
			printBoundaryRight(root.right)
			print(root.value)
		
		elif(root.left):
			printBoundaryRight(root.left)
			print(root.value)

		# do nothing if it is a leaf node, this way we 
		# avoid duplicates in output

# root = Node(20)
# root.left = Node(8)
# root.left.left = Node(4)
# root.left.right = Node(12)
# root.left.right.left = Node(10)
# root.left.right.right = Node(14)
# root.right = Node(22)
# root.right.right = Node(25)


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

# if (root):
    # print(root.value)
    
printBoundaryLeft(root)
# printLeaves(root)
# printBoundaryRight(root.right)

# Output: 20 8 4 10 14 25 22