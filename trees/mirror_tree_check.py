class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Given two trees, return true 
# if they are mirror of each other
def areMirror(a, b):
	
	# Base case : Both empty
	if a is None and b is None:
		return True
	
	# If only one is empty
	if a is None or b is None:
		return False
	
	# Both non-empty, compare them 
	# recursively. Note that in 
	# recursive calls, we pass left
	# of one tree and right of other tree
	return (a.data == b.data and
			areMirror(a.left, b.right) and
			areMirror(a.right , b.left))


root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)

result = areMirror(root1, root2)
if result:
    print("Yes they are mirror of each other")
else:
    print("No they are not mirror of each other")
	
