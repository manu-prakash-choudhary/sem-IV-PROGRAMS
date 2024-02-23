class node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

def sum(root):
	if(root == None):
		return 0
	return (sum(root.left) +
			root.data +
			sum(root.right))

def isSumTree(node):

	if(node == None or
	(node.left == None and
	node.right == None)):
		return True

	# Get sum of nodes in left and 
	# right subtrees 
	ls = sum(node.left)
	rs = sum(node.right)

	# if the node and both of its children
	# satisfy the property return 1 else 0
	if((node.data == ls + rs) and
		isSumTree(node.left) and
		isSumTree(node.right)):
		return True

	return False


root = node(26)
root.left= node(10)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(6)
root.right.right = node(3)

if(isSumTree(root)):
    print("The given tree is a SumTree ")
else:
    print("The given tree is not a SumTree ")
